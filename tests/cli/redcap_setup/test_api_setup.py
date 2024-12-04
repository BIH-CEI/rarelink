from typer.testing import CliRunner
from rarelink.cli.redcap_setup.api_setup import app as redcap_api_setup_app
from pathlib import Path
import pytest

runner = CliRunner()
CONFIG_FILE = Path.home() / ".rarelink_redcap_config.json"

# Fixture to clean up config file before and after tests
@pytest.fixture(autouse=True)
def cleanup_config_file():
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
    yield
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()


def test_redcap_api_setup_start_project_created():
    """
    Test the `redcap-api-setup start` command when the REDCap project is already created.
    """
    result = runner.invoke(
        redcap_api_setup_app, ["start"], input="y\nhttp://example.com/redcap/api/\nmy_api_token\n"
    )
    assert result.exit_code == 0
    assert "🚀 Welcome to the RareLink REDCap API Setup!" in result.stdout
    assert "Great! Let's set up the REDCap API access." in result.stdout
    assert "✅ REDCap API configuration saved locally" in result.stdout
    assert CONFIG_FILE.exists()
    config = CONFIG_FILE.read_text()
    assert "http://example.com/redcap/api/" in config
    assert "my_api_token" in config


def test_redcap_api_setup_start_project_not_created():
    """
    Test the `redcap-api-setup start` command when the REDCap project is not created.
    """
    result = runner.invoke(redcap_api_setup_app, ["start"], input="n\n")
    assert result.exit_code == 0
    assert "👉 Please run 'redcap-project-setup start'" in result.stdout
    assert "📖 Documentation: https://rarelink.readthedocs.io/en/latest/3_installation/3_1_setup_redcap_project.html" in result.stdout
    assert not CONFIG_FILE.exists()


def test_redcap_api_setup_view_no_config():
    """
    Test the `redcap-api-setup view` command when no configuration exists.
    """
    result = runner.invoke(redcap_api_setup_app, ["view"])
    assert result.exit_code != 0
    assert "❌ No REDCap configuration found" in result.stdout


def test_redcap_api_setup_reset():
    """
    Test the `redcap-api-setup reset` command.
    """
    CONFIG_FILE.write_text("test content")
    result = runner.invoke(redcap_api_setup_app, ["reset"])
    assert result.exit_code == 0
    assert "🔄 REDCap configuration has been reset." in result.stdout
    assert not CONFIG_FILE.exists()
