import typer
import json
from pathlib import Path
from dotenv import dotenv_values, set_key
from rarelink.cli.utils.terminal_utils import (
    masked_input,
    end_of_section_separator,
    between_section_separator,
)
from rarelink.cli.utils.string_utils import (
    success_text,
    error_text,
    hint_text,
    format_header,
    format_command,
    hyperlink,
)
from rarelink.cli.utils.config_utils import validate_env, validate_config

app = typer.Typer()

ENV_PATH = Path(".env")
CONFIG_FILE_ROOT = Path("rarelink_apiconfig.json") 
CONFIG_FILE_DOWNLOADS = Path.home() / "Downloads" / "rarelink_apiconfig.json" 


@app.command()
def app():
    """
    Configure the RareLink framework by setting up API keys and variables.
    This process ensures the .env file contains necessary configurations.
    """
    format_header("RareLink API Keys Setup")
    typer.echo(
        "This setup will guide you through configuring your RareLink API keys "
        "and variables."
    )
    between_section_separator()

    typer.echo(
        "You need:\n"
        "- A free BioPortal account and API key (create one "
        f"{hyperlink('HERE', 'https://bioportal.bioontology.org/login?redirect=https%3A%2F%2Fbioportal.bioontology.org%2F')}).\n"
        "- A REDCap project with API access (run "
        f"{format_command('`rarelink setup redcap-project`')} or visit our "
        f"{hyperlink('documentation', 'https://rarelink.readthedocs.io/en/latest/3_installation/3_2_setup_redcap_project.html')}."
    )
    between_section_separator()

    # Confirm readiness
    ready = typer.confirm("Do you have all the required accounts and API "
                          "access ready?")
    if not ready:
        typer.secho(
            "❌ Setup cannot proceed without the required accounts "
                "and API access.",
            fg=typer.colors.RED,
        )
        raise typer.Exit()

    # Load existing .env values
    env_values = dotenv_values(ENV_PATH)

    # Step 1: BioPortal API Key
    typer.echo("BioPortal API key is required for the RareLink functionalities."
        " It is free and you can find it in your BioPortal account settings.")
    bioportal_api_token = masked_input(
        "Step 1: Enter your BioPortal API key (input will be masked): ", mask="#"
    )
    typer.echo()
    between_section_separator()

    # Step 2: REDCap URL
    typer.echo("REDCap URL is the base URL of your REDCap instance - \
you can find it in your projects `API-Playground` settings (e.g., https://redcap.example.com/api/).")
    redcap_url = typer.prompt(
        "Step 2: Enter your REDCap URL",
        default=env_values.get("REDCAP_PROJECT_URL", ""),
        show_default=False,
    )

    typer.echo()
    between_section_separator()

    # Step 3: REDCap Project ID
    typer.echo(
    "The REDCap Project ID uniquely identifies your project within your "
    "REDCap instance. You can find it displayed as `PID - <number>` next to "
    "your project name. For example, if it says `PID - 1234`, enter `1234`.")
    redcap_project_id = typer.prompt(
        "Step 3: Enter your REDCap Project ID",
        default=env_values.get("REDCAP_PROJECT_ID", ""),
        show_default=False,
    )
    
    typer.echo()
    between_section_separator()

    # Step 4: REDCap API Token
    typer.echo("API Token is required to securely interact with your REDCap \
project. You can find it in your project's `API` settings.")
    redcap_api_token = masked_input(
        "Step 4: Enter your REDCap API Token (input will be masked): ", mask="#"
    )
    
    typer.echo()
    between_section_separator()


    # Update or create .env file
    if not ENV_PATH.exists():
        ENV_PATH.touch()

    try:
        set_key(str(ENV_PATH), "BIOPORTAL_API_TOKEN", bioportal_api_token)
        set_key(str(ENV_PATH), "REDCAP_PROJECT_URL", redcap_url)
        set_key(str(ENV_PATH), "REDCAP_PROJECT_ID", redcap_project_id)
        set_key(str(ENV_PATH), "REDCAP_API_TOKEN", redcap_api_token)

        # Save to root JSON configuration
        config = {
            "redcap-url": redcap_url,
            "id": redcap_project_id,
            "token": redcap_api_token,
            "bioportal_api_token": bioportal_api_token,
        }
        CONFIG_FILE_ROOT.write_text(json.dumps(config, indent=4))

        success_text("✅ API keys and configurations have been saved to your .env file.")
        success_text(f"✅ Configuration saved to the root directory as {CONFIG_FILE_ROOT}.")
    except Exception as e:
        typer.secho(
            error_text(f"❌ An error occurred while saving configurations: {e}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Optional: Save locally as JSON
    save_locally = typer.confirm(
        "Would you like to save this configuration in your Downloads folder as well?"
    )
    if save_locally:
        CONFIG_FILE_DOWNLOADS.write_text(json.dumps(config, indent=4))
        typer.secho(
            success_text(f"✅ Configuration saved locally at {CONFIG_FILE_DOWNLOADS}")
        )
        hint_text(
            "⚠️ API token is sensitive information! Please save it securely where "
            "only you have access."
        )

    # Automatically validate the generated .env file and JSON config
    typer.echo("🔄 Validating configurations...")
    try:
        validate_env(["bioportal_api_token", "REDCAP_PROJECT_URL", "REDCAP_PROJECT_ID", "REDCAP_API_TOKEN"])
        validate_config(["redcap-url", "id", "token", "bioportal_api_token"])
        success_text("✅ Validation successful! Your configurations are complete.")
    except typer.Exit:
        typer.secho(
            error_text("❌ Validation failed. Please fix the above issues and rerun the setup."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    between_section_separator()

    # Closing notes
    typer.echo(
        f"▶ Run {format_command('rarelink setup view')} to view your current settings."
    )
    typer.echo(
        f"▶ Run {format_command('rarelink setup reset')} to reset the configurations."
    )
    hint_text(
        "Note: API keys are saved securely in your RareLink environment. They "
        "are included in the .gitignore file to avoid publishing them. Ensure "
        "proper local backup if saved locally."
    )
    end_of_section_separator()
    
