from typer.testing import CliRunner
from rarelink.cli import app
from unittest.mock import patch

runner = CliRunner()

def test_status():
    """
    Test the `framework-setup status` command to check if it runs without error.
    """
    result = runner.invoke(app, ["framework", "status"])
    assert result.exit_code == 0
    assert "Checking RareLink framework status..." in result.stdout

@patch("subprocess.run")
def test_update(mock_subprocess_run):
    """
    Test the `framework update` command to check if it runs without error,
    updates RareLink and its submodules/Docker image, and prints a __pycache__
    cleanup summary.
    """
    # Mock subprocess.run to simulate successful execution for pip, git, and docker commands.
    mock_subprocess_run.return_value.returncode = 0

    result = runner.invoke(app, ["framework", "update"])

    # Assertions to ensure the command behaves as expected.
    assert result.exit_code == 0
    assert "Updating RareLink to the latest version..." in result.stdout
    assert "✅ RareLink has been successfully updated." in result.stdout
    # Updated expected message: note the space after the 🔄 emoji.
    assert "🔄 ...updating all RareLink Submodules" in result.stdout
    assert "✅ ToFHIR engine has been successfully updated." in result.stdout
    # Check that the __pycache__ cleanup phase prints a message.
    assert ("No __pycache__ directories found." in result.stdout or 
            "Cleaned " in result.stdout)

    # Verify subprocess.run was called with the correct arguments.
    mock_subprocess_run.assert_any_call(
        ["pip", "install", "--upgrade", "rarelink"], check=True
    )
    mock_subprocess_run.assert_any_call(
        ["git", "submodule", "update", "--init", "--recursive"], check=True
    )
    mock_subprocess_run.assert_any_call(
        ["git", "submodule", "update", "--remote", "--merge"], check=True
    )
    mock_subprocess_run.assert_any_call(
        ["docker", "pull", "srdc/tofhir-engine:latest"], check=True
    )
    
def test_version():
    """
    Test the `framework-setup version` command to check if it runs without error.
    """
    result = runner.invoke(app, ["framework", "version"])
    assert result.exit_code == 0
    assert "Fetching RareLink version..." in result.stdout

def test_reset():
    """
    Test the `framework-setup reset` command to check if it runs without error.
    """
    result = runner.invoke(app, ["framework", "reset"])
    assert result.exit_code == 0
    # Adjust expected text to match actual CLI output
    assert "▶▶▶ Reset RareLink Framework" in result.stdout

