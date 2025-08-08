"""
Initialization for REDCap mappings.

This module contains mapping functions for transforming flat REDCap data
into structured JSON format compatible with the RareLink-CDM LinkML schema.

Each mapping function corresponds to a specific schema in the RareLink-CDM.
Mappings are dynamically loaded into `MAPPING_FUNCTIONS` for centralized
usage in data processing pipelines.
"""

from .map_1_formal_criteria import map_formal_criteria
from .map_2_personal_information import map_personal_information
from .map_3_patient_status import map_patient_status
from .map_4_care_pathway import map_care_pathway
from .map_5_disease import map_disease
from .map_6_1_genetic_findings import map_genetic_findings
from .map_6_2_phenotypic_feature import map_phenotypic_feature
from .map_6_3_measurements import map_measurements
from .map_6_4_family_history import map_family_history
from .map_7_consent import map_consent
from .map_8_disability import map_disability
from .reverse_processing import REVERSE_PROCESSING
from .hgvs_variables import (
    HGVS_VARIABLES, 
    REFERENCE_GENOME, 
    REFERENCE_GENOME_MAPPING
)

all = [
    REVERSE_PROCESSING,
    HGVS_VARIABLES,
    REFERENCE_GENOME,
    REFERENCE_GENOME_MAPPING
]

# Centralized mapping registry for REDCap schemas.
# Keys correspond to schema names, values are mapping functions.

MAPPING_FUNCTIONS = {
    "formal_criteria": {
        "mapper": map_formal_criteria,
        "is_repeating": False
    },
    "personal_information": {
        "mapper": map_personal_information,
        "is_repeating": False
    },
    "patient_status": {
        "mapper": map_patient_status,
        "is_repeating": False
    },
    "care_pathway": {
        "mapper": map_care_pathway,
        "is_repeating": True
    },
    "disease": {
        "mapper": map_disease,
        "is_repeating": True
    },
    "genetic_findings": {
        "mapper": map_genetic_findings,
        "is_repeating": True
    },
    "phenotypic_feature": {
        "mapper": map_phenotypic_feature,
        "is_repeating": True
    },
    "measurements": {
        "mapper": map_measurements,
        "is_repeating": True
    },
    "family_history": {
        "mapper": map_family_history,
        "is_repeating": True
    },
    "consent": {
        "mapper": map_consent,
        "is_repeating": False
    },
    "disability": {
        "mapper": map_disability,
        "is_repeating": False
    },
}
