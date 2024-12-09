import typer
from rarelink.cli.framework import app as framework
from rarelink.cli.redcap_setup import app as redcap_setup_app

# Main Typer application
app = typer.Typer()

# Add command groups
app.add_typer(framework, name="framework", help="Setup and manage the\
 RareLink framework: `rarelink framework --help` for more information.")
app.add_typer(redcap_setup_app, name="redcap-setup", help="Setup and manage your\
 local REDCap project: `rarelink redcap-setup --help` for more information.")

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
    RareLink CLI.
    """
    pass

if __name__ == "__main__":
    app()