# from typer.testing import CliRunner
# from rarelink.cli.redcap_setup.data_dictionary import app as data_dictionary_app
# from pathlib import Path
# import pytest
# import json
# from unittest.mock import patch

# runner = CliRunner()

# # Temporary test config file
# TEST_CONFIG_FILE = Path.home() / ".rarelink_test_redcap_config.json"

# # Override the path used by the application to use the test config
# @pytest.fixture(autouse=True)
# def override_config_path(monkeypatch):
#     monkeypatch.setattr(
#         "rarelink.cli.redcap_setup.data_dictionary.CONFIG_FILE",
#         TEST_CONFIG_FILE,
#     )

# # Fixture to clean up test config file
# @pytest.fixture(autouse=True)
# def cleanup_test_config_file():
#     if TEST_CONFIG_FILE.exists():
#         TEST_CONFIG_FILE.unlink()
#     yield
#     if TEST_CONFIG_FILE.exists():
#         TEST_CONFIG_FILE.unlink()


# def setup_mock_config(api_url="http://example.com/redcap/api/", api_token="mock_api_token"):
#     """
#     Create a mock configuration file for testing.
#     """
#     config = {"api_url": api_url, "api_token": api_token}
#     TEST_CONFIG_FILE.write_text(json.dumps(config))


# def teardown_mock_config():
#     """
#     Remove the mock configuration file after testing.
#     """
#     if TEST_CONFIG_FILE.exists():
#         TEST_CONFIG_FILE.unlink()


# def test_upload_no_config():
#     """
#     Test the `upload` function when no REDCap configuration file exists.
#     """
#     if TEST_CONFIG_FILE.exists():
#         TEST_CONFIG_FILE.unlink()

#     result = runner.invoke(data_dictionary_app, ["upload"])
#     assert result.exit_code != 0
#     assert "No REDCap API configuration found" in result.stdout


# def test_upload_incomplete_config():
#     """
#     Test the `upload` function with incomplete REDCap configuration.
#     """
#     setup_mock_config(api_url="", api_token="mock_api_token")

#     result = runner.invoke(data_dictionary_app, ["upload"])
#     assert result.exit_code != 0
#     assert "Incomplete REDCap API configuration" in result.stdout

#     teardown_mock_config()


# @patch("requests.post")
# def test_upload_successful(mock_post):
#     """
#     Test the `upload` function with a valid configuration and successful API call.
#     """
#     setup_mock_config(api_url="http://example.com/redcap/api/", api_token="mock_api_token")

#     # Mock the requests.post method to simulate a successful API response
#     mock_post.return_value.status_code = 200
#     mock_post.return_value.text = "Success"

#     result = runner.invoke(data_dictionary_app, ["upload"])
#     assert result.exit_code == 0
#     assert "Data Dictionary uploaded successfully" in result.stdout

#     teardown_mock_config()


# @patch("requests.post")
# def test_upload_api_failure(mock_post):
#     """
#     Test the `upload` function when the API call fails.
#     """
#     setup_mock_config(api_url="http://example.com/redcap/api/", api_token="mock_api_token")

#     # Mock the requests.post method to simulate a failed API response
#     mock_post.side_effect = Exception("API call failed")

#     result = runner.invoke(data_dictionary_app, ["upload"])
#     assert result.exit_code != 0
#     assert "Failed to upload Data Dictionary" in result.stdout

#     teardown_mock_config()
