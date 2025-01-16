import logging

logger = logging.getLogger(__name__)

def get_nested_field(data: dict, field_path: str, highest_redcap_repeat_instance: bool = False):
    """
    Fetches a value from a nested dictionary based on a dotted field path,
    with support for processing lists of dictionaries in `repeated_elements`.

    Args:
        data (dict): The dictionary to search.
        field_path (str): Dotted path to the field.
        highest_redcap_repeat_instance (bool): Whether to fetch the value 
                                               from the highest redcap_repeat_instance.

    Returns:
        Any: The value of the field or None if not found.
    """
    keys = field_path.split(".")
    for i, key in enumerate(keys):
        if key.startswith("repeated_elements"):
            # Parse filter conditions like [redcap_repeat_instrument:rarelink_5_disease]
            if ":" in key:
                condition_key, condition_value = key.split(":")[1].strip("]").split("=")
                if isinstance(data, list):
                    data = [
                        elem for elem in data
                        if elem.get(condition_key) == condition_value
                    ]
                else:
                    logger.warning(f"Expected list for 'repeated_elements', got: {type(data)}")
                    return None

            # Handle max logic for `redcap_repeat_instance`
            if highest_redcap_repeat_instance:
                if isinstance(data, list) and len(data) > 0:
                    data = max(data, key=lambda x: x.get("redcap_repeat_instance", 0))
                else:
                    return None
            elif isinstance(data, list):
                return data  # Return all matching elements if no `max` condition
        elif isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data

