# src/rarelink/cli/redcap_setup/data_dictionary.py
import typer
from pathlib import Path
import requests
import json
from rarelink.cli.utils.string_utils import (
    error_text,
    success_text,
    hint_text,
    hyperlink,
    format_header,
)
from rarelink.cli.utils.terminal_utils import end_of_section_separator, confirm_action

app = typer.Typer()

# Documentation links
DOCS_REDCAP_PROJECT_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_2_setup_redcap_project.html"
DOCS_REDCAP_API_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_4_redcap_api.html"
DOCS_MANUAL_UPLOAD_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_3_setup_rarelink_instruments.html"
CHANGELOG_URL = "https://rarelink.readthedocs.io/en/latest/6_changelog.html"


@app.command()
def app():
    """
    Upload the most current RareLink-CDM Data Dictionary into an existing
    REDCap project.
    """
    format_header("RareLink-CDM Data Dictionary Upload")

    # Prompt user for the configuration file path
    config_file = Path(typer.prompt("Enter the path to your REDCap API configuration file"))

    # Check if the provided config file exists
    if not config_file.exists():
        typer.secho(
            error_text(
                f"No REDCap API configuration file found at {config_file}. Please run "
                f"`rarelink redcap-setup api-setup` or follow the documentation."
            )
        )
        typer.echo(f"📖 Documentation: {hyperlink('Setup REDCap API', DOCS_REDCAP_API_URL)}")
        raise typer.Exit(code=2)

    # Load API configuration
    try:
        config = json.loads(config_file.read_text())
    except json.JSONDecodeError:
        typer.secho(
            error_text(
                f"The configuration file at {config_file} is not valid JSON. Please check the file and try again."
            )
        )
        raise typer.Exit(code=2)

    api_url = config.get("api_url")
    api_token = config.get("api_token")
    if not api_url or not api_token:
        typer.secho(
            error_text(
                "Incomplete REDCap API configuration. Please reset and run `rarelink redcap-setup api-setup` again."
            )
        )
        raise typer.Exit(code=2)

    typer.secho(success_text("REDCap API configuration loaded successfully."))

    # Confirm upload
    if not confirm_action(
        "Are you ready to upload the RareLink-CDM Data Dictionary to your REDCap project?"
    ):
        typer.secho(
            error_text(
                f"Upload canceled. Refer to the manual upload instructions here: {hyperlink('Manual Upload Instructions', DOCS_MANUAL_UPLOAD_URL)}"
            )
        )
        raise typer.Exit()

    # Simulate loading the CSV string
    csv_string = "header1,header2\nvalue1,value2\nvalue3,value4"  # Replace with actual CSV data

    # Upload data dictionary
    data = {
        "api_token": api_token,
        "content": "metadata",
        "format": "csv",
        "data": csv_string,
        "returnFormat": "json",
    }

    try:
        response = requests.post(api_url, data=data)
        response.raise_for_status()
        typer.secho(success_text("Data Dictionary uploaded successfully."))
    except requests.RequestException as e:
        typer.secho(error_text(f"Failed to upload Data Dictionary: {e}"))
        raise typer.Exit(code=1)

    # Next steps
    typer.secho(hint_text("\n👉 Next steps:"))
    typer.echo("1. View the uploaded dictionary in REDCap.")
    typer.echo(f"2. Learn more about manual uploads here: {hyperlink('Manual Upload Instructions', DOCS_MANUAL_UPLOAD_URL)}")
    typer.echo(f"3. Explore REDCap project setup documentation here: {hyperlink('Setup REDCap Project', DOCS_REDCAP_PROJECT_URL)}")
    typer.echo(f"4. View the changelog for updates and changes here: {hyperlink('Changelog', CHANGELOG_URL)}")
    end_of_section_separator()
