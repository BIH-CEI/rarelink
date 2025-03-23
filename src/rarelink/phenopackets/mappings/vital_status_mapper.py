from typing import Dict, Any, Optional
import logging
from phenopackets import VitalStatus, OntologyClass, TimeElement, Age
from phenopackets.schema.v2 import VitalStatus as VitalStatusEnum

from rarelink.utils.field_access import get_multi_instrument_field_value, get_highest_instance
from rarelink.phenopackets.mappings.base_mapper import BaseMapper

logger = logging.getLogger(__name__)

class VitalStatusMapper(BaseMapper[VitalStatus]):
    """
    Mapper for VitalStatus entities in the Phenopacket schema.
    Maps patient vital status data to the VitalStatus block.
    """
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> Optional[VitalStatus]:
        """
        Map data to a single VitalStatus entity.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (list): List of instruments for field access
            **kwargs: Additional mapping parameters
                - dob (str, optional): Date of birth for age calculations
            
        Returns:
            Optional[VitalStatus]: Mapped VitalStatus entity or None on failure
        """
        # Extract date of birth from kwargs
        dob = kwargs.get('dob')
        
        # Define enum mapping for direct enum values
        status_enum_map = {
            "UNKNOWN_STATUS": VitalStatusEnum.Status.UNKNOWN_STATUS,
            "ALIVE": VitalStatusEnum.Status.ALIVE,
            "DECEASED": VitalStatusEnum.Status.DECEASED
        }
        
        # Initialize with default status enum value
        default_status_enum = status_enum_map["UNKNOWN_STATUS"]
        
        # Determine if a special default status has been specified
        string_status = "UNKNOWN_STATUS"
        if self.processor.mapping_config:
            if self.processor.mapping_config.get("status_field") == "_default_":
                string_status = self.processor.mapping_config.get("default_status", "UNKNOWN_STATUS")
                logger.debug(f"Using explicit default status: {string_status}")
                
        # Convert string status to enum value
        default_status_enum = status_enum_map.get(string_status, VitalStatusEnum.Status.UNKNOWN_STATUS)
        
        # Create a basic VitalStatus with just the status set
        vital_status = VitalStatus()
        vital_status.status = default_status_enum
        
        try:
            # Check if we're using a dummy instrument
            if not instruments or "__dummy__" in instruments or "_default_" in instruments:
                logger.debug(f"Using default vital status enum: {default_status_enum}")
                return vital_status
            
            # Get the patient status data
            highest_instance = None
            patient_status = None
            
            # Check for repeated elements
            if "repeated_elements" in data:
                for instrument in instruments:
                    highest_instance = get_highest_instance(
                        data.get("repeated_elements", []), instrument)
                    if highest_instance:
                        patient_status = highest_instance.get(instrument, {})
                        if patient_status:
                            break
            
            # Try direct access if not found in repeated elements
            if not patient_status:
                for instrument in instruments:
                    if instrument in data:
                        patient_status = data.get(instrument, {})
                        if patient_status:
                            break
            
            # If still no data, use default
            if not patient_status:
                logger.debug("No patient status data found, using default")
                return vital_status

            # Extract fields from mapping configuration
            status_field = self.processor.mapping_config.get("status_field")
            time_of_death_field = self.processor.mapping_config.get("time_of_death_field")
            cause_of_death_field = self.processor.mapping_config.get("cause_of_death_field")
            
            # Get status value using multi-instrument field access
            status_value = None
            if status_field and status_field != "_default_":
                status_value = get_multi_instrument_field_value(
                    data=data,
                    instruments=instruments,
                    field_paths=[status_field]
                )
            
            # Map status to string then to enum value
            if status_value:
                string_status = self.fetch_mapping_value("map_vital_status", status_value, "UNKNOWN_STATUS")
                vital_status.status = status_enum_map.get(string_status, default_status_enum)
                    
            # Time of death - only add if we have actual data
            if time_of_death_field and dob:
                death_date = get_multi_instrument_field_value(
                    data=data,
                    instruments=instruments,
                    field_paths=[time_of_death_field]
                )
                
                if death_date:
                    try:
                        iso_age = self.processor.convert_date_to_iso_age(death_date, dob)
                        if iso_age:
                            vital_status.time_of_death.CopyFrom(TimeElement(age=Age(iso8601duration=iso_age)))
                    except Exception as e:
                        logger.error(f"Error processing time of death for ISO age: {e}")

            # Cause of death - only add if we have actual data
            if cause_of_death_field:
                cause_value = get_multi_instrument_field_value(
                    data=data,
                    instruments=instruments,
                    field_paths=[cause_of_death_field]
                )
                
                if cause_value:
                    cause_id = self.process_code(cause_value)
                    cause_label = self.fetch_label(cause_value) or "Unknown Cause"
                    vital_status.cause_of_death.CopyFrom(OntologyClass(
                        id=cause_id,
                        label=cause_label
                    ))

            logger.debug(f"Created VitalStatus with status enum: {vital_status.status}")
            return vital_status
            
        except Exception as e:
            logger.error(f"Error mapping vital status: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            # Return the default VitalStatus on error
            return vital_status
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> list:
        """
        Map data to multiple VitalStatus entities.
        
        Note: VitalStatus mappers typically return just a single entity, but this
        method is required by the BaseMapper interface. It will wrap the single
        entity in a list if successful.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (list): List of instruments for field access
            **kwargs: Additional mapping parameters
            
        Returns:
            list: List containing a single mapped VitalStatus or empty list on failure
        """
        # For VitalStatus, we expect just a single entity
        vital_status = self._map_single_entity(data, instruments, **kwargs)
        
        if vital_status:
            return [vital_status]
        return []