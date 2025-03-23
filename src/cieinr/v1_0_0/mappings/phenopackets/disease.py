# src/cieinr/mappings/phenopackets/disease.py

# Disease block mapping for CIEINR - getting disease from basic_form (non-repeating)
DISEASE_BLOCK = {
    "term_field_1": "basic_form.iei_deficiency_basic", 
    "term_field_2": "basic_form.other_iei_deficiency",
    "term_field_3": "basic_form.non_genetic_iei",
    "term_field_4": "basic_form.non_genetic_iei_mondo",
    "term_field_5": None,
    "onset_date_field": "patient_demographics_initial_form.snomedct_298059007",
    "onset_category_field": None,
    "excluded_field": None,
    "primary_site_field": None
}