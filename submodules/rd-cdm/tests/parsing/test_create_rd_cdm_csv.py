import unittest
import os
import csv
from src.parsing.create_rd_cdm_csv import create_final_rd_cdm_csv

class TestCreateRdCdmCsv(unittest.TestCase):
    """
    Tests for the function that creates both individual and combined CSV files.

    This class includes methods to test the creation of the RD CDM CSV files,
    ensuring that individual and combined CSVs are created and contain the
    expected data.
    """

    def setUp(self):
        """
        Set up test environment.

        This method defines the version and expected output file paths for
        the individual and combined CSV files. It runs before each test method.
        """
        self.version = "v2_0_0_dev0"
        self.output_dir = f"res/{self.version}/"
        self.code_systems_csv = os.path.join(
            self.output_dir, f"rd_cdm_codesystems_{self.version}.csv")
        self.data_elements_csv = os.path.join(
            self.output_dir, f"rd_cdm_data_elements_{self.version}.csv")
        self.value_sets_csv = os.path.join(
            self.output_dir, f"rd_cdm_value_sets_{self.version}.csv")
        self.combined_csv = os.path.join(
            self.output_dir, f"rd_cdm_{self.version}.csv")

    def test_create_final_rd_cdm_csv(self):
        """
        Test if the individual and combined CSV files are correctly created.

        This method calls the function to create the individual and combined
        CSVs, verifies if each file exists, and ensures that the files are
        created correctly for code systems, data elements, value sets, and
        the combined RD CDM.
        """
        create_final_rd_cdm_csv(self.version)
        
        self.assertTrue(
            os.path.exists(self.code_systems_csv), 
            "Code systems CSV not created.")
        self.assertTrue(
            os.path.exists(self.data_elements_csv), 
            "Data elements CSV not created.")
        self.assertTrue(
            os.path.exists(self.value_sets_csv), 
            "Value sets CSV not created.")
        self.assertTrue(
            os.path.exists(self.combined_csv), 
            "Combined RD CDM CSV not created.")

if __name__ == "__main__":
    unittest.main()
