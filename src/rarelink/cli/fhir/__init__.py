import typer
from .setup import setup
from .hapi_server import hapi_server
from .restart_dockers import restart_dockers

app = typer.Typer()

app.command()(setup)
app.command()(hapi_server)
app.command()(restart_dockers)

@app.callback(invoke_without_command=True)
def fhir_group():
    """Manage the REDCap-toFHIR configurations and pipeline execution."""
    typer.echo("Welcome to RareLink FHIR tools!")
