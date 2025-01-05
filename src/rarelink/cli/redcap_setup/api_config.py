import typer
import json
from pathlib import Path
from rarelink.cli.utils.terminal_utils import masked_input
from rarelink.cli.utils.string_utils import (
    format_header,
    error_text,
    success_text,
    hint_text,
    hyperlink,
    format_command,
)
from rarelink.cli.utils.terminal_utils import end_of_section_separator, between_section_separator

app = typer.Typer()

CONFIG_FILE = Path.home() / "Downloads" / "rarelink_apiconfig.json"


@app.command()
def start():
    """
    Start the REDCap API setup process.
    """
    format_header("Welcome to the RareLink REDCap API Setup")

    project_created = typer.confirm(
        "Have you already created a REDCap project with your local administrator "
        "with API access for you?"
    )
    if not project_created:
        hint_text(
            "👉 Please run 'redcap-project-setup start' or follow the "
            "instructions in our documentation to create a REDCap project first."
        )
        typer.echo(
            f"📖 Documentation: {hyperlink('Setup REDCap Project',\
                'https://rarelink.readthedocs.io/en/latest/3_installation/3_1_setup_redcap_project.html')}"
        )
        raise typer.Exit()

    success_text("Great! Let's set up the REDCap API access.")

    # Inputs
    api_url = typer.prompt(
        "Enter the URL of your local REDCap instance (you can find this in "
        "the REDCap project URL)"
    )
    api_token = masked_input(
        "Enter your API token (input will be masked): ", mask="#"
    )
    typer.echo()

    is_admin = typer.confirm(
        "Are you a REDCap administrator and do you have access to the API "
        "super token?"
    )
    api_super_token = ""
    if is_admin:
        api_super_token = masked_input(
            "Enter your super API token (input will be masked, or press\
                Enter to skip): ",
            mask="#",
        )
        typer.echo()

    config = {
        "api_url": api_url,
        "api_token": api_token,
        "api_super_token": api_super_token,
    }
    CONFIG_FILE.write_text(json.dumps(config, indent=4))
    typer.secho(
        success_text(f"✅ REDCap API configuration saved\
            locally at {CONFIG_FILE}")
    )

    between_section_separator()

    typer.echo(f"▶ Run {format_command('rarelink redcap-setup api-config view')}\
        to see the current configuration.")
    typer.echo(f"▶ If you had a typo, you can run {format_command(
        'rarelink redcap-setup api-config start')} again.")
    typer.echo(f"▶ Run {format_command('rarelink redcap-setup api-config reset')}\
        to reset the configuration.")
    hint_text(
        "⚠️ API token is sensitive information! Please save it securely where "
        "only you have access."
    )
    end_of_section_separator()


@app.command()
def view():
    """
    View the current REDCap API configuration and its location.
    """
    if not CONFIG_FILE.exists():
        typer.secho(
            error_text(
                "❌ No REDCap configuration found. Please run \
                    `redcap-setup api-config start` first."
            )
        )
        raise typer.Exit(code=1)

    config = CONFIG_FILE.read_text()
    typer.secho(f"📄 Current REDCap Configuration:\n{config}",\
        fg=typer.colors.GREEN)

    # Display the configuration file location
    typer.secho(
        f"📁 Configuration File Location: {CONFIG_FILE.resolve()}",
        fg=typer.colors.BLUE,
    )

    end_of_section_separator()



@app.command()
def reset():
    """
    Reset the REDCap API configuration.
    """
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
        typer.secho(
            success_text("🔄 REDCap configuration has been reset.")
        )
    else:
        typer.secho(
            error_text("❌ No existing REDCap configuration found.")
        )
    end_of_section_separator()
