def convert_to_boolean(value: str, mapping: dict) -> bool:
    """A simple conversion function to convert a string to a boolean value.

    Args:
        value (str): any code or string value
        mapping (dict): True or False mapping 

    Returns:
        bool: True or False
    """
    return mapping.get(value.lower(), None)