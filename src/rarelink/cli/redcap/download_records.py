import typer
from pathlib import Path
from typing import Optional
import logging
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
from rarelink.utils.validation import validate_linkml_data
from rarelink_cdm.v2_0_0_dev1.mappings.redcap import MAPPING_FUNCTIONS

logger = logging.getLogger(__name__)
app = typer.Typer()

REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
BASE_SCHEMA_PATH = REPO_ROOT / "src/rarelink_cdm/v2_0_0_dev1/schema_definitions/rarelink_cdm.yaml"
ENV_PATH = Path(".env")  # Path to your .env file


@app.command()
def app(
    output_dir: Path = typer.Option(DEFAULT_OUTPUT_DIR, "--output-dir", "-o", help="Directory to save fetched and processed records"),
    linkml_schema: Optional[Path] = typer.Option(None, "--linkml", "-l", help="Path to custom LinkML schema for validation"),
    rarelink_cdm: bool = typer.Option(False, "--rarelink-cdm", help="Validate against the RareLink CDM schema"),
):
    """
    Fetch REDCap records, process them into the RareLink-CDM schema,
    validate the output, and save the results.
    """
    format_header("Fetch and Process REDCap Records")

    # Validate required environment variables
    validate_env(["REDCAP_API_TOKEN", "REDCAP_URL", "REDCAP_PROJECT_NAME"])
    
    # Also validate BioPortal token if we'll be doing validation
    if rarelink_cdm or linkml_schema:
        validate_env(["BIOPORTAL_API_TOKEN"])

    # Load environment variables
    env_values = dotenv_values(ENV_PATH)
    project_name = env_values["REDCAP_PROJECT_NAME"]
    api_url = env_values["REDCAP_URL"]
    api_token = env_values["REDCAP_API_TOKEN"]

    # Sanitize project name: replace spaces with underscores
    sanitized_project_name = project_name.replace(" ", "_")

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
        # Fetch REDCap data
        typer.echo(
            f"🔄 Fetching records for project '{sanitized_project_name}' "
            f"from REDCap..."
        )
        fetch_redcap_data(api_url, api_token, project_name, output_dir)

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

    except Exception as e:
        error_text(f"❌ Error: {e}")
        raise typer.Exit(1)

    end_of_section_separator()


if __name__ == "__main__":
    app()