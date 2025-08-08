from pathlib import Path
from dotenv import dotenv_values
import json
import typer
import re
import subprocess
from rarelink.cli.utils.string_utils import success_text, error_text, hyperlink

ENV_PATH = Path(".env")
CONFIG_FILE = Path("rarelink_apiconfig.json")
REDCAP_PROJECTS_FILE = Path("redcap-projects.json")

def validate_url(url, required_keyword=None):
    """
    Validate that a URL is syntactically valid.
    Accepts:
    - IP addresses (e.g., http://134.95.194.154:6080/fhir)
    - Hostnames (e.g., http://hapi-fhir:8080/fhir)
    - Hostnames with optional dots (e.g., http://localhost or http://my-app.local)
    - Optional paths (e.g., /fhir, /api)
    - REDCap-specific URLs with 'redcap' in the path (if required_keyword='redcap')
    """
    regex = (
        r"^(https?:\/\/)"  # Protocol (http or https)
        r"(([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+"  # Domain or hostname
        r"|localhost"  # OR localhost
        r"|([0-9]{1,3}\.){3}[0-9]{1,3})"  # OR IPv4 address
        r"(:[0-9]{1,5})?"  # Optional port (e.g., :8080)
        r"(\/[a-zA-Z0-9-._~%!$&'()*+,;=:@]*)*\/?$"  # Optional path
    )
    if not re.match(regex, url):
        typer.secho(
            f"❌ Invalid URL: {url}. Please ensure the URL is properly formatted "
            f"(e.g., https://example.com, http://hapi-fhir:8080/fhir).",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Check for required keyword in the URL (e.g., 'redcap')
    if required_keyword and required_keyword not in url:
        typer.secho(
            f"❌ URL must include the keyword '{required_keyword}': {url}.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    return True

def validate_env(required_keys):
    """
    Validate that required keys exist in the .env file and meet specific criteria.
    """
    env_values = dotenv_values(ENV_PATH)
    missing_keys = [key for key in required_keys if key not in env_values]
    invalid_keys = []

    if missing_keys:
        typer.secho(
            f"❌ Missing keys in .env: {', '.join(missing_keys)}",
            fg=typer.colors.RED,
        )
        typer.echo("Please run `rarelink framework setup` to configure these.")
        raise typer.Exit(1)

    # Validate API key lengths
    for key in ["BIOPORTAL_API_TOKEN", "REDCAP_API_TOKEN"]:
        if len(env_values.get(key, "")) < 32:
            invalid_keys.append(key)
    if invalid_keys:
        typer.secho(
            f"❌ Invalid keys in .env: {', '.join(invalid_keys)} (must be at least 32 characters).",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Validate REDCap URL
    redcap_url = env_values.get("REDCAP_URL", "")
    validate_url(redcap_url)

    # Validate REDCap Project ID
    project_id = env_values.get("REDCAP_PROJECT_ID", "")
    if not project_id.isdigit():
        typer.secho(
            f"❌ Invalid REDCap Project ID in .env: {project_id}. Must be a positive integer.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Validate FHIR Repo URL (if it exists)
    fhir_repo_url = env_values.get("FHIR_REPO_URL", "")
    if fhir_repo_url:
        validate_url(fhir_repo_url)


def validate_config(required_keys):
    """
    Validate that required keys exist in the JSON config file 
    and meet specific criteria.
    """
    if not CONFIG_FILE.exists():
        typer.secho(
            "❌ Configuration file missing. Please run `rarelink framework setup`.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    try:
        config = json.loads(CONFIG_FILE.read_text())
    except json.JSONDecodeError:
        typer.secho(
            "❌ Invalid JSON structure in configuration file.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        typer.secho(
            f"❌ Missing keys in {CONFIG_FILE.name}: {', '.join(missing_keys)}.",
            fg=typer.colors.RED,
        )
        typer.echo("Please run `rarelink framework setup` to configure these.")
        raise typer.Exit(1)

    # Validate API key lengths
    for key in ["bioportal_api_token", "token"]:
        if len(config.get(key, "")) < 32:
            typer.secho(
                f"❌ Invalid key in configuration file: {key} (must be at least 32 characters).",
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)

    # Validate REDCap URL
    redcap_url = config.get("redcap-url", "")
    if not validate_url(redcap_url):
        typer.secho(
            f"❌ Invalid REDCap URL in configuration file: {redcap_url}. URL must include 'redcap' and be valid.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Validate REDCap Project ID
    project_id = config.get("id", "")
    if not str(project_id).isdigit():
        typer.secho(
            f"❌ Invalid REDCap Project ID in configuration file: {project_id}. Must be a positive integer.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Validate FHIR Repo URL (if it exists)
    fhir_repo_url = config.get("fhirRepoUrl", "")
    if fhir_repo_url:
        validate_url(fhir_repo_url)

def validate_redcap_projects_json():
    """
    Validate the `redcap-projects.json` file in the root directory.
    Ensures:
    - The file exists.
    - The file has a valid JSON structure.
    - Each entry contains a valid 'id' and 'token'.
    """
    if not REDCAP_PROJECTS_FILE.exists():
        typer.secho(
            f"❌ Missing file: {REDCAP_PROJECTS_FILE.name}. Please ensure the file exists in the root directory.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    try:
        # Load JSON data
        with open(REDCAP_PROJECTS_FILE, "r") as file:
            projects = json.load(file)

        # Validate structure: Ensure it's a list
        if not isinstance(projects, list):
            typer.secho(
                f"❌ Invalid structure in {REDCAP_PROJECTS_FILE.name}. The file must contain a list of projects.",
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)

        for project in projects:
            # Validate 'id' is a string of digits
            project_id = project.get("id", "")
            if not project_id.isdigit():
                typer.secho(
                    f"❌ Invalid project ID in {REDCAP_PROJECTS_FILE.name}: {project_id}. Must be a string of digits.",
                    fg=typer.colors.RED,
                )
                raise typer.Exit(1)

            # Validate 'token' length
            token = project.get("token", "")
            if len(token) < 32:
                typer.secho(
                    f"❌ Invalid token in {REDCAP_PROJECTS_FILE.name} for project ID {project_id}: {token}. "
                    "Token must be at least 32 characters long.",
                    fg=typer.colors.RED,
                )
                raise typer.Exit(1)

    except json.JSONDecodeError:
        typer.secho(
            f"❌ Invalid JSON format in {REDCAP_PROJECTS_FILE.name}. Please check the file structure.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    except Exception as e:
        typer.secho(
            f"❌ Unexpected error while validating {REDCAP_PROJECTS_FILE.name}: {str(e)}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)



def validate_docker_and_compose(install_prompt=False):
    """
    Validates the presence of Docker and Docker Compose. Optionally prompts
    to install missing components.

    Args:
        install_prompt (bool): Whether to prompt the user to install Docker
                               and Docker Compose if not found.

    Raises:
        typer.Exit: If Docker or Docker Compose is not installed and cannot
                    be installed or the user declines installation.
    """
    # Validate Docker
    typer.echo("🔄 Validating Docker setup...")
    docker_installed = subprocess.run(
        ["docker", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if docker_installed.returncode != 0:
        typer.secho(
            error_text(
                "❌ Docker is not installed. "
                f"Install it via {hyperlink('Docker Website', 'https://www.docker.com/products/docker-desktop/')}."
            ),
            fg=typer.colors.RED,
        )
        if install_prompt:
            if typer.confirm("Do you want to install Docker Desktop "
                             "via Homebrew?"):
                try:
                    subprocess.run(["brew", "install", "--cask", "docker"], 
                                   check=True)
                    typer.echo("Starting Docker Desktop...")
                    subprocess.run(["open", "/Applications/Docker.app"], 
                                   check=True)
                    success_text("✅ Docker Desktop installed and started "
                                 "successfully.")
                except subprocess.CalledProcessError as e:
                    typer.secho(
                        error_text(f"❌ Failed to install/start Docker Desktop: {str(e)}"),
                        fg=typer.colors.RED,
                    )
                    raise typer.Exit(1)
            else:
                typer.secho(
                    error_text("❌ Docker is required to continue. Exiting."),
                    fg=typer.colors.RED,
                )
                raise typer.Exit(1)
        else:
            raise typer.Exit(1)
    else:
        typer.echo("Docker is already installed.")

    # Validate Docker Compose
    typer.echo("🔄 Validating Docker Compose setup...")
    docker_compose_installed = subprocess.run(
        ["docker-compose", "--version"], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if docker_compose_installed.returncode != 0:
        typer.secho(
            error_text(
                "❌ Docker Compose is not installed. "
                "Please install Docker Compose to continue."
            ),
            fg=typer.colors.RED,
        )
        if install_prompt:
            install_choice = typer.confirm(
                "Do you want to install Docker Compose via Homebrew? "
                "(Select 'No' to install via pip instead.)"
            )
            if install_choice:
                try:
                    subprocess.run(["brew", "install", "docker-compose"], 
                                   check=True)
                    success_text("✅ Docker Compose installed successfully via"
                                 " Homebrew.")
                except subprocess.CalledProcessError as e:
                    typer.secho(
                        error_text(f"❌ Failed to install Docker Compose via Homebrew: {str(e)}"),
                        fg=typer.colors.RED,
                    )
                    raise typer.Exit(1)
            else:
                try:
                    subprocess.run(["pip", "install", "docker-compose"],
                                   check=True)
                    success_text("✅ Docker Compose installed successfully "
                                 "via pip.")
                except subprocess.CalledProcessError as e:
                    typer.secho(
                        error_text(f"❌ Failed to install Docker Compose via pip: {str(e)}"),
                        fg=typer.colors.RED,
                    )
                    raise typer.Exit(1)
        else:
            raise typer.Exit(1)
    else:
        typer.echo("Docker Compose is already installed.")
