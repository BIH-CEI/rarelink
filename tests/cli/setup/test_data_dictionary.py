from typer.testing import CliRunner
from rarelink.cli.setup.data_dictionary import app as data_dictionary_app

runner = CliRunner()

def test_data_dictionary_callable():
    """
    Test if the `data-dictionary` command is callable.
    """
    result = runner.invoke(data_dictionary_app, ["app", "--help"])
    assert result.exit_code == 0, "The `data-dictionary` command is not callable."
    assert "Upload the most current RareLink-CDM Data Dictionary" in result.stdout, "Help text for `data-dictionary` command is missing."

if __name__ == "__main__":
    test_data_dictionary_callable()
    print("✅ Data Dictionary command is callable.")
