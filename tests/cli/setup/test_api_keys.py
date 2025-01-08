import json
from typer.testing import CliRunner
from rarelink.cli.setup.api_keys import app as api_keys
import pytest
from unittest.mock import patch

runner = CliRunner()

MOCK_CONFIG = {
    "redcap-url": "http://example.com/redcap/api/",
    "id": "1234",
    "token": "mock_token",
    "bioportal_api_key": "mock_bioportal_key",
}

@pytest.fixture
def temp_config_file(tmp_path):
    """Provide a temporary file path for storing configuration during tests."""
    temp_file = tmp_path / "rarelink_apiconfig.json"
    yield temp_file

def test_api_keys_start(temp_config_file, monkeypatch):
    """Test the `api-keys` setup command."""
    monkeypatch.setattr("rarelink.cli.setup.api_keys.MOCK_CONFIG", temp_config_file)

    with patch("rarelink.cli.setup.api_keys.masked_input", return_value="mock_token"):
        result = runner.invoke(api_keys, ["app"], input="y\nhttp://example.com/redcap/api/\n1234\nmock_bioportal_key\n")
    
    assert result.exit_code == 0
    assert "Validation successful" in result.stdout

    config = json.loads(temp_config_file.read_text())
    assert config["redcap-url"] == "http://example.com/redcap/api/"
    assert config["id"] == "1234"
    assert config["token"] == "mock_token"
    assert config["bioportal_api_key"] == "mock_bioportal_key"
