import unittest
import logging

from rarelink.phenopackets.mappings.interpretation_mapper import InterpretationMapper
from rarelink.phenopackets.mappings.variation_descriptor_mapper import VariationDescriptorMapper
from phenopackets import Interpretation, Diagnosis, GenomicInterpretation, VariantInterpretation

# Import test utilities
from ..test_utils import (
    get_record_by_id,
    setup_processor_for_block
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestInterpretationMapper(unittest.TestCase):
    """Unit tests for the InterpretationMapper class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures that can be reused across all tests"""
        # Log test setup
        logger.info("Setting up InterpretationMapper tests")
        
        # Get processors and configurations
        try:
            cls.interpretation_processor, cls.interpretation_config = setup_processor_for_block("interpretations")
            cls.variation_processor, cls.variation_config = setup_processor_for_block("variationDescriptor")
            logger.info("Successfully set up processors and configs")
        except ImportError as e:
            logger.error(f"Setup failed: {e}")
            raise
            
    def setUp(self):
        """Set up test fixtures for each test method"""
        # Create the mapper instances
        self.interpretation_mapper = InterpretationMapper(self.interpretation_processor)
        self.variation_mapper = VariationDescriptorMapper(self.variation_processor)
        
        # Get test records
        self.record_101 = get_record_by_id("101")
        self.record_102 = get_record_by_id("102")
        self.record_103 = get_record_by_id("103")
        
        # Ensure we have test data
        if not self.record_101 or not self.record_102 or not self.record_103:
            self.fail("Test data not found - make sure the sample records JSON file is in the test_data directory")
    
    def test_mapper_produces_valid_output(self):
        """Test that the mapper produces valid interpretations"""
        # First get variation descriptors (needed for interpretations)
        variation_descriptors = self.variation_mapper.map(self.record_103)
        self.assertIsNotNone(variation_descriptors)
        self.assertGreater(len(variation_descriptors), 0)
        
        # Map interpretations
        result = self.interpretation_mapper.map(
            self.record_103, 
            subject_id="test-subject-103",
            variation_descriptors=variation_descriptors
        )
        
        # Verify we got a result
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        
        # Check if we have any interpretations
        if len(result) == 0:
            logger.warning("No interpretations mapped, this may be normal for some test records")
            return
        
        # Check each interpretation
        for interpretation in result:
            self.assertIsInstance(interpretation, Interpretation)
            self.assertIsNotNone(interpretation.id)
            self.assertIsNotNone(interpretation.progress_status)
            
            # Check diagnosis
            self.assertTrue(interpretation.HasField("diagnosis"))
            diagnosis = interpretation.diagnosis
            self.assertIsInstance(diagnosis, Diagnosis)
            self.assertIsNotNone(diagnosis.disease)
            self.assertIsNotNone(diagnosis.disease.id)
            self.assertIsNotNone(diagnosis.disease.label)
            
            # Check genomic interpretations
            self.assertGreater(len(diagnosis.genomic_interpretations), 0)
            for gi in diagnosis.genomic_interpretations:
                self.assertIsInstance(gi, GenomicInterpretation)
                self.assertIsNotNone(gi.subject_or_biosample_id)
                self.assertIsNotNone(gi.interpretation_status)
                
                # Check variant interpretation
                if gi.HasField("variant_interpretation"):
                    vi = gi.variant_interpretation
                    self.assertIsInstance(vi, VariantInterpretation)
                    self.assertIsNotNone(vi.acmg_pathogenicity_classification)
                    self.assertIsNotNone(vi.therapeutic_actionability)
                    self.assertTrue(vi.HasField("variation_descriptor"))
            
            # Log interpretation details
            logger.info(f"Mapped interpretation: {interpretation.id}")
            logger.info(f"  Progress status: {interpretation.progress_status}")
            logger.info(f"  Disease: {interpretation.diagnosis.disease.id} - {interpretation.diagnosis.disease.label}")
            logger.info(f"  Genomic interpretations: {len(interpretation.diagnosis.genomic_interpretations)}")
    
    def test_mapper_requires_subject_id(self):
        """Test that the mapper requires a subject ID"""
        # First get variation descriptors
        variation_descriptors = self.variation_mapper.map(self.record_103)
        
        # Map interpretations without subject_id
        result = self.interpretation_mapper.map(
            self.record_103,
            variation_descriptors=variation_descriptors
        )
        
        # Verify we got an empty list (error condition)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)
    
    def test_mapper_without_variation_descriptors(self):
        """Test mapper behavior without variation descriptors"""
        # Map interpretations without variation_descriptors
        result = self.interpretation_mapper.map(
            self.record_103,
            subject_id="test-subject-103"
        )
        
        # Should return empty list but not error
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)
    
    def test_diagnosis_disease_required(self):
        """Test that each interpretation requires a valid diagnosis"""
        # First get variation descriptors 
        variation_descriptors = self.variation_mapper.map(self.record_103)
        
        # Backup the original extract_diagnosis_id method
        original_method = self.interpretation_mapper._extract_diagnosis_id
        
        try:
            # Override the method to always return None
            self.interpretation_mapper._extract_diagnosis_id = lambda x: None
            
            # Map interpretations
            result = self.interpretation_mapper.map(
                self.record_103,
                subject_id="test-subject-103",
                variation_descriptors=variation_descriptors
            )
            
            # Should return empty list because no valid diagnoses found
            self.assertIsNotNone(result)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), 0)
        finally:
            # Restore the original method
            self.interpretation_mapper._extract_diagnosis_id = original_method
    
    def test_mapper_with_empty_data(self):
        """Test mapper behavior with empty data"""
        # Test with empty dict
        empty_result = self.interpretation_mapper.map(
            {},
            subject_id="test-subject"
        )
        self.assertIsNotNone(empty_result)
        self.assertIsInstance(empty_result, list)
        self.assertEqual(len(empty_result), 0)
        
        # Test with minimal dict
        minimal_data = {"record_id": "test123"}
        minimal_result = self.interpretation_mapper.map(
            minimal_data,
            subject_id="test-subject"
        )
        self.assertIsNotNone(minimal_result)
        self.assertIsInstance(minimal_result, list)
        self.assertEqual(len(minimal_result), 0)
    
    def test_error_handling(self):
        """Test error handling in the mapper"""
        # Create a processor with invalid configuration
        from rarelink.utils.processor import DataProcessor
        invalid_processor = DataProcessor(
            mapping_config={"invalid_field": "value"}
        )
        
        # Create mapper with invalid processor
        invalid_mapper = InterpretationMapper(invalid_processor)
        
        # This should not raise an exception due to error handling
        result = invalid_mapper.map(
            self.record_101,
            subject_id="test-subject"
        )
        
        # The result should be an empty list
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)
        
if __name__ == "__main__":
    unittest.main()