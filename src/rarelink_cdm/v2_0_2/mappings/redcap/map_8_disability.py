"""
Mapping function for the Disability schema.

This module defines a function to map flat REDCap data entries to the
Disability schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined without additional processing.
"""

from rarelink.utils.mapping import map_entry

# Define mappings from REDCap fields to schema fields.
FIELD_MAPPINGS = {
    "rarelink_icf_score": "rarelink_icf_score",
    "rarelink_8_disability_complete": "rarelink_8_disability_complete",
}

def map_disability(entry):
    """
    Maps a flat REDCap entry to the Disability schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the Disability schema.
    """
    return map_entry(entry, FIELD_MAPPINGS)
