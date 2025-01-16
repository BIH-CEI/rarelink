import logging

logger = logging.getLogger(__name__)


def get_nested_field(data: dict, field_path: str, highest_redcap_repeat_instance: bool = False):
    """
    Fetches a value from a nested dictionary based on a dotted field path, 
    with support for special handling of repeated elements.

    Args:
        data (dict): The dictionary to search.
        field_path (str): Dotted path to the field.
        highest_redcap_repeat_instance (bool): Whether to fetch the value from the
                                               highest redcap_repeat_instance.

    Returns:
        Any: The value of the field or None if not found.
    """
    keys = field_path.split(".")
    for key in keys:
        # Handle repeated_elements with filtering or max logic
        if key.startswith("repeated_elements"):
            if not isinstance(data, list):
                logger.warning(f"Expected list for 'repeated_elements', got: {type(data)}")
                return None
            
            # Extract instrument name if specified (e.g., repeated_elements[rarelink_3_patient_status])
            if "[" in key and "]" in key:
                instrument_name = key[key.find("[") + 1 : key.find("]")]
                if instrument_name != "redcap_repeat_instance:max":
                    data = [
                        item for item in data
                        if item.get("redcap_repeat_instrument") == instrument_name
                    ]
            
            # Handle highest redcap_repeat_instance
            if highest_redcap_repeat_instance or "redcap_repeat_instance:max" in key:
                if data:
                    data = max(data, key=lambda x: x.get("redcap_repeat_instance", 0))
                else:
                    return None
        elif isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None

    return data
