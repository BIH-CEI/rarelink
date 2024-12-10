import typer
from pathlib import Path
import requests

app = typer.Typer()

# Define the URLs for the documentation and data dictionary
DOCS_RD_CDM_URL = "https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html"
DOCS_RARELINK_CDM_URL = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_2_rarelink_cdm_instruments.html"
DOCS_RARELINK_INSTRUMENTS_URL = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_2_rarelink_cdm_instruments.html#rarelink-cdm-instruments"
DOCS_UPLOAD_DATA_DICTIONARY_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_3_setup_rarelink_instruments.html"
DATA_DICTIONARY_DOWNLOAD_URL = "https://rarelink.readthedocs.io/en/latest/_downloads/97061f8438c4a3bb907919a76a5ab2c6/rarelink_v2_0_0_dev0_datadictionary.csv"
INSTRUMENTS_DOWNLOAD_URL = "https://rarelink.readthedocs.io/en/latest/_downloads/8bb7dfc55de14eb8984091463842254e/rarelink_cdm_single_instruments.zip"
XML_PROJECT_DOWNLOAD_URL = "http://127.0.0.1:8000/_downloads/25122ebc11409a8a4420e1a9dbd69fd8/rarelink_v2_0_0_redcap_project.xml"
RARELINK_TEMPLATE_PROJECT = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_3_rarelink_core_redcap_project.html"
CHANGELOG_URL = "https://rarelink.readthedocs.io/en/latest/6_changelog.html"

def get_current_version() -> str:
    """
    Simulate fetching the most current RD-CDM version.
    This could be extended to dynamically fetch the version from an API.
    """
    # For demonstration, hardcoded version
    return "v2_0_0_dev0"

def download_file(url: str, output_file: Path):
    """
    Generic function to download a file from a URL and save it locally.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        typer.secho(f"✅ File successfully downloaded to {output_file}", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Failed to download the file: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    
downloads_folder = Path.home() / "Downloads"

@app.command()
def rarelink_cdm_datadictionary():
    """
    Download the most current RareLink RD-CDM Data Dictionary.
    """
    typer.secho("🚀 RareLink RD-CDM Data Dictionary Download", fg=typer.colors.BRIGHT_BLUE, bold=True)
    typer.echo(f"📖 Learn more about the RD-CDM here: {DOCS_RD_CDM_URL}")
    typer.echo(f"📖 Learn more about the RareLink-CDM in REDCap here: {DOCS_RARELINK_CDM_URL}")
    typer.secho("-" * 80, fg=typer.colors.BRIGHT_BLACK)

    # Ask the user if they want to download the most current version
    current_version = get_current_version()
    proceed = typer.confirm(
        f"The most current RD-CDM Data Dictionary version is {current_version}. Would you like to download it?"
    )
    
    if not proceed:
        typer.secho("❌ Download canceled.", fg=typer.colors.RED)
        raise typer.Exit()

    output_file = Path.home() / f"rarelink_rd_cdm_{current_version}_data_dictionary_.csv"
    download_file(DATA_DICTIONARY_DOWNLOAD_URL, output_file)

    # Provide guidance for the next steps
    typer.secho("\n👉 Next steps:", fg=typer.colors.CYAN, bold=True)
    typer.echo("1. Use the `rarelink redcap-setup upload-data-dictionary` command to upload the dictionary.")
    typer.echo(f"2. Or follow the documentation here: {DOCS_UPLOAD_DATA_DICTIONARY_URL}")
    typer.echo(f"3. View the changelog for important version-related notes, updates and changes here: {CHANGELOG_URL}")

@app.command()
def rarelink_cdm_instruments():
    """
    Download the RareLink RD-CDM separate instruments as a .zip file.
    """
    typer.secho("🚀 RareLink-CDM - Single Instruments Download", fg=typer.colors.BRIGHT_BLUE, bold=True)
    typer.echo(f"📖 Learn more about the RD-CDM here: {DOCS_RD_CDM_URL}")
    typer.echo(f"📖 Learn more about the single RareLink-CDM Instruments here: {DOCS_RARELINK_INSTRUMENTS_URL}")
    
    typer.secho("-" * 80, fg=typer.colors.BRIGHT_BLACK)

    current_version = get_current_version()
       
    output_file = downloads_folder / f"rarelink_rd_cdm_{current_version}_instruments.zip"
    download_file(INSTRUMENTS_DOWNLOAD_URL, output_file)
    typer.secho(f"Please also view the changelog for important updates and changes here: {CHANGELOG_URL}", fg=typer.colors.BRIGHT_YELLOW)

@app.command()
def rarelink_template_project():
    """
    Download the preconfigured RareLink template project for REDCap as an XML file.
    """
    typer.secho("🚀 RareLink REDCap Project Download", fg=typer.colors.BRIGHT_BLUE, bold=True)
    typer.echo(f"📖 Learn more about the RD-CDM here: {DOCS_RD_CDM_URL}")
    typer.echo(f"📖 Learn more about the RareLink Core Template project here: {RARELINK_TEMPLATE_PROJECT}")
    
    typer.secho("-" * 80, fg=typer.colors.BRIGHT_BLACK)

    output_file = Path.home() / "rarelink_redcap_project.xml"
    download_file(XML_PROJECT_DOWNLOAD_URL, output_file)
    typer.secho(f"Please also view the changelog for important updates and changes here: {CHANGELOG_URL}", fg=typer.colors.BRIGHT_YELLOW)
