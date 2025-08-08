"""
Mapping function for the Measurement schema.

This module defines a function to map flat REDCap data entries to the
Measurement schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for prefix additions and numeric conversions.
"""

from rarelink.utils.mapping import map_entry
from rarelink.utils.code_processing import add_prefix_to_code

# Define mappings from REDCap fields to schema fields.
FIELD_MAPPINGS = {
    "measurement_category": "measurement_category",
    "measurement_status": "measurement_status",
    "ncit_c60819": "ncit_c60819",
    "ln_85353_1": "ln_85353_1",
    "ln_85353_1_other": "ln_85353_1_other",
    "ncit_c25712": "ncit_c25712",
    "ncit_c92571": "ncit_c92571",
    "ncit_c41255": "ncit_c41255",
    "ncit_c82577": "ncit_c82577",
    "snomedct_122869004_ncit": "snomedct_122869004_ncit",
    "snomedct_122869004_snomed": "snomedct_122869004_snomed",
    "snomedct_122869004": "snomedct_122869004",
    "snomedct_122869004_bdsite": "snomedct_122869004_bdsite",
    "snomedct_122869004_status": "snomedct_122869004_status",
    "rarelink_6_3_measurements_complete": "rarelink_6_3_measurements_complete",
}

# Additional processing for prefix additions and numeric conversions.
ADDITIONAL_PROCESSING = {
    "ncit_c60819": lambda x: add_prefix_to_code(x, "LOINC"),
    "ln_85353_1": lambda x: add_prefix_to_code(x, "LOINC"),
    "ncit_c25712": lambda x: float(x) if x else None,
    "snomedct_122869004_snomed": lambda x: add_prefix_to_code(x, "SNOMEDCT"),
    "snomedct_122869004_bdsite": lambda x: add_prefix_to_code(x, "SNOMEDCT"),
}

def map_measurements(entry):
    """
    Maps a flat REDCap entry to the Measurement schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the Measurement schema.
    """
    return map_entry(entry, FIELD_MAPPINGS, ADDITIONAL_PROCESSING)
