# src/cieinr/mappings/phenopackets/individual.py

# Individual block mapping for CIEINR
INDIVIDUAL_BLOCK = {
    "id_field": "record_id",
    "date_of_birth_field": "patient_demographics_initial_form.snomedct_184099003",
    "time_at_last_encounter_field": "patient_demographics_initial_form.visit_date_demographics",
    "sex_field": None,  # Will default to UNKNOWN_SEX in mapper
    "karyotypic_sex_field": None,  # Will default to UNKNOWN_KARYOTYPE
    "gender_field": None  # Will default to None
}
