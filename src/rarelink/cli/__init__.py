import click
from .framework import framework_setup
from .redcap import redcap_setup
from .capture import manual_capture, semi_auto_capture
from .generate import phenopacket, fhir_resource
from .validate import validate_phenopacket, validate_fhir

def cli():
    """RareLink Command Line Interface."""
    pass

# Add command groups
cli.add_command(framework_setup)
cli.add_command(redcap_setup)
cli.add_command(manual_capture)
cli.add_command(semi_auto_capture)
cli.add_command(phenopacket)
cli.add_command(fhir_resource)
cli.add_command(validate_phenopacket)
cli.add_command(validate_fhir)

if __name__ == "__main__":
    cli()