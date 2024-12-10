import typer
from pathlib import Path
import requests
import os

app = typer.Typer()

# URLs for documentation and downloads
DOCS_RD_CDM_URL = "https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html"
DOCS_RARELINK_CDM_URL = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_2_rarelink_cdm_instruments.html"
DOCS_RARELINK_INSTRUMENTS_URL = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_2_rarelink_cdm_instruments.html#rarelink-cdm-instruments"
DOCS_UPLOAD_DATA_DICTIONARY_URL = "https://rarelink.readthedocs.io/en/latest/3_installation/3_3_setup_rarelink_instruments.html"
DATA_DICTIONARY_DOWNLOAD_URL = "https://rarelink.readthedocs.io/en/latest/_downloads/97061f8438c4a3bb907919a76a5ab2c6/rarelink_v2_0_0_datadictionary.csv"
INSTRUMENTS_DOWNLOAD_URL = "https://rarelink.readthedocs.io/en/latest/_downloads/8bb7dfc55de14eb8984091463842254e/rarelink_cdm_single_instruments.zip"
XML_PROJECT_DOWNLOAD_URL = "to be added!..."
RARELINK_TEMPLATE_PROJECT = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_3_rarelink_core_redcap_project.html"
CHANGELOG_URL = "https://rarelink.readthedocs.io/en/latest/6_changelog.html"

def hyperlink(text: str, url: str) -> str:
    """
    Create a clickable hyperlink for terminal output with a fallback for 
    unsupported terminals.
    """
    if "TERM" in os.environ and os.environ["TERM"] not in ("dumb", ""):
        return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"
    else:
        return f"{text} ({url})"

def get_current_version() -> str:
    """
    Simulate fetching the most current RD-CDM version.
    Will be extended to dynamically fetch the version from an API.
    """
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
        typer.secho(f"✅ File successfully downloaded to {output_file}", 
                    fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Failed to download the file: {e}", 
                    fg=typer.colors.RED)
        raise typer.Exit(code=1)
    
def format_command(command: str) -> str:
    """
    Format a terminal command to make it stand out.
    """
    return typer.style(command, fg=typer.colors.BRIGHT_CYAN)

    
downloads_folder = Path.home() / "Downloads"

@app.command()
def rarelink_cdm_datadictionary():
    """
    Download the most current RareLink RD-CDM Data Dictionary.
    """
    typer.secho(
        "▶▶️▶️ RareLink-CDM REDCap Data Dictionary Download...",
        fg=typer.colors.BRIGHT_MAGENTA, bold=True)
    typer.secho("-" * 80, fg=typer.colors.BRIGHT_CYAN)
    typer.echo(
        f"📖 Learn more about the underlying CDM here: {hyperlink(
            'RD-CDM Documentation', DOCS_RD_CDM_URL)}")
    typer.echo(
        f"📖 Learn more about the RareLink-CDM in REDCap here: {hyperlink(
            'RareLink-CDM Documentation', DOCS_RARELINK_CDM_URL)}")

    current_version = get_current_version()
    proceed = typer.confirm(
        f"The most current RD-CDM Data Dictionary version is {current_version}. Would you like to download it?"
    )
    if not proceed:
        typer.secho("❌ Download canceled.", fg=typer.colors.RED)
        raise typer.Exit()

    output_file = downloads_folder / f"rarelink_rd_cdm_{current_version}_data_dictionary.csv"
    download_file(DATA_DICTIONARY_DOWNLOAD_URL, output_file)

    typer.secho("\n👉 Next steps:", bold=True)
    typer.echo(f"1. Use {format_command('rarelink redcap-setup upload-data-dictionary')}\
 to upload the data dictionary to your REDCap project.")
    typer.echo(
        f"2. For more information or manual setup check the {hyperlink(
            'Installation guide - REDCap Instruments', 
        DOCS_UPLOAD_DATA_DICTIONARY_URL)}")
    typer.secho(
        f"3. Please view the changelog for important updates or changes: {hyperlink(
            'View Changelog', CHANGELOG_URL)}", 
        fg=typer.colors.YELLOW)
    typer.secho("-" * 80, fg=typer.colors.BRIGHT_WHITE)

@app.command()
def rarelink_cdm_instruments():
    """
    Download the RareLink RD-CDM separate instruments as a .zip file.
    """
    typer.secho("▶▶️▶️ RareLink-CDM - Single Instruments Download...", 
                fg=typer.colors.BRIGHT_MAGENTA, bold=True)
    typer.secho("-" * 80, fg=typer.colors.BRIGHT_CYAN)
    
    typer.echo(
        f"📖 Learn more about the underlying CDM here: {hyperlink(
            'RD-CDM Documentation', DOCS_RD_CDM_URL)}")
    typer.echo(f"📖 Learn more about the single RareLink-CDM Instruments here: {hyperlink(
        'RareLink Instruments', DOCS_RARELINK_INSTRUMENTS_URL)}")

    current_version = get_current_version()
    proceed = typer.confirm(
        f"The most current RD-CDM Instruments version is {current_version}. Would you like to download it?"
    )
    if not proceed:
        typer.secho("❌ Download canceled.", fg=typer.colors.RED)
        raise typer.Exit()

    output_file = downloads_folder / f"rarelink_rd_cdm_{current_version}_instruments.zip"
    download_file(INSTRUMENTS_DOWNLOAD_URL, output_file)

    typer.secho("\n👉 Next steps:", bold=True)
    typer.echo("1. Unzip the instruments.")
    typer.echo(f"2. Use {format_command('rarelink redcap-setup upload-data-dictionary')}\
 to upload the data dictionary to your REDCap project.")
    typer.echo(
        f"3. For more information or manual setup check the {hyperlink(
            'Installation guide - REDCap Instruments', 
        DOCS_UPLOAD_DATA_DICTIONARY_URL)}")
    typer.secho(
        f"4. Please view the changelog for important updates or changes: {hyperlink(
            'View Changelog', CHANGELOG_URL)}", 
        fg=typer.colors.YELLOW)
    typer.secho("-" * 80, fg=typer.colors.BRIGHT_WHITE)

@app.command()
def rarelink_template_project():
    """
    Download the lates version of the preconfigured RareLink template project
    for REDCap as an XML file. Installing this project is only possible for or
    with REDCap administrators.
    """
    typer.secho("▶▶️▶️ RareLink REDCap Project Download", fg=typer.colors.BRIGHT_MAGENTA, bold=True)
    typer.secho("-" * 80, fg=typer.colors.BRIGHT_CYAN)

    typer.echo(
        f"📖 Learn more about the underlying CDM here: {hyperlink(
            'RD-CDM Documentation', DOCS_RD_CDM_URL)}")
    typer.echo(
        f"📖 Learn more about the RareLink-CDM in REDCap here: {hyperlink(
            'RareLink-CDM Documentation', DOCS_RARELINK_CDM_URL)}")
    typer.echo(f"📖 Learn more about the REDCap Template Project here: {hyperlink(
        'RareLink Core REDCap Project', RARELINK_TEMPLATE_PROJECT)}")

    current_version = get_current_version()
    proceed = typer.confirm(
        f"The most current RareLink Template Project version is {current_version}. Would you like to download it?"
    )
    if not proceed:
        typer.secho("❌ Download canceled.", fg=typer.colors.RED)
        raise typer.Exit()

    output_file = downloads_folder / "rarelink_redcap_project.xml"
    download_file(XML_PROJECT_DOWNLOAD_URL, output_file)

    typer.secho("\n👉 Next steps:", fg=typer.colors.BRIGHT_CYAN, bold=True)
    typer.echo("Note: You can only continue if you are a REDCap administrator.\
 Otherwise reach out to your REDCap admin to install the template project.")
    typer.echo(f"For more information check the documentation: {hyperlink(
        'RareLink Core REDCap Project', RARELINK_TEMPLATE_PROJECT)}")
    typer.echo(f"If you're a REDCap admin, you can run {format_command(
        'rarelink redcap-setup upload-project-template')}")
    typer.secho(
        f"-> Please view the changelog for important updates or changes: {hyperlink(
            'View Changelog', CHANGELOG_URL)}", 
        fg=typer.colors.YELLOW)
    typer.secho("-" * 80, fg=typer.colors.BRIGHT_WHITE)
