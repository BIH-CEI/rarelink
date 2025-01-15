"""
Mapping function for the Disease schema.

This module defines a function to map flat REDCap data entries to the
Disease schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for certain fields requiring standardized prefixes.
"""

from rarelink.utils.mapping import map_entry
from rarelink.utils.processing.codes import add_prefix_to_code

# Define mappings from REDCap fields to schema fields.
FIELD_MAPPINGS = {
    "disease_coding": "disease_coding",
    "snomed_64572001_mondo": "snomed_64572001_mondo",
    "snomed_64572001_ordo": "snomed_64572001_ordo",
    "snomed_64572001_icd10cm": "snomed_64572001_icd10cm",
    "snomed_64572001_icd11": "snomed_64572001_icd11",
    "snomed_64572001_omim_p": "snomed_64572001_omim_p",
    "loinc_99498_8": "loinc_99498_8",
    "snomed_424850005": "snomed_424850005",
    "snomed_298059007": "snomed_298059007",
    "snomed_423493009": "snomed_423493009",
    "snomed_432213005": "snomed_432213005",
    "snomed_363698007": "snomed_363698007",
    "snomed_263493007": "snomed_263493007",
    "snomed_246112005": "snomed_246112005",
    "rarelink_5_disease_complete": "rarelink_5_disease_complete",
}

# Define additional processing for certain fields.
ADDITIONAL_PROCESSING = {
    "snomed_64572001_icd10cm": lambda x: add_prefix_to_code(x, "ICD10CM"),
    "snomed_64572001_icd11": lambda x: add_prefix_to_code(x, "ICD11"),
    "snomed_64572001_omim_p": lambda x: add_prefix_to_code(x, "OMIM"),
    "snomed_363698007": lambda x: add_prefix_to_code(x, "SNOMEDCT"),
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
