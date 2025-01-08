import json
from typer.testing import CliRunner
from rarelink.cli.setup.api_keys import app as api_keys
from pathlib import Path
import pytest
import tempfile
from unittest.mock import patch

runner = CliRunner()

MOCK_CONFIG = {
    "api_url": "http://example.com/redcap/api/",
    "api_token": "mock_token",
    "api_super_token": "mock_super_token",
}

@pytest.fixture
def temp_config_file():
    """
    Provide a temporary file path for storing configuration during tests
    without creating the file initially.
    """
    with tempfile.NamedTemporaryFile(delete=True, suffix=".json") as temp_file:
        temp_file_path = Path(temp_file.name)
    # Ensure the file does not exist
    if temp_file_path.exists():
        temp_file_path.unlink()
    yield temp_file_path

def test_redcap_api_config_start_project_created(temp_config_file, monkeypatch):
    monkeypatch.setattr("rarelink.cli.redcap_setup.api_config.CONFIG_FILE",
                        temp_config_file)

    with patch("rarelink.cli.redcap_setup.api_config.masked_input",
               return_value="mock_token"):
        result = runner.invoke(
            api_keys,
            ["start"],
            input="y\nhttp://example.com/redcap/api/\nn\n",
        )
    assert result.exit_code == 0
    assert "▶▶▶ Welcome to the RareLink REDCap API Setup" in result.stdout

    config = json.loads(temp_config_file.read_text())
    assert config["api_url"] == "http://example.com/redcap/api/"
    assert config["api_token"] == "mock_token"
    assert config["api_super_token"] == ""


def test_redcap_api_config_view_no_config(temp_config_file, monkeypatch):
    """
    Test the `redcap-setup api-config view` command when no configuration exists.
    """
    monkeypatch.setattr("rarelink.cli.redcap_setup.api_config.CONFIG_FILE", 
                        temp_config_file)

    assert not temp_config_file.exists(), "Temporary config file should not\
        exist before the test."

    result = runner.invoke(api_keys, ["view"])
    
    assert result.exit_code == 1
    assert "❌ No REDCap configuration found" in result.stdout


def test_redcap_api_config_view_with_config(temp_config_file, monkeypatch):
    monkeypatch.setattr("rarelink.cli.redcap_setup.api_config.CONFIG_FILE",
                        temp_config_file)

    temp_config_file.write_text(json.dumps(MOCK_CONFIG))

    result = runner.invoke(api_keys, ["view"])
    assert result.exit_code == 0
    assert MOCK_CONFIG["api_url"] in result.stdout
    assert MOCK_CONFIG["api_token"] in result.stdout
    assert MOCK_CONFIG["api_super_token"] in result.stdout


def test_redcap_api_config_reset(temp_config_file, monkeypatch):
    monkeypatch.setattr("rarelink.cli.redcap_setup.api_config.CONFIG_FILE",
                        temp_config_file)

    temp_config_file.write_text(json.dumps(MOCK_CONFIG))

    result = runner.invoke(api_keys, ["reset"])
    assert result.exit_code == 0
    assert "🔄 REDCap configuration has been reset." in result.stdout
    assert not temp_config_file.exists()
