# DISEASE_BLOCK = {
#     "redcap_repeat_instrument": "rarelink_5_disease",
#     "term_fields": [
#         "disease.snomed_64572001_mondo",
#         "disease.snomed_64572001_ordo",
#         "disease.snomed_64572001_icd10cm",
#         "disease.snomed_64572001_icd11",
#         "disease.snomed_64572001_omim_p",
#     ],
#     "excluded_field": "disease.loinc_99498_8",
#     "onset_category_field": "disease.snomed_432213005",
#     "onset_date_field": "disease.snomed_424850005",
#     "primary_site_field": "disease.snomed_363698007",
# }



DISEASE_BLOCK = {
    "redcap_repeat_instrument": "rarelink_5_disease",
    "term_field_1": "snomed_64572001_mondo",
    "term_field_2": "snomed_64572001_ordo",
    "term_field_3": "snomed_64572001_icd10cm",
    "term_field_4": "disease.snomed_64572001_icd11",
    "term_field_5": "snomed_64572001_omim_p",
    "excluded_field": "loinc_99498_8",
    "onset_date_field": "snomed_298059007",
    "onset_category_field": "snomed_424850005",
    "primary_site_field": "snomed_363698007",
}

