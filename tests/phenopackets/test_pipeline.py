import tempfile
import unittest
from unittest.mock import patch, Mock

# Import the pipeline function and Phenopacket type.
from rarelink.phenopackets.pipeline import phenopacket_pipeline
from phenopackets import Phenopacket

class TestPhenopacketPipeline(unittest.TestCase):
    # Dummy mapping configuration that provides the required "individual" key.
    dummy_mapping = {"individual": {"dummy": "config"}}
    
    def setUp(self):
        # A simple dummy record as a dictionary.
        self.record = {
            "record_id": "101",
            "personal_information": {"snomedct_184099003": "2020-01-01"}
        }
    
    # Patch the functions that the pipeline uses.
    # Note: The pipeline imports create_phenopacket from 'rarelink.phenopackets' into its module;
    # therefore we patch 'rarelink.phenopackets.pipeline.create_phenopacket'
    # For writing, we assume that write_phenopackets is imported by the pipeline from 
    # 'rarelink.phenopackets' (i.e. it is re-exported in __init__.py), so we patch
    # 'rarelink.phenopackets.write_phenopackets'.
    @patch('rarelink.phenopackets.write_phenopackets')
    @patch('rarelink.phenopackets.pipeline.create_phenopacket')
    def test_basic_workflow(self, mock_create, mock_write):
        """Test that a single record is processed successfully."""
        # Set the patched create_phenopacket to return a dummy Phenopacket.
        dummy_pheno = Mock(spec=Phenopacket)
        dummy_pheno.id = "101"
        mock_create.return_value = dummy_pheno
        
        with tempfile.TemporaryDirectory() as tmpdir:
            result = phenopacket_pipeline(
                input_data=[self.record],
                output_dir=tmpdir,
                created_by="Tester",
                mapping_configs=self.dummy_mapping,
                timeout=10,
                debug=True
            )
            # The pipeline should return a list with one Phenopacket.
            self.assertEqual(len(result), 1)
            mock_create.assert_called_once()
            mock_write.assert_called_once()
    
    @patch('rarelink.phenopackets.write_phenopackets')
    @patch('rarelink.phenopackets.pipeline.create_phenopacket')
    def test_multiple_records(self, mock_create, mock_write):
        """Test that multiple records are processed correctly."""
        records = [
            self.record,
            {"record_id": "102", "personal_information": {"snomedct_184099003": "2020-02-27"}},
            {"record_id": "103", "personal_information": {"snomedct_184099003": "2020-01-01"}}
        ]
        # Create a dummy phenopacket for each record.
        dummy1 = Mock(spec=Phenopacket); dummy1.id = "101"
        dummy2 = Mock(spec=Phenopacket); dummy2.id = "102"
        dummy3 = Mock(spec=Phenopacket); dummy3.id = "103"
        mock_create.side_effect = [dummy1, dummy2, dummy3]
    
        with tempfile.TemporaryDirectory() as tmpdir:
            result = phenopacket_pipeline(
                input_data=records,
                output_dir=tmpdir,
                created_by="Tester",
                mapping_configs=self.dummy_mapping,
                timeout=10,
                debug=True
            )
            # Expect three Phenopackets.
            self.assertEqual(len(result), 3)
            self.assertEqual(mock_create.call_count, 3)
            mock_write.assert_called_once()
    
    @patch('rarelink.phenopackets.write_phenopackets')
    @patch('rarelink.phenopackets.pipeline.create_phenopacket')
    def test_error_handling(self, mock_create, mock_write):
        """
        Test that if one record processing fails, the pipeline still returns 
        the Phenopackets from the successful records.
        """
        dummy_pheno = Mock(spec=Phenopacket)
        dummy_pheno.id = "101"
        # First call succeeds; second call raises an error.
        mock_create.side_effect = [dummy_pheno, ValueError("Test error")]
        records = [self.record, {"record_id": "error_record"}]
    
        with tempfile.TemporaryDirectory() as tmpdir:
            result = phenopacket_pipeline(
                input_data=records,
                output_dir=tmpdir,
                created_by="Tester",
                mapping_configs=self.dummy_mapping,
                timeout=10,
                debug=True
            )
            # Only the first record should be processed successfully.
            self.assertEqual(len(result), 1)
            mock_write.assert_called_once()
    
    @patch('signal.alarm')
    @patch('signal.signal')
    @patch('rarelink.phenopackets.write_phenopackets')
    @patch('rarelink.phenopackets.pipeline.create_phenopacket')
    def test_timeout(self, mock_create, mock_write, mock_signal, mock_alarm):
        """Test that the timeout mechanism is set and then disabled correctly."""
        dummy_pheno = Mock(spec=Phenopacket)
        dummy_pheno.id = "101"
        mock_create.return_value = dummy_pheno
    
        with tempfile.TemporaryDirectory() as tmpdir:
            phenopacket_pipeline(
                input_data=[self.record],
                output_dir=tmpdir,
                created_by="Tester",
                mapping_configs=self.dummy_mapping,
                timeout=300,  # 5 minutes timeout.
                debug=True
            )
            # Verify that the signal handler was set.
            mock_signal.assert_called_once()
            # And that alarm was set (with 300 seconds) and later reset (with 0).
            self.assertEqual(mock_alarm.call_count, 2)
            mock_alarm.assert_any_call(300)
            mock_alarm.assert_any_call(0)
    
if __name__ == "__main__":
    unittest.main()
