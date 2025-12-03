"""
Mapping function for the Disease schema.

This module defines a function to map flat REDCap data entries to the
Disease schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for certain fields requiring standardized prefixes.
"""

from rarelink.utils.mapping import map_entry
from rarelink.utils.code_processing import add_prefix_to_code

# Define mappings from REDCap fields to schema fields.
FIELD_MAPPINGS = {
    "disease_coding": "disease_coding",
    "snomedct_64572001_mondo": "snomedct_64572001_mondo",
    "snomedct_64572001_ordo": "snomedct_64572001_ordo",
    "snomedct_64572001_icd10cm": "snomedct_64572001_icd10cm",
    "snomedct_64572001_icd11": "snomedct_64572001_icd11",
    "snomedct_64572001_omim_p": "snomedct_64572001_omim_p",
    "loinc_99498_8": "loinc_99498_8",
    "snomedct_424850005": "snomedct_424850005",
    "snomedct_298059007": "snomedct_298059007",
    "snomedct_423493009": "snomedct_423493009",
    "snomedct_432213005": "snomedct_432213005",
    "snomedct_363698007": "snomedct_363698007",
    "snomedct_263493007": "snomedct_263493007",
    "snomedct_246112005": "snomedct_246112005",
    "rarelink_5_disease_complete": "rarelink_5_disease_complete",
}

# Define additional processing for certain fields.
ADDITIONAL_PROCESSING = {
    "snomedct_64572001_icd10cm": lambda x: add_prefix_to_code(x, "ICD10CM"),
    "snomedct_64572001_icd11": lambda x: add_prefix_to_code(x, "ICD11"),
    "snomedct_64572001_omim_p": lambda x: add_prefix_to_code(x, "OMIM"),
    "snomedct_363698007": lambda x: add_prefix_to_code(x, "SNOMEDCT"),
}

def map_disease(entry):
    """
    Maps a flat REDCap entry to the Disease schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the Disease schema.
    """
    return map_entry(entry, FIELD_MAPPINGS, ADDITIONAL_PROCESSING)
