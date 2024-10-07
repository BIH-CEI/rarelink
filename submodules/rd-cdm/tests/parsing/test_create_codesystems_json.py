import unittest
import os
import json
from src.parsing.create_codesystems_json import create_codesystem_json

class TestCreateCodeSystemsJson(unittest.TestCase):
    """
    Tests for the function that creates code systems JSON.

    This class includes methods to test the creation of code systems in JSON
    format, ensuring the file is created, properly structured, and contains
    the expected keys and data types.
    """

    def setUp(self):
        """
        Set up test environment.

        This method defines the version and expected output file path for
        the code systems JSON file. It runs before each test method.
        """
        self.version = "v2_0_0_dev0"
        self.output_file = f"res/{self.version}/rd_cdm_codesystems_{self.version}.json"
    
    def test_create_codesystem_json(self):
        """
        Test if the code systems JSON file is correctly created.

        This method calls the function to create the code systems JSON, verifies
        if the file exists, checks the file structure, and ensures the presence
        of required keys like 'CodeSystems'.
        """
        create_codesystem_json(self.version)
        self.assertTrue(
            os.path.exists(self.output_file), "Output file not created")
        
        with open(self.output_file, 'r') as f:
            data = json.load(f)
        
        self.assertIsInstance(data, dict)
        self.assertIn("CodeSystems", data)

if __name__ == "__main__":
    unittest.main()
