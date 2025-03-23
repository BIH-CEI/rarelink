# field_access.py
from typing import Any, Dict, List, Optional, Callable
import logging

logger = logging.getLogger(__name__)

def get_field_value(
    data: Dict[str, Any],
    field_path: str,
    default_value: Any = None
) -> Any:
    """
    Get a field value from data, handling direct and nested access.
    
    Args:
        data: The data to extract from
        field_path: Field path to extract
        default_value: Value to return if not found
        
    Returns:
        The field value or default_value if not found
    """
    # Handle empty or None inputs
    if not data or not field_path:
        return default_value
    
    # Direct field access for simple paths
    if "." not in field_path:
        return data.get(field_path, default_value)
        
    # Process dotted path
    parts = field_path.split(".")
    current_data = data
    
    for part in parts:
        if isinstance(current_data, dict) and part in current_data:
            current_data = current_data[part]
        else:
            return default_value

    return current_data

def get_multi_instrument_field_value(
    data: Dict[str, Any],
    instruments: List[str],
    field_paths: List[str],
    default_value: Any = None
) -> Any:
    """
    Get a field value by checking across multiple instruments and paths.
    
    Args:
        data: The data to extract from
        instruments: List of instruments to check
        field_paths: List of field paths to check
        default_value: Value to return if not found
        
    Returns:
        The first valid field value or default_value
    """
    if not data or not instruments or not field_paths:
        return default_value
    
    # Map instrument names to their data field names for RareLink CDM
    cdm_field_map = {
        "rarelink_6_2_phenotypic_feature": "phenotypic_feature",
        "rarelink_5_disease": "disease",
        "rarelink_6_1_genetic_findings": "genetic_findings",
        "rarelink_6_3_measurements": "measurements",
        "rarelink_3_patient_status": "patient_status",
        "rarelink_4_care_pathway": "care_pathway",
        "rarelink_6_4_family_history": "family_history"
    }
    
    # Try each field path with each instrument
    for instrument in instruments:
        # Check instrument in top level data
        if instrument in data:
            for field_path in field_paths:
                # Handle direct or prefixed field
                field_name = field_path
                if "." in field_path:
                    prefix, name = field_path.split(".", 1)
                    if prefix == instrument:
                        field_name = name
                
                # Check in instrument data
                if isinstance(data[instrument], dict) and field_name in data[instrument]:
                    return data[instrument][field_name]
        
        # Check in repeated_elements
        if "repeated_elements" in data:
            elements = [e for e in data["repeated_elements"] 
                       if e.get("redcap_repeat_instrument") == instrument]
            
            for element in elements:
                # Try CDM data structure
                cdm_field = cdm_field_map.get(instrument)
                if cdm_field and cdm_field in element:
                    for field_path in field_paths:
                        field_name = field_path.split(".")[-1]
                        if field_name in element[cdm_field]:
                            return element[cdm_field][field_name]
                
                # Try direct instrument access
                if instrument in element:
                    for field_path in field_paths:
                        field_name = field_path
                        if "." in field_path:
                            prefix, name = field_path.split(".", 1)
                            if prefix == instrument:
                                field_name = name
                        
                        if field_name in element[instrument]:
                            return element[instrument][field_name]
                
                # Try field directly in element
                for field_path in field_paths:
                    field_name = field_path.split(".")[-1]
                    if field_name in element:
                        return element[field_name]
    
    return default_value

def get_highest_instance(data: List[Dict[str, Any]], instrument_name: str) -> Optional[Dict[str, Any]]:
    """
    Get the dictionary with the highest redcap_repeat_instance.
    
    Args:
        data: List of dictionaries from "repeated_elements"
        instrument_name: Name of the instrument to filter
        
    Returns:
        The dictionary with the highest instance or None
    """
    elements = [e for e in data if e.get("redcap_repeat_instrument") == instrument_name]
    if not elements:
        return None
    
    return max(elements, key=lambda x: x.get("redcap_repeat_instance", 0))


def generic_map_entities(
    data: Dict[str, Any], 
    processor: Any,
    dob: str = None,
    mapping_type: str = None,
    create_entity_func: Callable = None
) -> List[Any]:
    """
    Generic mapping function for various entity types.
    
    Args:
        data (dict): Input data dictionary
        processor: Data processor with mapping configuration
        dob (str, optional): Date of birth for age calculations
        mapping_type (str, optional): Type of mapping (e.g., 'diseases', 'phenotypic_features')
        create_entity_func (callable, optional): Function to create individual entities
    
    Returns:
        list: A list of mapped entities
    """
    # Validate input
    if not data or not processor or not mapping_type or not create_entity_func:
        logger.debug(f"Invalid input. Data: {bool(data)}, Processor: {bool(processor)}, Mapping Type: {mapping_type}, Create Func: {bool(create_entity_func)}")
        return []
    
    # Retrieve mapping configuration
    try:
        # Try to get the specific mapping configuration
        # Handle different types of processor input
        if hasattr(processor, 'mapping_config'):
            # If processor is an object with mapping_config attribute
            mapping_block = getattr(processor, 'mapping_config', {})
        elif isinstance(processor, dict):
            # If processor is a dictionary
            mapping_block = processor
        else:
            # Fallback to empty dict
            mapping_block = {}
        
        # Extract instruments
        instruments = []
        instrument_name = mapping_block.get("instrument_name")
        
        if isinstance(instrument_name, (list, set)):
            instruments = list(instrument_name)
        elif instrument_name:
            instruments = [instrument_name]
        
        # If no instruments, try using the redcap_repeat_instrument
        if not instruments:
            repeat_instrument = mapping_block.get("redcap_repeat_instrument")
            if repeat_instrument:
                instruments = [repeat_instrument]
        
        # Validate instruments
        if not instruments:
            logger.debug(f"No instruments found for {mapping_type}")
            
            # If no direct instruments, try searching in the data
            instruments = [
                key for key in data.keys() 
                if key not in ['record_id', 'repeated_elements']
            ]
            
            logger.debug(f"Fallback instruments from data: {instruments}")
        
        # Collect all possible field paths from the mapping block
        field_paths = []
        for i in range(1, 10):
            field_key = f"term_field_{i}"
            if field_key in mapping_block and mapping_block[field_key]:
                field_paths.append(mapping_block[field_key])
        
        # If no field paths found, try to derive from mapping block
        if not field_paths and instruments:
            # Look for fields that match our instruments or are direct fields
            for key, value in mapping_block.items():
                if value and isinstance(value, str):
                    # Include fields that match our instruments pattern or have no dot
                    if "." not in value:
                        field_paths.append(value)
                    else:
                        instrument, _ = value.split(".", 1)
                        if instrument in instruments:
                            field_paths.append(value)
        
        # If still no field paths, return empty list
        if not field_paths:
            logger.debug("No field paths found in mapping block")
            return []
        
        logger.debug(f"Using field paths: {field_paths}")
        
        # Try to find any field values across instruments
        for field_path in field_paths:
            found_value = get_multi_instrument_field_value(
                data=data, 
                instruments=instruments, 
                field_paths=[field_path]
            )
            
            if found_value:
                # If a value is found, try to create an entity
                entity = create_entity_func(data, processor, dob)
                
                # Return the entity if found
                if entity:
                    logger.debug(f"Successfully created entity with field {field_path}")
                    return [entity]
        
        logger.debug("No entity could be created")
        return []
    
    except Exception as e:
        logger.error(f"Failed to map {mapping_type}: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        return []
