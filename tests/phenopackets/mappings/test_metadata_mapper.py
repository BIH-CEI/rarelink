import unittest
import logging
from unittest.mock import Mock, patch

from rarelink.phenopackets.mappings.metadata_mapper import MetadataMapper
from phenopackets import MetaData
from rarelink_cdm import import_from_latest

CodeSystemsContainer = getattr(
    import_from_latest("python_datamodel"),
    "CodeSystemsContainer"
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestMetadataMapper(unittest.TestCase):
    """Unit tests for the MetadataMapper class"""
    
    def setUp(self):
        """Set up test fixtures for each test method"""
        # Create the mapper instance
        self.mapper = MetadataMapper(Mock())
        
        # Create a mock CodeSystemsContainer
        self.mock_code_systems = Mock(spec=CodeSystemsContainer)
        
        # Set up mock fields and values
        self.field_names = ["hp", "mondo", "ncbitaxon", "snomedct"]
        self.mock_fields = []
        
        # Create mock fields that dataclasses.fields would return
        for name in self.field_names:
            mock_field = Mock()
            mock_field.name = name
            self.mock_fields.append(mock_field)
            
            # Create and attach a mock value object to the container
            mock_value = Mock()
            mock_value.name = f"{name.upper()} Ontology"
            mock_value.url = f"http://example.org/{name}"
            mock_value.version = f"1.0.{name}"
            mock_value.prefix = name.upper()
            mock_value.iri_prefix = f"http://purl.obolibrary.org/obo/{name.upper()}_"
            
            setattr(self.mock_code_systems, name, mock_value)
    
    @patch('dataclasses.fields')
    def test_metadata_mapping(self, mock_dataclasses_fields):
        """Test that metadata is correctly mapped"""
        # Configure the mock to return our mock fields
        mock_dataclasses_fields.return_value = self.mock_fields
        
        # Map metadata
        created_by = "Test Creator"
        metadata = self.mapper.map({}, created_by=created_by, code_systems=self.mock_code_systems)
        
        # Verify the result
        self.assertIsNotNone(metadata)
        self.assertIsInstance(metadata, MetaData)
        self.assertEqual(metadata.created_by, created_by)
        self.assertEqual(metadata.phenopacket_schema_version, "2.0")
        
        # Verify created timestamp
        self.assertIsNotNone(metadata.created)
        
        # Verify resources
        self.assertEqual(len(metadata.resources), len(self.field_names))
        
        # Check each resource
        for i, name in enumerate(self.field_names):
            resource = metadata.resources[i]
            self.assertEqual(resource.id, name.lower())
            self.assertEqual(resource.name, f"{name.upper()} Ontology")
            self.assertEqual(resource.url, f"http://example.org/{name}")
            self.assertEqual(resource.version, f"1.0.{name}")
            self.assertEqual(resource.namespace_prefix, name.upper())
            self.assertEqual(resource.iri_prefix, f"http://purl.obolibrary.org/obo/{name.upper()}_")
    
    def test_metadata_without_code_systems(self):
        """Test that metadata is created without code_systems"""
        # Map metadata without code_systems
        created_by = "Test Creator"
        metadata = self.mapper.map({}, created_by=created_by)
        
        # Verify the result
        self.assertIsNotNone(metadata)
        self.assertIsInstance(metadata, MetaData)
        self.assertEqual(metadata.created_by, created_by)
        self.assertEqual(metadata.phenopacket_schema_version, "2.0")
        self.assertEqual(len(metadata.resources), 0)
    
    def test_timestamp_creation(self):
        """Test that timestamp is created correctly"""    
        # Map metadata
        metadata = self.mapper.map({}, created_by="Test Creator")
        
        # Just verify a timestamp exists, don't worry about exact value
        self.assertIsNotNone(metadata.created)
        self.assertTrue(hasattr(metadata.created, 'seconds'))
        self.assertTrue(hasattr(metadata.created, 'nanos'))
        
    def test_empty_created_by(self):
        """Test that metadata is created with empty created_by"""
        # Map metadata with empty created_by
        metadata = self.mapper.map({})
        
        # Verify the result
        self.assertIsNotNone(metadata)
        self.assertIsInstance(metadata, MetaData)
        self.assertEqual(metadata.created_by, "")
        
if __name__ == "__main__":
    unittest.main()