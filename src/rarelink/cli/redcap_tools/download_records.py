import typer
from pathlib import Path
import requests
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
from rarelink.cli.utils.file_utils import ensure_directory_exists, write_json
from rarelink.cli.utils.logging_utils import setup_logger, log_info
from rarelink.utils.mapping import MAPPING_FUNCTIONS
from rarelink.utils.processing.schemas import preprocess_flat_data


from rarelink.cli.utils.validation_utils import validate_env

app = typer.Typer()

DEFAULT_CONFIG_FILE = Path.home() / "Downloads" / "rarelink_apiconfig.json"
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"
ENV_PATH = Path(".env")  # Path to your .env file

@app.callback(invoke_without_command=True)
def download_records(output_dir: Path = DEFAULT_OUTPUT_DIR):
    """
    Fetch records from the configured REDCap project, save them locally as a
    JSON file, process them into the RareLink-CDM schema, and validate the 
    output.

    Args:
        output_dir (Path): Directory to save the fetched and processed records.
        \n Defaults to ~/Downloads/rarelink_records.
    """
    format_header("Fetch REDCap Records")

    # Validate environment
    validate_env(["BIOPORTAL_API_TOKEN", "REDCAP_API_TOKEN",
                  "REDCAP_URL", "REDCAP_PROJECT_ID"])

    # Display alert about production mode
    hint_text(
        "⚠️ IMPORTANT: If your project is in PRODUCTION mode, the downloaded"
        " data might be sensitive. \n"
        "It must only be stored within your organisational site's "
        "approved storage."
    )
    between_section_separator()

    # Load environment variables
    env_values = dotenv_values(ENV_PATH)
    api_token = env_values["REDCAP_API_TOKEN"]
    api_url = env_values["REDCAP_URL"]

    # Ensure output directory exists
    ensure_directory_exists(output_dir)

    output_file = output_dir / "records.json"
    processed_file = output_dir / "processed_records.json"

    # Check for existing files and ask for confirmation to overwrite
    if output_file.exists() or processed_file.exists():
        typer.secho(
            f"⚠️ Files already exist in the output directory: {output_dir}",
            fg=typer.colors.YELLOW
        )
        if not typer.confirm("Do you want to overwrite these files?"):
            typer.secho("❌ Operation canceled by the user.", fg=typer.colors.RED)
            raise typer.Exit(0)

    # Set up logger
    log_file = output_dir / "download_records.log"
    logger = setup_logger("download_records", log_file=log_file)

    # Prepare API request
    fields = {
        "token": api_token,
        "content": "record",
        "format": "json",
        "type": "flat",
    }

    try:
        # Send request to REDCap API
        response = requests.post(api_url, data=fields)
        response.raise_for_status()

        # Save the fetched data to a JSON file
        records = response.json()
        write_json(records, output_file)

        # Process the records into the RareLink-CDM schema
        typer.echo(
            "🔄 Processing records into the RareLink-CDM LinkML schema...")
        transformed_data = preprocess_flat_data(records, MAPPING_FUNCTIONS)
        write_json(transformed_data, processed_file)

        typer.echo(f"✅ Processed data saved to {processed_file}")
        
        # Validate the processed data against the LinkML schema
        typer.echo("🔄 Validating processed records against the "
                    "RareLink-CDM LinkML schema...")
        schema_path =\
            "src/rarelink_cdm/v2_0_0_dev0/schema_definitions/rarelink_cdm.yaml"

        try:
            import subprocess

            result = subprocess.run(
                ["linkml-validate", "--schema", str(schema_path),
                 str(processed_file)],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                success_text("✅ Validation successful!")
            else:
                typer.secho(
                    error_text(f"❌ Validation failed:\n{result.stderr}"),
                    fg=typer.colors.RED,
                )
        except FileNotFoundError:
            typer.secho(
                error_text(
                    "❌ Validation tool not found. Ensure 'linkml-validate' "
                    "is installed."),
                fg=typer.colors.RED,
            )

    except requests.exceptions.RequestException as e:
        log_info(logger, f"❌ Failed to fetch records: {e}")
        typer.secho(error_text(f"❌ Failed to fetch records: {e}"), 
                    fg=typer.colors.RED)
        raise typer.Exit(1)

    end_of_section_separator()


if __name__ == "__main__":
    app()
