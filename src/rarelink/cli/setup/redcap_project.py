import typer
from rarelink.cli.utils.string_utils import (
    format_header,
    hint_text,
    hyperlink,
    format_command,
)
from rarelink.cli.utils.terminal_utils import (
    end_of_section_separator,
    between_section_separator,
)

def app():
    """
    Start here if you want to set up your local REDCap Project for RareLink.
    """
    format_header("Welcome to the REDCap Project Setup")

    typer.echo(
        "👉 For more information on REDCap, visit our documentation:"
    )
    typer.echo(
        f"📖 Documentation: {hyperlink('RareLink REDCap Documentation', 'https://rarelink.readthedocs.io/en/latest/1_background/1_6_redcap.html')}"
    )
    
    between_section_separator()


    typer.secho(
        "To create a REDCap project, please follow these steps:",
        fg=typer.colors.GREEN,
        bold=True,
    )
    typer.echo(
        "0. Check if your institution has a REDCap instance — if not, read the "
        "documentation above."
    )
    typer.echo(
        "1. Contact your local REDCap administrator to create your REDCap "
        "project with BioPortal ontology service enabled (required for RareLink!)"
    )
    typer.echo(
        "2. Name your REDCap project, e.g.: 'RareLink - NameofyourInstitution'."
    )
    typer.echo(
        "3. Let your institutional account be added and provide you API access "
        "for the project."
    )
    typer.echo(
        "4. Follow the instructions given to you by your REDCap administrator "
        "to further set up your project."
    )
    hint_text(
        "👉 Be aware of development and production mode. Read the docs and "
        "discuss this with your REDCap admin!",
    )
    typer.echo("5. Copy the API token for the project and keep it secure.")
    typer.echo(
        f"6. Run {format_command('rarelink redcap-setup api-setup')}"
        " to set up the REDCap API access."
    )

    between_section_separator()

    typer.echo("👉 For detailed instructions, visit our documentation:"),
    typer.echo(
        f"📖 Documentation: {hyperlink('Setup REDCap Project', 'https://rarelink.readthedocs.io/en/latest/3_installation/3_2_setup_redcap_project.html')}"
    )
    end_of_section_separator()
    

