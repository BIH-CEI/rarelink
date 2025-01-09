import pytest
from typer.testing import CliRunner
from rarelink.cli.setup import app as setup_app

runner = CliRunner()

@pytest.mark.parametrize(
    "command,expected_output",
    [
        (
            ["redcap-project"],
            "Welcome to the REDCap Project Setup",
        ),
        (
            ["api-keys"],
            "RareLink API Keys Setup",
        ),
        (
            ["data-dictionary"],
            "RareLink-CDM Data Dictionary Upload",
        ),
        (
            ["view"],
            "Viewing Current Configuration",
        ),
        (
            ["reset"],
            "Resetting Configuration",
        ),
    ],
)
def test_setup_commands(command, expected_output):
    """
    Ensure that all `setup` commands run without errors and output expected text.
    """
    result = runner.invoke(setup_app, command)
    assert result.exit_code == 0, f"Command {command} failed with: {result.output}"
    assert expected_output in result.output
