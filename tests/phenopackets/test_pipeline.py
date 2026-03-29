# tests/phenopackets/test_pipeline.py
import tempfile
import unittest
from unittest.mock import patch, Mock

from rarelink.phenopackets.pipeline import phenopacket_pipeline
from phenopackets import Phenopacket


class TestPhenopacketPipeline(unittest.TestCase):
    dummy_mapping = {"individual": {"dummy": "config"}}

    def setUp(self):
        self.record = {
            "record_id": "101",
            "personal_information": {"snomedct_184099003": "2020-01-01"},
        }

    @patch('rarelink.phenopackets.pipeline.write_phenopackets')
    @patch('rarelink.phenopackets.pipeline.create_phenopacket')
    def test_basic_workflow(self, mock_create, mock_write):
        """Single record is created successfully and write is called."""
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
                debug=True,
            )
            self.assertEqual(result.n_created, 1)
            self.assertEqual(result.n_failed_creation, 0)
            mock_create.assert_called_once()
            mock_write.assert_called_once()

    @patch('rarelink.phenopackets.pipeline.write_phenopackets')
    @patch('rarelink.phenopackets.pipeline.create_phenopacket')
    def test_multiple_records(self, mock_create, mock_write):
        """Multiple records are all created successfully."""
        records = [
            self.record,
            {"record_id": "102", "personal_information": {"snomedct_184099003": "2020-02-27"}},
            {"record_id": "103", "personal_information": {"snomedct_184099003": "2020-01-01"}},
        ]
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
                debug=True,
            )
            self.assertEqual(result.n_created, 3)
            self.assertEqual(result.n_failed_creation, 0)
            self.assertEqual(mock_create.call_count, 3)
            mock_write.assert_called_once()

    @patch('rarelink.phenopackets.pipeline.write_phenopackets')
    @patch('rarelink.phenopackets.pipeline.create_phenopacket')
    def test_error_handling(self, mock_create, mock_write):
        """One record fails creation; the other succeeds."""
        dummy_pheno = Mock(spec=Phenopacket)
        dummy_pheno.id = "101"
        mock_create.side_effect = [dummy_pheno, ValueError("Test error")]
        records = [self.record, {"record_id": "error_record"}]

        with tempfile.TemporaryDirectory() as tmpdir:
            result = phenopacket_pipeline(
                input_data=records,
                output_dir=tmpdir,
                created_by="Tester",
                mapping_configs=self.dummy_mapping,
                timeout=10,
                debug=True,
            )
            self.assertEqual(result.n_created, 1)
            self.assertEqual(result.n_failed_creation, 1)
            self.assertEqual(result.failed_creations[0]["record_id"], "error_record")
            mock_write.assert_called_once()

    @patch('signal.alarm')
    @patch('signal.signal')
    @patch('rarelink.phenopackets.pipeline.write_phenopackets')
    @patch('rarelink.phenopackets.pipeline.create_phenopacket')
    def test_timeout(self, mock_create, mock_write, mock_signal, mock_alarm):
        """Timeout mechanism is set and then disabled correctly."""
        dummy_pheno = Mock(spec=Phenopacket)
        dummy_pheno.id = "101"
        mock_create.return_value = dummy_pheno

        with tempfile.TemporaryDirectory() as tmpdir:
            phenopacket_pipeline(
                input_data=[self.record],
                output_dir=tmpdir,
                created_by="Tester",
                mapping_configs=self.dummy_mapping,
                timeout=300,
                debug=True,
            )
            mock_signal.assert_called_once()
            self.assertEqual(mock_alarm.call_count, 2)
            mock_alarm.assert_any_call(300)
            mock_alarm.assert_any_call(0)


if __name__ == "__main__":
    unittest.main()