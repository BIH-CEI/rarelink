import typer
from pathlib import Path
from rarelink.cli.utils.string_utils import (
    format_command,
    hyperlink,
    error_text,
    hint_text,
    format_header,
)
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator,
    between_section_separator,
)
from rarelink.cli.utils.file_utils import download_file
from rarelink.cli.utils.version_utils import get_current_version

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

downloads_folder = Path.home() / "Downloads"

@app.command()
def rarelink_cdm_datadictionary():
    """
    Download the most current RareLink RD-CDM Data Dictionary.
    """
    format_header("RareLink-CDM REDCap Data Dictionary Download")
    typer.echo(
        f"📖 Learn more about the underlying CDM here: {hyperlink('RD-CDM Documentation', DOCS_RD_CDM_URL)}")
    typer.echo(
        f"📖 Learn more about the RareLink-CDM in REDCap here: {hyperlink('RareLink-CDM Documentation', DOCS_RARELINK_CDM_URL)}")

    current_version = get_current_version()
    proceed = typer.confirm(
        f"The most current RD-CDM Data Dictionary version is {current_version}. "
        "Would you like to download it?"
    )
    if not proceed:
        typer.secho(error_text("❌ Download canceled."))
        raise typer.Exit()

    output_file = downloads_folder / f"rarelink_rd_cdm_{current_version}_data_dictionary.csv"
    download_file(DATA_DICTIONARY_DOWNLOAD_URL, output_file)
    between_section_separator()

    hint_text("\n👉 Next steps")
    typer.echo(f"1. Use {format_command('rarelink redcap-setup upload-data-dictionary')} "
               "to upload the data dictionary to your REDCap project.")
    typer.echo(
        f"2. For more information or manual setup, check the {hyperlink('Installation guide - REDCap Instruments', DOCS_UPLOAD_DATA_DICTIONARY_URL)}")
    typer.secho(
        f"3. Please view the changelog for important updates or changes: {hyperlink('View Changelog', CHANGELOG_URL)}"),
    end_of_section_separator()


@app.command()
def rarelink_cdm_instruments():
    """
    Download the RareLink RD-CDM separate instruments as a .zip file.
    """
    format_header("RareLink-CDM - Single Instruments Download")
    typer.echo(
        f"📖 Learn more about the underlying CDM here: {hyperlink('RD-CDM Documentation', DOCS_RD_CDM_URL)}")
    typer.echo(
        f"📖 Learn more about the single RareLink-CDM Instruments here: {hyperlink('RareLink Instruments', DOCS_RARELINK_INSTRUMENTS_URL)}")

    current_version = get_current_version()
    proceed = typer.confirm(
        f"The most current RD-CDM Instruments version is {current_version}. "
        "Would you like to download it?"
    )
    if not proceed:
        typer.secho(error_text("❌ Download canceled."))
        raise typer.Exit()

    output_file = downloads_folder / f"rarelink_rd_cdm_{current_version}_instruments.zip"
    download_file(INSTRUMENTS_DOWNLOAD_URL, output_file)
    between_section_separator()

    hint_text("\n👉 Next steps:")
    typer.echo("1. Unzip the instruments.")
    typer.echo(
        f"2. Use {format_command('rarelink redcap-setup upload-data-dictionary')} "
        "to upload the data dictionary to your REDCap project.")
    typer.echo(
        f"3. For more information or manual setup check the {hyperlink('Installation guide - REDCap Instruments', DOCS_UPLOAD_DATA_DICTIONARY_URL)}")
    typer.secho(
        f"4. Please view the changelog for important updates or changes: {hyperlink('View Changelog', CHANGELOG_URL)}"),
    end_of_section_separator()
    
@app.command()
def rarelink_template_project():
    """
    Download the latest version of the preconfigured RareLink template project
    for REDCap as an XML file. Installing this project is only possible for or
    with REDCap administrators.
    """
    format_header("RareLink REDCap Project Download")
    typer.echo(
        f"📖 Learn more about the underlying CDM here: {hyperlink('RD-CDM Documentation', DOCS_RD_CDM_URL)}")
    typer.echo(
        f"📖 Learn more about the RareLink-CDM in REDCap here: {hyperlink('RareLink-CDM Documentation', DOCS_RARELINK_CDM_URL)}")
    typer.echo(
        f"📖 Learn more about the REDCap Template Project here: {hyperlink('RareLink Core REDCap Project', RARELINK_TEMPLATE_PROJECT)}")

    current_version = get_current_version()
    proceed = typer.confirm(
        f"The most current RareLink Template Project version is {current_version}. "
        "Would you like to download it?"
    )
    if not proceed:
        typer.secho(error_text("❌ Download canceled."))
        raise typer.Exit()

    output_file = downloads_folder / "rarelink_redcap_project.xml"
    download_file(XML_PROJECT_DOWNLOAD_URL, output_file)
    between_section_separator()

    hint_text("\n👉 Next steps:")
    typer.echo(
        "Note: You can only continue if you are a REDCap administrator. "
        "Otherwise, reach out to your REDCap admin to install the template project.")
    typer.echo(
        f"For more information check the documentation: {hyperlink('RareLink Core REDCap Project', RARELINK_TEMPLATE_PROJECT)}")
    typer.echo(
        f"If you're a REDCap admin, you can run {format_command('rarelink redcap-setup upload-project-template')}")
    typer.secho(
        f"-> Please view the changelog for important updates or changes: {hyperlink('View Changelog', CHANGELOG_URL)}"),
    end_of_section_separator()

    
    
