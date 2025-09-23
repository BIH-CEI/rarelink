"""
Mapping function for the PatientStatus schema.

This module defines a function to map flat REDCap data entries to the
PatientStatus schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for Boolean conversions and prefix additions.
"""

from rarelink.utils.mapping import map_entry
from rarelink.utils.code_processing import add_prefix_to_code, convert_to_boolean

# Metadata for the schema
IS_REPEATING = True  # Mark as repeating schema

FIELD_MAPPINGS = {
    "patient_status_date": "patient_status_date",
    "snomedct_278844005": "snomedct_278844005",
    "snomedct_398299004": "snomedct_398299004",
    "snomedct_184305005": "snomedct_184305005",
    "snomedct_105727008": "snomedct_105727008",
    "snomedct_412726003": "snomedct_412726003",
    "snomedct_723663001": "snomedct_723663001",
    "rarelink_3_patient_status_complete": "rarelink_3_patient_status_complete",
}

ADDITIONAL_PROCESSING = {
    "snomedct_184305005": lambda x: add_prefix_to_code(x, "ICD10CM"),
    "snomedct_723663001": lambda x: convert_to_boolean(x, 
                {"snomedct_373066001": True, "snomedct_373067005": False})
}

def map_patient_status(entry):
    """
    Maps a flat REDCap entry to the PatientStatus schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the PatientStatus schema.
    """
    return map_entry(entry, FIELD_MAPPINGS, ADDITIONAL_PROCESSING)

