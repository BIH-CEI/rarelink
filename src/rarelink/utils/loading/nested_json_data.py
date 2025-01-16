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
            # Process repeated elements as a list of dictionaries
            if isinstance(data, list):
                if highest_redcap_repeat_instance:
                    # Filter repeated elements for the given instrument
                    instrument_key = keys[i + 1].split(":")[1]
                    filtered_elements = [
                        element for element in data
                        if element.get("redcap_repeat_instrument") == instrument_key
                    ]
                    if not filtered_elements:
                        logger.warning(f"No elements found for instrument '{instrument_key}'")
                        return None
                    # Get the element with the highest redcap_repeat_instance
                    data = max(
                        filtered_elements,
                        key=lambda x: x.get("redcap_repeat_instance", 0),
                        default=None
                    )
                else:
                    return data
            else:
                logger.warning(f"Expected list for 'repeated_elements', got: {type(data)}")
                return None
        elif isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data

