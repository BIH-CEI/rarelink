from typer.testing import CliRunner
from rarelink.cli.redcap_setup.data_dictionary import app as data_dictionary_app

runner = CliRunner()

def test_upload_command_callable():
    """
    Test if the 'upload' command in the data_dictionary app is callable.
    """
    result = runner.invoke(data_dictionary_app, ["upload", "--help"])

    assert result.exit_code == 0, "The 'upload' command is not callable."
    assert "Upload the most current RareLink-CDM Data Dictionary" in result.output, "Command help text is missing."

if __name__ == "__main__":
    test_upload_command_callable()
    print("Upload command is callable.")
