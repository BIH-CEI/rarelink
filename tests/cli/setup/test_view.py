from typer.testing import CliRunner
from rarelink.cli.setup.view import app as view_app
import pytest
import json 

runner = CliRunner()

@pytest.fixture
def setup_mock_files(tmp_path):
    """Create mock .env and JSON config files."""
    env_file = tmp_path / ".env"
    config_file = tmp_path / "rarelink_apiconfig.json"
    env_file.write_text("BIOPORTAL_API_TOKEN=mock_token\nREDCAP_PROJECT_URL=http://example.com/redcap/api/\n")
    config_file.write_text(json.dumps({"id": "1234", "token": "mock_token"}))
    return env_file, config_file

def test_view_configuration(setup_mock_files, monkeypatch):
    """Test the `view` command."""
    env_file, config_file = setup_mock_files
    monkeypatch.setattr("rarelink.cli.setup.view.ENV_PATH", env_file)
    monkeypatch.setattr("rarelink.cli.setup.view.CONFIG_FILE", config_file)

    result = runner.invoke(view_app, ["app"])
    assert result.exit_code == 0
    assert "Current .env Configuration" in result.stdout
    assert "BIOPORTAL_API_TOKEN" in result.stdout
    assert "Current JSON Configuration" in result.stdout
