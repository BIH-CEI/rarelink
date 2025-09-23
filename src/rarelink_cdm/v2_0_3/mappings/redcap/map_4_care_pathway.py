"""
Mapping function for the CarePathway schema.

This module defines a function to map flat REDCap data entries to the
CarePathway schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for Boolean conversions and prefix additions.
"""

from rarelink.utils.mapping import map_entry

FIELD_MAPPINGS = {
    "hl7fhir_enc_period_start": "hl7fhir_enc_period_start",
    "hl7fhir_enc_period_end": "hl7fhir_enc_period_end",
    "snomedct_305058001": "snomedct_305058001",
    "hl7fhir_encounter_class": "hl7fhir_encounter_class",
    "rarelink_4_care_pathway_complete": "rarelink_4_care_pathway_complete",
}

def map_care_pathway(entry):
    """
    Maps a flat REDCap entry to the CarePathway schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the CarePathway schema.
    """
    return map_entry(entry, FIELD_MAPPINGS)
