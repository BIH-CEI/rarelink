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
        status_field = processor.get_field(data, VITAL_STATUS_BLOCK["status_field"])
        if not status_field:
            logger.warning("Vital status field not found.")
        status_label = processor.fetch_mapping_value("map_vital_status", status_field)
        status = status_label or "UNKNOWN_STATUS"

        # Time of Death
        time_of_death_field = processor.get_field(data, VITAL_STATUS_BLOCK["time_of_death_field"])
        if not time_of_death_field:
            logger.warning("Time of death field not found.")
        time_of_death = (
            processor.process_time_element(time_of_death_field) if time_of_death_field else None
        )

        # Cause of Death
        cause_of_death_field = processor.get_field(data, VITAL_STATUS_BLOCK["cause_of_death_field"])
        if not cause_of_death_field:
            logger.warning("Cause of death field not found.")
        cause_of_death_label = (
            processor.fetch_label(cause_of_death_field) if cause_of_death_field else None
        )
        cause_of_death = (
            OntologyClass(
                id=cause_of_death_field, 
                label=cause_of_death_label
            ) if cause_of_death_label else None
        )

        # Create the VitalStatus block
        vitalstatus = VitalStatus(
            status=status,
            time_of_death=time_of_death,
            cause_of_death=cause_of_death,
        )

        logger.info(f"Successfully mapped vital status: {vitalstatus}")
        return vitalstatus

    except Exception as e:
        logger.error(f"Failed to map vital status: {e}", exc_info=True)
        raise
