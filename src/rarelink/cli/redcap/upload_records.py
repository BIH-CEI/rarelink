import json
import requests
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
from rarelink.cli.utils.logging_utils import setup_logger
import logging

logger = logging.getLogger(__name__)
app = typer.Typer()

REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
ENV_PATH = Path(".env")  # Path to your .env file

# REDCap API configuration from environment
@app.command()
def app(input_file: Path):
    """
    Upload a JSON file to REDCap.

    Args:
        input_file (Path): Path to the JSON file containing records to upload.
    """
    format_header("Upload Records to REDCap")

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
        typer.echo(f"✅ Successfully read {len(records)} records from {input_file}")
    except Exception as e:
        error_text(f"❌ Error reading JSON file: {e}")
        raise typer.Exit(1)

    # Prepare data to upload to REDCap
    data = json.dumps(records)
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
        typer.echo(f"🔄 Uploading {len(records)} records to REDCap project '{project_name}'...")
        r = requests.post(api_url, data=fields)
        
        # Check the response status
        if r.status_code == 200:
            typer.echo(f"✅ Successfully uploaded {len(records)} records.")
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
