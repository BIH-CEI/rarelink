def get_nested_field(data: dict, field_path: str):
    """
    Fetches a value from a nested dictionary based on a dotted field path.

    Args:
        data (dict): The dictionary to search.
        field_path (str): Dotted path to the field (e.g.,
        "personal_information.snomed_184099003").

    Returns:
        The value of the field or None if not found.
    """
    keys = field_path.split(".")
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data

