"""
RareLink Main Package

RareLink - A Rare Disease Interoperability Framework in REDCap
linking registry use, FHIR, and Phenopackets.
"""

__version__ = "2.0.0"

# Import submodules to make them available
from . import cli
from . import utils
from . import phenopackets
from . import tofhir

__all__ = ["cli", "utils", "phenopackets", "tofhir", "__version__"]

from typer import Typer

# Initialize the Typer app for CLI commands
app = Typer()

# Optional: Add basic information for CLI
@app.command()
def version():
    """Show the current version of RareLink."""
    print(f"RareLink version: {__version__}")