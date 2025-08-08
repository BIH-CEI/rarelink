# src/rarelink/phenopackets/mappings/utils/common_utils.py
from typing import Any, Callable, Dict, List, Optional, Union
import logging
from datetime import datetime
from phenopackets import OntologyClass, TimeElement, Age

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, 
                 error_msg: str, 
                 debug: bool = False, 
                 default_return: Any = None, 
                 **kwargs) -> Any:
    """
    Execute a function safely with standardized error handling.
    
    Args:
        func (Callable): Function to execute
        error_msg (str): Message to log on error
        debug (bool, optional): Whether to log debug info
        default_return (Any, optional): Value to return on error
        **kwargs: Arguments to pass to func
        
    Returns:
        Any: Function result or default_return on error
    """
    try:
        return func(**kwargs)
    except Exception as e:
        logger.error(f"{error_msg}: {e}")
        if debug:
            import traceback
            logger.debug(traceback.format_exc())
        return default_return

def create_ontology_class(id_value: str, 
                          label: Optional[str] = None, 
                          default_label: str = "Unknown") -> OntologyClass:
    """
    Create an OntologyClass with standardized handling of missing labels.
    
    Args:
        id_value (str): Ontology ID
        label (str, optional): Label for the ontology term
        default_label (str, optional): Default label if none provided
        
    Returns:
        OntologyClass: The created ontology class
    """
    return OntologyClass(
        id=id_value,
        label=label or default_label
    )

def create_time_element(date_value: Union[str, datetime], 
                        dob: Union[str, datetime],
                        processor: Any) -> Optional[TimeElement]:
    """
    Create a TimeElement from a date and date of birth.
    
    Args:
        date_value (Union[str, datetime]): Date value
        dob (Union[str, datetime]): Date of birth
        processor (Any): Data processor with convert_date_to_iso_age method
        
    Returns:
        Optional[TimeElement]: TimeElement or None on failure
    """
    if not date_value or not dob:
        return None
    
    try:
        # Format dates as strings if needed
        date_str = date_value if isinstance(date_value, str) else str(date_value)
        dob_str = dob if isinstance(dob, str) else str(dob)
        
        # Convert to ISO age
        iso_age = processor.convert_date_to_iso_age(date_str, dob_str)
        if iso_age:
            return TimeElement(age=Age(iso8601duration=iso_age))
        return None
    except Exception as e:
        logger.error(f"Error creating TimeElement: {e}")
        return None

def get_data_elements(data: Dict[str, Any], 
                     instrument_name: str) -> List[Dict[str, Any]]:
    """
    Extract data elements for a given instrument.
    
    Args:
        data (Dict[str, Any]): Input data
        instrument_name (str): Name of the instrument
        
    Returns:
        List[Dict[str, Any]]: List of data elements
    """
    elements = []
    
    # Check for repeated_elements structure
    if isinstance(data, dict) and "repeated_elements" in data:
        repeated_elements = data["repeated_elements"]
        
        # Map instrument names to their data field names for RareLink CDM
        rarelink_cdm_field_map = {
            "rarelink_6_2_phenotypic_feature": "phenotypic_feature",
            "rarelink_5_disease": "disease",
            "rarelink_6_1_genetic_findings": "genetic_findings",
            "rarelink_6_3_measurements": "measurements",
            "rarelink_3_patient_status": "patient_status",
            "rarelink_4_care_pathway": "care_pathway",
            "rarelink_6_4_family_history": "family_history"
        }
        
        # Get the data field name based on the instrument name
        data_field = rarelink_cdm_field_map.get(instrument_name)
        
        # Filter elements for the target instrument
        for element in repeated_elements:
            if element.get("redcap_repeat_instrument") == instrument_name:
                # First try the RareLink CDM structure
                if data_field and data_field in element and isinstance(element[data_field], dict):
                    elements.append(element[data_field])
                # Then try the instrument name directly
                elif instrument_name in element and isinstance(element[instrument_name], dict):
                    elements.append(element[instrument_name])
                else:
                    # Last resort: use the element itself
                    elements.append(element)
    
    # If no elements found, try direct access
    if not elements and instrument_name in data and isinstance(data[instrument_name], dict):
        elements.append(data[instrument_name])
    
    return elements

def add_enum_classes_to_processor(processor: Any, enum_classes_config: Dict[str, Any]) -> None:
    """
    Add enum classes from the config to the processor.
    
    Args:
        processor (Any): Data processor with add_enum_class method
        enum_classes_config (Dict[str, Any]): Configuration with prefix to enum class mappings
    """
    if not enum_classes_config:
        return
        
    for prefix, enum_class_or_path in enum_classes_config.items():
        if enum_class_or_path:
            processor.add_enum_class(prefix, enum_class_or_path)