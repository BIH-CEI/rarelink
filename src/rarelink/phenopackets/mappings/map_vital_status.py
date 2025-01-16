import logging
from phenopackets import VitalStatus, OntologyClass
from rarelink.utils.processor import DataProcessor
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets import VITAL_STATUS_BLOCK

logger = logging.getLogger(__name__)

def map_vital_status(data: dict, processor: DataProcessor) -> VitalStatus:
    """
    Maps patient data to the VitalStatus block using a DataProcessor.

    Args:
        data (dict): Input data from the RareLink-CDM schema (or similar).
        processor (DataProcessor): Handles all data processing logic.

    Returns:
        VitalStatus: A Phenopacket VitalStatus block.
    """ 
    try:
        # Status
        status_field = processor.get_field(
            data, VITAL_STATUS_BLOCK["status_field"], highest_redcap_repeat_instance=True
        )
        if status_field:
            status_label = processor.fetch_mapping_value("map_vital_status", status_field)
            status = status_label or "UNKNOWN_STATUS"
        else:
            logger.warning("Vital status field not found.")
            status = "UNKNOWN_STATUS"

        # Time of Death
        time_of_death_field = processor.get_field(
            data, VITAL_STATUS_BLOCK["time_of_death_field"], highest_redcap_repeat_instance=True
        )
        if time_of_death_field:
            time_of_death = processor.process_time_element(time_of_death_field)
        else:
            logger.warning("Time of death field not found.")
            time_of_death = None

        # Cause of Death
        cause_of_death_field = processor.get_field(
            data, VITAL_STATUS_BLOCK["cause_of_death_field"], highest_redcap_repeat_instance=True
        )
        if cause_of_death_field:
            cause_of_death = OntologyClass(
                id=cause_of_death_field,
                label=processor.fetch_label(cause_of_death_field)
            )
        else:
            logger.warning("Cause of death field not found.")
            cause_of_death = None

        # Create and return the VitalStatus block
        vital_status = VitalStatus(
            status=status,
            time_of_death=time_of_death,
            cause_of_death=cause_of_death,
        )

        logger.info(f"Successfully mapped vital status: {vital_status}")
        return vital_status

    except Exception as e:
        logger.error(f"Failed to map vital status: {e}")
        raise
