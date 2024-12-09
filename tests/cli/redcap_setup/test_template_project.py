import requests
from typer.testing import CliRunner
from rarelink.cli import app
from unittest.mock import patch, MagicMock
from pathlib import Path
import pytest

runner = CliRunner()

# Path to the mock config file
MOCK_CONFIG_FILE = Path(__file__).parent / "mock_config.json"


def test_cli_help():
    """
    Test if the CLI help for the 'redcap-setup' group displays correctly.
    """
    result = runner.invoke(app, ["redcap-setup", "--help"])
    print(result.stdout)


def test_template_project_help():
    """
    Test if the CLI help for the 'template-project' command displays correctly
    and lists 'upload' as a subcommand.
    """
    result = runner.invoke(app, ["redcap-setup", "template-project", "--help"])
    print(result.stdout)  # Outputs the help structure
    assert "upload" in result.stdout  # Ensure 'upload' is listed under subcommands


@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
@patch("requests.post")  # Mock the HTTP POST request
def test_template_project_upload(mock_post):
    """
    Test the 'upload' command with a valid configuration and mocked API call.
    Ensures the command runs successfully and the API call is made correctly.
    """
    MOCK_CONFIG_FILE.write_text(
        '{"api_url": "http://example.com/redcap/api/", '
        '"api_super_token": "mock_super_token"}'
    )

    # Mock the API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = '{"message": "Project created successfully"}'
    mock_post.return_value = mock_response

    # Invoke the CLI command
    result = runner.invoke(
        app,
        ["redcap-setup", "template-project", "upload"],
        input="yes\n",  # Simulate typing "yes" for the API super token prompt
    )
    print(result.stdout)  # Debug the CLI output

    # Assertions
    assert result.exit_code == 0
    assert "🚀 RareLink Template Project Setup" in result.stdout
    assert "🔑 API Super Token detected. Proceeding with project creation..." \
        in result.stdout
    assert "✅ RareLink template project created successfully." in result.stdout

    # Ensure the mock POST request was called with correct arguments
    mock_post.assert_called_once_with(
        "http://example.com/redcap/api/",
        data={
            "token": "mock_super_token",
            "content": "project",
            "format": "json",
            "data": '{"project_title": "RareLink Template Project", '
                    '"purpose": 0, "purpose_other": "", '
                    '"project_notes": "RareLink template project created '
                    'via API."}'
        },
    )


@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
@patch("requests.post")
def test_template_project_with_super_token(mock_post):
    """
    Test the 'upload' command with a valid API super token, ensuring it
    successfully proceeds with project creation.
    """
    # Mock the API response
    mock_response = mock_post.return_value
    mock_response.status_code = 200
    mock_response.text = '{"message": "Project created successfully"}'

    # Invoke the CLI command
    result = runner.invoke(app, ["redcap-setup", "template-project", "upload"],
                           input="yes\n")

    # Assertions
    assert result.exit_code == 0

@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
def test_template_project_without_super_token():
    """
    Test the 'upload' command when the user does not have a super token,
    ensuring it exits with the correct error message.
    """
    result = runner.invoke(
        app, ["redcap-setup", "template-project", "upload"], input="no\n"
    )
    assert result.exit_code == 2  # Exit with code 2 for "no" response
    assert "⚠️ REDCap API Super Token is required for this operation." in \
        result.stdout


@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
def test_template_project_missing_config():
    """
    Test the 'upload' command when the configuration file is missing,
    ensuring it exits with the correct error message.
    """
    invalid_config_file = Path(__file__).parent / "missing_config.json"
    if invalid_config_file.exists():
        invalid_config_file.unlink()

    with patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE",
               invalid_config_file):
        result = runner.invoke(
            app, ["redcap-setup", "template-project", "upload"], input="yes\n"
        )
        assert result.exit_code == 2  # Exit expected for missing config
        assert "❌ Configuration file not found." in result.stdout


@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
def test_template_project_missing_super_token():
    """
    Test the 'upload' command when the configuration file lacks the super token,
    ensuring it exits with the correct error message.
    """
    incomplete_config_file = Path(__file__).parent / "incomplete_config.json"
    incomplete_config_file.write_text(
        '{"api_url": "http://example.com/redcap/api/"}'
    )

    with patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE",
               incomplete_config_file):
        result = runner.invoke(
            app, ["redcap-setup", "template-project", "upload"], input="yes\n"
        )
        assert result.exit_code == 2  # Exit expected for missing super token
        assert "❌ API super token not found in your configuration." in \
            result.stdout

    incomplete_config_file.unlink()


@patch("requests.post", side_effect=requests.RequestException("Mocked exception"))
@patch("rarelink.cli.redcap_setup.template_project.CONFIG_FILE", MOCK_CONFIG_FILE)
def test_template_project_api_exception(mock_post):
    """
    Test the 'upload' command when the API call raises an exception, ensuring it
    exits with the correct error message.
    """
    result = runner.invoke(
        app, ["redcap-setup", "template-project", "upload"], input="yes\n"
    )
    assert result.exit_code == 2  # Exit with code 2 for API exception
    assert "❌ Error during API request: Mocked exception" in result.stdout
