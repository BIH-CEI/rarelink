"""
Mapping function for the Consent schema.

This module defines a function to map flat REDCap data entries to the
Consent schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined without additional processing.
"""

from rarelink.utils.mapping import map_entry

# Define mappings from REDCap fields to schema fields.
FIELD_MAPPINGS = {
    "snomedct_309370004": "snomedct_309370004",
    "hl7fhir_consent_datetime": "hl7fhir_consent_datetime",
    "snomedct_386318002": "snomedct_386318002",
    "rarelink_consent_contact": "rarelink_consent_contact",
    "rarelink_consent_data": "rarelink_consent_data",
    "snomedct_123038009": "snomedct_123038009",
    "rarelink_biobank_link": "rarelink_biobank_link",
    "rarelink_7_consent_complete": "rarelink_7_consent_complete",
}

def map_consent(entry):
    """
    Maps a flat REDCap entry to the Consent schema.

    Args:
        entry (dict): A single REDCap record as a dictionary.

    Returns:
        dict: Mapped data conforming to the Consent schema.
    """
    return map_entry(entry, FIELD_MAPPINGS)
