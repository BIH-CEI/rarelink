from typer.testing import CliRunner
from rarelink.cli import app

runner = CliRunner()

def test_install():
    """
    Test the `framework-setup install` command.
    """
    result = runner.invoke(app, ["framework-setup", "install"])
    assert result.exit_code == 0  # Ensure the command exits successfully
    assert "Installing RareLink framework dependencies..." in result.stdout
    assert "Dependencies installed successfully." in result.stdout

def test_update():
    """
    Test the `framework-setup update` command.
    """
    result = runner.invoke(app, ["framework-setup", "update"])
    assert result.exit_code == 0  # Ensure the command exits successfully
    assert "Updating RareLink framework..." in result.stdout
    assert "Framework updated successfully." in result.stdout

