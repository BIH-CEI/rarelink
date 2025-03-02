import logging
from phenopackets import VitalStatus, OntologyClass, TimeElement, Age
from rarelink.utils.processor import DataProcessor
from rarelink.utils.loading import get_highest_instance 

logger = logging.getLogger(__name__)

def map_vital_status(data: dict,
                     processor: DataProcessor,
                     dob: str) -> VitalStatus:
    """
    Maps patient data to the VitalStatus block using a DataProcessor.

    Args:
        data (dict): Input data from the RareLink-CDM schema (or similar).
        processor (DataProcessor): Handles all data processing logic.
        dob (str): The individual's date of birth as an ISO8601 string.

    Returns:
        VitalStatus: A Phenopacket VitalStatus block.
    """
    # Fetching and preparation
    # --------------------------------------------------------------------------
    try:
        instrument_name = processor.mapping_config.get("instrument_name")
        if not instrument_name:
            raise ValueError(
                "Instrument name is missing from the mapping configuration.")

        # Fetch the highest redcap_repeat_instance for patient status 
        # (i.e. the most recent vital status)
        highest_instance = get_highest_instance(
            data.get("repeated_elements", []), instrument_name)
        if not highest_instance or "patient_status" not in highest_instance:
            logger.warning("No valid patient status data found.")
            return None

        # Extract fields from mapping configuration
        # ----------------------------------------------------------------------
        patient_status = highest_instance["patient_status"]
        status_field = patient_status.get(
            processor.mapping_config["status_field"])
        time_of_death_field = patient_status.get(
            processor.mapping_config["time_of_death_field"])
        cause_of_death_field = patient_status.get(
            processor.mapping_config["cause_of_death_field"])

        # Map and process fields
        # ----------------------------------------------------------------------
        status_label = processor.fetch_mapping_value(
            "map_vital_status", status_field) if status_field \
                else "UNKNOWN_STATUS"
        time_of_death = None
        if time_of_death_field and dob:
            try:
                iso_age = processor.convert_date_to_iso_age(time_of_death_field, dob)
                time_of_death = TimeElement(age=Age(iso8601duration=iso_age))
            except Exception as e:
                logger.error(f"Error processing time of death for ISO age: {e}")

        cause_of_death = (
            OntologyClass(
                id=cause_of_death_field,
                label=processor.fetch_label(cause_of_death_field)
            ) if cause_of_death_field else None
        )

        # Create the VitalStatus block
        # ----------------------------------------------------------------------
        return VitalStatus(
            status=status_label,
            time_of_death=time_of_death,
            cause_of_death=cause_of_death,
        )

    except Exception as e:
        logger.error(f"Failed to map vital status: {e}")
        raise
