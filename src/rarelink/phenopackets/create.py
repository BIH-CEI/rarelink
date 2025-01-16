from phenopackets import Phenopacket
from rarelink.phenopackets.mappings.map_individual import map_individual
from rarelink.phenopackets.mappings.map_metadata import map_metadata
from rarelink.utils.processor import DataProcessor 
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets import (
    INDIVIDUAL_BLOCK, 
    RESOURCE_CONFIG
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
    # Initialize the DataProcessor with the data model-specific mappings
    processor = DataProcessor(mapping_config=INDIVIDUAL_BLOCK)

    # Map the Individual block
    individual = map_individual(data, processor)

    # Map the Metadata block
    metadata = map_metadata(created_by=created_by, 
                            resources_config=RESOURCE_CONFIG)

    # Construct and return the Phenopacket
    return Phenopacket(
        id=data["record_id"],
        subject=individual,
        meta_data=metadata
    )
