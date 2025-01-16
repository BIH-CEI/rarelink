def get_nested_field(data: dict, field_path: str):
    """
    Fetches a value from a nested dictionary or list based on a dotted field 
    path. Handles repeated elements by selecting the latest entry (highest 
    `redcap_repeat_instance`).

    Args:
        data (dict): The dictionary to search.
        field_path (str): Dotted path to the field (e.g.,
        "personal_information.snomed_184099003" or "repeated_elements.patient_status.snomed_278844005").

    Returns:
        The value of the field or None if not found.
    """
    keys = field_path.split(".")
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        elif isinstance(data, list):
            # Handle lists by selecting the entry with the highest `redcap_repeat_instance`
            if key == "repeated_elements":
                # Ensure the list is sorted by `redcap_repeat_instance` (descending)
                data = sorted(
                    data,
                    key=lambda x: x.get("redcap_repeat_instance", 0),
                    reverse=True,
                )
                data = data[0] if data else None  # Select the latest entry
            else:
                return None  # Key doesn't match expected structure
        else:
            return None
    return data
