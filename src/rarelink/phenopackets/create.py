from phenopackets import Phenopacket
import logging
from typing import Dict, Any, Optional

from rarelink.utils.processor import DataProcessor
from rarelink.phenopackets.mappings import (
    map_individual,
    map_vital_status,
    map_metadata,
    map_diseases,
    map_interpretations,
    map_variation_descriptor,
    map_phenotypic_features,
    map_measurements
)

logger = logging.getLogger(__name__)

def create_phenopacket(
    data: dict, 
    created_by: str, 
    mapping_configs: Optional[Dict[str, Any]] = None
) -> Phenopacket:
    """
    Creates a Phenopacket for an individual record with flexible mapping configurations.

    Args:
        data (dict): Input dictionary containing all data.
        created_by (str): Creator's name for metadata.
        mapping_configs (dict, optional): Dictionary of mapping configurations 
            for different Phenopacket blocks.

    Returns:
        Phenopacket: A fully constructed Phenopacket.
    """
    # Validate and prepare mapping configurations
    if not mapping_configs:
        raise ValueError("Mapping configurations are required")

    try:
        # Individual Block ------------------------------------------------------
        individual_config = mapping_configs.get("individual", {})
        if not individual_config:
            raise ValueError("Individual mapping configuration is missing")
        
        individual_processor = DataProcessor(
            mapping_config=individual_config.get("mapping_block", {})
        )
        
        # Extract date of birth for subsequent blocks
        dob_field = individual_processor.get_field(data, "date_of_birth_field")
        dob_str = dob_field

        # Vital Status Block ----------------------------------------------------
        vital_status_config = mapping_configs.get("vitalStatus", {})
        vital_status_processor = DataProcessor(
            mapping_config=vital_status_config.get("mapping_block", {})
        )
        
        # Set instrument name for repeated elements processing
        vital_status_processor.mapping_config["instrument_name"] = \
            vital_status_config.get("instrument_name", "")
        
        vital_status = map_vital_status(
            data, 
            vital_status_processor, 
            dob=dob_str
        )

        # Individual Block with Vital Status ------------------------------------
        individual = map_individual(
            data, 
            individual_processor, 
            vital_status=vital_status
        )

        # Phenotypic Features Block --------------------------------------------
        phenotypic_feature_config = mapping_configs.get("phenotypicFeatures", {})
        phenotypic_feature_processor = DataProcessor(
            mapping_config=phenotypic_feature_config.get("mapping_block", {})
        )
        phenotypic_feature_processor.mapping_config["redcap_repeat_instrument"] = \
            phenotypic_feature_config.get("instrument_name", "")
        
        phenotypic_features = map_phenotypic_features(
            data,
            phenotypic_feature_processor,
            dob=individual.date_of_birth
        )
        
        # Measurements Block ----------------------------------------------------
        measurement_config = mapping_configs.get("measurements", {})
        measurement_processor = DataProcessor(
            mapping_config=measurement_config.get("mapping_block", {})
        )
        measurement_processor.mapping_config["redcap_repeat_instrument"] = \
            measurement_config.get("instrument_name", "")
        
        measurements = map_measurements(
            data, 
            measurement_processor, 
            dob=individual.date_of_birth
        )  

        # Disease Block ---------------------------------------------------------
        disease_config = mapping_configs.get("diseases", {})
        disease_processor = DataProcessor(
            mapping_config=disease_config.get("mapping_block", {})
        )
        disease_processor.mapping_config["redcap_repeat_instrument"] = \
            disease_config.get("instrument_name", "")
        
        diseases = map_diseases(
            data, 
            disease_processor,
            dob=individual.date_of_birth
        )
        
        # Genetics Block --------------------------------------------------------
        # Variation Descriptor
        variation_descriptor_config = mapping_configs.get("variationDescriptor", {})
        variation_descriptor_processor = DataProcessor(
            mapping_config=variation_descriptor_config.get("mapping_block", {})
        )
        variation_descriptor_processor.mapping_config["redcap_repeat_instrument"] = \
            variation_descriptor_config.get("instrument_name", "")
        
        variation_descriptor = map_variation_descriptor(
            data,
            variation_descriptor_processor
        )
        
        # Interpretations
        interpretation_config = mapping_configs.get("interpretations", {})
        interpretation_processor = DataProcessor(
            mapping_config=interpretation_config.get("mapping_block", {})
        )
        interpretation_processor.mapping_config["redcap_repeat_instrument"] = \
            interpretation_config.get("instrument_name", "")
        
        interpretations = map_interpretations(
            data,
            interpretation_processor,
            subject_id=individual.id,
            variation_descriptor=variation_descriptor
        )
        
        # Metadata --------------------------------------------------------------
        metadata_config = mapping_configs.get("metadata", {})
        metadata = map_metadata(
            created_by=created_by,
            code_systems=metadata_config.get("code_systems")
        )

        # Construct Phenopacket -------------------------------------------------
        return Phenopacket(
            id=data.get("record_id", "unknown"),
            subject=individual,
            phenotypic_features=phenotypic_features,
            measurements=measurements,
            diseases=diseases,
            meta_data=metadata,
            interpretations=interpretations
        )
     
    except Exception as e:
        logger.error(f"Error creating Phenopacket: {e}")
        raise