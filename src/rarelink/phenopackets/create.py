from phenopackets import Phenopacket
from rarelink.utils.processor import DataProcessor
from rarelink.phenopackets.mappings import (
    map_individual,
    map_vital_status,
    map_metadata
)
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets import (
    INDIVIDUAL_BLOCK,
    VITAL_STATUS_BLOCK,
    RARELINK_CODE_SYSTEMS
)

def create_phenopacket(data: dict, created_by: str) -> Phenopacket:
    """
    Creates a Phenopacket for an individual record.

    Args:
        data (dict): The input data for the individual.
        created_by (str): The creator's name (for metadata).

    Returns:
        Phenopacket: A fully constructed Phenopacket.
    """
    # Initialize the DataProcessor for individual mapping
    individual_processor = DataProcessor(mapping_config=INDIVIDUAL_BLOCK)
    individual = map_individual(data, individual_processor)
    
    # Initialize the DataProcessor for vital status mapping
    vital_status_processor = DataProcessor(mapping_config=VITAL_STATUS_BLOCK)
    vital_status = map_vital_status(data, vital_status_processor)

    # Map the Metadata block
    metadata = map_metadata(
        created_by=created_by, 
        code_systems=RARELINK_CODE_SYSTEMS
    )

    # Construct and return the Phenopacket
    return Phenopacket(
        id=data["record_id"],
        subject=individual,
        vitalstatus=vital_status,
        meta_data=metadata
    )
