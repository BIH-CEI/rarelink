# tests/cli/test_data_dictionary.py
from typer.testing import CliRunner
from src.rarelink.cli.redcap_setup.data_dictionary import app as data_dictionary_app
from pathlib import Path
import json

runner = CliRunner()

# Mock configuration file path
MOCK_CONFIG_FILE = Path.home() / ".rarelink_redcap_config.json"


def setup_mock_config(api_url: str, api_token: str):
    """
    Create a mock REDCap API configuration file for testing.
    """
    config = {"api_url": api_url, "api_token": api_token}
    MOCK_CONFIG_FILE.write_text(json.dumps(config))


def teardown_mock_config():
    """
    Remove the mock configuration file after tests.
    """
    if MOCK_CONFIG_FILE.exists():
        MOCK_CONFIG_FILE.unlink()


def test_upload_no_config():
    """
    Test the `upload` function when no REDCap configuration file exists.
    """
    if MOCK_CONFIG_FILE.exists():
        MOCK_CONFIG_FILE.unlink()  # Ensure the mock config doesn't exist

    result = runner.invoke(data_dictionary_app, ["upload"])
    assert result.exit_code != 0
    assert "No REDCap API configuration found" in result.stdout


def test_upload_incomplete_config():
    """
    Test the `upload` function with incomplete REDCap configuration.
    """
    setup_mock_config(api_url="", api_token="test_token")

    result = runner.invoke(data_dictionary_app, ["upload"])
    assert result.exit_code != 0
    assert "Incomplete REDCap API configuration" in result.stdout

    teardown_mock_config()


def test_upload_successful(mocker):
    """
    Test the `upload` function with a valid configuration and successful API call.
    """
    # Mock a valid configuration
    setup_mock_config(api_url="https://redcap.example.com/api/", api_token="test_token")

    # Mock the requests.post method to simulate a successful API response
    mock_post = mocker.patch("requests.post")
    mock_post.return_value.status_code = 200
    mock_post.return_value.text = "Success"

    result = runner.invoke(data_dictionary_app, ["upload"])
    assert result.exit_code == 0
    assert "Data Dictionary uploaded successfully" in result.stdout

    teardown_mock_config()


def test_upload_api_failure(mocker):
    """
    Test the `upload` function when the API call fails.
    """
    # Mock a valid configuration
    setup_mock_config(api_url="https://redcap.example.com/api/", api_token="test_token")

    # Mock the requests.post method to simulate a failed API response
    mock_post = mocker.patch("requests.post")
    mock_post.side_effect = Exception("API call failed")

    result = runner.invoke(data_dictionary_app, ["upload"])
    assert result.exit_code != 0
    assert "Failed to upload Data Dictionary" in result.stdout

    teardown_mock_config()
