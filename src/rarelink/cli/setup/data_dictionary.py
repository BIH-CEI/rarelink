import shutil
from pathlib import Path

import requests
import typer
from dotenv import dotenv_values

from rarelink._versions import DATA_DICT_LABEL
from rarelink.rarelink_cdm import get_data_dictionary_path
from rarelink.cli.utils.string_utils import (
    error_text,
    success_text,
    hint_text,
    format_header,
    hyperlink,
)
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator,
    between_section_separator,
    confirm_action,
)
from rarelink.cli.utils.validation_utils import validate_env

ENV_PATH = Path(".env")
config = dotenv_values(ENV_PATH)
app = typer.Typer()

# Documentation and download URLs
DOCS_RD_CDM_URL = "https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html"
DOCS_REDCAP_PROJECT_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_2_setup_redcap_project.html"
DOCS_UPLOAD_DATA_DICTIONARY_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_3_setup_rarelink_instruments.html"
CHANGELOG_URL = "https://rarelink.readthedocs.io/en/latest/6_changelog.html"

downloads_folder = Path.home() / "Downloads"
redcap_api_token = config.get("REDCAP_API_TOKEN")
redcap_url = config.get("REDCAP_URL")


@app.command()
def app():
    """
    Upload the most current RareLink-CDM Data Dictionary to an existing REDCap project.
    """
    format_header("RareLink-CDM Data Dictionary Upload")

    typer.echo("🔄 Validating the .env file...")
    try:
        validate_env(["REDCAP_URL", "REDCAP_PROJECT_ID", "REDCAP_API_TOKEN"])
        typer.echo("✅ Validation successful! Your configurations are complete.")
    except Exception as e:
        typer.secho(
            error_text(f"❌ Validation failed: {e}"),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    # Confirm upload action
    if not confirm_action(
        "Are you ready to upload the RareLink-CDM Data Dictionary to your REDCap project?"
    ):
        typer.secho(
            error_text(
                "Upload canceled. You can manually upload the data dictionary using "
                f"the instructions here: {hyperlink('Manual Upload Instructions', DOCS_UPLOAD_DATA_DICTIONARY_URL)}"
            )
        )
        raise typer.Exit()

    # Locate the data dictionary file from the package
    try:
        data_dict_path = get_data_dictionary_path()
    except FileNotFoundError as e:
        typer.secho(
            error_text(
                f"❌ Data Dictionary file not found in package ({DATA_DICT_LABEL}): {e}. "
                "Please reinstall rarelink or open an issue."
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    resource_name = data_dict_path.name

    typer.echo(f"📄 Using packaged RareLink-CDM Data Dictionary ({DATA_DICT_LABEL})...")

    # Optional: copy to Downloads for the user's convenience
    output_file = downloads_folder / resource_name
    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(data_dict_path, output_file)
        typer.echo(f"💾 A copy was saved to: {output_file}")
    except Exception as e:
        # Not fatal for REDCap upload: we can continue with the internal file
        typer.secho(
            hint_text(
                f"⚠️ Could not copy to Downloads folder: {e}. Continuing with internal file."
            )
        )

    # Use the packaged CSV content for upload
    csv_content = data_dict_path.read_text(encoding="utf-8")

    # Upload data dictionary to REDCap
    data = {
        "token": redcap_api_token,
        "content": "metadata",
        "format": "csv",
        "data": csv_content,
        "returnFormat": "json",
    }
    typer.echo("🔄 Uploading the data dictionary to your REDCap project...")
    try:
        response = requests.post(redcap_url, data=data)
        response.raise_for_status()
        success_text("✅ Data Dictionary uploaded successfully to your REDCap project.")
    except requests.RequestException as e:
        typer.secho(error_text(f"❌ Failed to upload Data Dictionary: {e}"))
        raise typer.Exit(1)

    between_section_separator()

    # Provide next steps
    hint_text("\n👉 Next steps:")
    typer.echo("1. View the uploaded dictionary in REDCap.")
    typer.echo(
        "2. Learn more about manual uploads here: "
        f"{hyperlink('Manual Upload Instructions', DOCS_UPLOAD_DATA_DICTIONARY_URL)}"
    )
    typer.echo(
        "3. Explore REDCap project setup documentation here: "
        f"{hyperlink('Setup REDCap Project', DOCS_REDCAP_PROJECT_URL)}"
    )
    typer.echo(
        "4. View the changelog for updates and changes here: "
        f"{hyperlink('Changelog', CHANGELOG_URL)}"
    )

    end_of_section_separator()
