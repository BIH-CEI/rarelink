from typer.testing import CliRunner
from rarelink.cli.redcap_setup import app  # Assuming the main CLI app is defined in rarelink/cli/__init__.py

runner = CliRunner()

def test_info_command():
    """
    Test the 'info' command of the template-project app.
    """
    result = runner.invoke(app, ["template-project", "info"])
    
    # Check the command runs successfully
    assert result.exit_code == 0, "The 'info' command did not execute successfully."
    
    # Verify the header is in the output
    assert "RareLink Template Project Information" in result.output, "Header not found in output."
    
    # Verify the warning message
    assert (
        "The 'template-project' feature is not implemented in the current RareLink version v2.0.0."
        in result.output
    ), "Warning message not found in output."
    
    # Verify the link to download the template project
    assert (
        "https://rarelink.readthedocs.io/en/latest/resources/rarelink_template_project.xml"
        in result.output
    ), "Download link not found in output."
    
    # Verify the link to the documentation
    assert (
        "https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_3_rarelink_core_redcap_project.html"
        in result.output
    ), "Documentation link not found in output."
    
    print("All assertions passed for the 'info' command.")

if __name__ == "__main__":
    test_info_command()
    print("Info command test completed successfully.")
