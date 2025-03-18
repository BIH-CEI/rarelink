# src/cieinr/mappings/phenopackets/disease.py

# Disease block mapping for CIEINR - getting disease from basic_form (non-repeating)
DISEASE_BLOCK = {
    "term_field_1": "basic_form.iei_deficiency_basic", 
    "term_field_2": "basic_form.other_iei_deficiency",
    "term_field_3": "non_genetic_iei",
    "term_field_4": "non_genetic_iei_mondo",
    "term_field_5": None,
    "onset_date_field": None,
    "onset_category_field": None,
    "excluded_field": None,
    "primary_site_field": None
}