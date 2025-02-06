"""
RareLink Main Package

RareLink - A Rare Disease Interoperability Framework in REDCap
linking registry use, FHIR, and Phenopackets.
"""

__version__ = "2.0.0.dev1"

from typer import Typer

# Initialize the Typer app for CLI commands
app = Typer()

# Optional: Add basic information for CLI
@app.command()
def version():
    """Show the current version of RareLink."""
    print(f"RareLink version: {__version__}")
