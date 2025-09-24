import typer
from pathlib import Path
import requests
from dotenv import dotenv_values
from rarelink.cli.utils.string_utils import (
    error_text,
    success_text,
    hint_text,
    format_header,
    hyperlink
)
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator, 
    between_section_separator,
    confirm_action
)
from rarelink.cli.utils.file_utils import download_file
from rarelink.cli.utils.version_utils import get_current_version
from rarelink.cli.utils.validation_utils import validate_env

ENV_PATH = Path(".env")
config = dotenv_values(ENV_PATH)
app = typer.Typer()

# Documentation and download URLs
DOCS_RD_CDM_URL = "https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html"
DOCS_REDCAP_PROJECT_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_2_setup_redcap_project.html"
DOCS_UPLOAD_DATA_DICTIONARY_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_3_setup_rarelink_instruments.html"
CHANGELOG_URL = "https://rarelink.readthedocs.io/en/latest/6_changelog.html"
DATA_DICTIONARY_DOWNLOAD_URL = "https://rarelink.readthedocs.io/en/latest/_downloads/3f4c4d4cb08501b7ab8ec1b7200f6c2f/rarelink_cdm_datadictionary%20-%20v2_0_4.csv"
downloads_folder = Path.home() / "Downloads"
redcap_api_token = config.get("REDCAP_API_TOKEN")
redcap_url = config.get("REDCAP_URL")

@app.command()
def app():
    """
    Upload the most current RareLink-CDM Data Dictionary to an existing REDCap project.
    """
    format_header("RareLink-CDM Data Dictionary Upload")

    typer.echo("🔄 Validating the .env file...")
    try:
        validate_env(["REDCAP_URL", "REDCAP_PROJECT_ID", "REDCAP_API_TOKEN"])
        typer.echo("✅ Validation successful! Your configurations are complete.")
    except Exception as e:
        typer.secho(
            error_text(f"❌ Validation failed: {e}"),
            fg=typer.colors.RED,
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
    typer.echo(f"🔄 Downloading the latest RareLink-CDM Data Dictionary version {current_version}...")
    download_file(DATA_DICTIONARY_DOWNLOAD_URL, output_file)

    csv_content = output_file.read_text()

    # Upload data dictionary to REDCap
    data = {
        "token": redcap_api_token,
        "content": "metadata",
        "format": "csv",
        "data": csv_content,
        "returnFormat": "json",
    }
    typer.echo("🔄 Uploading the data dictionary to your REDCap project...")
    try:
        response = requests.post(redcap_url, data=data)
        response.raise_for_status()
        success_text("✅ Data Dictionary uploaded successfully "
                                 "to your REDCap project.")
    except requests.RequestException as e:
        typer.secho(error_text(f"❌ Failed to upload Data Dictionary: {e}"))
        raise typer.Exit(1)

    between_section_separator()
    
    # Provide next steps
    hint_text("\n👉 Next steps:")
    typer.echo("1. View the uploaded dictionary in REDCap.")
    typer.echo(f"2. Learn more about manual uploads here: {hyperlink('Manual Upload Instructions', DOCS_UPLOAD_DATA_DICTIONARY_URL)}")
    typer.echo(f"3. Explore REDCap project setup documentation here: {hyperlink('Setup REDCap Project', DOCS_REDCAP_PROJECT_URL)}")
    typer.echo(f"4. View the changelog for updates and changes here: {hyperlink('Changelog', CHANGELOG_URL)}")
    
    end_of_section_separator()