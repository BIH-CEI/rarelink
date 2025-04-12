import pytest
from typer.testing import CliRunner
from rarelink.cli.redcap import app as redcap_tools_app

runner = CliRunner()

@pytest.mark.parametrize(
    "command",
    [
        ["download-records"],
        ["fetch-metadata"],
        ["upload-records"]
        
    ],
)
def test_redcap_tools_commands_executable(command):
    """
    Ensure that all `redcap` commands are executable without errors.
    """
    result = runner.invoke(redcap_tools_app, command, input="n\n")
    assert result.exit_code in [0, 1], (
        f"Command {command} failed unexpectedly with: {result.output}"
    )
