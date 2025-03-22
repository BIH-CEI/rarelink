"""
Fixed field access utility functions for multi-instrument support.
These functions improve field access across multiple instruments in the data structure.
"""

import logging
from typing import Callable, Any, List, Dict, Optional

logger = logging.getLogger(__name__)

def _get_multi_instrument_field_value(
    data: Dict[str, Any],
    instruments: List[str],
    field_paths: List[str],
    traverse_nested: bool = True
) -> Optional[Any]:
    """
    Gets a field value by checking across multiple instruments and field paths.
    Enhanced to support RareLink CDM data structure with instrument-specific data fields.
    
    Args:
        data (Dict[str, Any]): The data to extract from
        instruments (List[str]): List of instruments to check
        field_paths (List[str]): List of field paths to check
        traverse_nested (bool): Whether to traverse nested data
        
    Returns:
        Optional[Any]: The first valid field value found or None
    """
    if not data or not instruments or not field_paths:
        return None
        
    logger.debug(f"Using field paths: {field_paths}")
    logger.debug(f"Searching for field across instruments: {instruments}")
    
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
    
    for field_path in field_paths:
        logger.debug(f"Field paths to check: {[field_path]}")
        
        # Direct access for fields without instrument prefix
        if "." not in field_path:
            if field_path in data:
                return data[field_path]
        
        # Check in each instrument
        for instrument in instruments:
            logger.debug(f"Checking instrument: {instrument}")
            
            # CASE 1: Check if the instrument exists directly in data
            if instrument in data:
                logger.debug(f"Instrument {instrument} found in data")
                instrument_data = data[instrument]
                
                # If field_path has instrument prefix, extract the field name
                if "." in field_path:
                    path_parts = field_path.split(".", 1)
                    if path_parts[0] == instrument or path_parts[0] == rarelink_cdm_field_map.get(instrument, ""):
                        field_name = path_parts[1]
                    else:
                        field_name = field_path
                else:
                    field_name = field_path
                
                # Check in the instrument data
                if isinstance(instrument_data, dict) and field_name in instrument_data:
                    value = instrument_data[field_name]
                    logger.debug(f"Found value {value} for field {field_name} in instrument {instrument}")
                    return value
            else:
                logger.debug(f"Instrument {instrument} not found in data")
                
            # CASE 2: Check in repeated_elements
            if "repeated_elements" in data:
                # Find all elements for the current instrument
                instrument_elements = [
                    element for element in data["repeated_elements"]
                    if element.get("redcap_repeat_instrument") == instrument
                ]
                
                if instrument_elements:
                    logger.debug(f"Found {len(instrument_elements)} repeated elements for instrument {instrument}")
                    
                    # Check each element
                    for element in instrument_elements:
                        # Get the mapped data field name for RareLink CDM
                        data_field = rarelink_cdm_field_map.get(instrument)
                        
                        # Try the RareLink CDM approach first
                        if data_field and data_field in element:
                            element_data = element[data_field]
                            if isinstance(element_data, dict):
                                # If field_path has instrument prefix, extract the field name
                                if "." in field_path:
                                    path_parts = field_path.split(".", 1)
                                    if path_parts[0] == instrument or path_parts[0] == data_field:
                                        field_name = path_parts[1]
                                    else:
                                        field_name = field_path
                                else:
                                    field_name = field_path
                                    
                                # Check in the element data
                                if field_name in element_data:
                                    value = element_data[field_name]
                                    logger.debug(f"Found value {value} for field {field_name} in RareLink CDM element")
                                    return value
                        
                        # Try the direct approach next
                        if instrument in element:
                            element_data = element[instrument]
                            if isinstance(element_data, dict):
                                # If field_path has instrument prefix, extract the field name
                                if "." in field_path:
                                    path_parts = field_path.split(".", 1)
                                    if path_parts[0] == instrument:
                                        field_name = path_parts[1]
                                    else:
                                        field_name = field_path
                                else:
                                    field_name = field_path
                                    
                                # Check in the element data
                                if field_name in element_data:
                                    value = element_data[field_name]
                                    logger.debug(f"Found value {value} for field {field_name} in direct element")
                                    return value
                        
                        # Also check if the field is directly in the element (for flattened data)
                        field_name = field_path.split(".")[-1] if "." in field_path else field_path
                        if field_name in element:
                            value = element[field_name]
                            logger.debug(f"Found value {value} for field {field_name} directly in element")
                            return value
    
    logger.debug("No value found across specified instruments and field paths")
    return None

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
        for i in range(1, 6):
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
            found_value = _get_multi_instrument_field_value(
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