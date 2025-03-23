"""
Mapping function for the FamilyHistory schema.

This module defines a function to map flat REDCap data entries to the
FamilyHistory schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for prefix additions and numeric conversions.
"""

from rarelink.utils.mapping import map_entry
from rarelink.utils.code_processing import add_prefix_to_code

# Define mappings from REDCap fields to schema fields.
"""
Mapping function for the FamilyHistory schema.

This module defines a function to map flat REDCap data entries to the
FamilyHistory schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for prefix additions and numeric conversions.
"""

FIELD_MAPPINGS = {
    "family_history_pseudonym": "family_history_pseudonym",
    "snomedct_64245008": "snomedct_64245008",
    "snomedct_408732007": "snomedct_408732007",
    "snomedct_842009": "snomedct_842009",
    "snomedct_444018008": "snomedct_444018008",
    "hl7fhir_fmh_status": "hl7fhir_fmh_status",
    "loinc_54123_5": "loinc_54123_5",
    "loinc_54141_7": "loinc_54141_7",
    "loinc_54124_3": "loinc_54124_3",
    "snomedct_740604001": "snomedct_740604001",
    "loinc_54112_8": "loinc_54112_8",
    "loinc_92662_6": "loinc_92662_6",
    "loinc_75315_2": "loinc_75315_2",
    "rarelink_6_4_family_history_complete": "rarelink_6_4_family_history_complete",
}

# Additional processing for prefix additions and numeric conversions.
ADDITIONAL_PROCESSING = {
    "loinc_54112_8": lambda x: add_prefix_to_code(x, "ICD10CM"),
    "loinc_54141_7": lambda x: int(x) if x else None,
    "loinc_92662_6": lambda x: int(x) if x else None,
}

def map_family_history(entry):
    """
    Maps a flat REDCap entry to the FamilyHistory schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the FamilyHistory schema.
    """
    return map_entry(entry, FIELD_MAPPINGS, ADDITIONAL_PROCESSING)