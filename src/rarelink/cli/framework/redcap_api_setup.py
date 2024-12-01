# src/rarelink/cli/framework/redcap_api_setup.py
import typer
from pathlib import Path

app = typer.Typer()

CONFIG_FILE = Path.home() / ".rarelink_redcap_config.json"

@app.command()
def start():
    """
    Start the REDCap API setup process.
    """
    typer.echo("🚀 Welcome to the RareLink REDCap API Setup!")

    # Check if a REDCap project is already created
    project_created = typer.confirm(
        "Have you already created a REDCap project with your local administrator?"
    )
    if not project_created:
        typer.secho(
            "👉 Please follow the instructions in our documentation to create a REDCap project first.",
            fg=typer.colors.YELLOW,
        )
        typer.echo("📖 Documentation: https://rarelink.readthedocs.io/en/latest/3_installation/3_0_install_file.html")
        raise typer.Exit()

    typer.secho("Great! Let's set up the REDCap API access.", fg=typer.colors.GREEN)

    # Gather inputs
    api_url = typer.prompt("Enter the URL of your local REDCap instance")
    api_token = typer.prompt("Enter your API token (will not be shown)", hide_input=True)
    # api_super_token = typer.prompt(
    #     "Enter your super API token (if applicable, or press Enter to skip. \
    #         The API super token is usually only owned by the REDCap administrator)",
    #           hide_input=True, default=""
    # )

    # Save the configuration
    config = {
        "api_url": api_url,
        "api_token": api_token
        # "api_super_token": api_super_token,
    }
    CONFIG_FILE.write_text(typer.style(str(config), fg=typer.colors.BRIGHT_WHITE))
    typer.secho(f"✅ REDCap API configuration saved locally at {CONFIG_FILE}", fg=typer.colors.GREEN)


@app.command()
def view():
    """
    View the current REDCap API configuration.
    """
    if not CONFIG_FILE.exists():
        typer.secho("❌ No REDCap configuration found. Please run `redcap-api-setup start` first.", fg=typer.colors.RED)
        raise typer.Exit()

    config = CONFIG_FILE.read_text()
    typer.secho(f"📄 Current REDCap Configuration:\n{config}", fg=typer.colors.BRIGHT_WHITE)


@app.command()
def reset():
    """
    Reset the REDCap API configuration.
    """
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
        typer.secho("🔄 REDCap configuration has been reset.", fg=typer.colors.GREEN)
    else:
        typer.secho("❌ No existing REDCap configuration found.", fg=typer.colors.RED)
