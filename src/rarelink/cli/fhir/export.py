import typer
import subprocess
from pathlib import Path
from rarelink.cli.utils.terminal_utils import (
    between_section_separator, 
    end_of_section_separator
)
from rarelink.cli.utils.string_utils import (
    success_text,
    error_text,
    hint_text,
    format_command,
    hyperlink,
    format_header
)
from rarelink.cli.utils.validation_utils import (
    validate_env,
    validate_redcap_projects_json,
    validate_docker_and_compose
)

app = typer.Typer()

ENV_PATH = Path(".env")
REDCAP_PROJECTS_FILE = Path("redcap-project.json")
DOCKER_COMPOSE_PATH = "src/rarelink/tofhir/v2_0_4/docker-compose.yml"


@app.command()
def export():
    """
    CLI command to export data to the configured FHIR server 
    using the ToFHIR pipeline.
    """
    format_header("REDCap to FHIR export")

    # Step 1: Validation of setup files
    typer.echo("🔄 Validating setup files...")
    typer.echo("🔄 Validating the .env file...")
    try:
        validate_env([
            "BIOPORTAL_API_TOKEN",
            "REDCAP_URL",
            "REDCAP_PROJECT_ID",
            "REDCAP_API_TOKEN",
            "FHIR_REPO_URL"
        ])
    except Exception as e:
        typer.secho(
            error_text(f"❌ Validation of .env file failed: {str(e)}. "
                       f"Please run {format_command('rarelink setup keys')} "
                       "to configure the required keys."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    typer.echo("🔄 Validating the redcap-project.json file...")
    try:
        validate_redcap_projects_json()
    except Exception as e:
        typer.secho(
            error_text(f"❌ Validation of redcap-project.json failed: {str(e)}. "
                       f"Please run {format_command('rarelink fhir setup')} "
                       "to configure the required project."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    typer.echo("🔄 Validating Docker and Docker Compose setup...")
    validate_docker_and_compose()

    success_text("✅ All setup files are valid.")
    
    between_section_separator()

    # Step 4: Confirm readiness to export
    typer.secho(
        hint_text(
            "⚠️ Please ensure you are authorized to export real-world data to" 
            " the configured FHIR server. This includes verifying compliance with"
            "the ethical agreement and data protection regulations of your study"
            " or registry."
        ),
        fg=typer.colors.YELLOW,
    )
    ready_to_export = typer.confirm(
        "Are you sure you want to proceed with the export?")
    if not ready_to_export:
        typer.secho(
            error_text("❌ Export canceled. Please ensure all requirements are "
                       "met before proceeding."),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    between_section_separator()

    # Step 5: Notify about batch mode
    typer.secho(
            "HINT: The export process is configured in batch mode. Changes made "
            "after export require rerunning the pipeline. "
            f"For more information, please refer to our documentation: {hyperlink('ToFHIR Module Documentation', 'https://rarelink.readthedocs.io/en/latest/4_user_guide/4_4_tofhir_module.html')}."
        )
    between_section_separator()

    # Step 6: Execute Docker Compose
    typer.echo("🔄 Starting the ToFHIR pipeline...")
    try:
        subprocess.run(
            ["docker-compose", "-f", DOCKER_COMPOSE_PATH, "--project-directory",
             "./", "-p", "tofhir-redcap", "down"],
            check=True
        )
        subprocess.run(
            ["docker-compose", "-f", DOCKER_COMPOSE_PATH, "--project-directory",
             "./", "-p", "tofhir-redcap", "up", "-d"],
            check=True
        )
        success_text("✅ REDCap-ToFHIR pipeline is now running...")
    except subprocess.CalledProcessError as e:
        typer.secho(
            error_text(f"❌ Failed to start the ToFHIR pipeline: {str(e)}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    between_section_separator()

    # Final message
    typer.secho(f"The data should now be written to your FHIR server - run {format_command('docker logs -f tofhir')} to check the logs.",
    )
    
    
    end_of_section_separator()
