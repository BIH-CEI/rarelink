"""
Mapping function for the PersonalInformation schema.

This module defines a function to map flat REDCap data entries to the
PersonalInformation schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for Boolean conversions and prefix additions.
"""

from rarelink.utils.mapping import map_entry

FIELD_MAPPINGS = {
    "snomedct_184099003": "snomedct_184099003",
    "snomedct_281053000": "snomedct_281053000",
    "snomedct_1296886006": "snomedct_1296886006",
    "snomedct_263495000": "snomedct_263495000",
    "snomedct_370159000": "snomedct_370159000",
    "rarelink_2_personal_information_complete": "rarelink_2_personal_information_complete",
}

def map_personal_information(entry):
    """
    Maps a flat REDCap entry to the PersonalInformation schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the PersonalInformation schema.
    """
    return map_entry(entry, FIELD_MAPPINGS)
