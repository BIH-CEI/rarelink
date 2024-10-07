import unittest
import os
import json
from src.parsing.create_data_elements_json import create_data_elements_json

class TestCreateDataElementsJson(unittest.TestCase):
    """
    Tests for the function that creates data elements JSON.

    This class includes methods to test the creation of data elements in JSON
    format, ensuring the file is created, properly structured, and contains
    the expected keys and data types.
    """

    def setUp(self):
        """
        Set up test environment.

        This method defines the version and expected output file path for
        the data elements JSON file. It runs before each test method.
        """
        self.version = "v2_0_0_dev0"
        self.output_file = f"res/{self.version}/rd_cdm_data_elements_{self.version}.json"
    
    def test_create_data_elements_json(self):
        """
        Test if the data elements JSON file is correctly created.

        This method calls the function to create the data elements JSON, verifies
        if the file exists, checks the file structure, and ensures the presence
        of required keys like 'dataElements' and the correct data type.
        """
        create_data_elements_json(self.version)
        self.assertTrue(
            os.path.exists(self.output_file), "Output file not created")
        
        with open(self.output_file, 'r') as f:
            data = json.load(f)
        
        self.assertIsInstance(data, dict)
        self.assertIn("dataElements", data)
        
        for element in data["dataElements"]:
            self.assertIn("dataType", element)
            self.assertIsInstance(element["dataType"], str)

if __name__ == "__main__":
    unittest.main()
