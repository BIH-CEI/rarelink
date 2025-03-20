import logging
from typing import Callable, Any, List, Dict, Union, Set
from rarelink.utils.processor import DataProcessor

logger = logging.getLogger(__name__)

def _get_multi_instrument_field_value(
    data: Dict[str, Any], 
    instruments: Union[List[str], Set[str], str], 
    field_paths: List[str]
) -> Any:
    """
    Retrieve a field value from multiple instruments in order of priority.
    
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
    
    # Iterate through each instrument
    for instrument in instruments:
        logger.debug(f"Checking instrument: {instrument}")
        
        # Check if the instrument exists in the data
        if instrument not in data:
            logger.debug(f"Instrument {instrument} not found in data")
            continue
        
        # Get the instrument-specific data
        instrument_data = data[instrument]
        
        # Try each field path for this instrument
        for field_path in field_paths:
            # Handle nested field paths
            if '.' in field_path:
                # Split the path
                parts = field_path.split('.')
                current_data = instrument_data
                
                # Traverse nested structure
                for part in parts:
                    if isinstance(current_data, dict) and part in current_data:
                        current_data = current_data[part]
                    else:
                        current_data = None
                        break
                
                value = current_data
            else:
                # Direct field access
                value = instrument_data.get(field_path)
            
            if value is not None:
                logger.debug(f"Found value {value} for field {field_path} in instrument {instrument}")
                return value
    
    logger.debug("No value found across specified instruments and field paths")
    return None

def _extract_instruments(mapping_config: Dict[str, Any], processor: Any = None) -> List[str]:
    """
    Extract instruments from the mapping configuration.
    
    Args:
        mapping_config (dict): Mapping configuration dictionary
        processor (optional): Processor object or configuration
    
    Returns:
        List of instrument names
    """
    # Try to extract instruments from mapping configuration
    instruments = None
    
    # Try getting instrument_name if mapping_config is a dictionary
    if isinstance(mapping_config, dict):
        instruments = mapping_config.get('instrument_name')
    
    # If no instruments found, try getting from processor
    if not instruments and processor:
        # Handle different types of processor input
        if hasattr(processor, 'mapping_config'):
            # If processor is an object with mapping_config attribute
            config = getattr(processor, 'mapping_config', {})
            if isinstance(config, dict):
                instruments = config.get('instrument_name')
        elif isinstance(processor, dict):
            # If processor is a dictionary
            instruments = processor.get('instrument_name')
    
    # Normalize to list
    if isinstance(instruments, str):
        instruments = [instruments]
    elif isinstance(instruments, set):
        instruments = list(instruments)
    
    # If still no instruments, try finding plausible instrument keys
    if not instruments:
        # Try to find keys that look like instruments
        possible_instruments = [
            key for key in (mapping_config.keys() if isinstance(mapping_config, dict) else [])
            if key not in ['instrument_name', 'mapping_block', 'label_dicts', 'mapping_dicts', 'enum_classes']
        ]
        instruments = possible_instruments
    
    # Log for debugging
    logger.debug(f"Extracted instruments: {instruments}")
    
    return instruments or []

def generic_map_entities(
    data: Dict[str, Any], 
    processor: DataProcessor,  # Using Any to avoid specific import
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
            full_config = getattr(processor, 'mapping_config', {})
        elif isinstance(processor, dict):
            # If processor is a dictionary
            full_config = processor
        else:
            # Fallback to empty dict
            full_config = {}
        
        # Get mapping configuration for specific type
        mapping_config = full_config.get(mapping_type, {})
        logger.debug(f"Mapping configuration for {mapping_type}: {mapping_config}")
        
        # Extract instruments
        instruments = _extract_instruments(mapping_config, processor)
        
        # Validate instruments
        if not instruments:
            logger.debug(f"No instruments found for {mapping_type}")
            
            # If no direct instruments, try searching in the data
            instruments = [
                key for key in data.keys() 
                if key not in ['record_id', 'repeated_elements']
            ]
            
            logger.debug(f"Fallback instruments from data: {instruments}")
        
        # Get the mapping block (specific fields to look for)
        mapping_block = mapping_config.get('mapping_block', {}) if isinstance(mapping_config, dict) else {}
        
        # Collect all possible field paths from the mapping block
        field_paths = []
        for i in range(1, 6):
            field_key = f"term_field_{i}"
            if field_key in mapping_block and mapping_block[field_key]:
                field_paths.append(mapping_block[field_key])
        
        # If no field paths found, try to derive from mapping block
        if not field_paths:
            field_paths = [
                value for key, value in mapping_block.items() 
                if value and isinstance(value, str)
            ]
        
        # If still no field paths, return empty list
        if not field_paths:
            logger.debug("No field paths found in mapping block")
            return []
        
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