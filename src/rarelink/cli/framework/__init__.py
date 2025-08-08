import typer
from rarelink.cli.framework.status import status
from rarelink.cli.framework.reset import reset
from rarelink.cli.framework.update import update
from rarelink.cli.framework.version import version

# Initialize the framework Typer application
app = typer.Typer()

@app.callback(invoke_without_command=True)
def framework():
    """
    Setup and manage the RareLink framework.

    Use this command group to configure global settings
    """

app.command()(status)
app.command()(reset)
app.command()(update)
app.command()(version)

if __name__ == "__main__":
    app()
