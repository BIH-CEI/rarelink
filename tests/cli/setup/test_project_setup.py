from typer.testing import CliRunner
from rarelink.cli import app as cli_app

runner = CliRunner()

def test_redcap_project_setup_start():
    """Test the `redcap-project` setup command."""
    result = runner.invoke(cli_app, ["setup", "redcap-project"])
    assert result.exit_code == 0
    assert "▶▶▶ Welcome to the REDCap Project Setup" in result.stdout
