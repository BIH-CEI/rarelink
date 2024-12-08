# src/rarelink/cli/redcap_setup/data_dictionary.py
import typer
from pathlib import Path
import requests
import json

app = typer.Typer()

# Define the configuration file path
CONFIG_FILE = Path.home() / ".rarelink_redcap_config.json"

# Documentation links
DOCS_REDCAP_PROJECT_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_2_setup_redcap_project.html"
DOCS_REDCAP_API_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_4_redcap_api.html"
DOCS_MANUAL_UPLOAD_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_3_setup_rarelink_instruments.html"
CHANGELOG_URL = "https://rarelink.readthedocs.io/en/latest/6_changelog.html"

@app.command()
def upload():
    """
    Upload the most current RareLink-CDM Data Dictionary into an existing REDCap project.
    """
    typer.secho("🚀 RareLink-CDM Data Dictionary Upload", fg=typer.colors.BRIGHT_BLUE, bold=True)

    # Check if API token is generated
    typer.secho("Checking REDCap API configuration...", fg=typer.colors.CYAN)
    if not CONFIG_FILE.exists():
        typer.secho(
            "❌ No REDCap API configuration found. Please run `rarelink redcap-setup api-setup` "
            f"or follow the documentation: {DOCS_REDCAP_API_URL}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=2)

    # Load API configuration
    config = json.loads(CONFIG_FILE.read_text())
    api_url = config.get("api_url")
    api_token = config.get("api_token")
    if not api_url or not api_token:
        typer.secho(
            "❌ Incomplete REDCap API configuration. Please reset and run `rarelink redcap-setup api-setup` again.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=2)

    typer.secho("REDCap API configuration loaded successfully.", fg=typer.colors.GREEN)

    # Confirm upload
    proceed = typer.confirm(
        "Are you ready to upload the RareLink-CDM Data Dictionary to your REDCap project?"
    )
    if not proceed:
        typer.secho(
            f"❌ Upload canceled. Refer to the manual upload instructions here: {DOCS_MANUAL_UPLOAD_URL}",
            fg=typer.colors.RED,
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
        typer.secho("✅ Data Dictionary uploaded successfully.", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Failed to upload Data Dictionary: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # Next steps
    typer.secho("\n👉 Next steps:", fg=typer.colors.CYAN, bold=True)
    typer.echo("1. View the uploaded dictionary in REDCap.")
    typer.echo(f"2. Learn more about manual uploads here: {DOCS_MANUAL_UPLOAD_URL}")
    typer.echo(f"3. Explore REDCap project setup documentation here: {DOCS_REDCAP_PROJECT_URL}")
    typer.echo(f"4. View the changelog for updates and changes here: {CHANGELOG_URL}")
