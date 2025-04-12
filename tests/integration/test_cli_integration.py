# tests/integration/test_cli_integration.py
import unittest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
from typer.testing import CliRunner

class TestCliIntegration(unittest.TestCase):
    """
    Integration tests for the CLI commands working together.
    """
    
    def setUp(self):
        """Set up test environment."""
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name)
        
        # Create a mock .env file in the temporary directory.
        self.env_content = """
REDCAP_API_TOKEN=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
REDCAP_URL=https://redcap.example.com/api/
REDCAP_PROJECT_ID=12345
REDCAP_PROJECT_NAME=Test Project
BIOPORTAL_API_TOKEN=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
CREATED_BY=Test User
FHIR_REPO_URL=http://hapi-fhir:8080/fhir
"""
        self.env_file = self.output_dir / ".env"
        self.env_file.write_text(self.env_content.strip())
        
        # Create a mock redcap-projects.json file in the temporary directory.
        self.redcap_projects_content = """
[
    {
        "id": "12345",
        "token": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }
]
"""
        self.redcap_projects_file = self.output_dir / "redcap-projects.json"
        self.redcap_projects_file.write_text(self.redcap_projects_content.strip())
    
    def tearDown(self):
        """Clean up after tests."""
        self.temp_dir.cleanup()
    
    @patch('rarelink.cli.framework.status.subprocess.run')
    def test_framework_status_command(self, mock_run):
        """Test the framework status command."""
        from rarelink.cli import app
        
        mock_run.return_value = MagicMock(returncode=0)
        
        result = self.runner.invoke(app, ["framework", "status"])
        
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Checking RareLink framework status", result.stdout)
        self.assertIn("framework is installed and operational", result.stdout)
        
        mock_run.assert_called_once_with(["pip", "show", "rarelink"], check=True)
    
    @patch('rarelink.cli.fhir.export.validate_env')
    @patch('rarelink.cli.fhir.export.validate_redcap_projects_json')
    @patch('rarelink.cli.fhir.export.validate_docker_and_compose')
    @patch('subprocess.run')
    def test_fhir_export_command(self, mock_run, mock_validate_docker, mock_validate_json, mock_validate_env):
        """Test the FHIR export command."""
        from rarelink.cli.fhir import app as fhir_app
        
        mock_validate_env.return_value = None
        mock_validate_json.return_value = None
        mock_validate_docker.return_value = None
        mock_run.return_value = MagicMock(returncode=0)
        
        # Change cwd so configuration files are found.
        original_cwd = os.getcwd()
        os.chdir(self.output_dir)
        try:
            with patch.object(Path, 'exists', return_value=True):
                result = self.runner.invoke(fhir_app, ["export"], input="y\n")
        finally:
            os.chdir(original_cwd)
        
        self.assertEqual(result.exit_code, 0)
        self.assertIn("REDCap to FHIR export", result.stdout)
        self.assertIn("All setup files are valid", result.stdout)
        mock_run.assert_called()
    
    @patch('rarelink.cli.fhir.hapi_server.subprocess.run')
    def test_fhir_hapi_server_command(self, mock_run):
        """Test the FHIR HAPI server command."""
        from rarelink.cli.fhir import app as fhir_app
        
        # Setup mocks for various subprocess calls.
        mock_run.side_effect = [
            MagicMock(returncode=0, stdout=b"Docker version"),  # docker --version
            MagicMock(returncode=0),  # docker network create
            MagicMock(stdout=b""),    # docker ps -a for existing container
            MagicMock(stdout=b""),    # docker ps for running container
            MagicMock(returncode=0)   # docker run command
        ]
        
        result = self.runner.invoke(fhir_app, ["hapi-server"])
        
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Setting up a Local HAPI FHIR Server", result.stdout)
        self.assertIn("HAPI FHIR server is already running", result.stdout)
        self.assertGreaterEqual(mock_run.call_count, 3)
    
    @patch('rarelink.cli.setup.keys.write_env_file')
    @patch('rarelink.cli.setup.keys.validate_env')
    @patch('pathlib.Path.write_text')
    def test_setup_keys_command(self, mock_write_text, mock_validate_env, mock_write_env_file):
        """Test the setup keys command."""
        from rarelink.cli.setup import app as setup_app
        
        mock_validate_env.return_value = None
        mock_write_env_file.return_value = None
        
        with patch('rarelink.cli.setup.keys.masked_input', 
                   side_effect=["bioportal-api-key", "redcap-api-token"]):
            original_cwd = os.getcwd()
            os.chdir(self.output_dir)
            try:
                result = self.runner.invoke(
                    setup_app,
                    ["keys"],
                    input="y\n"
                          "https://redcap.example.com/api/\n"
                          "12345\n"
                          "Test Project\n"
                          "Test User\n"
                          "n\n"
                )
            finally:
                os.chdir(original_cwd)
        
        self.assertEqual(result.exit_code, 0, f"Command failed: {result.stdout}")
        mock_write_env_file.assert_called()
        mock_validate_env.assert_called()
    
    def test_phenopackets_export_command(self):
        """Test the phenopackets export command."""
        from rarelink.cli.phenopackets import app as phenopackets_app
        
        # Create test input and output paths
        input_path = self.output_dir / "test-records.json"
        output_dir = self.output_dir / "phenopackets_output"
        
        # Write a valid test record with all required fields
        # Make sure this record has the exact fields that the mappings require
        input_path.write_text('''[
            {
                "record_id": "101", 
                "date_of_birth": "2000-01-01",
                "sex": "Male"
            }
        ]''')
        
        # Change cwd so that the CLI finds .env and other configuration files
        original_cwd = os.getcwd()
        os.chdir(self.output_dir)
        try:
            # For testing purposes, we just want to make sure the command runs without errors
            # The --skip-validation flag helps avoid complex validation checks
            result = self.runner.invoke(
                phenopackets_app,
                [
                    "export",
                    "--input-path", str(input_path),
                    "--output-dir", str(output_dir),
                    "--skip-validation"
                ],
                input="y\n"  # Accept default mapping
            )
        finally:
            os.chdir(original_cwd)
        
        # Verify the command completed successfully without errors
        self.assertEqual(result.exit_code, 0, 
                        f"Phenopackets export command failed: {result.stdout}")
        self.assertIn("REDCap to Phenopackets Export", result.stdout)
        
        # Optionally verify the output file was created
        output_file = output_dir / "failures.json"
        self.assertTrue(output_file.exists() or "No failures occurred" in result.stdout,
                    "Expected either failures.json to be created or no failures to occur")
    
    @patch('os.environ.get')
    @patch('requests.post')
    def test_redcap_fetch_metadata_command(self, mock_post, mock_environ_get):
        """Test the REDCap fetch metadata command."""
        from rarelink.cli.redcap import app as redcap_app
        
        # Mock os.environ.get to return our test values
        def get_env_var(key, default=None):
            env_vars = {
                "REDCAP_API_TOKEN": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "REDCAP_URL": "https://redcap.example.com/api/",
                "REDCAP_PROJECT_ID": "12345",
                "REDCAP_PROJECT_NAME": "Test Project"
            }
            return env_vars.get(key, default)
        
        mock_environ_get.side_effect = get_env_var
        
        # Mock the response from requests.post
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"project_title": "Test Project"}]
        mock_post.return_value = mock_response
        
        # Change cwd so that .env and redcap-projects.json are found.
        original_cwd = os.getcwd()
        os.chdir(self.output_dir)
        try:
            result = self.runner.invoke(redcap_app, ["fetch-metadata"])
        finally:
            os.chdir(original_cwd)
        
        self.assertEqual(result.exit_code, 0, f"Fetch metadata command failed: {result.stdout}")
        self.assertIn("Fetching REDCap Project Metadata", result.stdout)
        self.assertIn("Project Name: Test Project", result.stdout)
        mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()
    