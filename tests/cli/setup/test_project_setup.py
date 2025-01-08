from typer.testing import CliRunner
from rarelink.cli import app as cli_app

runner = CliRunner()

def test_redcap_project_setup_start():
    """
    Test the `redcap-setup start` command.
    """
    result = runner.invoke(cli_app, ["redcap-setup", "start"])
    print(result.stdout)  # Debug the output
    assert result.exit_code == 0
    assert "▶▶▶ Welcome to the REDCap Project Setup" in result.stdout
    # Ensure it includes separators as part of the verification
    assert "================================================================================" in result.stdout
