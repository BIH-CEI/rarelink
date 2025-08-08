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
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name)
        
        # Mock .env file
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
        
        # Mock redcap-projects.json file
        self.redcap_projects_content = """
[
    {"id": "12345", "token": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
]
"""
        self.redcap_projects_file = self.output_dir / "redcap-projects.json"
        self.redcap_projects_file.write_text(self.redcap_projects_content.strip())

    def tearDown(self):
        self.temp_dir.cleanup()

    @patch('subprocess.run')
    def test_framework_status_command(self, mock_run):
        from rarelink.cli import app
        mock_run.return_value = MagicMock(returncode=0)
        result = self.runner.invoke(app, ["framework", "status"])
        self.assertEqual(result.exit_code, 0)
        mock_run.assert_called_once_with(["pip", "show", "rarelink"], check=True)

    @patch('subprocess.run')
    def test_fhir_export_command(self, mock_run):
        from rarelink.cli.fhir import app as fhir_app
        mock_run.return_value = MagicMock(returncode=0)

        original_cwd = os.getcwd()
        os.chdir(self.output_dir)
        try:
            with patch.object(Path, 'exists', return_value=True):
                result = self.runner.invoke(fhir_app, ["export"], input="y\n")
        finally:
            os.chdir(original_cwd)

        self.assertEqual(result.exit_code, 0)
        mock_run.assert_called()

    @patch('subprocess.run')
    def test_fhir_hapi_server_command(self, mock_run):
        from rarelink.cli.fhir import app as fhir_app
        mock_run.side_effect = [
            MagicMock(returncode=0, stdout=b"Docker version"),
            MagicMock(returncode=0),
            MagicMock(stdout=b""),
            MagicMock(stdout=b""),
            MagicMock(returncode=0)
        ]

        result = self.runner.invoke(fhir_app, ["hapi-server"])
        self.assertEqual(result.exit_code, 0)
        self.assertGreaterEqual(mock_run.call_count, 3)

    @patch('rarelink.cli.setup.keys.write_env_file')
    @patch('rarelink.cli.setup.keys.validate_env')
    def test_setup_keys_command(self, mock_validate_env, mock_write_env_file):
        from rarelink.cli.setup import app as setup_app
        mock_validate_env.return_value = None
        mock_write_env_file.return_value = None

        with patch('rarelink.cli.setup.keys.masked_input', side_effect=["bioportal-api-key", "redcap-api-token"]):
            original_cwd = os.getcwd()
            os.chdir(self.output_dir)
            try:
                result = self.runner.invoke(setup_app, ["keys"], input="y\nhttps://redcap.example.com/api/\n12345\nTest Project\nTest User\nn\n")
            finally:
                os.chdir(original_cwd)

        self.assertEqual(result.exit_code, 0)
        mock_write_env_file.assert_called()
        mock_validate_env.assert_called()

    def test_phenopackets_export_command(self):
        from rarelink.cli.phenopackets import app as phenopackets_app
        input_path = self.output_dir / "test-records.json"
        output_dir = self.output_dir / "phenopackets_output"

        input_path.write_text('[{"record_id": "101", "date_of_birth": "2000-01-01", "sex": "Male"}]')

        original_cwd = os.getcwd()
        os.chdir(self.output_dir)
        try:
            result = self.runner.invoke(phenopackets_app, ["export", "--input-path", str(input_path), "--output-dir", str(output_dir), "--skip-validation"], input="y\n")
        finally:
            os.chdir(original_cwd)

        self.assertEqual(result.exit_code, 0)
        self.assertIn("REDCap to Phenopackets Export", result.stdout)

    @patch('requests.post')
    def test_redcap_fetch_metadata_command(self, mock_post):
        from rarelink.cli.redcap import app as redcap_app
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"project_title": "Test Project"}]
        mock_post.return_value = mock_response

        env = {"REDCAP_API_TOKEN": "aaa", "REDCAP_URL": "https://redcap.example.com/api/", "REDCAP_PROJECT_ID": "12345", "REDCAP_PROJECT_NAME": "Test Project"}
        original_cwd = os.getcwd()
        os.chdir(self.output_dir)
        try:
            result = self.runner.invoke(redcap_app, ["fetch-metadata"], env=env)
        finally:
            os.chdir(original_cwd)

        self.assertEqual(result.exit_code, 0)
        mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()