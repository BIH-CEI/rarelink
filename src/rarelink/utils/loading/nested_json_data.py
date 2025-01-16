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
        if key == "repeated_elements":
            # Handle repeated_elements as a list of dictionaries
            if isinstance(data, list):
                if highest_redcap_repeat_instance:
                    # Find the dictionary with the highest redcap_repeat_instance
                    data = max(
                        data,
                        key=lambda x: x.get("redcap_repeat_instance", 0),
                        default=None
                    )
                else:
                    # If no filtering, return the list itself
                    return data
            else:
                logger.warning(f"Expected list for 'repeated_elements', got: {type(data)}")
                return None
        elif isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data
