import typer
from pathlib import Path
from rarelink.cli.utils.string_utils import (
    format_header,
    success_text,
    error_text,
    format_command,
)
from rarelink.cli.utils.terminal_utils import end_of_section_separator

app = typer.Typer()

ENV_PATH = Path(".env")
CONFIG_FILE = Path("rarelink_apiconfig.json")

@app.command()
def app():
    """
    Reset all RareLink configuration by wiping the .env and JSON files.
    """
    format_header("Resetting Configuration")

    # Confirm reset action
    confirm = typer.confirm(
        "This will delete your current RareLink configuration, including API "
        "keys and settings. Are you sure you want to proceed?"
    )
    if not confirm:
        typer.secho(
            "❌ Reset operation canceled by the user.",
            fg=typer.colors.RED,
        )
        end_of_section_separator()
        raise typer.Exit()

    # Remove .env file
    if ENV_PATH.exists():
        ENV_PATH.unlink()
        typer.secho(success_text("✅ .env file has been removed."), fg=typer.colors.GREEN)
    else:
        typer.secho(error_text("❌ No .env file found to remove."), fg=typer.colors.RED)

    # Remove JSON configuration file
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
        typer.secho(
            success_text("✅ rarelink_apiconfig.json has been removed."),
            fg=typer.colors.GREEN,
        )
    else:
        typer.secho(
            error_text("❌ No rarelink_apiconfig.json file found to remove."),
            fg=typer.colors.RED,
        )

    # Suggest reconfiguration
    typer.echo(
        f"🔄 RareLink API-keys configuration has been reset. Run {format_command('rarelink setup api-keys')} to reconfigure."
    )
    end_of_section_separator()
