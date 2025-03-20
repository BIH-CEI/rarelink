import copy
import logging
from typing import List, Any
from phenopackets import TimeElement, Age

logger = logging.getLogger(__name__)

def multi_onset_adapter(mapping_func, feature_type: str, feature_data: dict, processor, dob: str = None) -> List[Any]:
    """
    A generic adapter that wraps any mapping function creating a feature block.
    If multi‑onset is enabled in the mapping config and any onset_date_fields have values,
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
    # Create the base feature using the provided mapping function.
    base_feature = mapping_func(feature_type, feature_data, processor, dob)
    
    # If multi_onset is not enabled or no onset_date_fields are defined, return the base feature.
    onset_fields = processor.mapping_config.get("onset_date_fields", [])
    if not processor.mapping_config.get("multi_onset", False) or not onset_fields:
        return [base_feature]
    
    features = []
    found_onset = False
    for field in onset_fields:
        onset_value = _get_field_value(feature_data, field)
        if onset_value:
            found_onset = True
            try:
                # Convert the onset value to a string if needed
                onset_date_str = onset_value if isinstance(onset_value, str) else str(onset_value)
                # Ensure dob is a string in proper format
                dob_str = dob if isinstance(dob, str) else (str(dob) if dob else None)
                iso_age = processor.convert_date_to_iso_age(onset_date_str, dob_str)
                if iso_age:
                    onset = TimeElement(age=Age(iso8601duration=iso_age))
                    # Instead of direct assignment (which is not allowed),
                    # create a deep copy of the base feature, clear its onset field, and merge the new onset.
                    feature_copy = copy.deepcopy(base_feature)
                    feature_copy.ClearField("onset")
                    feature_copy.onset.MergeFrom(onset)
                    features.append(feature_copy)
                    logger.debug(f"Created feature with onset from field '{field}': {iso_age}")
            except Exception as e:
                logger.error(f"Error processing onset for field '{field}': {e}")
    # If no valid onset values were found, return the base feature as a single-element list.
    if not found_onset:
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
