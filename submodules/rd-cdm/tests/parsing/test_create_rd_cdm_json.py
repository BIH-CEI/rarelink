import unittest
import os
import json
from src.parsing.create_rd_cdm_json import create_final_rd_cdm_json

class TestCreateRdCdmJson(unittest.TestCase):
    """Tests for the function that creates the final RD CDM JSON file."""

    def setUp(self):
        """Set up test environment."""
        self.version = "v2_0_0_dev0"
        self.output_file = f"res/{self.version}/rd_cdm_{self.version}.json"

    def test_create_final_rd_cdm_json(self):
        """Test if the final RD CDM JSON file is correctly created.
        
        This test is a combination of the tests for the individual JSON files
        (code systems, data elements, and value sets) that are combined to create
        the final RD CDM JSON file.
        """
        result = create_final_rd_cdm_json(self.version)
        
        
        self.assertTrue(os.path.exists(self.output_file), "Output file not created")
        
        self.assertIsNotNone(result, "Final RD CDM creation failed.")
        
        with open(self.output_file, 'r') as f:
            data = json.load(f)
        
        self.assertIn("metadata", data)
        self.assertIn("codeSystems", data)
        self.assertIn("dataElements", data)
        self.assertIn("valueSets", data)

if __name__ == "__main__":
    unittest.main()
