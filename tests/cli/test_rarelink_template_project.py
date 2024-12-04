from typer.testing import CliRunner
from rarelink.cli.redcap_setup.rarelink_template_project import app
from unittest.mock import patch, mock_open

runner = CliRunner()

# Mock configuration for REDCap API
mock_config = {
    "api_url": "http://example.com/redcap/api/",
    "api_super_token": "mock_super_token"
}

@patch("rarelink.cli.redcap_setup.rarelink_template_project.CONFIG_FILE", "/tmp/mock_config.json")
@patch("builtins.open", new_callable=mock_open, read_data='{"api_url": "http://example.com/redcap/api/", "api_super_token": "mock_super_token"}')
@patch("requests.post")
def test_rarelink_template_project_with_super_token(mock_post, mock_file):
    """
    Test the `rarelink_template_project` command when the user has a super token.
    """
    # Mock the API response
    mock_response = mock_post.return_value
    mock_response.status_code = 200
    mock_response.text = '{"message": "Project created successfully"}'

    result = runner.invoke(app, ["rarelink-template-project"], input="yes\n")
    assert result.exit_code == 0
    assert "🔑 API Super Token detected. Proceeding with project creation..." in result.stdout
    assert "✅ RareLink template project created successfully." in result.stdout
    assert mock_post.called

@patch("rarelink.cli.redcap_setup.rarelink_template_project.CONFIG_FILE", "/tmp/mock_config.json")
@patch("builtins.open", new_callable=mock_open)
def test_rarelink_template_project_without_super_token(mock_file):
    """
    Test the `rarelink_template_project` command when the user does not have a super token.
    """
    result = runner.invoke(app, ["rarelink-template-project"], input="no\n")
    assert result.exit_code == 0
    assert "⚠️ REDCap API Super Token is required for this operation." in result.stdout
    assert "📖 Documentation for setting up a RareLink project" in result.stdout
    assert "rarelink redcap-setup download rarelink_template_project" in result.stdout

@patch("rarelink.cli.redcap_setup.rarelink_template_project.CONFIG_FILE", "/tmp/mock_config.json")
@patch("builtins.open", new_callable=mock_open, read_data='{}')
def test_rarelink_template_project_missing_config(mock_file):
    """
    Test the `rarelink_template_project` command when the configuration file is missing.
    """
    result = runner.invoke(app, ["rarelink-template-project"], input="yes\n")
    assert result.exit_code == 1
    assert "❌ Configuration file not found." in result.stdout

@patch("rarelink.cli.redcap_setup.rarelink_template_project.CONFIG_FILE", "/tmp/mock_config.json")
@patch("builtins.open", new_callable=mock_open, read_data='{"api_url": "http://example.com/redcap/api/"}')
def test_rarelink_template_project_missing_super_token(mock_file):
    """
    Test the `rarelink_template_project` command when the super token is missing.
    """
    result = runner.invoke(app, ["rarelink-template-project"], input="yes\n")
    assert result.exit_code == 1
    assert "❌ API super token not found in your configuration." in result.stdout
