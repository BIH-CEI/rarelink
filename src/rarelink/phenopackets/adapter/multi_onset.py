import copy
import logging
from typing import List, Any, Dict, Optional, Callable
from phenopackets import TimeElement, Age

logger = logging.getLogger(__name__)

def multi_onset_adapter(
    mapping_func: Callable[[str, Dict, Any, Optional[str]], Any],
    feature_type: str, 
    feature_data: dict, 
    processor, 
    dob: str = None
) -> List[Any]:
    """
    A generic adapter that wraps any mapping function creating a feature block.
    If multi-onset is enabled in the mapping config and any onset_date_fields have values,
    it creates a deep copy of the base feature for each valid onset value.
    
    Args:
        mapping_func (callable): Function that creates a single feature block.
        feature_type (str): The type value for the feature.
        feature_data (dict): Data for the feature.
        processor: The DataProcessor instance.
        dob (str, optional): Date of birth for age calculations.
        
    Returns:
        List[Any]: A list of feature blocks.
    """
    # Create the base feature using the provided mapping function
    base_feature = mapping_func(feature_type, feature_data, processor, dob)
    
    # If multi_onset is not enabled or no onset_date_fields defined, return the base feature.
    if not processor.mapping_config.get("multi_onset", False):
        logger.debug("Multi-onset not enabled, returning single feature")
        return [base_feature]
    
    # Get onset fields from config
    onset_fields = processor.mapping_config.get("onset_date_fields", [])
    if not onset_fields:
        logger.debug("No onset date fields configured, returning single feature")
        return [base_feature]
    
    # Create a list to store all features
    features = []
    found_onset = False
    
    # Process each onset field
    for field in onset_fields:
        # Strip any instrument prefix from the field name
        field_name = field.split(".")[-1] if "." in field else field
        
        # Try to get the onset value
        onset_value = feature_data.get(field_name)
        if onset_value:
            found_onset = True
            try:
                # Convert the onset value to a string if needed
                onset_date_str = onset_value if isinstance(onset_value, str) else str(onset_value)
                # Ensure dob is a string in proper format
                dob_str = dob if isinstance(dob, str) else (str(dob) if dob else None)
                
                logger.debug(f"Processing onset field '{field_name}' with value '{onset_date_str}'")
                
                # Calculate age at onset
                iso_age = processor.convert_date_to_iso_age(onset_date_str, dob_str)
                if iso_age:
                    # Create a new onset TimeElement
                    onset = TimeElement(age=Age(iso8601duration=iso_age))
                    
                    # Create a deep copy of the base feature
                    feature_copy = copy.deepcopy(base_feature)
                    
                    # Clear the existing onset field and set the new one
                    feature_copy.ClearField("onset")
                    feature_copy.onset.MergeFrom(onset)
                    
                    # Add the feature to our list
                    features.append(feature_copy)
                    logger.debug(f"Created feature with onset from field '{field_name}': {iso_age}")
            except Exception as e:
                logger.error(f"Error processing onset for field '{field_name}': {e}")
                import traceback
                logger.debug(traceback.format_exc())
    
    # If no valid onset values were found, return the base feature
    if not found_onset or not features:
        logger.debug("No valid onset values found, returning base feature")
        return [base_feature]
    
    return features

def _get_field_value(data: dict, field_path: str):
    """
    Get a field value from data, handling direct and nested access.
    
    Args:
        data (dict): The data to extract from.
        field_path (str): Field path, can be simple or dotted.
        
    Returns:
        Any: The field value or None if not found.
    """
    if not field_path or not data:
        return None
        
    if "." not in field_path:
        return data.get(field_path)
        
    parts = field_path.split(".", 1)
    if len(parts) == 2 and parts[0] in data:
        nested_data = data.get(parts[0])
        if isinstance(nested_data, dict):
            return nested_data.get(parts[1])
            
    if field_path in data:
        return data[field_path]
    
    return None