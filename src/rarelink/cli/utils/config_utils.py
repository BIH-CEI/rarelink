from pathlib import Path
from dotenv import dotenv_values
import json
import typer
import re

ENV_PATH = Path(".env")
CONFIG_FILE = Path("rarelink_apiconfig.json")

def validate_env(required_keys):
    """
    Validate that required keys exist in the .env file and meet specific criteria.
    """
    env_values = dotenv_values(ENV_PATH)
    missing_keys = [key for key in required_keys if key not in env_values]
    invalid_keys = []

    if missing_keys:
        typer.secho(
            f"❌ Missing keys in .env: {', '.join(missing_keys)}",
            fg=typer.colors.RED,
        )
        typer.echo("Please run `rarelink framework setup` to configure these.")
        raise typer.Exit(1)

    # Validate API key lengths
    for key in ["BIOPORTAL_API_KEY", "REDCAP_API_TOKEN"]:
        if len(env_values.get(key, "")) < 32:
            invalid_keys.append(key)
    if invalid_keys:
        typer.secho(
            f"❌ Invalid keys in .env: {', '.join(invalid_keys)} (must be at least 32 characters).",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Validate REDCap URL
    redcap_url = env_values.get("REDCAP_PROJECT_URL", "")
    if not validate_url(redcap_url):
        typer.secho(
            f"❌ Invalid REDCap URL in .env: {redcap_url}. URL must include 'redcap' and be valid.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Validate REDCap Project ID
    project_id = env_values.get("REDCAP_PROJECT_ID", "")
    if not project_id.isdigit():
        typer.secho(
            f"❌ Invalid REDCap Project ID in .env: {project_id}. Must be a positive integer.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

def validate_config(required_keys):
    """
    Validate that required keys exist in the JSON config file and meet specific criteria.
    """
    if not CONFIG_FILE.exists():
        typer.secho(
            "❌ Configuration file missing. Please run `rarelink framework setup`.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    try:
        config = json.loads(CONFIG_FILE.read_text())
    except json.JSONDecodeError:
        typer.secho(
            "❌ Invalid JSON structure in configuration file.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        typer.secho(
            f"❌ Missing keys in {CONFIG_FILE.name}: {', '.join(missing_keys)}.",
            fg=typer.colors.RED,
        )
        typer.echo("Please run `rarelink framework setup` to configure these.")
        raise typer.Exit(1)

    # Validate API key lengths
    for key in ["bioportal_api_key", "token"]:
        if len(config.get(key, "")) < 32:
            typer.secho(
                f"❌ Invalid key in configuration file: {key} (must be at least 32 characters).",
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)

    # Validate REDCap URL
    redcap_url = config.get("redcap-url", "")
    if not validate_url(redcap_url):
        typer.secho(
            f"❌ Invalid REDCap URL in configuration file: {redcap_url}. URL must include 'redcap' and be valid.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Validate REDCap Project ID
    project_id = config.get("id", "")
    if not str(project_id).isdigit():
        typer.secho(
            f"❌ Invalid REDCap Project ID in configuration file: {project_id}. Must be a positive integer.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

def validate_url(url):
    """
    Validate that the URL is valid and includes 'redcap'.
    """
    regex = r"^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(\/[a-zA-Z0-9-]+)*\/?$"
    return "redcap" in url and re.match(regex, url)
