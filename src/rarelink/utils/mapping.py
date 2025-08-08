def map_entry(entry: dict, field_mappings: dict, additional_processing=None):
    """
    General function to map an entry based on a field-to-field mapping.

    Args:
        entry (dict): The original flat dictionary.
        field_mappings (dict): A mapping of target_field -> source_field.
        additional_processing (dict): Optional processing for specific fields.

    Returns:
        dict: The mapped entry.
    """
    mapped_entry = {}
    for target_field, source_field in field_mappings.items():
        value = entry.get(source_field, "")
        if additional_processing and target_field in additional_processing:
            value = additional_processing[target_field](value)
        mapped_entry[target_field] = value
    return mapped_entry