# src/rarelink/utils/loading/nested_json_data.py
import logging

logger = logging.getLogger(__name__)

def get_nested_field(data: dict, field_path: str, highest_redcap_repeat_instance: bool = False, default_value=None):
    """
    Fetches a value from a nested dictionary based on a dotted field path,
    with support for processing lists of dictionaries in `repeated_elements`.
    Enhanced to handle multiple data models with graceful fallbacks.

    Args:
        data (dict): The dictionary to search.
        field_path (str): Dotted path to the field.
        highest_redcap_repeat_instance (bool): Whether to fetch the value 
                                               from the highest redcap_repeat_instance.
        default_value: Value to return if field cannot be found

    Returns:
        Any: The value of the field or default_value if not found.
    """
    # Handle empty or None data
    if not data:
        return default_value
        
    # Direct field access for simple paths
    if "." not in field_path:
        return data.get(field_path, default_value)
        
    # Process dotted path
    keys = field_path.split(".")
    current_data = data
    
    for i, key in enumerate(keys):
        # Debug logging
        logger.debug(f"Processing key '{key}' at level {i} with data type: {type(current_data)}")

        # Handle repeated_elements specially
        if key == "repeated_elements":
            # Ensure we have a list to work with
            if not isinstance(current_data, dict) or "repeated_elements" not in current_data:
                logger.debug(f"No 'repeated_elements' found in data at level {i}")
                return default_value
                
            current_data = current_data.get("repeated_elements", [])
            continue

        # Filter repeated_elements by condition
        if i > 0 and keys[i-1] == "repeated_elements" and "[" in key and ":" in key:
            try:
                # Extract filter conditions like "redcap_repeat_instrument:rarelink_3_patient_status"
                condition_key, condition_value = key.split(":")[1].strip("]").split("=")
                logger.debug(f"Filtering on condition: {condition_key}={condition_value}")

                if isinstance(current_data, list):
                    current_data = [
                        elem for elem in current_data
                        if elem.get(condition_key) == condition_value
                    ]
                    
                    # If we need the element with highest repeat instance
                    if highest_redcap_repeat_instance and current_data:
                        current_data = max(current_data, key=lambda x: x.get("redcap_repeat_instance", 0))
                        
                else:
                    logger.debug(f"Expected list for filtering, got: {type(current_data)}")
                    return default_value
            except Exception as e:
                logger.error(f"Error filtering repeated elements: {e}")
                return default_value
            continue

        # Normal dictionary access
        if isinstance(current_data, dict):
            if key in current_data:
                current_data = current_data[key]
            else:
                # Try with different key formats for compatibility
                alt_key = key.replace(".", "_")  # Try with underscores instead of dots
                if alt_key in current_data:
                    current_data = current_data[alt_key]
                else:
                    logger.debug(f"Key '{key}' not found in data")
                    return default_value
        elif isinstance(current_data, list):
            # If we're trying to access a field in a list, try to find it in each item
            if i < len(keys) - 1:  # Not the last key, so we need to drill down
                found = False
                for item in current_data:
                    if isinstance(item, dict) and key in item:
                        current_data = item[key]
                        found = True
                        break
                if not found:
                    logger.debug(f"Key '{key}' not found in any list item")
                    return default_value
            else:  # Last key, return all matching values as a list
                result = []
                for item in current_data:
                    if isinstance(item, dict) and key in item:
                        result.append(item[key])
                return result or default_value
        else:
            logger.debug(f"Cannot process key '{key}' in data of type {type(current_data)}")
            return default_value

    return current_data