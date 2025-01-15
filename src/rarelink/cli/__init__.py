import typer
from rarelink.cli.framework import app as framework
from rarelink.cli.setup import app as redcap_setup_app
from rarelink.cli.redcap_tools import app as redcap_tools_app
from rarelink.cli.fhir import app as fhir_app
from rarelink.cli.utils.string_utils import format_command

# Main Typer application
app = typer.Typer()

# Add command groups
app.add_typer(framework, name="framework", help=f"Configure global settings\
 of the RareLink framework - {format_command('rarelink framework --help')}")
app.add_typer(redcap_setup_app, name="setup", help=f"Setup the RareLink\
 framework locally - {format_command('rarelink setup --help')}")
app.add_typer(redcap_tools_app, name="redcap", help=f"Interact with a\
 REDCap project: {format_command('rarelink redcap --help')}\
 for more information.")
app.add_typer(fhir_app, name="fhir", help=f"Setup, manage, and execute the\
 REDCap-FHIR module: {format_command('rarelink fhir --help')}\
 for more information.")

def version_callback(value: bool):
    """
    Display the RareLink version and exit.
    """
    if value:
        typer.echo("RareLink version 2.0.0.dev0")
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the RareLink version and exit.",
    )
):
    """
    Welcome to the RareLink CLI! This tool is designed to help you setup and 
    manage the RareLink framework around your local REDCap project,
    interact with your REDCap project, and perform various tasks.
    """
    pass

if __name__ == "__main__":
    app()
