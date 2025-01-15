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
from rarelink.cli.utils.logging_utils import setup_logger, log_info
from rarelink.utils.loading.fetch import fetch_redcap_data
from rarelink.utils.processing.schemas import process_redcap_data
from rarelink.utils.validation import validate_linkml_data
from rarelink.utils.loading.project_and_schema import load_project_and_schema_info
from rarelink_cdm.v2_0_0_dev0.mappings.redcap import MAPPING_FUNCTIONS

app = typer.Typer()

DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
ENV_PATH = Path(".env")  # Path to your .env file


@app.command()
def download_records(output_dir: Path = DEFAULT_OUTPUT_DIR):
    """
    Fetch REDCap records, process them into the RareLink-CDM schema, 
    and validate the output.
    
    Args:
        output_dir (Path): Directory to save fetched and processed records.
        Defaults to ~/Downloads/rarelink_records.
    """
    format_header("Fetch REDCap Records")

    # Validate required environment variables
    validate_env(["BIOPORTAL_API_TOKEN", "REDCAP_API_TOKEN", "REDCAP_URL", "REDCAP_PROJECT_ID"])

    # Display a caution message for sensitive data
    hint_text(
        "⚠️ IMPORTANT: If your project is in PRODUCTION mode, the downloaded data"
        " might be sensitive. Ensure compliance with data storage policies."
    )
    between_section_separator()

    # Load project and schema information
    project_info = load_project_and_schema_info(ENV_PATH)
    project_name = project_info["project_name"]
    schema_name = project_info["schema_name"]

    # Ensure output directory exists
    ensure_directory_exists(output_dir)

    # Define paths for output files
    records_file = output_dir / f"{project_name}-records.json"
    processed_file = output_dir / f"{schema_name}_linkml.json"

    # Check for existing files and prompt for overwrite confirmation
    if records_file.exists() or processed_file.exists():
        typer.secho(f"⚠️ Files already exist in the output directory: {output_dir}", fg=typer.colors.YELLOW)
        if not typer.confirm("Do you want to overwrite these files?"):
            typer.secho("❌ Operation canceled by the user.", fg=typer.colors.RED)
            raise typer.Exit(0)

    # Set up logging
    log_file = output_dir / "download_records.log"
    logger = setup_logger("download_records", log_file=log_file)

    try:
        # Fetch REDCap data
        api_url = dotenv_values(ENV_PATH)["REDCAP_URL"]
        api_token = dotenv_values(ENV_PATH)["REDCAP_API_TOKEN"]
        typer.echo("🔄 Fetching records from REDCap...")
        fetch_redcap_data(api_url, api_token, project_name, output_dir)
        typer.echo(f"✅ Records saved to {records_file}")

        # Process REDCap data
        typer.echo("🔄 Processing records into the RareLink-CDM schema...")
        process_redcap_data(records_file, MAPPING_FUNCTIONS, schema_name, output_dir)
        typer.echo(f"✅ Processed data saved to {processed_file}")

        # Validate the processed data
        schema_path = Path("src/rarelink_cdm/v2_0_0_dev0/schema_definitions/rarelink_cdm.yaml")
        typer.echo("🔄 Validating processed records against the LinkML schema...")
        if validate_linkml_data(schema_path, processed_file):
            success_text("✅ Validation successful!")
        else:
            typer.secho(error_text(f"❌ Validation failed for {processed_file}"), fg=typer.colors.RED)

    except Exception as e:
        log_info(logger, f"❌ Error: {e}")
        typer.secho(error_text(f"❌ Error: {e}"), fg=typer.colors.RED)
        raise typer.Exit(1)

    end_of_section_separator()


if __name__ == "__main__":
    app()
