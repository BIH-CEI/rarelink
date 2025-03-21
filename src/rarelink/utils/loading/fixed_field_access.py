"""
Fixed field access utility functions for multi-instrument support.
These functions improve field access across multiple instruments in the data structure.
"""

import logging
from typing import Callable, Any, List, Dict, Union, Set

logger = logging.getLogger(__name__)

def _get_multi_instrument_field_value(
    data: Dict[str, Any], 
    instruments: Union[List[str], Set[str], str], 
    field_paths: List[str]
) -> Any:
    """
    Retrieve a field value from multiple instruments in order of priority.
    Enhanced to handle both direct and prefixed field paths.
    
    Args:
        data (dict): The complete data dictionary
        instruments (list/set/str): Instrument names to check, in order of priority
        field_paths (list): List of field paths to check for each instrument
    
    Returns:
        The first non-None value found, or None if no value is found
    """
    # Normalize instruments to a list
    if isinstance(instruments, str):
        instruments = [instruments]
    elif isinstance(instruments, set):
        instruments = list(instruments)
    
    # Validate inputs
    if not data or not instruments or not field_paths:
        return None
    
    logger.debug(f"Searching for field across instruments: {instruments}")
    logger.debug(f"Field paths to check: {field_paths}")
    
    # First, try direct access if any field path contains an instrument name
    for field_path in field_paths:
        if "." in field_path:
            instrument_name, field_name = field_path.split(".", 1)
            if instrument_name in data:
                instrument_data = data[instrument_name]
                if isinstance(instrument_data, dict) and field_name in instrument_data:
                    value = instrument_data.get(field_name)
                    if value is not None:
                        logger.debug(f"Found value {value} using direct path: {field_path}")
                        return value
    
    # Then try each instrument with extracted field names
    for instrument_name in instruments:
        logger.debug(f"Checking instrument: {instrument_name}")
        
        # Check if the instrument exists in the data
        if instrument_name not in data:
            logger.debug(f"Instrument {instrument_name} not found in data")
            continue
        
        # Get the instrument-specific data
        instrument_data = data[instrument_name]
        if not isinstance(instrument_data, dict):
            logger.debug(f"Instrument {instrument_name} data is not a dictionary")
            continue
        
        # Try each field path for this instrument
        for field_path in field_paths:
            # Handle different field path formats
            
            # Case 1: Direct field in the instrument (no dot notation)
            if "." not in field_path:
                field_name = field_path
            # Case 2: Field path with specified instrument
            elif field_path.startswith(f"{instrument_name}."):
                field_name = field_path.split(".", 1)[1]
            # Case 3: Field path with different instrument - skip
            else:
                continue
                
            # Check if the field exists in this instrument
            if field_name in instrument_data:
                value = instrument_data.get(field_name)
                if value is not None:
                    logger.debug(f"Found value {value} for field {field_name} in instrument {instrument_name}")
                    return value
    
    # Also check for fields directly in full_data to support legacy mappings
    for field_path in field_paths:
        if "." not in field_path and field_path in data:
            value = data.get(field_path)
            if value is not None:
                logger.debug(f"Found value {value} in top-level data for field {field_path}")
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