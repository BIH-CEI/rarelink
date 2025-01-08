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
DATA_DICTIONARY_DOWNLOAD_URL = "https://rarelink.readthedocs.io/en/latest/_downloads/f734b286306ee9c7f574d3330e8b0a6a/rarelink_cdm_v2_0_0_dev0_datadictionary.csv"
INSTRUMENTS_DOWNLOAD_URL = "https://rarelink.readthedocs.io/en/latest/_downloads/418a358bee84578db6fcab6a51f3ce59/rarelink_cdm_v2_0_0_dev0_instruments.zip"
XML_PROJECT_DOWNLOAD_URL = "https://rarelink.readthedocs.io/en/latest/_downloads/99408edf976b9d46455ecc9d39262261/rarelink_v2_0_0_dev0_redcap_project.xml"
RARELINK_TEMPLATE_PROJECT = "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_3_rarelink_core_redcap_project.html"
CHANGELOG_URL = "https://rarelink.readthedocs.io/en/latest/6_changelog.html"

downloads_folder = Path.home() / "Downloads"

@app.command()
def data_dictionary():
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

    output_file = downloads_folder / f"rarelink_rd_cdm_{current_version}_datadictionary.csv"
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


# @app.command()
# def rarelink_cdm_instruments():
#     """
#     Download the RareLink RD-CDM separate instruments as a .zip file.
#     """
#     format_header("RareLink-CDM - Single Instruments Download")
#     typer.echo(
#         f"📖 Learn more about the underlying CDM here: {hyperlink('RD-CDM Documentation', DOCS_RD_CDM_URL)}")
#     typer.echo(
#         f"📖 Learn more about the single RareLink-CDM Instruments here: {hyperlink('RareLink Instruments', DOCS_RARELINK_INSTRUMENTS_URL)}")

#     current_version = get_current_version()
#     proceed = typer.confirm(
#         f"The most current RD-CDM Instruments version is {current_version}. "
#         "Would you like to download it?"
#     )
#     if not proceed:
#         typer.secho(error_text("❌ Download canceled."))
#         raise typer.Exit()

#     output_file = downloads_folder / f"rarelink_rd_cdm_{current_version}_instruments.zip"
#     download_file(INSTRUMENTS_DOWNLOAD_URL, output_file)
#     between_section_separator()

#     hint_text("\n👉 Next steps:")
#     typer.echo("1. Unzip the instruments.")
#     typer.echo(
#         f"2. Use {format_command('rarelink redcap-setup upload-data-dictionary')} "
#         "to upload the data dictionary to your REDCap project.")
#     typer.echo(
#         f"3. For more information or manual setup check the {hyperlink('Installation guide - REDCap Instruments', DOCS_UPLOAD_DATA_DICTIONARY_URL)}")
#     typer.secho(
#         f"4. Please view the changelog for important updates or changes: {hyperlink('View Changelog', CHANGELOG_URL)}"),
#     end_of_section_separator()
    
    
