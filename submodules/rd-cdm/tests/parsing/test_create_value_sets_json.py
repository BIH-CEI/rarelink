import unittest
import os
import json
from src.parsing.create_value_sets_json import create_value_set_json

class TestCreateValueSetsJson(unittest.TestCase):
    """
    Tests for the function that creates value sets JSON.

    This class includes methods to test the creation of value sets in JSON
    format, ensuring the file is created, properly structured, and contains
    the expected version and key data.
    """

    def setUp(self):
        """
        Set up test environment.

        This method defines the version and expected output file path for
        the value sets JSON file. It runs before each test method.
        """
        self.version = "v2_0_0_dev0"
        self.output_file = f"res/{self.version}/rd_cdm_value_sets_{self.version}.json"
    
    def test_create_value_sets_json(self):
        """
        Test if the value sets JSON file is correctly created.

        This method calls the function to create the value sets JSON, verifies
        if the file exists, checks the file structure, and ensures the presence
        of required keys like 'valueSets' and the correct version.
        """
        create_value_set_json(self.version)
        self.assertTrue(
            os.path.exists(self.output_file), "Output file not created")
        
        with open(self.output_file, 'r') as f:
            data = json.load(f)
        
        self.assertIsInstance(data, dict, "Output is not a dictionary")
        self.assertIn("valueSets", data, "'valueSets' not found in JSON")
        self.assertEqual(
            data.get("version"), self.version, "Version mismatch in JSON"
            )

if __name__ == "__main__":
    unittest.main()
