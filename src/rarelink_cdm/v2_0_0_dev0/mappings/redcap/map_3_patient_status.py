"""
Mapping function for the PatientStatus schema.

This module defines a function to map flat REDCap data entries to the
PatientStatus schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for Boolean conversions and prefix additions.
"""

from rarelink.utils.mapping import map_entry
from rarelink.utils.processing.codes import add_prefix_to_code

# Metadata for the schema
IS_REPEATING = True  # Mark as repeating schema

FIELD_MAPPINGS = {
    "patient_status_date": "patient_status_date",
    "snomed_278844005": "snomed_278844005",
    "snomed_398299004": "snomed_398299004",
    "snomed_184305005": "snomed_184305005",
    "snomed_105727008": "snomed_105727008",
    "snomed_412726003": "snomed_412726003",
    "snomed_723663001": "snomed_723663001",
    "rarelink_3_patient_status_complete": "rarelink_3_patient_status_complete",
}

ADDITIONAL_PROCESSING = {
    "snomed_184305005": lambda x: add_prefix_to_code(x, "ICD10CM"),
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
