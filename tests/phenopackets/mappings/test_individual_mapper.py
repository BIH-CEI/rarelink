import unittest
import logging

from rarelink.phenopackets.mappings.individual_mapper import IndividualMapper
from phenopackets import Individual, VitalStatus
from phenopackets.schema.v2 import VitalStatus as VitalStatusEnum


from tests.phenopackets.test_utils import (
    get_record_by_id,
    setup_processor_for_block
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestIndividualMapper(unittest.TestCase):
    """Unit tests for the IndividualMapper class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures that can be reused across all tests"""
        # Log test setup
        logger.info("Setting up IndividualMapper tests")
        
        # Get processor and configuration for individual
        try:
            cls.processor, cls.config = setup_processor_for_block("individual")
            logger.info("Successfully set up processor and config for individual")
        except ImportError as e:
            logger.error(f"Setup failed: {e}")
            raise
            
    def setUp(self):
        """Set up test fixtures for each test method"""
        # Create the mapper instance
        self.mapper = IndividualMapper(self.processor)
        
        # Get test records
        self.record_101 = get_record_by_id("101")
        self.record_102 = get_record_by_id("102")
        self.record_103 = get_record_by_id("103")
        
        # Ensure we have test data
        if not self.record_101 or not self.record_102:
            self.fail("Test data not found - make sure the sample records JSON file is in the test_data directory")
    
    def test_mapper_produces_valid_output(self):
        """Test that the mapper produces a valid Individual from record 101"""
        # Map individual
        result = self.mapper.map(self.record_101)
        
        # Verify we got a result
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Individual)
        
        # Check required fields
        self.assertIsNotNone(result.id)
        self.assertEqual(result.taxonomy.id, "NCBITaxon:9606")
        self.assertEqual(result.taxonomy.label, "Homo sapiens")
        
        # Log the result
        logger.info(f"Mapped individual: {result.id}")
    
    def test_mapper_handles_vital_status(self):
        """Test that the mapper correctly handles a provided VitalStatus"""
        # Create a mock vital status
        vital_status = VitalStatus()
        vital_status.status = VitalStatusEnum.Status.ALIVE
        
        # Map individual with vital status
        result = self.mapper.map(self.record_101, vital_status=vital_status)
        
        # Verify vital status was set correctly
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.vital_status)
        self.assertEqual(result.vital_status.status, VitalStatusEnum.Status.ALIVE)
    
    def test_mapper_extracts_gender(self):
        """Test that the mapper correctly extracts gender information"""
        # Map individual
        result = self.mapper.map(self.record_101)
        
        # Verify gender extraction
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.gender)
        
        # Log gender details
        logger.info(f"Gender: {result.gender.id} - {result.gender.label}")
    
    def test_mapper_with_empty_data(self):
        """Test mapper behavior with empty data"""
        # Test with empty dict
        empty_result = self.mapper.map({})
        self.assertIsNone(empty_result)
        
        # Test with minimal dict
        minimal_data = {"record_id": "test123"}
        minimal_result = self.mapper.map(minimal_data)
        self.assertIsNone(minimal_result)
    
    def test_error_handling(self):
        """Test error handling in the mapper"""
        # Create a processor with invalid configuration
        from rarelink.utils.processor import DataProcessor
        invalid_processor = DataProcessor(
            mapping_config={"invalid_field": "value"}
        )
        
        # Create mapper with invalid processor
        invalid_mapper = IndividualMapper(invalid_processor)
        
        # This should not raise an exception due to error handling
        result = invalid_mapper.map(self.record_101)
        
        # The result should be None due to error handling
        self.assertIsNone(result)
        
if __name__ == "__main__":
    unittest.main()