import typer
from pathlib import Path
from dotenv import dotenv_values
from rarelink.cli.utils.string_utils import format_header, error_text
from rarelink.cli.utils.terminal_utils import end_of_section_separator

app = typer.Typer()

ENV_PATH = Path(".env")
CONFIG_FILE = Path("rarelink_apiconfig.json")

@app.command()
def app():
    """
    View the current RareLink API configuration and its location.
    """
    format_header("Viewing Current Configuration")

    # View .env contents
    if ENV_PATH.exists():
        env_values = dotenv_values(ENV_PATH)
        typer.secho("📄 Current .env Configuration:", fg=typer.colors.GREEN)
        for key, value in env_values.items():
            typer.echo(f"{key}: {value}")
    else:
        typer.secho(
            error_text("❌ No .env file found in the root directory."),
            fg=typer.colors.RED,
        )

    typer.echo()

    # View JSON configuration
    if CONFIG_FILE.exists():
        config_content = CONFIG_FILE.read_text()
        typer.secho("📄 Current JSON Configuration:", fg=typer.colors.GREEN)
        typer.echo(config_content)
    else:
        typer.secho(
            error_text("❌ No rarelink_apiconfig.json file found in the root directory."),
            fg=typer.colors.RED,
        )

    end_of_section_separator()
