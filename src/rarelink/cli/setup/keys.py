import typer
import json
from pathlib import Path
from dotenv import dotenv_values
from rarelink.cli.utils.write_utils import write_env_file
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
from rarelink.cli.utils.validation_utils import validate_env

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
        f"{format_command('rarelink setup redcap-project')} or visit our "
        f"{hyperlink('documentation', 'https://rarelink.readthedocs.io/en/latest/3_installation/3_2_setup_redcap_project.html')}."
    )
    between_section_separator()

    # Confirm readiness
    ready = typer.confirm(
        "Do you have all the required accounts and API access ready?")
    if not ready:
        typer.secho(
            "❌ Setup cannot proceed without the required accounts and API access.",
            fg=typer.colors.RED,
        )
        raise typer.Exit()

    # Load existing .env values
    env_values = dotenv_values(ENV_PATH)

    # Step 1: BioPortal API Key
    typer.echo("BioPortal API key is required for RareLink functionalities.")
    bioportal_api_token = masked_input(
        "Step 1: Enter your BioPortal API key (input will be masked): ", mask="#"
    )
    typer.echo()
    between_section_separator()

    # Step 2: REDCap URL
    typer.echo(
        "The REDCap URL is the base URL of your REDCap instance. "
        "You can find it in your project's `API-Playground` settings "
        "(e.g., https://redcap.example.com/api/)."
    )
    redcap_url = typer.prompt(
        "Step 2: Enter your REDCap URL",
        default=env_values.get("REDCAP_URL", ""),
        show_default=False,
    )

    typer.echo()
    between_section_separator()

    # Step 3: REDCap project ID and project name
    typer.echo(
        "The REDCap Project ID uniquely identifies your project within your "
        "REDCap instance. You can find it displayed as `PID - <number>` next to"
        " your project name. For example, if it says `PID - 1234`, enter `1234`."
    )
    redcap_project_id = typer.prompt(
        "Step 3: Enter your REDCap Project ID",
        default=env_values.get("REDCAP_PROJECT_ID", ""),
        show_default=False,
    )
    redcap_project_name = typer.prompt(
        "Step 4: Enter your REDCap Project Name",
        default=env_values.get("REDCAP_PROJECT_NAME", ""),
        show_default=False,
    )

    typer.echo()
    between_section_separator()

    # Step 4: REDCap API Token
    typer.echo(
        "The API Token is required to securely interact with your REDCap "
        "project. You can find it in your project's `API` settings."
    )
    redcap_api_token = masked_input(
        "Step 5: Enter your REDCap API Token (input will be masked): ", mask="#"
    )
    
    typer.echo()
    between_section_separator()
    
    # Step 5: Created By
    typer.echo(
        "The 'Created By' field is added to the metadata of the Phenopackets."
    )
    created_by = typer.prompt(
        "Step 6: Enter your name or identifier for the 'Created By' field",
        default=env_values.get("CREATED_BY", ""),
        show_default=False,
    )
    typer.echo()
    between_section_separator()

    # Update or create the .env file
    if not ENV_PATH.exists():
        ENV_PATH.touch()

    try:
        # Save values to the .env file, ensuring they are stored as strings
        write_env_file(ENV_PATH, "BIOPORTAL_API_TOKEN", bioportal_api_token)
        write_env_file(ENV_PATH, "REDCAP_URL", redcap_url)
        write_env_file(ENV_PATH, "REDCAP_PROJECT_ID", redcap_project_id)
        write_env_file(ENV_PATH, "REDCAP_PROJECT_NAME", f'"{redcap_project_name}"')  # Ensure it's treated as a string
        write_env_file(ENV_PATH, "REDCAP_API_TOKEN", redcap_api_token)
        write_env_file(ENV_PATH, "CREATED_BY", f'"{created_by}"')  # Ensure it's treated as a string
        success_text(
            f"✅ API keys and configurations have been saved to {ENV_PATH}.")
    except Exception as e:
        typer.secho(
            error_text(f"❌ An error occurred while saving configurations: {e}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    between_section_separator()

    # Create the JSON configuration file
    config = {
        "bioportal_api_token": bioportal_api_token,
        "redcap-url": redcap_url,
        "id": redcap_project_id,
        "token": redcap_api_token,
    }

    try:
        CONFIG_FILE_ROOT.write_text(json.dumps(config, indent=4))
        success_text(f"✅ Configuration saved to {CONFIG_FILE_ROOT}.")
    except Exception as e:
        typer.secho(
            error_text(f"❌ Failed to save JSON configuration file: {e}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Optional: Save the JSON configuration to Downloads
    save_locally = typer.confirm(
        "Would you like to save this configuration in your "
        "Downloads folder as well?"
    )
    if save_locally:
        try:
            CONFIG_FILE_DOWNLOADS.write_text(json.dumps(config, indent=4))
            success_text(f"✅ Configuration saved to {CONFIG_FILE_DOWNLOADS}.")
        except Exception as e:
            typer.secho(
                error_text(f"❌ Failed to save configuration in Downloads: {e}"),
                fg=typer.colors.RED,
            )

    between_section_separator()

    # Validate the .env file
    typer.echo("🔄 Validating the .env file...")
    try:
        validate_env(
            [
            "BIOPORTAL_API_TOKEN", 
            "REDCAP_URL", 
            "REDCAP_PROJECT_ID",
            "REDCAP_API_TOKEN",
            "CREATED_BY"
            ]
        )
        success_text("✅ Validation successful! Your configurations are complete.")
    except Exception as e:
        typer.secho(
            error_text(f"❌ Validation failed: {e}"),
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
        "proper local backup if necessary."
    )
    end_of_section_separator()
