import requests
from typer.testing import CliRunner
from rarelink.cli import app
from unittest.mock import patch
from pathlib import Path
import pytest

runner = CliRunner()

# Path to the mock config file
MOCK_CONFIG_FILE = Path(__file__).parent / "mock_config.json"

@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
@patch("requests.post")
def test_template_project_with_super_token(mock_post):
    mock_response = mock_post.return_value
    mock_response.status_code = 200
    mock_response.text = '{"message": "Project created successfully"}'
    
    result = runner.invoke(app, ["redcap-setup", "template-project", "upload"], input="yes\n")
    assert result.exit_code == 0
    assert "🔑 API Super Token detected. Proceeding with project creation..." in result.stdout
    assert "✅ RareLink template project created successfully." in result.stdout
    assert mock_post.called

@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
def test_template_project_without_super_token():
    result = runner.invoke(app, ["redcap-setup", "template-project", "upload"], input="no\n")
    assert result.exit_code == 2  # Exit expected for "no" response
    assert "⚠️ REDCap API Super Token is required for this operation." in result.stdout

@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
def test_template_project_missing_config():
    invalid_config_file = Path(__file__).parent / "missing_config.json"
    if invalid_config_file.exists():
        invalid_config_file.unlink()
    
    with patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", invalid_config_file):
        result = runner.invoke(app, ["redcap-setup", "template-project", "upload"], input="yes\n")
        assert result.exit_code == 2  # Exit expected for missing config
        assert "❌ Configuration file not found." in result.stdout

@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
def test_template_project_missing_super_token():
    incomplete_config_file = Path(__file__).parent / "incomplete_config.json"
    incomplete_config_file.write_text('{"api_url": "http://example.com/redcap/api/"}')
    
    with patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", incomplete_config_file):
        result = runner.invoke(app, ["redcap-setup", "template-project", "upload"], input="yes\n")
        assert result.exit_code == 2  # Exit expected for missing super token
        assert "❌ API super token not found in your configuration." in result.stdout
    
    incomplete_config_file.unlink()

@patch("requests.post", side_effect=requests.RequestException("Mocked exception"))
@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
def test_template_project_api_exception(mock_post):
    result = runner.invoke(app, ["redcap-setup", "template-project", "upload"], input="yes\n")
    assert result.exit_code == 2  # Exit expected for API exception
    assert "❌ Error during API request: Mocked exception" in result.stdout
