import pytest
from typer.testing import CliRunner
from rarelink.cli.redcap_tools import app as redcap_tools_app

runner = CliRunner()

@pytest.mark.parametrize(
    "command,expected_output",
    [
        (
            ["download-records"],
            "Fetch REDCap Records",
        ),
    ],
)
def test_redcap_tools_commands(command, expected_output):
    """
    Ensure that all `redcap_tools` commands run without errors and output 
    expected text.
    """
    result = runner.invoke(redcap_tools_app, command)
    assert result.exit_code == 0, f"Command {command} failed with: {result.output}"
    assert expected_output in result.output

# Example for adding future commands:
# Uncomment and extend the list in @pytest.mark.parametrize to test additional commands.
# e.g.,
# ("upload-records", "Upload Records to REDCap"),
# ("fetch-metadata", "Fetch Metadata from REDCap")
