import pytest
from typer.testing import CliRunner
from rarelink.cli.fhir import app as fhir_app

runner = CliRunner()

@pytest.mark.parametrize(
    "command,expected_output",
    [
        (
            ["setup"],
            "RareLink FHIR Setup",
        ),
        (
            ["hapi-server"],
            "Setting up a Local HAPI FHIR Server",
        ),
        (
            ["export"],
            "REDCap to FHIR export",
        ),
        (
            ["restart-dockers"],
            "Stopping all running containers...",
        ),
    ],
)
def test_fhir_commands(command, expected_output):
    """
    Ensure that all `fhir` commands run without errors and output expected text.
    """
    result = runner.invoke(fhir_app, command)
    assert result.exit_code == 0, f"Command {command} failed with: {result.output}"
    assert expected_output in result.output
