def convert_to_boolean(value: str, mapping: dict) -> bool:
    """
    Converts a string value to a boolean based on a mapping.

    Args:
        value (str): String value to convert (e.g., "true", "false").
        mapping (dict): A dictionary mapping string values to booleans.

    Returns:
        bool: Converted boolean value or None if no match is found.
    """
    return mapping.get(value.lower(), None)
