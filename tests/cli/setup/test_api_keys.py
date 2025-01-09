import json
from typer.testing import CliRunner
from rarelink.cli.setup.api_keys import api_keys_app  # Import the Typer instance, not the function

from unittest.mock import patch

runner = CliRunner()

def test_api_keys_executable():
    """Test that the `api-keys` command is executable."""
    # Run the command with minimal input to ensure it doesn't fail immediately
    result = runner.invoke(api_keys_app, input="y\nhttp://example.com/redcap/api/\n1234\nmock_token\nmock_bioportal_key\nn\n")
    
    # Assert that the command runs and exits without an error
    assert result.exit_code == 0
    print("CLI Output:", result.output)
