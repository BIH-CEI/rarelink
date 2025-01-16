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
from rarelink.utils.loading import get_nested_field
import logging

logger = logging.getLogger(__name__)

def process_repeated_elements(data: list, processor: DataProcessor, map_function):
    """
    Processes multiple repeated elements into Phenopacket sub-blocks.

    Args:
        data (list): The repeated elements data.
        processor (DataProcessor): Processor for field mapping.
        map_function (function): Mapping function to process each element.

    Returns:
        list: A list of processed Phenopacket sub-blocks.
    """
    processed_elements = []
    for element in data:
        try:
            processed_elements.append(map_function(element, processor))
        except Exception as e:
            logger.warning(f"Failed to process repeated element: {e}")
    return processed_elements


def create_phenopacket(data: dict, created_by: str) -> Phenopacket:
    """
    Creates a Phenopacket for an individual record.

    Args:
        data (dict): The input data for the individual.
        created_by (str): The creator's name (for metadata).

    Returns:
        Phenopacket: A fully constructed Phenopacket.
    """
    try:
        # Initialize the DataProcessor for vital status mapping
        vital_status_processor = DataProcessor(mapping_config=VITAL_STATUS_BLOCK)
        vital_status = map_vital_status(data, vital_status_processor)

        # Initialize the DataProcessor for individual mapping
        individual_processor = DataProcessor(mapping_config=INDIVIDUAL_BLOCK)
        individual = map_individual(data, individual_processor, vital_status=vital_status)

        # Map the Metadata block
        metadata = map_metadata(
            created_by=created_by, 
            code_systems=RARELINK_CODE_SYSTEMS
        )

        # Construct and return the Phenopacket
        return Phenopacket(
            id=data["record_id"],
            subject=individual,
            meta_data=metadata
        )
    except Exception as e:
        logger.error(f"Error creating Phenopacket for record ID: {data.get('record_id')} - {e}")
        raise


    # # Process other repeated elements
    # repeated_elements = data.get("repeated_elements", [])
    # disease_processor = DataProcessor(mapping_config={...})  # Define mappings for disease
    # diseases = process_repeated_elements(
    #     [el for el in repeated_elements if el["redcap_repeat_instrument"] == "rarelink_5_disease"],
    #     disease_processor,
    #     map_disease,
    # )

    # phenotype_processor = DataProcessor(mapping_config={...})  # Define mappings for phenotypes
    # phenotypes = process_repeated_elements(
    #     [el for el in repeated_elements if el["redcap_repeat_instrument"] == "rarelink_6_2_phenotypic_feature"],
    #     phenotype_processor,
    #     map_phenotype,
    # )