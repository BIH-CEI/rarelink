import json
import requests
import typer
from pathlib import Path
from dotenv import dotenv_values
import importlib.resources as resources 
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator,
    between_section_separator,
)
from rarelink.cli.utils.string_utils import (
    format_command,
    format_header,
    success_text,
    error_text,
    hint_text,
)
from rarelink.cli.utils.validation_utils import validate_env
from rarelink.utils.schema_processing import linkml_to_redcap  
from rarelink_cdm import get_latest_version, import_from_latest
import logging

def validate_linkml_data(*args, **kwargs):
    from rarelink.utils.validation import validate_linkml_data as _impl
    return _impl(*args, **kwargs)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
app = typer.Typer()

try:
    _redcap = import_from_latest("mappings.redcap")
    REVERSE_PROCESSING = getattr(_redcap, "REVERSE_PROCESSING")
except Exception as e:
    logging.getLogger(__name__).error(f"Could not import REVERSE_PROCESSING from latest CDM: {e}")
    raise

DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
ENV_PATH = Path(".env")

def _resolve_latest_schema_path() -> Path:
    """
    Locate the LinkML schema file inside the latest rarelink_cdm vX_Y_Z
    package and return a concrete Path on disk.
    """
    latest = get_latest_version()  # e.g., 'v2_0_2'
    pkg = f"rarelink_cdm.{latest}.schema_definitions"
    res = resources.files(pkg) / "rarelink_cdm.yaml"
    # as_file extracts to a temp file if needed so tools can read a real path
    with resources.as_file(res) as p:
        return Path(p)

def _load_latest_template_dict() -> dict:
    """
    Load the REDCap template.json from the latest rarelink_cdm package.
    """
    latest = get_latest_version()
    pkg = f"rarelink_cdm.{latest}.mappings.redcap"
    res = resources.files(pkg) / "template.json"
    with resources.as_file(res) as p:
        return json.loads(Path(p).read_text(encoding="utf-8"))

@app.command()
def app(input_file: Path = typer.Option(
    None, prompt="Enter the path to the JSON file containing LinkML records")):
    """
    Upload a validated LinkML JSON file to REDCap after transforming 
    it to the appropriate format.
    """
    format_header("Upload Records to REDCap")

    # Validate required environment variables
    validate_env(["REDCAP_API_TOKEN", "REDCAP_URL", "REDCAP_PROJECT_NAME"])

    # Load environment variables
    env_values = dotenv_values(ENV_PATH)
    api_url = env_values["REDCAP_URL"]
    api_token = env_values["REDCAP_API_TOKEN"]
    project_name = env_values["REDCAP_PROJECT_NAME"]

    # Display caution message for sensitive data
    hint_text(
        f"⚠️ IMPORTANT: Ensure compliance with data storage policies when "
        f"uploading records to the REDCap project '{project_name}'."
    )
    hint_text(
        f"NOTE: Data with the same record-ID will be overwritten in the REDCap "
        f"project! Make sure you have a backup of the data before proceeding: "
        f"run {format_command('`rarelink redcap download-records`')}"
    )
    typer.confirm("Do you want to proceed?", abort=True)
        
    between_section_separator()

    # Ensure the input file exists
    if not input_file.exists():
        error_text(f"❌ File not found: {input_file}")
        raise typer.Exit(1)

    # Step 1: Validate LinkML data
    typer.echo("🔄 Validating LinkML data before transformation...")
    schema_path = _resolve_latest_schema_path()
    if not validate_linkml_data(schema_path, input_file):
        error_text(
            "❌ Validation of LinkML data failed. "
            f"Please run {format_command(f'linkml-validate --schema {schema_path} {input_file}')} for details"
        )
        raise typer.Exit(1)
    success_text("✅ Validation successful!")

    # Step 2: Count `record_id` instances in the input file
    try:
        with open(input_file, 'r') as file:
            input_data = json.load(file)
        record_id_count = len(input_data)
    except Exception as e:
        error_text(f"❌ Error reading input file: {e}")
        raise typer.Exit(1)

    # Step 3: Transform LinkML data to REDCap flat format using MAPPING_FUNCTIONS
    processed_file = DEFAULT_OUTPUT_DIR / f"{project_name.replace(' ', '_')}-import-records.json"

    try:
        template_dict = _load_latest_template_dict()
    except Exception as e:
        error_text(f"❌ Error loading template.json from latest CDM: {e}")
        raise typer.Exit(1)

    linkml_to_redcap(input_file, processed_file, template_dict, REVERSE_PROCESSING)

    # Step 4: Read the processed file to prepare for upload
    try:
        with open(processed_file, 'r') as file:
            flat_records = json.load(file)
        typer.echo(f"✅ Processed file contains {record_id_count} flattened records "
                   f"for upload to REDCap.")
    except Exception as e:
        error_text(f"❌ Error reading processed file: {e}")
        raise typer.Exit(1)

    # Step 5: Prepare data to upload to REDCap
    data = json.dumps(flat_records)
    fields = {
        'token': api_token,
        'content': 'record',
        'format': 'json',
        'type': 'flat',
        'data': data,
    }

    # Make the API request to upload the records
    try:
        typer.echo(f"🔄 Uploading {record_id_count} records to "
                   f"REDCap project '{project_name}'...")
        response = requests.post(api_url, data=fields)
        if response.status_code == 200:
            success_text(
                f"✅ Successfully uploaded {record_id_count} records.")
        else:
            error_text(f"❌ Failed to upload records. HTTP Status: "
                       f"{response.status_code} - Error response: "
                       f"{response.text}")
            raise typer.Exit(1)
    except Exception as e:
        error_text(f"❌ Error: {e}")
        raise typer.Exit(1)

    end_of_section_separator()
