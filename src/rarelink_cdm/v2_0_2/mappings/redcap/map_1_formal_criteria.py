"""
Mapping function for the FormalCriteria schema.

This module defines a function to map flat REDCap data entries to the
FormalCriteria schema defined in the RareLink-CDM LinkML model.

"""

from rarelink.utils.mapping import map_entry

FIELD_MAPPINGS = {
    "snomedct_422549004": "snomedct_422549004",
    "snomedct_399423000": "snomedct_399423000",
    "rarelink_1_formal_criteria_complete": "rarelink_1_formal_criteria_complete",
}

def map_formal_criteria(entry):
    """
    Maps a flat REDCap entry to the FormalCriteria schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the FormalCriteria schema.
    """
    return map_entry(entry, FIELD_MAPPINGS)
