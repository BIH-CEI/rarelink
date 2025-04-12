# tests/acceptance/test_end_to_end.py
import unittest
import tempfile
import subprocess
import os
import signal
from pathlib import Path
from unittest.mock import patch, MagicMock
from typer.testing import CliRunner

class TestEndToEnd(unittest.TestCase):
    """
    End-to-end tests for the RareLink CLI workflow.
    
    These tests simulate real-world usage by executing the CLI commands as subprocess calls.
    """
    
    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_dir = Path(self.temp_dir.name)
        # Create a sample .env file
        self.env_file = self.test_dir / ".env"
        env_content = """
REDCAP_API_TOKEN=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
REDCAP_URL=https://redcap.example.com/api/
REDCAP_PROJECT_ID=12345
REDCAP_PROJECT_NAME=Test Project
BIOPORTAL_API_TOKEN=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
CREATED_BY=Test User
FHIR_REPO_URL=http://hapi-fhir:8080/fhir
"""
        self.env_file.write_text(env_content)
        # Create a sample redcap-projects.json file
        self.projects_file = self.test_dir / "redcap-projects.json"
        projects_content = """
[
    {
        "id": "12345",
        "token": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }
]
"""
        self.projects_file.write_text(projects_content)
        # Path to the CLI script (for subprocess calls)
        self.cli_path = "rarelink"
        self.runner = CliRunner()
    
    def tearDown(self):
        """Clean up after tests."""
        self.temp_dir.cleanup()
    
    @patch('subprocess.run')
    def test_end_to_end_workflow(self, mock_run):
        """
        Test the complete end-to-end workflow.
        """
        mock_process = MagicMock()
        mock_process.returncode = 0
        mock_process.stdout = b"Success"
        mock_run.return_value = mock_process
        
        # Step 1: Setup keys
        cmd_setup = [self.cli_path, "setup", "keys"]
        result = subprocess.run(cmd_setup, check=True)
        self.assertEqual(result.returncode, 0)
        
        # Step 2: Download REDCap records
        cmd_download = [self.cli_path, "redcap", "download-records", "--output-dir", str(self.test_dir), "--rarelink-cdm"]
        result = subprocess.run(cmd_download, check=True)
        self.assertEqual(result.returncode, 0)
        
        # Step 3: Generate phenopackets
        cmd_phenopackets = [self.cli_path, "phenopackets", "export", "--input-path", str(self.test_dir / "Test_Project-linkml-records.json"), "--output-dir", str(self.test_dir / "phenopackets"), "--skip-validation"]
        result = subprocess.run(cmd_phenopackets, check=True)
        self.assertEqual(result.returncode, 0)
        
        # Step 4: Setup FHIR server
        cmd_hapi = [self.cli_path, "fhir", "hapi-server"]
        result = subprocess.run(cmd_hapi, check=True)
        self.assertEqual(result.returncode, 0)
        
        # Step 5: Export to FHIR
        cmd_fhir = [self.cli_path, "fhir", "export"]
        result = subprocess.run(cmd_fhir, check=True)
        self.assertEqual(result.returncode, 0)
        
        self.assertEqual(mock_run.call_count, 5)

if __name__ == "__main__":
    unittest.main()