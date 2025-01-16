def get_nested_field(data: dict, field_path: str):
    """
    Fetches a value from a nested dictionary or list based on a dotted field path.

    Args:
        data (dict): The dictionary to search.
        field_path (str): Dotted path to the field (e.g., "personal_information.snomed_184099003").
                          For arrays, include a key like "repeated_elements[redcap_repeat_instance:max]".

    Returns:
        The value of the field or None if not found.
    """
    keys = field_path.split(".")
    for key in keys:
        if isinstance(data, list) and key.startswith("[") and key.endswith("]"):
            # Handle list filtering for max redcap_repeat_instance
            list_key, condition = key.strip("[]").split(":")
            if condition == "max":
                data = max(data, key=lambda x: x.get(list_key, 0), default=None)
            else:
                raise ValueError(f"Unsupported condition: {condition}")
        elif isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data
