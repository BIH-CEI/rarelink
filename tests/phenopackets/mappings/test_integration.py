import unittest
import logging

from rarelink.phenopackets.mappings.individual_mapper import IndividualMapper
from rarelink.phenopackets.mappings.vital_status_mapper import VitalStatusMapper
from rarelink.phenopackets.mappings.disease_mapper import DiseaseMapper
from rarelink.phenopackets.mappings.phenotypic_feature_mapper import PhenotypicFeatureMapper
from rarelink.phenopackets.mappings.variation_descriptor_mapper import VariationDescriptorMapper
from rarelink.phenopackets.mappings.interpretation_mapper import InterpretationMapper

# Import test utilities
from tests.phenopackets.test_utils import (
    get_record_by_id,
    setup_processor_for_block
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestIntegrationMapping(unittest.TestCase):
    """Integration tests for mappers working together"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures that can be reused across all tests"""
        # Log test setup
        logger.info("Setting up integration tests")
        
        # Get processors and configurations for each mapper
        try:
            cls.individual_processor, _ = setup_processor_for_block("individual")
            cls.vital_status_processor, _ = setup_processor_for_block("vitalStatus")
            cls.disease_processor, _ = setup_processor_for_block("diseases")
            cls.phenotypic_processor, _ = setup_processor_for_block("phenotypicFeatures")
            cls.variation_processor, _ = setup_processor_for_block("variationDescriptor")
            cls.interpretation_processor, _ = setup_processor_for_block("interpretations")
            logger.info("Successfully set up processors for integration test")
        except ImportError as e:
            logger.error(f"Setup failed: {e}")
            raise
            
    def setUp(self):
        """Set up test fixtures for each test method"""
        # Create the mapper instances
        self.individual_mapper = IndividualMapper(self.individual_processor)
        self.vital_status_mapper = VitalStatusMapper(self.vital_status_processor)
        self.disease_mapper = DiseaseMapper(self.disease_processor)
        self.phenotypic_mapper = PhenotypicFeatureMapper(self.phenotypic_processor)
        self.variation_mapper = VariationDescriptorMapper(self.variation_processor)
        self.interpretation_mapper = InterpretationMapper(self.interpretation_processor)
        
        # Get test records
        self.record_101 = get_record_by_id("101")
        self.record_102 = get_record_by_id("102")
        self.record_103 = get_record_by_id("103")
        
        # Ensure we have test data
        if not self.record_101 or not self.record_102 or not self.record_103:
            self.fail("Test data not found - make sure the sample records JSON file is in the test_data directory")
    
    def test_individual_with_vital_status(self):
        """Test that VitalStatus can be mapped and passed to Individual mapping"""
        # First map the vital status
        vital_status = self.vital_status_mapper.map(self.record_101)
        self.assertIsNotNone(vital_status)
        
        # Log the vital status
        logger.info(f"Mapped vital status: {vital_status.status}")
        
        # Now use the vital status when mapping the individual
        individual = self.individual_mapper.map(self.record_101, vital_status=vital_status)
        self.assertIsNotNone(individual)
        
        # Verify that the vital status was correctly included
        self.assertIsNotNone(individual.vital_status)
        
        # Log the individual details
        logger.info(f"Mapped individual with ID: {individual.id}")
        
    def test_basic_phenopacket_elements(self):
        """Test mapping basic elements for a phenopacket (individual, vital status, diseases)"""
        # Extract date of birth for calculations
        dob = None
        if "personal_information" in self.record_101:
            dob = self.record_101["personal_information"].get("snomedct_184099003")
        
        # Map vital status
        vital_status = self.vital_status_mapper.map(self.record_101, dob=dob)
        self.assertIsNotNone(vital_status)
        
        # Map individual with vital status
        individual = self.individual_mapper.map(self.record_101, vital_status=vital_status)
        self.assertIsNotNone(individual)
        
        # Map diseases with date of birth
        diseases = self.disease_mapper.map(self.record_101, dob=dob)
        self.assertIsNotNone(diseases)
        self.assertGreater(len(diseases), 0)
        
        # Log the phenopacket components
        logger.info(f"Individual: {individual.id}")
        logger.info(f"Vital Status: {vital_status.status}")
        logger.info(f"Diseases: {len(diseases)}")
        for disease in diseases:
            logger.info(f"  {disease.term.id} - {disease.term.label}")
        
        # These elements could be combined into a phenopacket
        self.assertTrue(individual.IsInitialized())
        self.assertTrue(vital_status.IsInitialized())
        for disease in diseases:
            self.assertTrue(disease.IsInitialized())
            
    def test_phenotypic_features_integration(self):
        """Test integration of phenotypic features with other elements"""
        # Use record 102 which should have features with onset/resolution
        record = self.record_102
        
        # Extract date of birth for calculations
        dob = None
        if "personal_information" in record:
            dob = record["personal_information"].get("snomedct_184099003")
            
        # Map vital status and individual
        vital_status = self.vital_status_mapper.map(record, dob=dob)
        individual = self.individual_mapper.map(record, vital_status=vital_status)
        
        # Map diseases
        diseases = self.disease_mapper.map(record, dob=dob)
        
        # Map phenotypic features
        features = self.phenotypic_mapper.map(record, dob=dob)
        
        # Verify we have all components
        self.assertIsNotNone(individual)
        self.assertIsNotNone(vital_status)
        self.assertGreater(len(diseases), 0)
        self.assertGreater(len(features), 0)
        
        # Log components
        logger.info(f"Individual: {individual.id}")
        logger.info(f"Diseases: {len(diseases)}")
        logger.info(f"Phenotypic Features: {len(features)}")
        
        # Verify there's no overlap between disease and feature IDs
        disease_ids = [disease.term.id for disease in diseases]
        feature_ids = [feature.type.id for feature in features]
        common_ids = set(disease_ids).intersection(set(feature_ids))
        self.assertEqual(len(common_ids), 0, "There should be no overlap between disease and feature IDs")
        
        # Extract features with temporal aspects
        features_with_onset = [f for f in features if f.HasField("onset")]
        features_with_resolution = [f for f in features if f.HasField("resolution")]
        
        logger.info(f"Features with onset: {len(features_with_onset)} out of {len(features)}")
        logger.info(f"Features with resolution: {len(features_with_resolution)} out of {len(features)}")
        
        # Verify we have some features with onset
        self.assertGreater(len(features_with_onset), 0, "Should have some features with onset")
        
    def test_genetic_interpretation_workflow(self):
        """Test the complete genetic interpretation workflow"""
        # Use record 103 which has genetic data
        record = self.record_103
        
        # 1. Extract date of birth for calculations
        dob = None
        if "personal_information" in record:
            dob = record["personal_information"].get("snomedct_184099003")
        
        # 2. Map individual 
        vital_status = self.vital_status_mapper.map(record, dob=dob)
        self.assertIsNotNone(vital_status)
        
        individual = self.individual_mapper.map(record, vital_status=vital_status)
        self.assertIsNotNone(individual)
        
        # Log individual ID for reference
        logger.info(f"Individual: {individual.id}")
        
        # 3. Map variation descriptors
        variation_descriptors = self.variation_mapper.map(record)
        self.assertIsNotNone(variation_descriptors)
        
        # Verify we got variation descriptors
        self.assertGreater(len(variation_descriptors), 0, 
                         "No variation descriptors found - this record may not have genetic data")
        
        # Log the variation descriptors
        logger.info(f"Mapped {len(variation_descriptors)} variation descriptors")
        for instance_id, descriptor in variation_descriptors.items():
            logger.info(f"  Descriptor {instance_id}: {descriptor.id}")
            if descriptor.HasField("gene_context") and descriptor.gene_context.symbol:
                logger.info(f"    Gene: {descriptor.gene_context.symbol}")
        
        # 4. Map interpretations using the individual ID and variation descriptors
        interpretations = self.interpretation_mapper.map(
            record,
            subject_id=individual.id,
            variation_descriptors=variation_descriptors
        )
        
        # Verify interpretations
        self.assertIsNotNone(interpretations)
        
        # Log the interpretations (may be empty for some records)
        if interpretations:
            logger.info(f"Mapped {len(interpretations)} interpretations")
            for interpretation in interpretations:
                logger.info(f"  Interpretation {interpretation.id}")
                logger.info(f"    Disease: {interpretation.diagnosis.disease.id} - {interpretation.diagnosis.disease.label}")
                logger.info(f"    Status: {interpretation.progress_status}")
                
                # Log genomic interpretations
                genomic_count = len(interpretation.diagnosis.genomic_interpretations)
                logger.info(f"    Genomic interpretations: {genomic_count}")
                
                for gi in interpretation.diagnosis.genomic_interpretations:
                    logger.info(f"      Subject: {gi.subject_or_biosample_id}")
                    logger.info(f"      Status: {gi.interpretation_status}")
                    
                    if gi.HasField("variant_interpretation"):
                        vi = gi.variant_interpretation
                        logger.info(f"      ACMG classification: {vi.acmg_pathogenicity_classification}")
                        logger.info(f"      Actionability: {vi.therapeutic_actionability}")
        else:
            logger.info("No interpretations mapped - this is normal for some records")
            
    def test_full_phenopacket_assembly(self):
        """Test the assembly of a complete phenopacket with all mapper components"""
        # Use record 103 which should have all component types
        record = self.record_103
        
        # Extract date of birth
        dob = None
        if "personal_information" in record:
            dob = record["personal_information"].get("snomedct_184099003")
            
        # Map all components
        vital_status = self.vital_status_mapper.map(record, dob=dob)
        individual = self.individual_mapper.map(record, vital_status=vital_status)
        diseases = self.disease_mapper.map(record, dob=dob)
        features = self.phenotypic_mapper.map(record, dob=dob)
        variation_descriptors = self.variation_mapper.map(record)
        
        # Map interpretations if we have variation descriptors
        interpretations = []
        if variation_descriptors:
            interpretations = self.interpretation_mapper.map(
                record,
                subject_id=individual.id,
                variation_descriptors=variation_descriptors
            )
            
        # Verify all components
        self.assertIsNotNone(individual)
        self.assertIsNotNone(vital_status)
        self.assertGreater(len(diseases), 0)
        self.assertGreater(len(features), 0)
        
        # Log component counts
        logger.info(f"Individual: {individual.id}")
        logger.info(f"Diseases: {len(diseases)}")
        logger.info(f"Phenotypic Features: {len(features)}")
        logger.info(f"Variation Descriptors: {len(variation_descriptors)}")
        logger.info(f"Interpretations: {len(interpretations)}")
        
        # Verify all components are properly initialized and could be included in a phenopacket
        self.assertTrue(individual.IsInitialized())
        self.assertTrue(vital_status.IsInitialized())
        
        for disease in diseases:
            self.assertTrue(disease.IsInitialized())
            
        for feature in features:
            self.assertTrue(feature.IsInitialized())
            
        for descriptor in variation_descriptors.values():
            self.assertTrue(descriptor.IsInitialized())
            
        for interpretation in interpretations:
            self.assertTrue(interpretation.IsInitialized())
            
        logger.info("All phenopacket components are properly initialized")
        
if __name__ == "__main__":
    unittest.main()