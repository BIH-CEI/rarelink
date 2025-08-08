import pytest
from typer.testing import CliRunner
from rarelink.cli.fhir import app as fhir_app

runner = CliRunner()

@pytest.mark.parametrize(
    "command",
    [
        ["setup"],
        ["hapi-server"],
        ["export"],
        ["restart-dockers"],
    ],
)
def test_fhir_commands_executable(command):
    """
    Ensure that all `fhir` commands are executable without errors.
    """
    result = runner.invoke(fhir_app, command, input="n\n")
    assert result.exit_code in [0, 1], (
        f"Command {command} failed unexpectedly with: {result.output}"
    )
