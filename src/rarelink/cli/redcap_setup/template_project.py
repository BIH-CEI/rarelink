import typer
import requests
import json
from pathlib import Path

app = typer.Typer()

# Configuration file path (for storing tokens and URLs)
CONFIG_FILE = Path.home() / ".rarelink_redcap_config.json"

# Documentation URLs
DOCS_TEMPLATE_PROJECT = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_3_rarelink_core_redcap_project.html"

def load_config():
    """
    Load REDCap API configuration from the config file.
    """
    if not CONFIG_FILE.exists():
        typer.secho("❌ Configuration file not found. Please run `rarelink redcap-setup api` to configure your REDCap API.", fg=typer.colors.RED)
        raise typer.Exit()
    return json.loads(CONFIG_FILE.read_text())


@app.command()
def rarelink_template_project():
    """
    Set up a RareLink template project in REDCap.
    """
    typer.secho("🚀 RareLink Template Project Setup", fg=typer.colors.BRIGHT_BLUE, bold=True)

    # Ask if the user has an API super token
    has_super_token = typer.confirm("Do you have an API super token? (Only accessible for REDCap ADMINS!)")

    if not has_super_token:
        # Provide instructions for setting up with the administrator
        typer.secho("⚠️ REDCap API Super Token is required for this operation.", fg=typer.colors.YELLOW)
        typer.echo(f"📖 Documentation for setting up a RareLink project: {DOCS_TEMPLATE_PROJECT}")
        typer.echo("👉 Please follow the instructions with your local REDCap administrator.")
        typer.echo("👉 To download the RareLink template XML, run:")
        typer.secho("rarelink redcap-setup download rarelink_template_project", fg=typer.colors.CYAN)
        raise typer.Exit()

    typer.secho("🔑 API Super Token detected. Proceeding with project creation...", fg=typer.colors.GREEN)

    # Load configuration
    config = load_config()
    if "api_super_token" not in config or not config["api_super_token"]:
        typer.secho("❌ API super token not found in your configuration. Please update it.", fg=typer.colors.RED)
        raise typer.Exit()

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
        typer.secho(f"HTTP Status: {response.status_code}", fg=typer.colors.CYAN)
        typer.secho(response.text, fg=typer.colors.BRIGHT_WHITE)

        if response.status_code == 200:
            typer.secho("✅ RareLink template project created successfully.", fg=typer.colors.GREEN)
        else:
            typer.secho("❌ Failed to create the RareLink template project. Check your configuration and API permissions.", fg=typer.colors.RED)

    except requests.RequestException as e:
        typer.secho(f"❌ Error during API request: {e}", fg=typer.colors.RED)
