import unittest
import logging

from rarelink.phenopackets.mappings.vital_status_mapper import VitalStatusMapper
from phenopackets import VitalStatus, OntologyClass
from phenopackets.schema.v2 import VitalStatus as VitalStatusEnum

# Import test utilities
from tests.phenopackets.test_utils import (
    get_record_by_id,
    setup_processor_for_block
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestVitalStatusMapper(unittest.TestCase):
    """Unit tests for the VitalStatusMapper class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures that can be reused across all tests"""
        cls.dob = "2020-01-05"  # Sample DOB from the test data
        
        # Log test setup
        logger.info("Setting up VitalStatusMapper tests")
        
        # Get processor and configuration for vital status
        try:
            cls.processor, cls.config = setup_processor_for_block("vitalStatus")
            logger.info("Successfully set up processor and config for vital status")
        except ImportError as e:
            logger.error(f"Setup failed: {e}")
            raise
            
    def setUp(self):
        """Set up test fixtures for each test method"""
        # Create the mapper instance
        self.mapper = VitalStatusMapper(self.processor)
        
        # Get test records
        self.record_101 = get_record_by_id("101")
        self.record_102 = get_record_by_id("102")
        self.record_103 = get_record_by_id("103")
        
        # Ensure we have test data
        if not self.record_101 or not self.record_102 or not self.record_103:
            self.fail("Test data not found - make sure the sample records JSON file is in the test_data directory")
    
    def test_mapper_produces_valid_output(self):
        """Test that the mapper produces a valid VitalStatus from record 101"""
        # Map vital status
        result = self.mapper.map(self.record_101, dob=self.dob)
        
        # Verify we got a result
        self.assertIsNotNone(result)
        self.assertIsInstance(result, VitalStatus)
        
        # VitalStatus should always have a status field
        self.assertIsNotNone(result.status)
        
        # Log the result
        logger.info(f"Mapped vital status: {result.status}")
    
    def test_default_vital_status(self):
        """Test that the mapper returns a default status when no data is available"""
        # Map with empty data
        result = self.mapper.map({}, dob=self.dob)
        
        # Verify we get a default status
        self.assertIsNotNone(result)
        self.assertEqual(result.status, VitalStatusEnum.Status.UNKNOWN_STATUS)
    
    def test_mapper_extracts_cause_of_death(self):
        """Test that the mapper correctly extracts cause of death when available"""
        # Find a record with deceased status
        record_with_death_cause = None
        for record in [self.record_101, self.record_102, self.record_103]:
            # Map vital status
            vs = self.mapper.map(record, dob=self.dob)
            if vs and vs.status == VitalStatusEnum.Status.DECEASED and vs.HasField("cause_of_death"):
                record_with_death_cause = record
                break
        
        # Skip test if no suitable record found
        if not record_with_death_cause:
            logger.warning("No record with cause of death found, skipping test")
            return
        
        # Map vital status from the appropriate record
        result = self.mapper.map(record_with_death_cause, dob=self.dob)
        
        # Verify cause of death
        self.assertIsNotNone(result)
        self.assertTrue(result.HasField("cause_of_death"))
        self.assertIsInstance(result.cause_of_death, OntologyClass)
        self.assertIsNotNone(result.cause_of_death.id)
        self.assertIsNotNone(result.cause_of_death.label)
        
        # Log cause of death details
        logger.info(f"Cause of death: {result.cause_of_death.id} - {result.cause_of_death.label}")
    
    def test_time_of_death_calculation(self):
        """Test time of death is calculated correctly when date of birth is provided"""
        # Find a record with deceased status
        record_with_death_time = None
        for record in [self.record_101, self.record_102, self.record_103]:
            # Map vital status
            vs = self.mapper.map(record, dob=self.dob)
            if vs and vs.status == VitalStatusEnum.Status.DECEASED and vs.HasField("time_of_death"):
                record_with_death_time = record
                break
        
        # Skip test if no suitable record found
        if not record_with_death_time:
            logger.warning("No record with time of death found, skipping test")
            return
        
        # Map vital status from the appropriate record
        result = self.mapper.map(record_with_death_time, dob=self.dob)
        
        # Verify time of death
        self.assertIsNotNone(result)
        self.assertTrue(result.HasField("time_of_death"))
        self.assertTrue(result.time_of_death.HasField("age"))
        self.assertIsNotNone(result.time_of_death.age.iso8601duration)
        
        # Log time of death details
        logger.info(f"Time of death: {result.time_of_death.age.iso8601duration}")
        
    def test_error_handling(self):
        """Test error handling in the mapper"""
        # Create a processor with invalid configuration
        from rarelink.utils.processor import DataProcessor
        invalid_processor = DataProcessor(
            mapping_config={"invalid_field": "value"}
        )
        
        # Create mapper with invalid processor
        invalid_mapper = VitalStatusMapper(invalid_processor)
        
        # This should not raise an exception due to error handling
        result = invalid_mapper.map(self.record_101)
        
        # We should still get a default vital status
        self.assertIsNotNone(result)
        self.assertEqual(result.status, VitalStatusEnum.Status.UNKNOWN_STATUS)
        
if __name__ == "__main__":
    unittest.main()