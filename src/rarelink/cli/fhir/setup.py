import typer
import json
import subprocess
from pathlib import Path
from rarelink.cli.utils.terminal_utils import (
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
FHIR_CONFIG_FILE = Path("rarelink_fhirconfig.json")


@app.command()
def setup():
    """
    Configure the ToFHIR pipeline for the RareLink framework.
    """
    format_header("RareLink ToFHIR Setup")
    typer.echo("Starting the ToFHIR setup process.")

    # Validate API keys setup
    typer.echo("🔄 Validating configurations...")
    try:
        validate_env(["BIOPORTAL_API_TOKEN", "REDCAP_PROJECT_URL", "REDCAP_PROJECT_ID", "REDCAP_API_TOKEN"])
        validate_config(["redcap-url", "id", "token", "bioportal_api_token"])
    except Exception:
        typer.secho(
            error_text(
                "❌ API keys are not set up correctly. Run "
                f"{format_command('rarelink setup api-keys')} first to set up the BIOPORTAL API key, REDCap project ID, URL, and API Token."
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    success_text("✅ API keys and configurations validated successfully.")
    between_section_separator()

    # ToFHIR setup instructions
    typer.echo(
        f"For guidance on setting up the ToFHIR module, refer to our "
        f"{hyperlink('documentation', 'https://rarelink.readthedocs.io/en/latest/4_user_guide/4_4_tofhir_module.html')}."
    )

    # FHIR server question
    typer.echo("You need a FHIR server to export (or import) FHIR records.")
    fhir_server_accessible = typer.confirm(
        "Do you have an accessible and running FHIR server?"
    )

    if fhir_server_accessible:
        # Ask for an existing FHIR server URL
        fhir_repo_url = typer.prompt(
            "Enter the FHIR repository URL for your server (e.g., http://100.11.000.111:0000/fhir)",
            show_default=False,
        )

        # Save the FHIR configuration
        fhir_config = {"fhirRepoUrl": fhir_repo_url}
        FHIR_CONFIG_FILE.write_text(json.dumps(fhir_config, indent=4))
        success_text(f"✅ FHIR configuration saved to {FHIR_CONFIG_FILE}.")
    else:
        hint_text(
            "⚠️ Space left to implement FHIR server creation steps. "
            "Consider setting up a FHIR server or consult our documentation."
        )
        typer.echo("Returning to setup...")
        return

    # Docker & Colima setup
    typer.echo("Docker and Colima are required to manage the ToFHIR pipeline.")
    colima_installed = subprocess.run(
        ["colima", "start"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    if colima_installed.returncode != 0:
        typer.secho(
            error_text(
                "❌ Colima is not installed or could not be started. "
                f"We recommend installing Colima via {hyperlink('Homebrew', 'https://brew.sh/')}."
            ),
            fg=typer.colors.RED,
        )
        install_colima = typer.confirm("Do you want to install Colima via Homebrew?")
        if install_colima:
            try:
                subprocess.run(["brew", "install", "colima"], check=True)
                subprocess.run(["colima", "start"], check=True)
                success_text("✅ Colima installed and started successfully.")
            except subprocess.CalledProcessError as e:
                typer.secho(
                    error_text(f"❌ Failed to install/start Colima: {str(e)}"),
                    fg=typer.colors.RED,
                )
                raise typer.Exit(1)
        else:
            typer.secho(
                error_text("❌ Colima is required to continue. Exiting setup."),
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)
    else:
        success_text("✅ Colima is already running.")

    between_section_separator()

    # Closing hints
    typer.echo(
        "▶ Run the next steps for the ToFHIR module, such as "
        f"{format_command('rarelink fhir export')}."
    )
    hint_text("Refer to the documentation for more advanced usage and examples.")
    end_of_section_separator()
