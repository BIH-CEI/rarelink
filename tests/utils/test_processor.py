# tests/utils/test_processor.py
import unittest
from unittest.mock import patch, MagicMock
from rarelink.utils.processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    """Tests for the DataProcessor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mapping_config = {
            "id_field": "record_id",
            "date_of_birth_field": "personal_information.snomedct_184099003",
            "sex_field": "personal_information.snomedct_281053000",
            "redcap_repeat_instrument": "rarelink_5_disease"
        }
        self.processor = DataProcessor(self.mapping_config)
        self.test_data = {
            "record_id": "101",
            "personal_information": {
                "snomedct_184099003": "2020-01-05",
                "snomedct_281053000": "snomedct_248153007"
            }
        }
    
    def test_initialization(self):
        """Test processor initialization."""
        self.assertEqual(self.processor.mapping_config, self.mapping_config)
        self.assertFalse(self.processor.debug_mode)
        self.processor.enable_debug(True)
        self.assertTrue(self.processor.debug_mode)
    
    def test_get_field(self):
        """Test get_field method."""
        result = self.processor.get_field(self.test_data, "id_field")
        self.assertEqual(result, "101")
        result = self.processor.get_field(self.test_data, "date_of_birth_field")
        self.assertEqual(result, "2020-01-05")
        result = self.processor.get_field(self.test_data, "missing_field", "default")
        self.assertEqual(result, "default")
    
    @patch('rarelink.utils.processor.processor.process_code')
    def test_process_code(self, mock_process_code):
        """Test process_code method."""
        mock_process_code.return_value = "MONDO:0123456"
        result = self.processor.process_code("mondo_0123456")
        self.assertEqual(result, "MONDO:0123456")
        mock_process_code.assert_called_once_with("mondo_0123456")
    
    @patch('rarelink.utils.processor.processor.convert_date_to_iso_age')
    def test_convert_date_to_iso_age(self, mock_convert):
        """Test convert_date_to_iso_age method."""
        mock_convert.return_value = "P3Y2M"
        result = self.processor.convert_date_to_iso_age("2023-03-07", "2020-01-05")
        self.assertEqual(result, "P3Y2M")
        mock_convert.assert_called_once_with("2023-03-07", "2020-01-05")
    
    @patch('rarelink.utils.processor.processor.date_to_timestamp')
    def test_date_to_timestamp(self, mock_date_to_timestamp):
        """Test date_to_timestamp method."""
        mock_timestamp = MagicMock()
        mock_date_to_timestamp.return_value = mock_timestamp
        result = self.processor.date_to_timestamp("2020-01-05")
        self.assertEqual(result, mock_timestamp)
        mock_date_to_timestamp.assert_called_once_with("2020-01-05")
    
    @patch('rarelink.utils.processor.processor.fetch_label')
    def test_fetch_label(self, mock_fetch_label):
        """Test fetch_label method."""
        mock_fetch_label.return_value = "Test Disease"
        # Create an enum class for testing
        class TestEnum:
            pass
        # Add enum class to processor for lookup
        self.processor.add_enum_class("MONDO", TestEnum)
        result = self.processor.fetch_label("MONDO:0123456", TestEnum)
        self.assertEqual(result, "Test Disease")
        mock_fetch_label.assert_called_once_with("MONDO:0123456", TestEnum)
    
    def test_add_enum_class(self):
        """Test add_enum_class method."""
        class TestEnum1:
            pass
        self.processor.add_enum_class("TEST1", TestEnum1)
        self.assertIn("TEST1", self.processor.enum_classes)
        self.assertEqual(self.processor.enum_classes["TEST1"], TestEnum1)
        with patch('importlib.import_module') as mock_import:
            mock_module = MagicMock()
            mock_enum_class = MagicMock()
            mock_module.TestEnum2 = mock_enum_class
            mock_import.return_value = mock_module
            self.processor.add_enum_class("TEST2", "test_module.TestEnum2")
            mock_import.assert_called_once_with("test_module")
            self.assertIn("TEST2", self.processor.enum_classes)
    
    @patch('rarelink.utils.processor.processor.normalize_hgnc_id')
    def test_normalize_hgnc_id(self, mock_normalize):
        """Test normalize_hgnc_id method."""
        mock_normalize.return_value = "HGNC:1234"
        result = self.processor.normalize_hgnc_id("1234")
        self.assertEqual(result, "HGNC:1234")
        mock_normalize.assert_called_once_with("1234")
    
    def test_generate_unique_id(self):
        """Test generate_unique_id method."""
        id1 = self.processor.generate_unique_id()
        id2 = self.processor.generate_unique_id()
        self.assertIsInstance(id1, str)
        self.assertIsInstance(id2, str)
        self.assertNotEqual(id1, id2)
        self.assertEqual(len(id1), 30)
        id3 = self.processor.generate_unique_id(length=10)
        self.assertEqual(len(id3), 10)

if __name__ == "__main__":
    unittest.main()
