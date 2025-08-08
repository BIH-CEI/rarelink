"""
Mapping function for the PhenotypicFeature schema.

This module defines a function to map flat REDCap data entries to the
PhenotypicFeature schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for prefix additions.
"""

from rarelink.utils.mapping import map_entry
from rarelink.utils.code_processing import add_prefix_to_code

# Define mappings from REDCap fields to schema fields.
FIELD_MAPPINGS = {
    "snomedct_8116006": "snomedct_8116006",
    "snomedct_363778006": "snomedct_363778006",
    "snomedct_8116006_onset": "snomedct_8116006_onset",
    "snomedct_8116006_resolut": "snomedct_8116006_resolut",
    "hp_0003674": "hp_0003674",
    "hp_0011008": "hp_0011008",
    "hp_0012824": "hp_0012824",
    "hp_0012823_hp1": "hp_0012823_hp1",
    "hp_0012823_hp2": "hp_0012823_hp2",
    "hp_0012823_hp3": "hp_0012823_hp3",
    "hp_0012823_ncbitaxon": "hp_0012823_ncbitaxon",
    "hp_0012823_snomedct": "hp_0012823_snomedct",
    "phenotypicfeature_evidence": "phenotypicfeature_evidence",
    "rarelink_6_2_phenotypic_feature_complete": "rarelink_6_2_phenotypic_feature_complete",
}

# Additional processing for prefix additions.
ADDITIONAL_PROCESSING = {
    "hp_0012823_ncbitaxon": lambda x: add_prefix_to_code(x, "NCBITAXON"),
    "hp_0012823_snomedct": lambda x: add_prefix_to_code(x, "SNOMEDCT"),
}

def map_phenotypic_feature(entry):
    """
    Maps a flat REDCap entry to the PhenotypicFeature schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the PhenotypicFeature schema.
    """
    return map_entry(entry, FIELD_MAPPINGS, ADDITIONAL_PROCESSING)
