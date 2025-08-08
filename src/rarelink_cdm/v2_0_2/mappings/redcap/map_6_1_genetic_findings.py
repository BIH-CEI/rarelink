"""
Mapping function for the GeneticFindings schema.

This module defines a function to map flat REDCap data entries to the
GeneticFindings schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for Boolean conversions and prefix additions.
"""

from rarelink.utils.mapping import map_entry
from rarelink.utils.code_processing import add_prefix_to_code

# Define mappings from REDCap fields to schema fields.
FIELD_MAPPINGS = {
    "genetic_diagnosis_code": "genetic_diagnosis_code",
    "snomedct_106221001_mondo": "snomedct_106221001_mondo",
    "snomedct_106221001_omim_p": "snomedct_106221001_omim_p",
    "ga4gh_progress_status": "ga4gh_progress_status",
    "ga4gh_interp_status": "ga4gh_interp_status",
    "loinc_81304_8": "loinc_81304_8",
    "loinc_62374_4": "loinc_62374_4",
    "loinc_lp7824_8": "loinc_lp7824_8",
    "variant_expression": "variant_expression",
    "loinc_81290_9": "loinc_81290_9",
    "loinc_48004_6": "loinc_48004_6",
    "loinc_48005_3": "loinc_48005_3",
    "variant_validation": "variant_validation",
    "loinc_48018_6": "loinc_48018_6",
    "loinc_53034_5": "loinc_53034_5",
    "loinc_53034_5_other": "loinc_53034_5_other",
    "loinc_48002_0": "loinc_48002_0",
    "loinc_48019_4": "loinc_48019_4",
    "loinc_48019_4_other": "loinc_48019_4_other",
    "loinc_53037_8": "loinc_53037_8",
    "ga4gh_therap_action": "ga4gh_therap_action",
    "loinc_93044_6": "loinc_93044_6",
    "rarelink_6_1_genetic_findings_complete": "rarelink_6_1_genetic_findings_complete",
}

# Additional processing for Boolean conversion and prefix additions.
ADDITIONAL_PROCESSING = {
    "snomedct_106221001_omim_p": lambda x: add_prefix_to_code(x, "OMIM"),
    "variant_validation": lambda x: {"yes": True, "no": False}.get(x.lower(), None),
    "loinc_53034_5_other": lambda x: add_prefix_to_code(x, "LOINC"),
    "loinc_48019_4_other": lambda x: add_prefix_to_code(x, "LOINC")
}

def map_genetic_findings(entry):
    """
    Maps a flat REDCap entry to the GeneticFindings schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the GeneticFindings schema.
    """
    return map_entry(entry, FIELD_MAPPINGS, ADDITIONAL_PROCESSING)
