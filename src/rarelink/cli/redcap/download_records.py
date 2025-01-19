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
from rarelink.utils.loading import fetch_redcap_data
from rarelink.utils.processing.schemas import redcap_to_linkml
from rarelink.utils.validation import validate_linkml_data
from rarelink_cdm.v2_0_0_dev0.mappings.redcap import MAPPING_FUNCTIONS
import logging


logger = logging.getLogger(__name__)
app = typer.Typer()

REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
BASE_SCHEMA_PATH = REPO_ROOT / "src/rarelink_cdm/v2_0_0_dev0/schema_definitions/rarelink_cdm.yaml"
ENV_PATH = Path(".env")  # Path to your .env file


@app.command()
def app(output_dir: Path = DEFAULT_OUTPUT_DIR):
    """
    Fetch REDCap records, process them into the RareLink-CDM schema,
    validate the output, and save the results.

    Args:
        output_dir (Path): Directory to save fetched and processed records.
        Defaults to ~/Downloads/rarelink_records.
    """
    format_header("Fetch and Process REDCap Records")

    # Validate required environment variables
    validate_env(["BIOPORTAL_API_TOKEN", 
                  "REDCAP_API_TOKEN",
                  "REDCAP_URL", 
                  "REDCAP_PROJECT_NAME"])

    # Load environment variables
    env_values = dotenv_values(ENV_PATH)
    project_name = env_values["REDCAP_PROJECT_NAME"]
    api_url = env_values["REDCAP_URL"]
    api_token = env_values["REDCAP_API_TOKEN"]

    # Display caution message for sensitive data
    hint_text(
        f"⚠️ IMPORTANT: If your project '{project_name}' is in PRODUCTION mode, "
        "ensure compliance with data storage policies."
    )
    between_section_separator()

    # Ensure output directory exists
    ensure_directory_exists(output_dir)

    # Define output file paths
    records_file = output_dir / f"{project_name}-records.json"
    processed_file = output_dir / f"{project_name}-linkml-records.json"

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

    # Set up logging
    log_file = output_dir / "download_records.log"
    logger = setup_logger("fetch_and_process", log_file=log_file)

    try:
        # Fetch REDCap data
        typer.echo(
            f"🔄 Fetching records for project '{project_name}' from REDCap...")
        fetch_redcap_data(api_url, api_token, project_name, output_dir)
        typer.echo(f"✅ Records saved to {records_file}")

        # Process REDCap data using `redcap_to_linkml`
        typer.echo(f"🔄 Processing records for project '{project_name}'...")
        redcap_to_linkml(records_file, processed_file, MAPPING_FUNCTIONS)
        typer.echo(f"✅ Processed data saved to {processed_file}")
        
        # Validation
        typer.echo(
            "🔄 Validating processed records against the LinkML schema...")
        if validate_linkml_data(BASE_SCHEMA_PATH, processed_file):
            success_text("✅ Validation successful!")
        else:
            error_text(f"❌ Validation failed for {processed_file}")

    except Exception as e:
        error_text(f"❌ Error: {e}")
        raise typer.Exit(1)

    end_of_section_separator()


if __name__ == "__main__":
    app()
