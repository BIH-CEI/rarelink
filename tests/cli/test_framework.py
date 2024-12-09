from typer.testing import CliRunner
from rarelink.cli import app

runner = CliRunner()

def test_status():
    """
    Test the `framework-setup status` command to check if it runs without error.
    """
    result = runner.invoke(app, ["framework", "status"])
    assert result.exit_code == 0
    assert "Checking RareLink framework status..." in result.stdout

def test_update():
    """
    Test the `framework-setup update` command to check if it runs without error.
    """
    result = runner.invoke(app, ["framework", "update"])
    assert result.exit_code == 0
    assert "Updating RareLink to the latest version..." in result.stdout

def test_version():
    """
    Test the `framework-setup version` command to check if it runs without error.
    """
    result = runner.invoke(app, ["framework", "version"])
    assert result.exit_code == 0
    assert "Fetching RareLink version..." in result.stdout

def test_reset():
    """
    Test the `framework-setup reset` command to check if it runs without error.
    """
    result = runner.invoke(app, ["framework", "reset"])
    assert result.exit_code == 0
    assert "Resetting the RareLink framework..." in result.stdout
