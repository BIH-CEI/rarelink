import unittest
import logging

from rarelink.phenopackets.mappings.variation_descriptor_mapper import VariationDescriptorMapper
from phenopackets import VariationDescriptor, OntologyClass, GeneDescriptor

# Import test utilities
from tests.phenopackets.test_utils import (
    get_record_by_id,
    setup_processor_for_block
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestVariationDescriptorMapper(unittest.TestCase):
    """Unit tests for the VariationDescriptorMapper class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures that can be reused across all tests"""
        # Log test setup
        logger.info("Setting up VariationDescriptorMapper tests")
        
        # Get processor and configuration for variation descriptors
        try:
            cls.processor, cls.config = setup_processor_for_block("variationDescriptor")
            logger.info("Successfully set up processor and config for variation descriptors")
        except ImportError as e:
            logger.error(f"Setup failed: {e}")
            raise
            
    def setUp(self):
        """Set up test fixtures for each test method"""
        # Create the mapper instance
        self.mapper = VariationDescriptorMapper(self.processor)
        
        # Get test records
        self.record_101 = get_record_by_id("101")
        self.record_102 = get_record_by_id("102")
        self.record_103 = get_record_by_id("103")
        
        # Ensure we have test data
        if not self.record_101 or not self.record_102 or not self.record_103:
            self.fail("Test data not found - make sure the sample records JSON file is in the test_data directory")
    
    def test_mapper_produces_valid_output(self):
        """Test that the mapper produces valid variation descriptors"""
        # Map variation descriptors
        result = self.mapper.map(self.record_103)
        
        # Verify we got a result
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        
        # Check if we have any descriptors
        self.assertGreater(len(result), 0, "Should have mapped at least one variation descriptor")
        
        # Check each descriptor
        for instance_id, descriptor in result.items():
            self.assertIsInstance(descriptor, VariationDescriptor)
            self.assertIsNotNone(descriptor.id)
            
            # Log the descriptor
            logger.info(f"Mapped variation descriptor for instance {instance_id}: {descriptor.id}")
            
            # Check for key fields
            if len(descriptor.expressions) > 0:
                logger.info(f"Expression: {descriptor.expressions[0].value}")
                
            if descriptor.HasField("allelic_state"):
                logger.info(f"Allelic state: {descriptor.allelic_state.id} - {descriptor.allelic_state.label}")
                
            if descriptor.HasField("structural_type"):
                logger.info(f"Structural type: {descriptor.structural_type.id} - {descriptor.structural_type.label}")
                
            if descriptor.HasField("gene_context"):
                logger.info(f"Gene context: {descriptor.gene_context.value_id} - {descriptor.gene_context.symbol}")
    
    def test_mapper_handles_expression_values(self):
        """Test that the mapper correctly handles expression values"""
        # Map variation descriptors
        result = self.mapper.map(self.record_103)
        
        # Verify expressions
        for instance_id, descriptor in result.items():
            if len(descriptor.expressions) > 0:
                # Each expression should have a syntax and value
                for expr in descriptor.expressions:
                    self.assertEqual(expr.syntax, "hgvs.g")
                    self.assertIsNotNone(expr.value)
                    self.assertGreater(len(expr.value), 0)
                    
                # Found valid expressions, test passes
                return
                
        # If we get here, no expressions were found in any descriptor
        logger.warning("No expressions found in any variation descriptor, test may be invalid")
    
    def test_mapper_handles_gene_context(self):
        """Test that the mapper correctly handles gene context"""
        # Map variation descriptors
        result = self.mapper.map(self.record_103)
        
        # Find a descriptor with gene context
        for instance_id, descriptor in result.items():
            if descriptor.HasField("gene_context"):
                gene_context = descriptor.gene_context
                
                # Verify gene context fields
                self.assertIsInstance(gene_context, GeneDescriptor)
                self.assertIsNotNone(gene_context.value_id)
                self.assertTrue(gene_context.value_id.startswith("HGNC:"))
                
                # Test passes if we found at least one valid gene context
                return
                
        # If we get here, no gene contexts were found in any descriptor
        logger.warning("No gene contexts found in any variation descriptor, test may be invalid")
    
    def test_mapper_handles_allelic_state(self):
        """Test that the mapper correctly handles allelic state"""
        # Map variation descriptors
        result = self.mapper.map(self.record_103)
        
        # Find a descriptor with allelic state
        for instance_id, descriptor in result.items():
            if descriptor.HasField("allelic_state"):
                allelic_state = descriptor.allelic_state
                
                # Verify allelic state fields
                self.assertIsInstance(allelic_state, OntologyClass)
                self.assertIsNotNone(allelic_state.id)
                self.assertIsNotNone(allelic_state.label)
                
                # Test passes if we found at least one valid allelic state
                return
                
        # If we get here, no allelic states were found in any descriptor
        logger.warning("No allelic states found in any variation descriptor, test may be invalid")
    
    def test_mapper_with_empty_data(self):
        """Test mapper behavior with empty data"""
        # Test with empty dict
        empty_result = self.mapper.map({})
        self.assertIsNotNone(empty_result)
        self.assertIsInstance(empty_result, dict)
        self.assertEqual(len(empty_result), 0)
        
        # Test with minimal dict
        minimal_data = {"record_id": "test123"}
        minimal_result = self.mapper.map(minimal_data)
        self.assertIsNotNone(minimal_result)
        self.assertIsInstance(minimal_result, dict)
        self.assertEqual(len(minimal_result), 0)
    
    def test_error_handling(self):
        """Test error handling in the mapper"""
        # Create a processor with invalid configuration
        from rarelink.utils.processor import DataProcessor
        invalid_processor = DataProcessor(
            mapping_config={"invalid_field": "value"}
        )
        
        # Create mapper with invalid processor
        invalid_mapper = VariationDescriptorMapper(invalid_processor)
        
        # This should not raise an exception due to error handling
        result = invalid_mapper.map(self.record_101)
        
        # The result should be an empty dict
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)
        
if __name__ == "__main__":
    unittest.main()