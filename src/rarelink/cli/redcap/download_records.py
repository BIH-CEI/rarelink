import typer
from pathlib import Path
from typing import Optional
import logging
import importlib.resources as resources 
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
    format_command
)
from rarelink.cli.utils.validation_utils import validate_env
from rarelink.cli.utils.file_utils import ensure_directory_exists
from rarelink.utils.redcap import fetch_redcap_data
from rarelink.utils.schema_processing import redcap_to_linkml
from rarelink_cdm import import_from_latest, get_latest_version

def validate_linkml_data(*args, **kwargs):
    """
    Lazy import to avoid utils <-> cli circular import during module import.
    Test patches target this symbol: rarelink.cli.redcap.download_records.validate_linkml_data
    """
    from rarelink.utils.validation import validate_linkml_data as _impl
    return _impl(*args, **kwargs)

logger = logging.getLogger(__name__)
app = typer.Typer()

try:
    _redcap = import_from_latest("mappings.redcap")
    MAPPING_FUNCTIONS = getattr(_redcap, "MAPPING_FUNCTIONS")
except Exception as e:
    logging.getLogger(__name__).error(f"Could not import MAPPING_FUNCTIONS from latest CDM: {e}")
    raise

REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
ENV_PATH = Path(".env")  # Path to your .env file

def _resolve_latest_schema_path() -> Path:
    """
    Finds the rarelink_cdm YAML schema in the latest vX_Y_Z package using
    importlib.resources, and returns a concrete filesystem Path.
    """
    latest = get_latest_version()  # e.g., 'v2_0_2'
    package = f"rarelink_cdm.{latest}.schema_definitions"
    try:
        # NOTE: files() returns a Traversable; / "rarelink_cdm.yaml" appends the filename
        schema_res = resources.files(package) / "rarelink_cdm.yaml"
        # Some tools need a real path on disk; as_file extracts to a temp file if needed
        with resources.as_file(schema_res) as p:
            return Path(p)
    except Exception as e:
        logger.error(f"Failed to locate latest CDM schema in package '{package}': {e}")
        raise

# late-bound default; only computed if --rarelink-cdm is chosen
BASE_SCHEMA_PATH: Optional[Path] = None

RARELINK_CDM_INSTRUMENTS = [
    "rarelink_1_formal_criteria",
    "rarelink_2_personal_information",
    "rarelink_3_patient_status",
    "rarelink_4_care_pathway",
    "rarelink_5_disease",
    "rarelink_6_1_genetic_findings",
    "rarelink_6_2_phenotypic_feature",
    "rarelink_6_3_measurements",
    "rarelink_6_4_family_history",
    "rarelink_7_consent",
    "rarelink_8_disability"
]
@app.command()
def app(
    output_dir: Path = typer.Option(DEFAULT_OUTPUT_DIR, "--output-dir", "-o", help="Directory to save fetched and processed records"),
    records: str = typer.Option(None, "--records", "-r", help="Specific record IDs to fetch (comma-separated, e.g., '101,102,103')"),
    instruments: str = typer.Option(None, "--instruments", "-i", help="Specific instruments/forms to fetch (comma-separated, e.g., 'form1,form2')"),
    linkml_schema: Optional[Path] = typer.Option(None, "--linkml", "-l", help="Path to custom LinkML schema for validation"),
    rarelink_cdm: Optional[bool] = typer.Option(None, "--rarelink-cdm", help="Use RareLink-CDM instruments and schema"),
    filter_logic: Optional[str] = typer.Option(None, "--filter", help="REDCap filter logic to apply (e.g. [age] > 30)"),
):
    """
    Fetch REDCap records, process them into the RareLink-CDM schema,
    validate the output, and save the results.
    
    This enhanced version allows fetching specific records and instruments,
    and will interactively prompt for RareLink-CDM usage or custom schema validation.
    """
    global BASE_SCHEMA_PATH
    format_header("Fetch and Process REDCap Records")

    # Validate required environment variables
    validate_env(["REDCAP_API_TOKEN", "REDCAP_URL", "REDCAP_PROJECT_NAME"])
    
    # Load environment variables
    env_values = dotenv_values(ENV_PATH)
    project_name = env_values["REDCAP_PROJECT_NAME"]
    api_url = env_values["REDCAP_URL"]
    api_token = env_values["REDCAP_API_TOKEN"]

    # Sanitize project name: replace spaces with underscores
    sanitized_project_name = project_name.replace(" ", "_")
    
    # Interactive prompts
    # Ask about RareLink-CDM if not specified
    if rarelink_cdm is None:
        rarelink_cdm = typer.confirm(
            "Are you using RareLink-CDM instruments and want to validate against RareLink-CDM schema?",
            default=False,
        )
    
    # Ask about custom LinkML schema if not using RareLink-CDM
    if not rarelink_cdm and linkml_schema is None:
        use_custom_schema = typer.confirm(
            "Do you have a custom LinkML schema available for validation?",
            default=False,
        )
        if use_custom_schema:
            schema_path = typer.prompt(
                "Enter the path to your LinkML schema file",
                type=Path,
            )
            linkml_schema = schema_path
    
    # Ask about specific records if not provided
    if records is None:
        fetch_specific_records = typer.confirm(
            "Do you want to fetch specific record IDs?",
            default=False,
        )
        if fetch_specific_records:
            record_ids = typer.prompt(
                "Enter comma-separated record IDs to fetch",
                default="",
            )
            if record_ids:
                records = record_ids
    
    # Ask about specific instruments if not using RareLink-CDM or not provided
    if not rarelink_cdm and instruments is None:
        fetch_specific_instruments = typer.confirm(
            "Do you want to fetch specific REDCap instruments/forms?",
            default=False,
        )
        if fetch_specific_instruments:
            instrument_names = typer.prompt(
                "Enter comma-separated instrument names to fetch",
                default="",
            )
            if instrument_names:
                instruments = instrument_names
                
    # Process records string into a list if provided
    record_list = None
    if records:
        record_list = [r.strip() for r in records.split(",")]
        
    # Process instruments string into a list if provided
    instrument_list = None
    if instruments:
        instrument_list = [i.strip() for i in instruments.split(",")]
    
    # Apply RareLink-CDM instruments if selected
    selected_instruments = instrument_list or []
    if rarelink_cdm:
        # Add RareLink instruments to any additional specified instruments
        for instrument in RARELINK_CDM_INSTRUMENTS:
            if instrument not in selected_instruments:
                selected_instruments.append(instrument)
        typer.echo(f"🔍 Using RareLink-CDM instruments: {', '.join(RARELINK_CDM_INSTRUMENTS)}")
        
        # If additional instruments were specified, show them too
        additional = [i for i in selected_instruments if i not in RARELINK_CDM_INSTRUMENTS]
        if additional:
            typer.echo(f"🔍 Additional instruments selected: {', '.join(additional)}")
    elif selected_instruments:
        typer.echo(f"🔍 Using specified instruments: {', '.join(selected_instruments)}")

    # Also validate BioPortal token if we'll be doing validation
    if rarelink_cdm or linkml_schema:
        validate_env(["BIOPORTAL_API_TOKEN"])

    # Display caution message for sensitive data
    hint_text(
        f"⚠️ IMPORTANT: If your project '{sanitized_project_name}' is in "
        "PRODUCTION mode, ensure compliance with data storage policies."
    )
    between_section_separator()

    # Ensure output directory exists
    ensure_directory_exists(output_dir)

    # Define output file paths with sanitized project name
    records_file = output_dir / f"{sanitized_project_name}-records.json"
    processed_file = output_dir / f"{sanitized_project_name}-linkml-records.json"

    # Check for existing files and prompt for overwrite confirmation
    if records_file.exists() or processed_file.exists():
        typer.secho(
            f"⚠️ Files already exist in the output directory: {output_dir}",
            fg=typer.colors.YELLOW,
        )
        if not typer.confirm("Do you want to overwrite these files?"):
            typer.secho("❌ Operation canceled by the user.", 
                        fg=typer.colors.RED)
            raise typer.Exit(0)

    # Determine which schema to use for validation
    validation_schema = None
    if rarelink_cdm:
        # Resolve the latest RareLink CDM schema only when needed
        if BASE_SCHEMA_PATH is None:
            BASE_SCHEMA_PATH = _resolve_latest_schema_path()
        validation_schema = BASE_SCHEMA_PATH
        typer.echo(f"🔄 Using RareLink CDM schema for validation: {validation_schema}")
    elif linkml_schema:
        validation_schema = linkml_schema
        typer.echo(f"🔄 Using custom LinkML schema for validation: {validation_schema}")
        if not validation_schema.exists():
            typer.secho(
                error_text(f"❌ Schema file not found: {validation_schema}"),
                fg=typer.colors.RED
            )
            raise typer.Exit(1)

    try:
        # Prepare REDCap API parameters
        api_params = {
            "format": "json",
            "filterLogic": filter_logic,
        }
        
        # Add specific records if provided
        if record_list:
            api_params["records"] = record_list
            record_info = f" for {len(record_list)} specific records"
        else:
            record_info = ""
            
        # Add specific instruments if provided
        if selected_instruments:
            api_params["forms"] = selected_instruments
            form_info = f" from {len(selected_instruments)} instruments"
        else:
            form_info = ""
            
        # Fetch REDCap data
        typer.echo(
            f"🔄 Fetching records{record_info}{form_info} for project '{sanitized_project_name}' "
            f"from REDCap..."
        )
        fetch_redcap_data(api_url, api_token, project_name, output_dir, api_params)
        typer.echo(f"✅ Raw data saved to {records_file}")

        # Process REDCap data into LinkML format
        typer.echo(f"🔄 Processing records for project "
                   f"'{sanitized_project_name}'...")
        redcap_to_linkml(records_file, processed_file, MAPPING_FUNCTIONS)
        typer.echo(f"✅ Processed data saved to {processed_file}")
        
        # Validation (if schema provided)
        if validation_schema:
            typer.echo(
                "🔄 Validating processed records against the LinkML schema..."
            )
            if validate_linkml_data(validation_schema, processed_file):
                success_text("✅ Validation successful!")
            else:
                error_text(f"❌ Validation failed for {processed_file}")
                hint_text(
                    f"👉 Run {format_command('linkml-validate --schema ' + str(validation_schema) + ' ' + str(processed_file))}"
                    f" to see the detailed validation errors."
                )
        else:
            # No validation requested - provide hint
            typer.secho(
                "ℹ️ No validation performed. For best results, validate your data against a schema.",
                fg=typer.colors.BLUE
            )
            hint_text(
                f"👉 To validate against RareLink CDM schema: {format_command('rarelink redcap download-records --rarelink-cdm')}"
            )
            hint_text(
                f"👉 To validate against a custom schema: {format_command('rarelink redcap download-records --linkml /path/to/schema.yaml')}"
            )
        
        # HGVS validation hint
        hint_text(
            f"⚠️ NOTE: If genetic HGVS mutations are included in your "
            f"dataset, please run {format_command('rarelink redcap validate-hgvs')}"
        )
        hint_text("to ensure proper phenopackets and genomics quality of the "
                  "genetic data.")

    except ValueError as e:
        if "No records found matching" in str(e):
            error_text(f"❌ {e}")
            hint_text("Please check that the specified record IDs exist in your REDCap project.")
            raise typer.Exit(1)
        else:
            error_text(f"❌ Error: {e}")
            raise typer.Exit(1)
    except Exception as e:
        error_text(f"❌ Error: {e}")
        raise typer.Exit(1)

    end_of_section_separator()


if __name__ == "__main__":
    app()