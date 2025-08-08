import typer
from .export import export

app = typer.Typer()

app.command()(export)

@app.callback(invoke_without_command=True)
def phenopackets():
    """Manage the REDCap-toFHIR configurations and pipeline execution."""
