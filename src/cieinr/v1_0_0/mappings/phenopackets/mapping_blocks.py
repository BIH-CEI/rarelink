"""
Mapping blocks for the CIEINR v1.0.0 data model.

These mappings define how fields in the CIEINR data model map to fields
required for phenopacket construction. These mappings leverage RareLink's 
data processing capabilities while adding CIEINR-specific fields.
"""

from typing import Dict, Any

# Individual block mapping
INDIVIDUAL_BLOCK = {
    "id_field": "record_id",
    "date_of_birth_field": "patient_demographics_initial_form.snomedct_184099003",
    "time_at_last_encounter_field": "patient_demographics_initial_form.visit_date_demographics",
    "sex_field": None,  # Will default to UNKNOWN_SEX in RareLink's mapper
    "karyotypic_sex_field": None,  # Will default to UNKNOWN_KARYOTYPE
    "gender_field": None  # Will default to None
}

# Vital status block mapping
VITAL_STATUS_BLOCK = {
    "status_field": "_default_",  # Special marker for default value
    "time_of_death_field": None,
    "cause_of_death_field": None,
    "default_status": "UNKNOWN_STATUS"  # Explicitly set default
}

# Disease block mapping - designed to work with non-repeated elements
DISEASE_BLOCK = {
    "term_field_1": "basic_form.iei_deficiency_basic", 
    "term_field_2": "basic_form.other_iei_deficiency",
    "term_field_3": None,
    "term_field_4": None,
    "term_field_5": None,
    "onset_date_field": None,
    "onset_category_field": None,
    "excluded_field": None,
    "primary_site_field": None
}

# Phenotypic features block mapping
PHENOTYPIC_FEATURES_BLOCK = {
    "redcap_repeat_instrument": "infections_initial_form",
    "type_field": "type_of_infection",
    "onset_field": None,  
    "resolution_field": None,
    "severity_field": "infection_severity",
    "spatial_pattern_field": None,
    "temporal_pattern_field": "infection_times_obseverd",
    "laterality_field": None,
    "evidence_code_field": None,
    "excluded_field": None,
    "modifiers_field": None,
}

# Mapping dictionaries for code conversions
MAPPING_DICTS = [
    {
        "name": "map_sex",
        "mapping": {
            "snomedct_248152002": "FEMALE",
            "snomedct_248153007": "MALE",
            "snomedct_32570691000036108": "OTHER_SEX",
            "": "UNKNOWN_SEX"
        },
    },
    {
        "name": "map_vital_status",
        "mapping": {
            "snomedct_438949009": "ALIVE",
            "snomedct_419099009": "DECEASED",
            "snomedct_185924006": "UNKNOWN_STATUS",
            "": "UNKNOWN_STATUS"
        },
    },
    {
        "name": "map_clinical_status",
        "mapping": {
            "active": "ACTIVE",
            "recurrence": "RECURRENCE",
            "remission": "REMISSION",
            "resolved": "RESOLVED",
            "": "UNKNOWN_STATUS"
        }
    },
    {
        "name": "map_mondo_codes",
        "mapping": {
            # Our mapping will use LinkML enum labels by default,
            # but this could be used for special cases
        }
    },
    {
        "name": "map_disease_verification_status",
        "mapping": {
            # Not used in the current model, but kept for compatibility
            "verified": "false",
            "unverified": "true",
            "": "false"
        }
    },
    {
        "name": "map_infection_severity",
        "mapping": {
            # Will use LinkML enum labels by default
        }
    },
    {
        "name": "map_infection_temporal_pattern",
        "mapping": {
            # Will use LinkML enum labels by default
        }
    }
]

def get_mapping_by_name(name: str, to_boolean: bool = False) -> Dict[str, Any]:
    """
    Get a mapping dictionary by name.
    
    Args:
        name: Name of the mapping to retrieve
        to_boolean: Whether to convert string values "true"/"false" to boolean
        
    Returns:
        Dictionary with the mapping
        
    Raises:
        KeyError: If no mapping with the given name exists
    """
    for mapping_dict in MAPPING_DICTS:
        if mapping_dict["name"] == name:
            mapping = mapping_dict["mapping"]
            if to_boolean:
                return {key: value.lower() == "true" for key, value in mapping.items()}
            return mapping
    raise KeyError(f"No mapping found for name: {name}")