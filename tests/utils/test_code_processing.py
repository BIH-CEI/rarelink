
# tests/utils/test_code_processing.py
import unittest
from rarelink.utils.code_processing import (
    process_code,
    normalize_hgnc_id,
    add_prefix_to_code,
    remove_prefix_from_code,
    convert_to_boolean
)

class TestCodeProcessing(unittest.TestCase):
    """Tests for code processing utilities."""
    
    def test_process_code(self):
        """Test process_code function with various inputs."""
        # Test case: already has colon format
        self.assertEqual(process_code("HP:0001250"), "HP:0001250")
        
        # Test case: uppercase the prefix
        self.assertEqual(process_code("hp:0001250"), "HP:0001250")
        
        # Test case: convert underscore to colon
        self.assertEqual(process_code("hp_0001250"), "HP:0001250")
        
        # Test case: special handling for SNOMED -> SNOMEDCT
        self.assertEqual(process_code("SNOMED:123456"), "SNOMEDCT:123456")
        self.assertEqual(process_code("snomed_123456"), "SNOMEDCT:123456")
        
        # Test case: special handling for ICD10CM
        self.assertEqual(process_code("icd10cm_g12_21"), "ICD10CM:G12.21")
        
        # Test case: special handling for LOINC
        self.assertEqual(process_code("loinc_12345_6"), "LOINC:12345-6")
        self.assertEqual(process_code("loinc_la12345_6"), "LOINC:LA12345-6")
        
        # Test case: empty input
        self.assertEqual(process_code(""), "")
        self.assertIsNone(process_code(None))
    
    def test_normalize_hgnc_id(self):
        """Test normalize_hgnc_id function."""
        # Test case: already in standard format
        self.assertEqual(normalize_hgnc_id("HGNC:1234"), "HGNC:1234")
        
        # Test case: numeric only
        self.assertEqual(normalize_hgnc_id("1234"), "HGNC:1234")
        
        # Test case: extract from URL format
        self.assertEqual(normalize_hgnc_id("some text with HGNC:1234 embedded"), "HGNC:1234")
        
        # Test case: empty input
        self.assertEqual(normalize_hgnc_id(""), "")
        self.assertIsNone(normalize_hgnc_id(None))
    
    def test_add_prefix_to_code(self):
        """Test add_prefix_to_code function."""
        # Test case: add prefix
        self.assertEqual(add_prefix_to_code("G12.21", "ICD10CM"), "ICD10CM:G12.21")
        
        # Test case: already has prefix
        self.assertEqual(add_prefix_to_code("ICD10CM:G12.21", "ICD10CM"), "ICD10CM:G12.21")
        
        # Test case: empty input
        self.assertEqual(add_prefix_to_code("", "ICD10CM"), "")
        self.assertIsNone(add_prefix_to_code(None, "ICD10CM"))
    
    def test_remove_prefix_from_code(self):
        """Test remove_prefix_from_code function."""
        # Test case: remove prefix
        self.assertEqual(remove_prefix_from_code("ICD10CM:G12.21", "ICD10CM"), "G12.21")
        
        # Test case: doesn't have the prefix
        self.assertEqual(remove_prefix_from_code("G12.21", "ICD10CM"), "G12.21")
        
        # Test case: empty input
        self.assertEqual(remove_prefix_from_code("", "ICD10CM"), "")
        self.assertIsNone(remove_prefix_from_code(None, "ICD10CM"))
    
    def test_convert_to_boolean(self):
        """Test convert_to_boolean function."""
        # Create a test mapping
        test_mapping = {
            "true": True,
            "yes": True,
            "1": True,
            "false": False,
            "no": False,
            "0": False
        }
        
        # Test cases
        self.assertTrue(convert_to_boolean("true", test_mapping))
        self.assertTrue(convert_to_boolean("yes", test_mapping))
        self.assertTrue(convert_to_boolean("1", test_mapping))
        self.assertFalse(convert_to_boolean("false", test_mapping))
        self.assertFalse(convert_to_boolean("no", test_mapping))
        self.assertFalse(convert_to_boolean("0", test_mapping))
        
        # Test case: value not in mapping
        self.assertIsNone(convert_to_boolean("maybe", test_mapping))