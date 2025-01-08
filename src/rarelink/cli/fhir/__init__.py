import typer
from .setup import setup
# from .execute_pipeline import execute_pipeline
# from .write_resources import write_resources

app = typer.Typer()

app.command()(setup)
# app.command()(execute_pipeline)
# app.command()(write_resources)

@app.callback(invoke_without_command=True)
def fhir_group():
    """Manage the REDCap-toFHIR configurations and pipeline execution."""
    typer.echo("Welcome to RareLink FHIR tools!")
