import typer
from pathlib import Path
from dotenv import dotenv_values
import requests
from rarelink.cli.utils.string_utils import success_text, error_text, format_header

app = typer.Typer()

ENV_PATH = Path(".env")  # Path to your .env file


def fetch_project_name(api_url, api_token):
    """
    Fetch the project metadata from the REDCap API to determine the project name.

    Args:
        api_url (str): URL of the REDCap API.
        api_token (str): API token for accessing REDCap.

    Returns:
        dict: The metadata as retrieved from the API.
    """
    fields = {
        "token": api_token,
        "content": "metadata",
        "format": "json",
    }
    response = requests.post(api_url, data=fields)
    if response.status_code == 200:
        metadata = response.json()
        return metadata
    else:
        raise Exception(f"Failed to fetch project metadata: {response.text}")


@app.command("metadata")
def app():
    """
    Fetch and display project metadata from the REDCap API.
    """
    try:
        # Load environment variables
        env_values = dotenv_values(ENV_PATH)
        api_url = env_values["REDCAP_URL"]
        api_token = env_values["REDCAP_API_TOKEN"]

        format_header("Fetching REDCap Project Metadata")

        # Fetch metadata
        typer.echo("🔄 Fetching metadata from REDCap...")
        metadata = fetch_project_name(api_url, api_token)

        # Display project title and metadata
        project_name = metadata[0].get("project_title", "default_project")
        typer.echo(success_text(f"✅ Project Name: {project_name}"))
        typer.echo("🔍 Full Metadata:")
        typer.echo(metadata)

    except Exception as e:
        typer.secho(error_text(f"❌ Error fetching metadata: {e}"), fg=typer.colors.RED)
        raise typer.Exit(1)
