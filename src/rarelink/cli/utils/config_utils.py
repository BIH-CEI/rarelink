from pathlib import Path
from dotenv import dotenv_values
import json
import typer

ENV_PATH = Path(".env")
CONFIG_FILE = Path.home() / "Downloads" / "rarelink_apiconfig.json"

def validate_env(required_keys):
    """Validate that required keys exist in the .env file."""
    env_values = dotenv_values(ENV_PATH)
    missing_keys = [key for key in required_keys if key not in env_values]
    if missing_keys:
        typer.secho(
            f"❌ Missing keys in .env: {', '.join(missing_keys)}",
            fg=typer.colors.RED,
        )
        typer.echo("Please run `rarelink framework setup` to configure these.")
        raise typer.Exit(1)

def validate_config(required_keys):
    """Validate that required keys exist in the JSON config file."""
    if not CONFIG_FILE.exists():
        typer.secho(
            "❌ Configuration file missing. Please run "
            "`rarelink framework setup`.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    config = json.loads(CONFIG_FILE.read_text())
    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        typer.secho(
            f"❌ Missing keys in {CONFIG_FILE.name}: {', '.join(missing_keys)}",
            fg=typer.colors.RED,
        )
        typer.echo("Please run `rarelink framework setup` to configure these.")
        raise typer.Exit(1)
