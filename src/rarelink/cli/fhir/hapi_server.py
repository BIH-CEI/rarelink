import typer
import subprocess
from pathlib import Path
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator
)
from rarelink.cli.utils.string_utils import (
    success_text,
    error_text,
    format_header,
    hint_text
)

app = typer.Typer()

ENV_PATH = Path(".env")
CONFIG_FILE_ROOT = Path("rarelink_apiconfig.json")
FHIR_CONFIG_FILE = Path("rarelink_fhirconfig.json")


@app.command()
def hapi_server():
    """
    CLI command to set up a local HAPI FHIR server with Docker, 
    avoiding conflicts.
    """
    format_header("Setting up a Local HAPI FHIR Server")

    # Check if Docker is installed
    try:
        subprocess.run(["docker", "--version"], 
                       check=True, stdout=subprocess.PIPE)
    except FileNotFoundError:
        typer.secho(
            error_text(
                "❌ Docker is not installed or not available in your PATH. "
                "Please install Docker from https://www.docker.com/get-started."
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Define network and container names
    network_name = "shared-network"
    container_name = "hapi-fhir"

    # Ensure Docker network exists
    typer.echo(f"Ensuring Docker network '{network_name}' exists...")
    subprocess.run(
        ["docker", "network", "create", network_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Check if the container already exists
    typer.echo("Checking for existing HAPI FHIR server container...")
    existing_containers = subprocess.run(
        ["docker", "ps", "-a", "--filter", f"name={container_name}",
         "--format", "{{.Names}}"],
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()

    if existing_containers == container_name:
        typer.secho("✅ A HAPI FHIR server container already exists.",
                    fg=typer.colors.GREEN)
        # Check if the container is running
        running_containers = subprocess.run(
            ["docker", "ps", "--filter", f"name={container_name}",
             "--format", "{{.Names}}"],
            stdout=subprocess.PIPE,
            text=True,
        ).stdout.strip()
        if running_containers == container_name:
            success_text("✅ HAPI FHIR server is already running at "
                         "http://localhost:8080.")
        else:
            typer.secho(
                "🔄 Restarting the existing HAPI FHIR server container...",
                        fg=typer.colors.YELLOW)
            subprocess.run(["docker", "start", container_name], check=True)
            success_text("✅ HAPI FHIR server is now running at "
                         "http://localhost:8080.")
        return

    # Start a new HAPI FHIR server container
    try:
        typer.echo("Starting a new HAPI FHIR server on port 8080...")
        subprocess.run(
            [
                "docker", "run", "-d", "-p", "8080:8080", "--name", container_name,
                "--network", network_name, "hapiproject/hapi:v6.4.0"
            ],
            check=True,
        )
        success_text("✅ HAPI FHIR server is running at http://localhost:8080.")
        hint_text(
            "⚠️ Data is stored inside the Docker container. Ensure the container "
            "is not removed to preserve data."
        )
    except subprocess.CalledProcessError as e:
        typer.secho(
            error_text(f"❌ Failed to start the HAPI FHIR server: {str(e)}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    end_of_section_separator()
