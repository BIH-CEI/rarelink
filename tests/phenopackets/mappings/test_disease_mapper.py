# tests/phenopackets/mappings/test_disease_mapper.py
import unittest
import logging

# Import the mapper and dependencies
from rarelink.phenopackets.mappings.disease_mapper import DiseaseMapper
from phenopackets import Disease

# Import test utilities
from ..test_utils import (
    get_record_by_id,
    setup_processor_for_block,
    get_disease_instances_from_record
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestDiseaseMapper(unittest.TestCase):
    """Unit tests for the DiseaseMapper class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures that can be reused across all tests"""
        cls.dob = "2020-01-05"  # Sample DOB from the test data
        
        # Log test setup
        logger.info("Setting up DiseaseMapper tests")
        
        # Get processor and configuration for diseases
        try:
            cls.processor, cls.config = setup_processor_for_block("diseases")
            logger.info("Successfully set up processor and config for diseases")
        except ImportError as e:
            logger.error(f"Setup failed: {e}")
            raise
            
    def setUp(self):
        """Set up test fixtures for each test method"""
        # Create the mapper instance
        self.mapper = DiseaseMapper(self.processor)
        
        # Get test records
        self.record_101 = get_record_by_id("101")
        self.record_102 = get_record_by_id("102")
        
        # Ensure we have test data
        if not self.record_101 or not self.record_102:
            self.fail("Test data not found - make sure the sample records JSON file is in the test_data directory")
    
    def test_mapper_produces_valid_output(self):
        """Test that the mapper produces valid diseases from record 101"""
        # Record 101 has diseases
        result = self.mapper.map(self.record_101, dob=self.dob)
        
        # Verify we got a result
        self.assertIsNotNone(result)
        
        # Handle both cases: single Disease object or a list of Disease objects
        if hasattr(result, 'term'):  # It's a single Disease object
            diseases = [result]
            logger.info("Mapper returned a single Disease object")
        else:  # It's a list (or should be)
            self.assertIsInstance(result, list, f"Expected a list but got {type(result).__name__}")
            diseases = result
        
        # Check that we have diseases
        self.assertGreater(len(diseases), 0, "Should have mapped at least one disease")
        
        # Log the results
        logger.info(f"Found {len(diseases)} diseases from record 101")
        
        # Check each disease
        for disease in diseases:
            self.assertIsInstance(disease, Disease)
            self.assertIsNotNone(disease.term)
            self.assertIsNotNone(disease.term.id)
            self.assertIsNotNone(disease.term.label)
            logger.info(f"Disease: {disease.term.id} - {disease.term.label}")
    
    def test_mapper_handles_different_disease_codings(self):
        """Test that the mapper can handle different disease codings (MONDO, ORPHA, ICD10CM)"""
        diseases = self.mapper.map(self.record_101, dob=self.dob)
        
        # Normalize result to list if needed
        if not isinstance(diseases, list):
            diseases = [diseases]
        
        # Extract IDs to check
        disease_ids = [d.term.id for d in diseases]
        
        # Check for various disease coding systems
        has_mondo = any("MONDO:" in d_id for d_id in disease_ids)
        has_orpha = any("ORPHA:" in d_id for d_id in disease_ids)
        has_icd10 = any("ICD10CM:" in d_id for d_id in disease_ids)
        
        # Verify we found at least one coding system
        self.assertTrue(has_mondo or has_orpha or has_icd10,
                       "Should map at least one disease coding system")
        
        # Log findings
        logger.info(f"Found MONDO diseases: {has_mondo}")
        logger.info(f"Found ORPHA diseases: {has_orpha}")
        logger.info(f"Found ICD10CM diseases: {has_icd10}")
    
    def test_mapper_extracts_onset_correctly(self):
        """Test that the mapper extracts onset dates correctly"""
        diseases = self.mapper.map(self.record_101, dob=self.dob)
        
        # Normalize result to list if needed
        if not isinstance(diseases, list):
            diseases = [diseases]
        
        # At least one disease should have onset
        has_onset = any(d.HasField("onset") for d in diseases)
        self.assertTrue(has_onset, "At least one disease should have onset")
        
        # Find a disease with onset date
        for disease in diseases:
            if disease.HasField("onset") and disease.onset.HasField("age"):
                # Verify it has a valid ISO age format
                iso_age = disease.onset.age.iso8601duration
                self.assertRegex(iso_age, r'^P\d+Y\d+M$', 
                                f"Invalid ISO age format: {iso_age}")
                
                # Log the onset
                logger.info(f"Disease {disease.term.id} has onset: {iso_age}")
    
    def test_mapper_with_empty_data(self):
        """Test mapper behavior with empty data"""
        # Test with empty dict
        empty_result = self.mapper.map({}, dob=self.dob)
        self.assertIsNotNone(empty_result)
        
        # Handle result normalization
        if not isinstance(empty_result, list):
            empty_result = [empty_result] if empty_result else []
            
        self.assertEqual(len(empty_result), 0, "Empty data should produce empty result")
        
        # Test with minimal dict
        minimal_data = {"record_id": "test123"}
        minimal_result = self.mapper.map(minimal_data, dob=self.dob)
        self.assertIsNotNone(minimal_result)
        
        # Handle result normalization
        if not isinstance(minimal_result, list):
            minimal_result = [minimal_result] if minimal_result else []
            
        self.assertEqual(len(minimal_result), 0, "Minimal data should produce empty result")
    
    def test_specific_disease_case(self):
        """Test mapping a specific disease case"""
        # Get all disease instances from record 101
        disease_instances = get_disease_instances_from_record(self.record_101)
        
        # Make sure we found disease instances
        self.assertGreater(len(disease_instances), 0, "No disease instances found in test data")
        
        # Find a disease with an ID
        test_disease = None
        for disease in disease_instances:
            for field in ['snomedct_64572001_mondo', 'snomedct_64572001_ordo', 'snomedct_64572001_icd10cm']:
                if field in disease and disease[field]:
                    test_disease = disease
                    break
            if test_disease:
                break
        
        if not test_disease:
            self.fail("Could not find disease with ID in test data")
        
        # Get the expected ID
        expected_id = None
        for field, prefix in [
            ('snomedct_64572001_mondo', 'MONDO:'),
            ('snomedct_64572001_ordo', 'ORPHA:'),
            ('snomedct_64572001_icd10cm', 'ICD10CM:')
        ]:
            if field in test_disease and test_disease[field]:
                value = test_disease[field]
                if not value.startswith(prefix):
                    value = f"{prefix}{value}"
                expected_id = value
                break
        
        # Create test data with just this disease
        test_data = {
            "record_id": "test_specific",
            "repeated_elements": [{
                "redcap_repeat_instrument": "rarelink_5_disease",
                "redcap_repeat_instance": 1,
                "disease": test_disease
            }]
        }
        
        # Map and validate
        mapped_diseases = self.mapper.map(test_data, dob=self.dob)
        
        # Normalize result to list if needed
        if not isinstance(mapped_diseases, list):
            mapped_diseases = [mapped_diseases]
        
        # Should have exactly one disease
        self.assertEqual(len(mapped_diseases), 1, "Should have mapped exactly one disease")
        
        # Verify it's the expected disease
        mapped_disease = mapped_diseases[0]
        self.assertEqual(mapped_disease.term.id, expected_id)
    
    def test_error_handling(self):
        """Test error handling in the mapper"""
        # Create a processor with invalid configuration
        from rarelink.utils.processor import DataProcessor
        invalid_processor = DataProcessor(
            mapping_config={"invalid_field": "value"}
        )
        
        # Create mapper with invalid processor
        invalid_mapper = DiseaseMapper(invalid_processor)
        
        # This should not raise an exception due to error handling
        result = invalid_mapper.map(self.record_101, dob=self.dob)
        
        # The result should be empty but not None
        self.assertIsNotNone(result)
        
        # Normalize result to list if needed
        if not isinstance(result, list):
            result = [result] if result else []
            
        self.assertEqual(len(result), 0, "Invalid configuration should produce empty result")
        
if __name__ == "__main__":
    unittest.main()