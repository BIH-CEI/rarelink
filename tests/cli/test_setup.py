import pytest
from typer.testing import CliRunner
from rarelink.cli.setup import app as setup_app

runner = CliRunner()

@pytest.mark.parametrize(
    "command",
    [
        ["redcap-project"],
        ["keys"],
        ["data-dictionary"],
        ["view"],
        ["reset"],
    ],
)
def test_setup_commands_executable(command):
    """
    Ensure that all `setup` commands are executable without errors.
    """
    result = runner.invoke(setup_app, command, input="n\n")
    assert result.exit_code in [0, 1], (
        f"Command {command} failed unexpectedly with: {result.output}"
    )
