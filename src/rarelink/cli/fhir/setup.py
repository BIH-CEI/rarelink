import typer
from pathlib import Path
from rarelink.cli.utils.file_utils import ensure_directory_exists, write_json
from rarelink.cli.utils.string_utils import format_header, success_text, hint_text, error_text

def setup():
    """
    Interactive setup for the toFHIR configuration.
    Guides the user to provide the REDCap URL, project ID, and API token.
    """
    format_header("Welcome to the toFHIR Configuration Setup")
    typer.echo(
        "This process will guide you through setting up the REDCap integration "
        "for toFHIR."
    )
    hint_text(
        "💡 Make sure you have your REDCap instance URL, project ID, and API "
        "token ready."
    )
    typer.echo()

    # Step 1: Get REDCap URL
    redcap_url = typer.prompt("Step 1: Enter the URL of your REDCap instance")
    if not redcap_url.startswith("http"):
        typer.secho(
            error_text(
                "❌ Invalid URL. Ensure it starts with http:// or https://"
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    # Step 2: Get REDCap Project ID
    project_id = typer.prompt("Step 2: Enter the REDCap project ID")
    if not project_id.isdigit():
        typer.secho(
            error_text(
                "❌ Invalid project ID. Ensure it contains only digits."
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    # Step 3: Get REDCap API Token
    api_token = typer.prompt(
        "Step 3: Enter the REDCap API token", hide_input=True
    )
    if len(api_token) < 32:  # Example validation for token length
        typer.secho(
            error_text(
                "❌ Invalid API token. Ensure it is the correct length."
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    typer.echo()

    # Save Configuration
    format_header("Saving Configuration")
    env_path = Path(".env")
    json_path = Path("src/rarelink/tofhir/v2.0.0.dev0/redcap-projects.json")
    ensure_directory_exists(json_path.parent)

    # Save to .env
    with open(env_path, "w") as f:
        f.write(f"REDCAP_PROJECT_ID={project_id}\n")
        f.write(f"REDCAP_PROJECT_URL={redcap_url}\n")
        f.write(f"REDCAP_API_TOKEN={api_token}\n")

    # Generate redcap-projects.json
    write_json([{"id": project_id, "token": api_token}], json_path)

    success_text("✅ Configuration saved successfully!")
    typer.echo(f"- REDCap details written to: {env_path}")
    typer.echo(
        f"- REDCap projects file generated at: {json_path}"
    )
    hint_text(
        "🎉 Setup complete! You can now proceed with running the toFHIR pipeline."
    )
