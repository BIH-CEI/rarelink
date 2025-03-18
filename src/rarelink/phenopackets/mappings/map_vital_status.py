# src/rarelink/phenopackets/mappings/map_vital_status.py
import logging
from phenopackets import VitalStatus, OntologyClass, TimeElement, Age
from rarelink.utils.processor import DataProcessor
from rarelink.utils.loading import get_highest_instance
from phenopackets.schema.v2 import VitalStatus as VitalStatusEnum  # Import enum directly

logger = logging.getLogger(__name__)


def map_vital_status(data: dict,
                     processor: DataProcessor,
                     dob: str = None) -> VitalStatus:
    """
    Maps patient data to the VitalStatus block using a DataProcessor.
    Enhanced to use direct enum values for more reliable serialization.

    Args:
        data (dict): Input data from any schema.
        processor (DataProcessor): Handles all data processing logic.
        dob (str, optional): The individual's date of birth for age calculations.

    Returns:
        VitalStatus: A Phenopacket VitalStatus block.
    """
    # Define enum mapping
    status_enum_map = {
        "UNKNOWN_STATUS": VitalStatusEnum.Status.UNKNOWN_STATUS,
        "ALIVE": VitalStatusEnum.Status.ALIVE,
        "DECEASED": VitalStatusEnum.Status.DECEASED
    }
    
    # Initialize with default status enum value
    default_status_enum = status_enum_map["UNKNOWN_STATUS"]
    
    # Determine if a special default status has been specified
    string_status = "UNKNOWN_STATUS"
    if processor.mapping_config:
        if processor.mapping_config.get("status_field") == "_default_":
            string_status = processor.mapping_config.get("default_status", "UNKNOWN_STATUS")
            logger.debug(f"Using explicit default status: {string_status}")
            
    # Convert string status to enum value
    default_status_enum = status_enum_map.get(string_status, VitalStatusEnum.Status.UNKNOWN_STATUS)
    
    logger.debug(f"Starting vital status mapping with default status enum: {default_status_enum}")
    
    # Create a basic VitalStatus with just the status set
    vital_status = VitalStatus()
    vital_status.status = default_status_enum
    
    try:
        instrument_name = processor.mapping_config.get("instrument_name")
        
        # If no instrument name or special "__dummy__" marker, use default
        if not instrument_name or instrument_name == "__dummy__" or instrument_name == "_default_":
            logger.debug(f"Using default vital status enum: {default_status_enum}")
            return vital_status
            
        # Check if we have data specific to this instrument
        has_data = False
        
        # Try to find repeated elements
        if "repeated_elements" in data:
            repeated_elements = data.get("repeated_elements", [])
            if any(element.get("redcap_repeat_instrument") == instrument_name for element in repeated_elements):
                has_data = True
                
        # Try direct access
        if instrument_name in data:
            has_data = True
            
        # If no data found, use default
        if not has_data:
            logger.debug(f"No data found for instrument {instrument_name}, using default status enum")
            return vital_status
        
        # Get the patient status data
        highest_instance = None
        patient_status = None
        
        # Check for repeated elements
        if "repeated_elements" in data:
            highest_instance = get_highest_instance(
                data.get("repeated_elements", []), instrument_name)
            if highest_instance:
                patient_status = highest_instance.get(instrument_name, {})
                
        # Try direct access if not found in repeated elements
        if not patient_status and instrument_name in data:
            patient_status = data.get(instrument_name, {})
            
        # If still no data, use default
        if not patient_status:
            logger.debug("No patient status data found, using default")
            return vital_status

        # Extract fields from mapping configuration
        # ----------------------------------------------------------------------
        status_field = processor.mapping_config.get("status_field")
        time_of_death_field = processor.mapping_config.get("time_of_death_field")
        cause_of_death_field = processor.mapping_config.get("cause_of_death_field")
        
        # Get status value
        status_value = None
        if status_field and status_field != "_default_":
            if "." in status_field:
                # Handle nested field access
                parts = status_field.split(".", 1)
                if parts[0] in patient_status and isinstance(patient_status[parts[0]], dict):
                    status_value = patient_status[parts[0]].get(parts[1])
            else:
                # Direct field access
                status_value = patient_status.get(status_field)
        
        # Map status to string then to enum value
        if status_value:
            string_status = processor.fetch_mapping_value(
                "map_vital_status", status_value, "UNKNOWN_STATUS")
            vital_status.status = status_enum_map.get(string_status, default_status_enum)
                
        # Time of death - only add if we have actual data
        if time_of_death_field and dob:
            death_date = None
            if "." in time_of_death_field:
                # Handle nested field access
                parts = time_of_death_field.split(".", 1)
                if parts[0] in patient_status and isinstance(patient_status[parts[0]], dict):
                    death_date = patient_status[parts[0]].get(parts[1])
            else:
                # Direct field access
                death_date = patient_status.get(time_of_death_field)
                
            if death_date:
                try:
                    iso_age = processor.convert_date_to_iso_age(death_date, dob)
                    vital_status.time_of_death.CopyFrom(TimeElement(age=Age(iso8601duration=iso_age)))
                except Exception as e:
                    logger.error(f"Error processing time of death for ISO age: {e}")

        # Cause of death - only add if we have actual data
        if cause_of_death_field:
            cause_value = None
            if "." in cause_of_death_field:
                # Handle nested field access
                parts = cause_of_death_field.split(".", 1)
                if parts[0] in patient_status and isinstance(patient_status[parts[0]], dict):
                    cause_value = patient_status[parts[0]].get(parts[1])
            else:
                # Direct field access
                cause_value = patient_status.get(cause_of_death_field)
                
            if cause_value:
                cause_label = processor.fetch_label(cause_value) or "Unknown Cause"
                vital_status.cause_of_death.CopyFrom(OntologyClass(
                    id=cause_value,
                    label=cause_label
                ))

        logger.debug(f"Created VitalStatus with status enum: {vital_status.status}")
        return vital_status

    except Exception as e:
        logger.error(f"Failed to map vital status: {e}")
        # Return the default VitalStatus
        return vital_status