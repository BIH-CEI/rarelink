# tests/phenopackets/mappings/test_base_mapper.py
import unittest
import logging
from typing import Dict, Any, List, Optional

from rarelink.phenopackets.mappings.base_mapper import BaseMapper
from rarelink.utils.processor import DataProcessor

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Define a simple test entity class
class EntityTest:
    """Simple test entity for BaseMapper tests"""
    def __init__(self, id: str, value: Any = None):
        self.id = id
        self.value = value
    
    def __eq__(self, other):
        if not isinstance(other, EntityTest):
            return False
        return self.id == other.id and self.value == other.value
    
    def __repr__(self):
        return f"EntityTest(id='{self.id}', value={self.value})"

# Define concrete mapper implementations for testing
class SingleMapperTest(BaseMapper[EntityTest]):
    """Test mapper that returns a single entity"""
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> Optional[EntityTest]:
        """Map data to a single EntityTest"""
        # If there's an 'error' flag in the data, raise an exception to test error handling
        if data.get('error'):
            raise ValueError("Test error")
        
        # Get ID from data using the field name from the config
        id_field = self.processor.mapping_config.get('id_field', 'id')
        id_value = data.get(id_field)
        
        # If no ID found, return None
        if not id_value:
            return None
        
        # Create and return a EntityTest
        value_field = self.processor.mapping_config.get('value_field', 'value')
        value = data.get(value_field)
        
        return EntityTest(id_value, value)
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> List[EntityTest]:
        """Default implementation that wraps _map_single_entity"""
        entity = self._map_single_entity(data, instruments, **kwargs)
        return [entity] if entity else []

class MultiMapperTest(BaseMapper[EntityTest]):
    """Test mapper that returns multiple entities"""
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> Optional[EntityTest]:
        """Default implementation that returns the first entity"""
        entities = self._map_multi_entity(data, instruments, **kwargs)
        return entities[0] if entities else None
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> List[EntityTest]:
        """Map data to multiple TestEntities"""
        # If there's an 'error' flag in the data, raise an exception to test error handling
        if data.get('error'):
            raise ValueError("Test error")
        
        # Get list of items from data
        items = data.get('items', [])
        
        # Create an entity for each item
        entities = []
        for item in items:
            if isinstance(item, dict) and 'id' in item:
                entity = EntityTest(item['id'], item.get('value'))
                entities.append(entity)
        
        return entities

class BaseMapperTest(unittest.TestCase):
    """Unit tests for the BaseMapper class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create processors for single and multi mappers
        self.single_processor = DataProcessor(mapping_config={
            'id_field': 'entity_id',
            'value_field': 'entity_value'
        })
        
        self.multi_processor = DataProcessor(mapping_config={
            'multi_entity': True
        })
        
        # Create mappers
        self.single_mapper = SingleMapperTest(self.single_processor)
        self.multi_mapper = MultiMapperTest(self.multi_processor)
    
    def test_map_single_entity(self):
        """Test mapping a single entity"""
        # Test data
        data = {
            'entity_id': 'test123',
            'entity_value': 'test_value'
        }
        
        # Map using single mapper
        result = self.single_mapper.map(data)
        
        # Verify result
        self.assertIsNotNone(result)
        self.assertIsInstance(result, EntityTest)
        self.assertEqual(result.id, 'test123')
        self.assertEqual(result.value, 'test_value')
    
    def test_map_multi_entity(self):
        """Test mapping multiple entities"""
        # Test data
        data = {
            'items': [
                {'id': 'item1', 'value': 'value1'},
                {'id': 'item2', 'value': 'value2'},
                {'id': 'item3', 'value': 'value3'}
            ]
        }
        
        # Map using multi mapper
        result = self.multi_mapper.map(data)
        
        # Verify result
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        
        # Check individual entities
        self.assertEqual(result[0].id, 'item1')
        self.assertEqual(result[1].id, 'item2')
        self.assertEqual(result[2].id, 'item3')
    
    def test_error_handling_single_entity(self):
        """Test error handling for single entity mapper"""
        # Test data with error flag
        data = {
            'entity_id': 'error_test',
            'error': True
        }
        
        # Map using single mapper - should not raise exception
        result = self.single_mapper.map(data)
        
        # Verify result is None due to error handling
        self.assertIsNone(result)
    
    def test_error_handling_multi_entity(self):
        """Test error handling for multi entity mapper"""
        # Test data with error flag
        data = {
            'items': [{'id': 'item1'}],
            'error': True
        }
        
        # Map using multi mapper - should not raise exception
        result = self.multi_mapper.map(data)
        
        # Verify result is empty list due to error handling
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)
    
    def test_empty_data_handling(self):
        """Test handling of empty data"""
        # Empty data
        data = {}
        
        # Map using single mapper
        single_result = self.single_mapper.map(data)
        
        # Verify result is None for single mapper
        self.assertIsNone(single_result)
        
        # Map using multi mapper
        multi_result = self.multi_mapper.map(data)
        
        # Verify result is empty list for multi mapper
        self.assertIsNotNone(multi_result)
        self.assertIsInstance(multi_result, list)
        self.assertEqual(len(multi_result), 0)
    
    def test_get_field(self):
        """Test the get_field method"""
        # Test data
        data = {
            'direct_field': 'direct_value',
            'instrument1': {
                'nested_field': 'nested_value'
            }
        }
        
        # Set up field name in config
        self.single_processor.mapping_config['test_field'] = 'direct_field'
        self.single_processor.mapping_config['nested_field'] = 'instrument1.nested_field'
        
        # Test direct field access
        direct_value = self.single_mapper.get_field(data, 'test_field')
        self.assertEqual(direct_value, 'direct_value')
        
        # Test nested field access
        nested_value = self.single_mapper.get_field(data, 'nested_field')
        self.assertEqual(nested_value, 'nested_value')
        
        # Test non-existent field
        missing_value = self.single_mapper.get_field(data, 'missing_field', default='default')
        self.assertEqual(missing_value, 'default')
    
    def test_get_instruments(self):
        """Test the _get_instruments method"""
        # Test different instrument configurations
        
        # Single instrument name
        self.single_processor.mapping_config['instrument_name'] = 'instrument1'
        instruments = self.single_mapper._get_instruments()
        self.assertEqual(instruments, ['instrument1'])
        
        # List of instrument names
        self.single_processor.mapping_config['instrument_name'] = ['instrument1', 'instrument2']
        instruments = self.single_mapper._get_instruments()
        self.assertEqual(instruments, ['instrument1', 'instrument2'])
        
        # Set of instrument names
        self.single_processor.mapping_config['instrument_name'] = {'instrument1', 'instrument2'}
        instruments = self.single_mapper._get_instruments()
        self.assertIn('instrument1', instruments)
        self.assertIn('instrument2', instruments)
        
        # Additional repeat instrument
        self.single_processor.mapping_config['redcap_repeat_instrument'] = 'instrument3'
        instruments = self.single_mapper._get_instruments()
        self.assertIn('instrument1', instruments)
        self.assertIn('instrument2', instruments)
        self.assertIn('instrument3', instruments)
        
        # Dummy instrument should be filtered out
        self.single_processor.mapping_config['instrument_name'] = ['instrument1', '__dummy__']
        instruments = self.single_mapper._get_instruments()
        self.assertEqual(instruments, ['instrument1', 'instrument3'])
    
    def test_safe_execute(self):
        """Test the safe_execute method"""
        # Test function that succeeds
        def success_func(value):
            return value * 2
        
        # Test function that fails
        def error_func(value):
            raise ValueError(f"Error with {value}")
        
        # Test successful execution
        result = self.single_mapper.safe_execute(
            success_func,
            "Success function failed",
            value=5
        )
        self.assertEqual(result, 10)
        
        # Test error handling
        result = self.single_mapper.safe_execute(
            error_func,
            "Error function failed",
            default_return="default",
            value=5
        )
        self.assertEqual(result, "default")
    
    def test_process_code(self):
        """Test process_code method delegation"""
        # Mock the processor's method
        original_process_code = self.single_processor.process_code
        
        try:
            # Replace with test implementation
            test_result = "PROCESSED:CODE"
            self.single_processor.process_code = lambda code: test_result
            
            # Test delegation
            result = self.single_mapper.process_code("test_code")
            self.assertEqual(result, test_result)
        finally:
            # Restore original method
            self.single_processor.process_code = original_process_code
    
    
    def test_fetch_mapping_value(self):
        """Test fetch_mapping_value method delegation"""
        # Mock the processor's method
        original_fetch_mapping_value = self.single_processor.fetch_mapping_value
        
        try:
            # Replace with test implementation
            test_result = "mapped_value"
            self.single_processor.fetch_mapping_value = lambda name, code, default=None: test_result
            
            # Test delegation
            result = self.single_mapper.fetch_mapping_value("map_name", "code")
            self.assertEqual(result, test_result)
        finally:
            # Restore original method
            self.single_processor.fetch_mapping_value = original_fetch_mapping_value

if __name__ == "__main__":
    unittest.main()