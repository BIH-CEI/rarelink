# tests/cli/test_framework.py
from typer.testing import CliRunner
from rarelink.cli import app

runner = CliRunner()

def test_update():
    result = runner.invoke(app, ["framework-setup", "update"])
    assert result.exit_code == 0
    assert "Updating RareLink framework..." in result.stdout

def test_reset():
    result = runner.invoke(app, ["framework-setup", "reset"])
    assert result.exit_code == 0
    assert "Framework reset successfully." in result.stdout

def test_status():
    result = runner.invoke(app, ["framework-setup", "status"])
    assert result.exit_code == 0
    assert "Framework status: All good!" in result.stdout
