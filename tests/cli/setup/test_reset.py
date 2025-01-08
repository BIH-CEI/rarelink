from typer.testing import CliRunner
from rarelink.cli.setup.reset import app as reset_app

runner = CliRunner()

def test_reset_command_callable():
    """
    Test if the `reset` command is callable.
    """
    result = runner.invoke(reset_app, ["app", "--help"])
    assert result.exit_code == 0, "The `reset` command is not callable."
    assert "Reset all RareLink configuration" in result.stdout, "Help text for `reset` command is missing."

if __name__ == "__main__":
    test_reset_command_callable()
    print("✅ Reset command is callable.")
