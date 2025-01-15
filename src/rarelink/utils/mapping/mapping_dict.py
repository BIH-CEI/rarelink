from .map_to_linkml_schema import map_formal_criteria, map_personal_information, map_patient_status, map_care_pathway, map_disease, map_genetic_findings, map_phenotypic_feature, map_measurements, map_family_history, map_consent, map_disability
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
    "disability": map_disability
}