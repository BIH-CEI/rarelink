import unittest
import logging

from rarelink.phenopackets.mappings.phenotypic_feature_mapper import PhenotypicFeatureMapper
from phenopackets import PhenotypicFeature

# Import test utilities
from tests.phenopackets.test_utils import (
    get_record_by_id,
    setup_processor_for_block
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestPhenotypicFeatureMapper(unittest.TestCase):
    """Unit tests for the PhenotypicFeatureMapper class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures that can be reused across all tests"""
        cls.dob = "2020-01-05"  # Sample DOB from the test data
        
        # Log test setup
        logger.info("Setting up PhenotypicFeatureMapper tests")
        
        # Get processor and configuration for phenotypic features
        try:
            cls.processor, cls.config = setup_processor_for_block("phenotypicFeatures")
            logger.info("Successfully set up processor and config for phenotypic features")
        except ImportError as e:
            logger.error(f"Setup failed: {e}")
            raise
            
    def setUp(self):
        """Set up test fixtures for each test method"""
        # Create the mapper instance
        self.mapper = PhenotypicFeatureMapper(self.processor)
        
        # Get test records
        self.record_101 = get_record_by_id("101")
        self.record_102 = get_record_by_id("102")
        self.record_103 = get_record_by_id("103")
        
        # Ensure we have test data
        if not self.record_101 or not self.record_102 or not self.record_103:
            self.fail("Test data not found - make sure the sample records JSON file is in the test_data directory")
    
    def test_mapper_produces_valid_output(self):
        """Test that the mapper produces valid phenotypic features"""
        # Map phenotypic features
        result = self.mapper.map(self.record_101, dob=self.dob)
        
        # Verify we got a result
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        
        # Check if we have any features
        self.assertGreater(len(result), 0, "Should have mapped at least one phenotypic feature")
        
        # Check the first feature
        feature = result[0]
        self.assertIsInstance(feature, PhenotypicFeature)
        self.assertIsNotNone(feature.type)
        self.assertIsNotNone(feature.type.id)
        self.assertIsNotNone(feature.type.label)
        
        # Log the feature details
        logger.info(f"Mapped feature: {feature.type.id} - {feature.type.label}")
        
        # Check additional properties
        if feature.HasField("onset"):
            logger.info(f"Onset: {feature.onset}")
        
        if feature.HasField("severity"):
            logger.info(f"Severity: {feature.severity.id} - {feature.severity.label}")
            
        if feature.evidence:
            logger.info(f"Evidence: {feature.evidence[0].evidence_code.id} - {feature.evidence[0].evidence_code.label}")
            
        if feature.modifiers:
            logger.info(f"Modifiers: {len(feature.modifiers)}")
            for modifier in feature.modifiers:
                logger.info(f"  {modifier.id} - {modifier.label}")
    
    def test_mapper_handles_multiple_features(self):
        """Test that the mapper correctly handles multiple phenotypic features"""
        # Map phenotypic features
        result = self.mapper.map(self.record_103, dob=self.dob)
        
        # Verify we got multiple features
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 1, "Should have mapped multiple phenotypic features")
        
        # Log the number of features
        logger.info(f"Mapped {len(result)} phenotypic features")
        
        # Check feature types are different
        feature_types = {feature.type.id for feature in result}
        self.assertGreater(len(feature_types), 1, "Features should have different types")
        
        # Log unique feature types
        logger.info(f"Unique feature types: {feature_types}")
    
    def test_mapper_handles_onset_and_resolution(self):
        """Test that the mapper correctly handles onset and resolution dates"""
        # Map phenotypic features
        result = self.mapper.map(self.record_102, dob=self.dob)
        
        # Find features with onset and resolution
        features_with_onset = [f for f in result if f.HasField("onset")]
        features_with_resolution = [f for f in result if f.HasField("resolution")]
        
        # At least some features should have onset
        self.assertGreater(len(features_with_onset), 0, "Some features should have onset")
        
        # Log onset details
        for feature in features_with_onset:
            logger.info(f"Feature {feature.type.label} has onset: {feature.onset}")
        
        # Log resolution details if any
        if features_with_resolution:
            logger.info(f"Found {len(features_with_resolution)} features with resolution")
            for feature in features_with_resolution:
                logger.info(f"Feature {feature.type.label} has resolution: {feature.resolution}")
    
    def test_mapper_handles_evidence_and_severity(self):
        """Test that the mapper correctly handles evidence and severity"""
        # Map phenotypic features
        result = self.mapper.map(self.record_103, dob=self.dob)
        
        # Find features with evidence and severity
        features_with_evidence = [f for f in result if f.evidence]
        features_with_severity = [f for f in result if f.HasField("severity")]
        
        # Log evidence details if any
        if features_with_evidence:
            logger.info(f"Found {len(features_with_evidence)} features with evidence")
            for feature in features_with_evidence:
                logger.info(f"Feature {feature.type.label} has evidence: {feature.evidence[0].evidence_code.label}")
        
        # Log severity details if any
        if features_with_severity:
            logger.info(f"Found {len(features_with_severity)} features with severity")
            for feature in features_with_severity:
                logger.info(f"Feature {feature.type.label} has severity: {feature.severity.label}")
    
    def test_mapper_with_empty_data(self):
        """Test mapper behavior with empty data"""
        # Test with empty dict
        empty_result = self.mapper.map({}, dob=self.dob)
        self.assertIsNotNone(empty_result)
        self.assertIsInstance(empty_result, list)
        self.assertEqual(len(empty_result), 0)
        
        # Test with minimal dict
        minimal_data = {"record_id": "test123"}
        minimal_result = self.mapper.map(minimal_data, dob=self.dob)
        self.assertIsNotNone(minimal_result)
        self.assertIsInstance(minimal_result, list)
        self.assertEqual(len(minimal_result), 0)
    
    def test_error_handling(self):
        """Test error handling in the mapper"""
        # Create a processor with a configuration that will definitely fail
        from rarelink.utils.processor import DataProcessor
        invalid_processor = DataProcessor(
            mapping_config={
                # Force using an instrument that doesn't exist in the test data
                "redcap_repeat_instrument": "non_existent_instrument",
                # Override any default configuration
                "type_field": "non_existent_field"
            }
        )
        
        # Create mapper with invalid processor
        invalid_mapper = PhenotypicFeatureMapper(invalid_processor)
        
        # Create a minimal data structure with no relevant data
        minimal_data = {"record_id": "test_error"}
        
        # This should not raise an exception due to error handling
        result = invalid_mapper.map(minimal_data, dob=self.dob)
        
        # The result should be an empty list
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)
        
if __name__ == "__main__":
    unittest.main()