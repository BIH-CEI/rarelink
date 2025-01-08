import typer
from pathlib import Path
import requests
from dotenv import dotenv_values
from rarelink.cli.utils.string_utils import (
    error_text,
    success_text,
    hint_text,
    format_header,
    hyperlink,
    format_command,
)
from rarelink.cli.utils.terminal_utils import end_of_section_separator, confirm_action
from rarelink.cli.utils.file_utils import download_file
from rarelink.cli.utils.version_utils import get_current_version

app = typer.Typer()

# Documentation and download URLs
DOCS_RD_CDM_URL = "https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html"
DOCS_REDCAP_PROJECT_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_2_setup_redcap_project.html"
DOCS_UPLOAD_DATA_DICTIONARY_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_3_setup_rarelink_instruments.html"
CHANGELOG_URL = "https://rarelink.readthedocs.io/en/latest/6_changelog.html"
DATA_DICTIONARY_DOWNLOAD_URL = "https://rarelink.readthedocs.io/en/latest/_downloads/<hashed_path>/rarelink_cdm_datadictionary%20-%20v2_0_0_dev0.csv"
downloads_folder = Path.home() / "Downloads"

@app.command()
def app():
    """
    Upload the most current RareLink-CDM Data Dictionary to an existing REDCap project.
    """
    format_header("RareLink-CDM Data Dictionary Upload")

    # Load configuration from .env
    env_values = dotenv_values(".env")
    api_url = env_values.get("REDCAP_PROJECT_URL")
    api_token = env_values.get("REDCAP_API_TOKEN")

    # Check if configuration is valid
    if not api_url or not api_token:
        typer.secho(
            error_text(
                "❌ Missing REDCap configuration in .env. Ensure the following keys are set:\n"
                "- REDCAP_PROJECT_URL\n"
                "- REDCAP_API_TOKEN"
            ),
            fg=typer.colors.RED,
        )
        typer.echo(
            f"Run {format_command('rarelink setup api-keys')} to configure your environment."
        )
        raise typer.Exit(1)

    # Confirm upload action
    if not confirm_action(
        "Are you ready to upload the RareLink-CDM Data Dictionary to your REDCap project?"
    ):
        typer.secho(
            error_text(
                f"Upload canceled. You can manually upload the data dictionary using the instructions here: "
                f"{hyperlink('Manual Upload Instructions', DOCS_UPLOAD_DATA_DICTIONARY_URL)}"
            )
        )
        raise typer.Exit()

    # Download the latest data dictionary
    current_version = get_current_version()
    output_file = downloads_folder / f"rarelink_cdm_datadictionary - {current_version}.csv"
    typer.echo(f"Downloading the latest RareLink-CDM Data Dictionary version {current_version}...")
    download_file(DATA_DICTIONARY_DOWNLOAD_URL, output_file)
    typer.secho(success_text(f"✅ Data Dictionary downloaded to {output_file}."))

    # Read the CSV file content
    csv_content = output_file.read_text()

    # Upload data dictionary to REDCap
    data = {
        "token": api_token,
        "content": "metadata",
        "format": "csv",
        "data": csv_content,
        "returnFormat": "json",
    }

    try:
        response = requests.post(api_url, data=data)
        response.raise_for_status()
        typer.secho(success_text("✅ Data Dictionary uploaded successfully "
                                 "to your REDCap project."))
    except requests.RequestException as e:
        typer.secho(error_text(f"❌ Failed to upload Data Dictionary: {e}"))
        raise typer.Exit(1)

    # Provide next steps
    hint_text("\n👉 Next steps:")
    typer.echo("1. View the uploaded dictionary in REDCap.")
    typer.echo(f"2. Learn more about manual uploads here: {hyperlink('Manual Upload Instructions', DOCS_UPLOAD_DATA_DICTIONARY_URL)}")
    typer.echo(f"3. Explore REDCap project setup documentation here: {hyperlink('Setup REDCap Project', DOCS_REDCAP_PROJECT_URL)}")
    typer.echo(f"4. View the changelog for updates and changes here: {hyperlink('Changelog', CHANGELOG_URL)}")
    end_of_section_separator()
