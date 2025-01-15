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

# Centralized mapping registry for REDCap schemas.
# Keys correspond to schema names, values are mapping functions.
MAPPING_FUNCTIONS = {
    "formal_criteria": map_formal_criteria,
    "personal_information": map_personal_information,
    "patient_status": map_patient_status,
    "care_pathway": map_care_pathway,
    "disease": map_disease,
    "genetic_findings": map_genetic_findings,
    "phenotypic_feature": map_phenotypic_feature,
    "measurements": map_measurements,
    "family_history": map_family_history,
    "consent": map_consent,
    "disability": map_disability,
}
