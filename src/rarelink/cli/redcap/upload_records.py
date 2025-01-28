import json
import requests
import tempfile
import typer
from pathlib import Path
from dotenv import dotenv_values
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator,
    between_section_separator,
)
from rarelink.cli.utils.string_utils import (
    format_header,
    success_text,
    error_text,
    hint_text,
)
from rarelink.cli.utils.validation_utils import validate_env
from rarelink.cli.utils.file_utils import ensure_directory_exists
from rarelink.cli.utils.logging_utils import setup_logger
from rarelink.utils.validation import validate_linkml_data
from rarelink.utils.processing.schemas import linkml_to_redcap  # Adjust the import to the correct module
from rarelink_cdm.v2_0_0_dev0.mappings.redcap import MAPPING_FUNCTIONS
import logging

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
app = typer.Typer()

REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
ENV_PATH = Path(".env")  # Path to your .env file
BASE_SCHEMA_PATH = REPO_ROOT / "src/rarelink_cdm/v2_0_0_dev0/schema_definitions/rarelink_cdm.yaml"

# Define the function to upload records to REDCap
@app.command()
def app(input_file: Path = None):
    """
    Upload a validated LinkML JSON file to REDCap after transforming it to the appropriate format.

    Args:
        input_file (Path): Path to the JSON file containing LinkML records to upload.
    """
    format_header("Upload Records to REDCap")

    # If no input file is provided, prompt the user to enter one
    if input_file is None:
        input_file = Path(typer.prompt("Enter the path to the JSON file containing LinkML records"))

    # Validate required environment variables
    validate_env(["REDCAP_API_TOKEN", "REDCAP_URL", "REDCAP_PROJECT_NAME"])

    # Load environment variables
    env_values = dotenv_values(ENV_PATH)
    api_url = env_values["REDCAP_URL"]
    api_token = env_values["REDCAP_API_TOKEN"]

    # Display caution message for sensitive data
    project_name = env_values["REDCAP_PROJECT_NAME"]
    hint_text(
        f"⚠️ IMPORTANT: Ensure compliance with data storage policies when uploading records "
        f"to the REDCap project '{project_name}'."
    )
    between_section_separator()

    # Ensure the input file exists
    if not input_file.exists():
        error_text(f"❌ File not found: {input_file}")
        raise typer.Exit(1)

    # Read the JSON file
    try:
        with open(input_file, 'r') as file:
            records = json.load(file)
        typer.echo(f"✅ Successfully read {len(records)} instances from {input_file}")
    except Exception as e:
        error_text(f"❌ Error reading JSON file: {e}")
        raise typer.Exit(1)

    # Step 1: Validate LinkML data
    typer.echo("🔄 Validating LinkML data before transformation...")
    
    # Step 1a: Write records to a temporary file
    try:
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
            json.dump(records, temp_file, indent=2)
            temp_file_path = temp_file.name
        
        # Validate using the temporary file
        if not validate_linkml_data(BASE_SCHEMA_PATH, Path(temp_file_path)):
            error_text("❌ Validation of LinkML data failed.")
            raise typer.Exit(1)
        
        success_text("✅ Validation successful!")
    except Exception as e:
        error_text(f"❌ Validation failed: {e}")
        raise typer.Exit(1)
    
    # Step 2: Transform LinkML data to REDCap flat format using MAPPING_FUNCTIONS
    # Define the output processed file path (with project name)
    sanitized_project_name = project_name.replace(" ", "_")
    processed_file = Path(DEFAULT_OUTPUT_DIR) / f"{sanitized_project_name}-import-records.json"

    try:
        # Pass the records and MAPPING_FUNCTIONS to the transformation function
        # The function now writes the transformed data to the processed_file internally
        linkml_to_redcap(records, processed_file, MAPPING_FUNCTIONS)
    except Exception as e:
        error_text(f"❌ Error in transformation: {e}")
        raise typer.Exit(1)

    # Read the processed file to prepare for upload
    try:
        with open(processed_file, 'r') as file:
            flat_records = json.load(file)
        typer.echo(f"✅ Successfully read {len(flat_records)} instances from {processed_file}")
    except Exception as e:
        error_text(f"❌ Error reading processed file: {e}")
        raise typer.Exit(1)

    # Prepare data to upload to REDCap
    data = json.dumps(flat_records)
    fields = {
        'token': api_token,
        'content': 'record',
        'format': 'json',
        'type': 'flat',
        'data': data,
    }

    # Set up logging
    log_file = Path(f"{input_file.stem}_upload.log")
    logger = setup_logger("upload_record", log_file=log_file)

    try:
        # Make the API request to upload the records
        typer.echo(f"🔄 Uploading {len(flat_records)} instances to REDCap project '{project_name}'...")
        r = requests.post(api_url, data=fields)
        
        # Check the response status
        if r.status_code == 200:
            typer.echo(f"✅ Successfully uploaded {len(flat_records)} instances.")
            success_text(f"Response: {r.text}")
        else:
            typer.echo(f"❌ Failed to upload records. HTTP Status: {r.status_code}")
            error_text(f"Error response: {r.text}")
            raise typer.Exit(1)

    except Exception as e:
        error_text(f"❌ Error: {e}")
        raise typer.Exit(1)

    end_of_section_separator()

if __name__ == "__main__":
    app()
