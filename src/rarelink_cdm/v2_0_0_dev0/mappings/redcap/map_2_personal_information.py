"""
Mapping function for the PersonalInformation schema.

This module defines a function to map flat REDCap data entries to the
PersonalInformation schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for Boolean conversions and prefix additions.
"""

from rarelink.utils.mapping import map_entry

FIELD_MAPPINGS = {
    "snomed_184099003": "snomed_184099003",
    "snomed_281053000": "snomed_281053000",
    "snomed_1296886006": "snomed_1296886006",
    "snomed_263495000": "snomed_263495000",
    "snomed_370159000": "snomed_370159000",
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
