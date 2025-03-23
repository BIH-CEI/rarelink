import unittest
import logging

from rarelink.phenopackets.mappings.measurement_mapper import MeasurementMapper
from phenopackets import Measurement

# Import test utilities
from tests.phenopackets.test_utils import (
    get_record_by_id,
    setup_processor_for_block
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestMeasurementMapper(unittest.TestCase):
    """Unit tests for the MeasurementMapper class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures that can be reused across all tests"""
        cls.dob = "2020-01-05"  # Sample DOB from the test data
        
        # Log test setup
        logger.info("Setting up MeasurementMapper tests")
        
        # Get processor and configuration for measurements
        try:
            cls.processor, cls.config = setup_processor_for_block("measurements")
            logger.info("Successfully set up processor and config for measurements")
        except ImportError as e:
            logger.error(f"Setup failed: {e}")
            raise
            
    def setUp(self):
        """Set up test fixtures for each test method"""
        # Create the mapper instance
        self.mapper = MeasurementMapper(self.processor)
        
        # Get test records
        self.record_101 = get_record_by_id("101")
        self.record_102 = get_record_by_id("102")
        self.record_103 = get_record_by_id("103")
        
        # Ensure we have test data
        if not self.record_101 or not self.record_102 or not self.record_103:
            self.fail("Test data not found - make sure the sample records JSON file is in the test_data directory")
    
    def test_mapper_produces_valid_output(self):
        """Test that the mapper produces valid measurements"""
        # Map measurements
        result = self.mapper.map(self.record_101, dob=self.dob)
        
        # Verify we got a result
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        
        # Check if we have any measurements
        self.assertGreater(len(result), 0, "Should have mapped at least one measurement")
        
        # Check the first measurement
        measurement = result[0]
        self.assertIsInstance(measurement, Measurement)
        self.assertIsNotNone(measurement.assay)
        self.assertIsNotNone(measurement.assay.id)
        self.assertIsNotNone(measurement.assay.label)
        
        # Log the measurement details
        logger.info(f"Mapped measurement: {measurement.assay.id} - {measurement.assay.label}")
        
        # Check additional properties
        if measurement.HasField("value"):
            if measurement.value.HasField("quantity"):
                logger.info(f"Value: {measurement.value.quantity.value}")
                if measurement.value.quantity.HasField("unit"):
                    logger.info(f"Unit: {measurement.value.quantity.unit.id} - {measurement.value.quantity.unit.label}")
            elif measurement.value.HasField("ontology_class"):
                logger.info(f"Value: {measurement.value.ontology_class.id} - {measurement.value.ontology_class.label}")
        
        if measurement.HasField("time_observed"):
            logger.info(f"Time observed: {measurement.time_observed}")
            
        if measurement.HasField("procedure"):
            logger.info(f"Procedure: {measurement.procedure.code.id} - {measurement.procedure.code.label}")
    
    def test_mapper_maps_multiple_measurements(self):
        """Test that the mapper correctly maps measurements from records"""
        # Check all three records for measurements
        results_101 = self.mapper.map(self.record_101, dob=self.record_101["personal_information"]["snomedct_184099003"])
        results_102 = self.mapper.map(self.record_102, dob=self.record_102["personal_information"]["snomedct_184099003"]) 
        results_103 = self.mapper.map(self.record_103, dob=self.record_103["personal_information"]["snomedct_184099003"])
        
        # Log results from all records
        logger.info(f"Mapped {len(results_101)} measurements from record 101")
        logger.info(f"Mapped {len(results_102)} measurements from record 102")
        logger.info(f"Mapped {len(results_103)} measurements from record 103")
        
        # Verify we got at least one measurement from each record
        self.assertGreaterEqual(len(results_101), 1, "Should have mapped at least one measurement from record 101")
        self.assertGreaterEqual(len(results_102), 1, "Should have mapped at least one measurement from record 102") 
        self.assertGreaterEqual(len(results_103), 1, "Should have mapped at least one measurement from record 103")
        
        # Verify that in total, we have multiple measurements across records
        total_measurements = len(results_101) + len(results_102) + len(results_103)
        self.assertGreater(total_measurements, 2, "Should have mapped multiple measurements across all records")
        
        # Log the measurement assays from record 102 (which should have multiple)
        for i, measurement in enumerate(results_102):
            logger.info(f"Measurement {i+1} from record 102: {measurement.assay.id} - {measurement.assay.label}")
    
    def test_measurement_value_and_unit_mapping(self):
        """Test that measurement values and units are correctly mapped"""
        # Record 101's first measurement has value 5.01 with UO_0000276 unit
        result = self.mapper.map(self.record_101, dob=self.dob)
        
        # Find the first measurement
        if len(result) > 0:
            measurement = result[0]
            
            # Check value
            self.assertTrue(measurement.HasField("value"), "Measurement should have a value")
            self.assertTrue(measurement.value.HasField("quantity"), "Value should be a quantity")
            
            # Verify the value is close to 5.01
            self.assertAlmostEqual(measurement.value.quantity.value, 5.01, places=2, 
                                  msg="Value should be approximately 5.01")
            
            # Verify unit is mapped
            self.assertTrue(measurement.value.quantity.HasField("unit"), "Quantity should have a unit")
            self.assertEqual(measurement.value.quantity.unit.id, "UO:0000276", 
                            "Unit ID should be UO:0000276")
            
            logger.info(f"Verified measurement value: {measurement.value.quantity.value} {measurement.value.quantity.unit.id}")
    
    def test_time_observed_mapping(self):
        """Test that measurement time_observed is correctly mapped"""
        # Record 102's measurement has time_observed field with date 2022-10-14
        result = self.mapper.map(self.record_102, dob=self.record_102["personal_information"]["snomedct_184099003"])
        
        if len(result) > 0:
            # At least one of the measurements should have time_observed
            found_time = False
            for measurement in result:
                if measurement.HasField("time_observed"):
                    found_time = True
                    logger.info(f"Found time_observed: {measurement.time_observed}")
                    break
                    
            self.assertTrue(found_time, "At least one measurement should have time_observed")
    
    def test_procedure_mapping(self):
        """Test that procedure information is correctly mapped"""
        # Some measurements have procedure information in ncit_c41255 field
        result = self.mapper.map(self.record_101, dob=self.dob)
        
        if len(result) > 0:
            # At least one of the measurements should have procedure
            found_procedure = False
            for measurement in result:
                if measurement.HasField("procedure"):
                    found_procedure = True
                    logger.info(f"Found procedure: {measurement.procedure.code.id} - {measurement.procedure.code.label}")
                    break
                    
            self.assertTrue(found_procedure, "At least one measurement should have procedure information")
    
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
    
    def test_different_measurement_categories(self):
        """Test handling of different measurement categories"""
        # Record 102 has both vital-signs and laboratory measurements
        result = self.mapper.map(self.record_102, dob=self.record_102["personal_information"]["snomedct_184099003"])
        
        # Check if we have different categories of measurements
        categories = set()
        for measurement in result:
            # Categorize based on assay field patterns
            categories.add(measurement.assay.id.split(":")[0] if ":" in measurement.assay.id else "OTHER")
            
        logger.info(f"Found measurement categories: {categories}")
        self.assertGreater(len(categories), 0, "Should find at least one measurement category")
    
    def test_error_handling(self):
        """Test error handling in the mapper"""
        # Create a processor with invalid configuration
        from rarelink.utils.processor import DataProcessor
        invalid_processor = DataProcessor(
            mapping_config={"invalid_field": "value"}
        )
        
        # Create mapper with invalid processor
        invalid_mapper = MeasurementMapper(invalid_processor)
        
        # This should not raise an exception due to error handling
        result = invalid_mapper.map(self.record_101, dob=self.dob)
        
        # The result should be an empty list
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)
        
if __name__ == "__main__":
    unittest.main()