import typer
from pathlib import Path
import requests
import json
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator,
    between_section_separator,
)
from rarelink.cli.utils.string_utils import (
    format_header,
    success_text,
    error_text,
    format_command,
    hint_text,
)
from rarelink.cli.utils.file_utils import ensure_directory_exists, write_json
from rarelink.cli.utils.logging_utils import setup_logger, log_info
from rarelink_cdm.v2_0_0_dev0.processing import preprocess_flat_data, MAPPING_FUNCTIONS

app = typer.Typer()

DEFAULT_CONFIG_FILE = Path.home() / "Downloads" / "rarelink_redcap_config.json"
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "rarelink_records"


@app.callback(invoke_without_command=True)
def download_records(output_dir: Path = DEFAULT_OUTPUT_DIR):
    """
    Fetch records from the configured REDCap project, save them locally as a\n
    JSON file, process them into the RareLink-CDM schema, and validate the output.

    Args:
        output_dir (Path): Directory to save the fetched and processed records.\n Defaults to ~/Downloads/rarelink_records.
    """
    format_header("Fetch REDCap Records")

    # Display alert about production mode
    hint_text(
        "⚠️ IMPORTANT: If your project is in PRODUCTION mode, the downloaded data might be sensitive.\n"
        "It must only be stored within your organisational site's approved storage."
    )
    between_section_separator()

    # Check if the API configuration has been set up
    api_config_done = typer.confirm("Have you already set up an API configuration file?")
    if not api_config_done:
        typer.echo(
            f"👉 Please run the following command to set up your REDCap API configuration: {format_command('rarelink redcap-setup api-config start')}",
        )
        raise typer.Exit(code=1)

    # Prompt for the path to the API configuration file
    config_file_path = typer.prompt(
        "Enter the path to your API configuration file", default=str(DEFAULT_CONFIG_FILE)
    )
    config_file = Path(config_file_path)

    if not config_file.exists():
        typer.secho(
            error_text(f"❌ Configuration file not found at {config_file_path}."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    # Load configuration
    try:
        config = config_file.read_text()
        config_data = json.loads(config)
    except Exception as e:
        typer.secho(error_text(f"❌ Failed to load configuration: {e}"), 
                    fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # Ensure output directory exists
    ensure_directory_exists(output_dir)

    # Set up logger
    log_file = output_dir / "download_records.log"
    logger = setup_logger("download_records", log_file=log_file)

    # Prepare API request
    fields = {
        "token": config_data["api_token"],
        "content": "record",
        "format": "json",
        "type": "flat",
    }

    try:
        # Send request to REDCap API
        response = requests.post(config_data["api_url"], data=fields)
        response.raise_for_status()

        # Save the fetched data to a JSON file
        records = response.json()
        output_file = output_dir / "records.json"
        write_json(records, output_file)

        log_info(logger, f"✅ Records successfully downloaded to {output_file}")
        success_text(f"✅ Records successfully downloaded to {output_file}")

        # Process the records into the RareLink-CDM schema
        success_text("🔄 Processing records into the RareLink-CDM schema...")
        transformed_data = preprocess_flat_data(records, MAPPING_FUNCTIONS)
        processed_file = output_dir / "processed_records.json"
        write_json(transformed_data, processed_file)

        success_text(f"✅ Processed data saved to {processed_file}")

        # Validate the processed data against the LinkML schema
        schema_path = "src/rarelink_cdm/v2_0_0_dev0/schema_definitions/rarelink_cdm.yaml"

        try:
            import subprocess

            result = subprocess.run(
                ["linkml-validate", "--schema", str(schema_path), str(processed_file)],
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
                    "❌ Validation tool not found. Ensure 'linkml-validate' is installed."),
                fg=typer.colors.RED,
            )
    except requests.exceptions.RequestException as e:
        log_info(logger, f"❌ Failed to fetch records: {e}")
        typer.secho(error_text(f"❌ Failed to fetch records: {e}"), 
                    fg=typer.colors.RED)
        raise typer.Exit(code=1)

    end_of_section_separator()


if __name__ == "__main__":
    app()
