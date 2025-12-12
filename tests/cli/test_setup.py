import pytest
from typer.testing import CliRunner

from rarelink.cli.setup import app as setup_app
import rarelink.cli.setup.data_dictionary as data_dict_module  # submodule where the command lives

runner = CliRunner()


@pytest.mark.parametrize(
    "command",
    [
        ["redcap-project"],
        ["keys"],
        ["data-dictionary"],
        ["view"],
        ["reset"],
    ],
)
def test_setup_commands_executable(command):
    """
    Ensure that all `setup` commands are executable without errors.
    """
    result = runner.invoke(setup_app, command, input="n\n")
    assert result.exit_code in [0, 1], (
        f"Command {command} failed unexpectedly with: {result.output}"
    )


def test_data_dictionary_command_uses_packaged_file(tmp_path, monkeypatch):
    """
    Ensure that the data-dictionary upload command can find the packaged
    data dictionary file and uses it for the upload.
    """

    # --- Arrange: fake data dictionary file -------------------------------
    data_dict_path = tmp_path / "rarelink_cdm_data_dictionary.csv"
    data_dict_content = "field_name,form_name\nid,baseline_form\n"
    data_dict_path.write_text(data_dict_content, encoding="utf-8")

    # Patch the symbol where it is used: in rarelink.cli.setup.data_dictionary
    monkeypatch.setattr(
        data_dict_module, "get_data_dictionary_path", lambda: data_dict_path
    )

    # Avoid depending on real .env validation logic
    monkeypatch.setattr(
        data_dict_module, "validate_env", lambda required_keys: None
    )

    # Make confirm_action() always “yes” so the command continues
    monkeypatch.setattr(
        data_dict_module, "confirm_action", lambda message: True
    )

    # Redirect the Downloads folder to a *different* temporary directory
    # so tests don’t touch the real home directory and avoid same-file copies
    downloads_dir = tmp_path / "downloads"
    monkeypatch.setattr(
        data_dict_module, "downloads_folder", downloads_dir
    )

    # Also patch the REDCap config that was read at import time
    monkeypatch.setattr(
        data_dict_module, "redcap_url", "https://example.com/redcap/api/"
    )
    monkeypatch.setattr(
        data_dict_module, "redcap_api_token", "TEST_TOKEN"
    )

    # Fake requests.post so we don't actually call any API
    class DummyResponse:
        def raise_for_status(self):
            return None

    def fake_post(url, data):
        # Some minimal assertions to be sure we sent what we expect
        assert url == "https://example.com/redcap/api/"
        assert data["token"] == "TEST_TOKEN"
        assert data["content"] == "metadata"
        assert data["format"] == "csv"
        # Ensure the CSV we send is the one from our fake file
        assert "field_name,form_name" in data["data"]
        return DummyResponse()

    # 👇 Only patch the post function, not the whole requests module
    monkeypatch.setattr(data_dict_module.requests, "post", fake_post)

    # --- Act --------------------------------------------------------------
    result = runner.invoke(setup_app, ["data-dictionary"])

    # --- Assert -----------------------------------------------------------
    assert result.exit_code == 0, result.output
    # Check that it actually reports using the packaged data dictionary
    assert "Using packaged RareLink-CDM Data Dictionary" in result.output

    # Ensure the copy to Downloads happened
    copied_file = downloads_dir / data_dict_path.name
    assert copied_file.exists()
    assert copied_file.read_text(encoding="utf-8") == data_dict_content


def test_data_dictionary_command_handles_missing_file(tmp_path, monkeypatch):
    """
    Ensure that when the packaged data dictionary cannot be found
    (FileNotFoundError), the command fails gracefully with exit code 1.
    """

    def fake_get_data_dictionary_path():
        raise FileNotFoundError("test file not found")

    monkeypatch.setattr(
        data_dict_module, "get_data_dictionary_path", fake_get_data_dictionary_path
    )

    # We still need validate_env to not blow up earlier
    monkeypatch.setattr(
        data_dict_module, "validate_env", lambda required_keys: None
    )

    # Confirm_action can return True; we won't reach upload anyway
    monkeypatch.setattr(
        data_dict_module, "confirm_action", lambda message: True
    )

    # Patch redcap config as before (not strictly needed here, but keeps things clean)
    monkeypatch.setattr(
        data_dict_module, "redcap_url", "https://example.com/redcap/api/"
    )
    monkeypatch.setattr(
        data_dict_module, "redcap_api_token", "TEST_TOKEN"
    )

    result = runner.invoke(setup_app, ["data-dictionary"])

    # Should exit with error because of FileNotFoundError
    assert result.exit_code == 1
    assert "Data Dictionary file not found in package" in result.output
    assert "Please reinstall rarelink or open an issue" in result.output
