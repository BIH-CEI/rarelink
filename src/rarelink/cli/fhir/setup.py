import typer
import json
import subprocess
from pathlib import Path
from dotenv import dotenv_values
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
from rarelink.cli.utils.validation_utils import (
    validate_env,
    validate_redcap_projects_json,
    validate_docker_and_compose
)
from rarelink.cli.utils.write_utils import write_env_file

app = typer.Typer()

ENV_PATH = Path(".env")
REDCAP_PROJECTS_FILE = Path("redcap-projects.json")


@app.command()
def setup():
    """
    CLI Command to configure the toFHIR pipeline for the RareLink framework.
    """
    format_header("RareLink FHIR Setup")
    typer.echo("Starting the FHIR setup process.")

    # Step 1: Validate existing .env file
    typer.echo("🔄 Validating the existing .env file...")
    if not ENV_PATH.exists():
        typer.secho(
            error_text(
                f"❌ .env file not found. Please run {format_command('rarelink setup keys')} first to generate the required API keys."
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    try:
        env_values = dotenv_values(ENV_PATH)
        validate_env(["BIOPORTAL_API_TOKEN", "REDCAP_URL", 
                      "REDCAP_PROJECT_ID", "REDCAP_API_TOKEN"])
        success_text("✅ .env file validated successfully.")
    except Exception as e:
        typer.secho(
            error_text(
                f"❌ Validation failed: {str(e)}. Please fix the .env file or rerun {format_command('rarelink setup keys')}."
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    between_section_separator()

    # Step 2: FHIR Server Setup
    typer.echo("You need a FHIR server to export (or import) FHIR records.")
    typer.secho(
        hint_text(
            "Note: Please make sure you only write real-world data to a"
            " secure FHIR server that is within the scope of the respective"
            " ethical agreement of your study/registry."
        ),
        fg=typer.colors.YELLOW,
    )
    fhir_server_accessible = typer.confirm(
        "Do you have an accessible and running FHIR server to write data"
        " to (or import data from)?"
    )

    if not fhir_server_accessible:
        typer.secho(
            hint_text(
                "⚠️ If you do not have a FHIR server, run "
                f"{format_command('rarelink fhir hapi-server')} to create your own local FHIR server."
            ),
            fg=typer.colors.YELLOW,
        )
        raise typer.Exit(1)

    # Ask for the FHIR URL
    fhir_repo_url = typer.prompt(
        "Enter the FHIR repository URL for your server "
        "(e.g., http://example.com/fhir)",
        default=env_values.get("FHIR_REPO_URL", ""),
        show_default=False,
    )

    # Update or add FHIR_REPO_URL to the .env file
    try:
        write_env_file(ENV_PATH, "FHIR_REPO_URL", fhir_repo_url)
        success_text(f"✅ FHIR repository URL added to {ENV_PATH}.")
    except Exception as e:
        typer.secho(
            error_text(f"❌ Failed to update .env file: {str(e)}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    between_section_separator()

    # Step 3: Write the redcap-projects.json file
    typer.echo("🔄 Writing the redcap-projects.json file...")
    redcap_projects_content = [
        {
            "id": env_values["REDCAP_PROJECT_ID"],
            "token": env_values["REDCAP_API_TOKEN"]
        }
    ]
    try:
        REDCAP_PROJECTS_FILE.write_text(
            json.dumps(redcap_projects_content, indent=4))
        success_text(
            f"✅ redcap-projects.json file written to {REDCAP_PROJECTS_FILE}.")
    except Exception as e:
        typer.secho(
            error_text(
                f"❌ Failed to write redcap-projects.json file: {str(e)}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    between_section_separator()

    # Step 4: Docker & Docker Compose setup
    typer.echo("Docker is required to manage the ToFHIR pipeline.")
    docker_installed = subprocess.run(
        ["docker", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    if docker_installed.returncode != 0:
        typer.secho(
            error_text(
                "❌ Docker is not installed. "
                f"We recommend installing Docker Desktop via {hyperlink('Docker Website', 'https://www.docker.com/products/docker-desktop/')}."
            ),
            fg=typer.colors.RED,
        )
        install_docker = typer.confirm(
            "Do you want to install Docker Desktop via Homebrew?")
        if install_docker:
            try:
                subprocess.run(["brew", "install", "--cask", "docker"],
                               check=True)
                typer.echo("Starting Docker Desktop...")
                subprocess.run(["open", "/Applications/Docker.app"],check=True)
                success_text(
                    "✅ Docker Desktop installed and started successfully.")
            except subprocess.CalledProcessError as e:
                typer.secho(
                    error_text(
                        f"❌ Failed to install/start Docker Desktop: {str(e)}"),
                    fg=typer.colors.RED,
                )
                raise typer.Exit(1)
        else:
            typer.secho(
                error_text("❌ Docker is required to continue. Exiting setup."),
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)
    else:
        success_text("✅ Docker is already installed.")

    between_section_separator()

    typer.echo("🔄 Validating Docker and Docker Compose setup...")
    validate_docker_and_compose()

    between_section_separator()

    # Step 5: Validate the updated .env file
    typer.echo("🔄 Validating the updated .env file...")
    try:
        # Pass the required keys explicitly
        validate_env([
            "BIOPORTAL_API_TOKEN",
            "REDCAP_URL",
            "REDCAP_PROJECT_ID",
            "REDCAP_API_TOKEN",
            "FHIR_REPO_URL"
        ])
        success_text("✅ Environment variables validated successfully.")
    except Exception as e:
        typer.secho(
            error_text(f"❌ Validation failed: {str(e)}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    
    # Step 6: Validate the redcap-project.json file
    typer.echo("🔄 Validating the redcap-projects.json file...")
    try:
        validate_redcap_projects_json()  # Call the imported validation function
        success_text("✅ redcap-projects.json validated successfully.")
    except Exception as e:
        typer.secho(
            error_text(
                f"❌ Validation of redcap-projects.json failed: {str(e)}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    
    between_section_separator()

    # Closing hints
    typer.echo(
        "▶ Run the next steps for the ToFHIR module, such as "
        f"{format_command('rarelink fhir export')}."
    )
    hint_text("Refer to the documentation for more advanced "
              "usage guide and examples.")
    end_of_section_separator()
