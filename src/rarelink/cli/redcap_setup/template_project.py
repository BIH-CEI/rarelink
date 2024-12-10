import typer
import requests
import json
from pathlib import Path
from rarelink.cli.utils.string_utils import (
    format_header,
    error_text,
    success_text,
    hint_text,
    format_command,
)
from rarelink.cli.utils.terminal_utils import (
    confirm_action,
    end_of_section_separator,
    between_section_separator,
)
from rarelink.cli.utils.file_utils import read_json

app = typer.Typer(name="template-project") 

# Configuration file path (for storing tokens and URLs)
CONFIG_FILE = Path.home() / ".rarelink_redcap_config.json"

# Documentation URLs
DOCS_TEMPLATE_PROJECT = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_3_rarelink_core_redcap_project.html"

def load_config():
    """
    Load REDCap API configuration from the config file.
    """
    if not CONFIG_FILE.exists():
        typer.secho(error_text("Configuration file not found. Please configure your REDCap API."))
        raise typer.Exit(code=2)

    try:
        config = read_json(CONFIG_FILE)
        if "api_super_token" not in config or not config["api_super_token"]:
            typer.secho(error_text("API super token not found in your configuration."))
            raise typer.Exit(code=2)
        return config
    except json.JSONDecodeError:
        typer.secho(error_text("Configuration file is not valid JSON."))
        raise typer.Exit(code=2)

@app.command()
def upload():
    """
    Set up a RareLink template project in REDCap.
    """
    format_header("RareLink Template Project Setup")

    # Ask if the user has an API super token
    if not confirm_action(
        "Do you have an API super token? (Only accessible for REDCap ADMINS!)"
    ):
        # Provide instructions for setting up with the administrator
        typer.secho(hint_text("⚠️ REDCap API Super Token is required for this operation."))
        typer.echo(f"📖 Documentation for setting up a RareLink project: {DOCS_TEMPLATE_PROJECT}")
        typer.echo("👉 Please follow the instructions with your local REDCap administrator.")
        typer.echo("👉 To download the RareLink template XML, run:")
        typer.secho(format_command("rarelink redcap-setup download rarelink_template_project"))
        raise typer.Exit(code=2)

    typer.secho(success_text("API Super Token detected. Proceeding with project creation..."))

    # Load configuration
    config = load_config()

    # Example project details
    record = {
        "project_title": "RareLink Template Project",
        "purpose": 0,  # Adjust according to REDCap purpose codes
        "purpose_other": "",
        "project_notes": "RareLink template project created via API."
    }
    data = json.dumps(record)

    # API fields
    fields = {
        "token": config["api_super_token"],
        "content": "project",
        "format": "json",
        "data": data,
    }

    try:
        # Make the API request
        response = requests.post(config["api_url"], data=fields)
        between_section_separator()
        typer.echo(hint_text(f"HTTP Status: {response.status_code}"))
        typer.echo(response.text)

        if response.status_code == 200:
            typer.secho(success_text("RareLink template project created successfully."))
        else:
            typer.secho(error_text("Failed to create the RareLink template project. Check your configuration and API permissions."))
            raise typer.Exit(code=2)

    except requests.RequestException as e:
        typer.secho(error_text(f"Error during API request: {e}"))
        raise typer.Exit(code=2)

    end_of_section_separator()
