import typer
from .export import export
# from .view import view

app = typer.Typer()

app.command()(export)
#app.command()(view)

@app.callback(invoke_without_command=True)
def phenopackets():
    """Manage the REDCap-toFHIR configurations and pipeline execution."""
    typer.echo("Welcome to RareLink FHIR tools!")
