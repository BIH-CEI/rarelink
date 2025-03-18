# Individual block mapping
INDIVIDUAL_BLOCK = {
    "id_field": "record_id",
    "date_of_birth_field": "patient_demographics_initial_form.snomedct_184099003",
    "time_at_last_encounter_field": "patient_demographics_initial_form.visit_date_demographics",
    "sex_field": None,  # Will default to UNKNOWN_SEX in RareLink's mapper
    "karyotypic_sex_field": None,  # Will default to UNKNOWN_KARYOTYPE
    "gender_field": None  # Will default to None
}

VITAL_STATUS_BLOCK = {
    "status_field": "_default_",  # Special marker for default value
    "time_of_death_field": None,
    "cause_of_death_field": None,
    "default_status": "UNKNOWN_STATUS"  # Explicitly set default
}

