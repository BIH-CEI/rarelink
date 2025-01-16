from phenopackets import Phenopacket
from rarelink.utils.processor import DataProcessor
from rarelink.phenopackets.mappings import (
    map_individual,
    map_vital_status,
    map_metadata,
    map_diseases
)
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets import (
    INDIVIDUAL_BLOCK,
    VITAL_STATUS_BLOCK,
    RARELINK_CODE_SYSTEMS
)
import logging

logger = logging.getLogger(__name__)

def create_phenopacket(data: dict, created_by: str) -> Phenopacket:
    """
    Creates a Phenopacket for an individual record.

    Args:
        data (dict): Input dictionary containing all data.
        created_by (str): Creator's name for metadata.

    Returns:
        Phenopacket: A fully constructed Phenopacket.
    """
    try:
        # Vital Status
        vital_status_processor = DataProcessor(mapping_config=VITAL_STATUS_BLOCK)
        vital_status = map_vital_status(data, vital_status_processor)

        # Individual
        individual_processor = DataProcessor(mapping_config=INDIVIDUAL_BLOCK)
        individual = map_individual(data, individual_processor, vital_status=vital_status)

        # Diseases
        disease_processor = DataProcessor(mapping_config={})  # No config needed for hardcoded mapping
        diseases = map_diseases(data, disease_processor)
        
        # Metadata
        metadata = map_metadata(
            created_by=created_by, 
            code_systems=RARELINK_CODE_SYSTEMS
        )

        # Construct Phenopacket
        return Phenopacket(
            id=data["record_id"],
            subject=individual,
            diseases=diseases,
            meta_data=metadata,
        )
    except Exception as e:
        logger.error(f"Error creating Phenopacket: {e}")
        raise