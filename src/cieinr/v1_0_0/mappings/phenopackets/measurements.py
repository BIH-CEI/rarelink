# CBC Measurement block mapping for CIEINR
CBC_MEASUREMENT_BLOCK = {
    "redcap_repeat_instrument": "cbc",
    "time_observed_field": "cbc_date",
    "multi_measurement": True,
    "measurement_fields": [
        {
            "assay": "cbc_haemoglobin", 
            "value": "cbc_haemoglobin_val", 
            "unit": "cbc_haemoglobin_unit", 
            "interpretation": "cbc_haemoglobin_range", 
            "value_type": "dual"
        },
        {
            "assay": "cbc_platelets", 
            "value": "cbc_platelets_val", 
            "unit": "cbc_platelets_unit", 
            "interpretation": "cbc_platelets_range", 
            "value_type": "dual"
        },
        {
            "assay": "cbc_leukocytes", 
            "value": "cbc_leukocytes_val", 
            "unit": "cbc_leukocytes_unit", 
            "interpretation": "cbc_leukocytes_range", 
            "value_type": "dual"
        },
        {
            "assay": "cbc_neutrophils", 
            "value": "cbc_neutrophils_val", 
            "unit": "cbc_neutrophils_unit", 
            "interpretation": "cbc_neutrophils_range", 
            "value_type": "dual"
        },
        {
            "assay": "cbc_eosinophils", 
            "value": "cbc_eosinophils_val", 
            "unit": "cbc_eosinophils_unit", 
            "interpretation": "cbc_eosinophils_range", 
            "value_type": "dual"
        },
        {
            "assay": "cbc_lymphocytes", 
            "value": "cbc_lymphocytes_val", 
            "unit": "cbc_lymphocytes_unit", 
            "interpretation": "cbc_lymphocytes_range", 
            "value_type": "dual"
        },
        {
            "assay": "cbc_monocytes", 
            "value": "cbc_monocytes_val", 
            "unit": "cbc_monocytes_unit", 
            "interpretation": "cbc_monocytes_range", 
            "value_type": "dual"
        }
    ]
}

# Lymphocytes Phenotype Measurement block mapping
LYMPHOCYTES_PHENOTYPE_BLOCK = {
    "redcap_repeat_instrument": "lymphocytes_phenotype",
    "time_observed_field": "lympheno_test_date",
    "multi_measurement": True,
    "measurement_fields": [
        {
            "assay": "lympheno_loinc_8122_4",             # Base field contains the LOINC code
            "interpretation": "lympheno_loinc_8122_4_int", # Interpretation field (preferred)
            "value": "lympheno_loinc_8122_4_val",         # Numeric value field (fallback) 
            "unit": "lympheno_loinc_8122_4_unit",         # Primary unit field
            "unit_alt": "lympheno_loinc_8122_4_unito",    # Alternative unit field
            "value_type": "dual"                          # Can be either ontology or quantity
        },
        {
            "assay": "lympheno_loinc_24467_3",
            "interpretation": "lympheno_loinc_24467_3_int",
            "value": "lympheno_loinc_24467_3_val", 
            "unit": "lympheno_loinc_24467_3_unit",
            "unit_alt": "lympheno_loinc_24467_3_unito",
            "value_type": "dual"
        },
        {
            "assay": "lympheno_loinc_14135_8",
            "interpretation": "lympheno_loinc_14135_8_int",
            "value": "lympheno_loinc_14135_8_val", 
            "unit": "lympheno_loinc_14135_8_unit",
            "unit_alt": "lympheno_loinc_14135_8_unito",
            "value_type": "dual"
        },
        {
            "assay": "lympheno_loinc_8116_6",
            "interpretation": "lympheno_loinc_8116_6_int",
            "value": "lympheno_loinc_8116_6_val", 
            "unit": "lympheno_loinc_8116_6_unit",
            "unit_alt": "lympheno_loinc_8116_6_unito",
            "value_type": "dual"
        },
        {
            "assay": "lympheno_loinc_9558_8",
            "interpretation": "lympheno_loinc_9558_8_int",
            "value": "lympheno_loinc_9558_8_val", 
            "unit": "lympheno_loinc_9558_8_unit",
            "unit_alt": "lympheno_loinc_9558_8_unito",
            "value_type": "dual"
        },
        {
            "assay": "lympheno_loinc_9728_7",
            "interpretation": "lympheno_loinc_9728_7_int",
            "value": "lympheno_loinc_9728_7_val", 
            "unit": "lympheno_loinc_9728_7_unit",
            "unit_alt": "lympheno_loinc_9728_7_unito",
            "value_type": "dual"
        }
    ]
}

# Lymphocyte Function Measurement block mapping
LYMPHOCYTE_FUNCTION_BLOCK = {
    "redcap_repeat_instrument": "lymphocyte_functionnk_cytotoxicity",
    "time_observed_field": "lymphfunc_date",
    "multi_measurement": True,
    "measurement_fields": [
        {
            "assay": "lymphfunc_ncit_c88791", 
            "value": "lymphfunc_ncit_c88791_val",
            "value_type": "ontology"
        },
        {
            "assay": "lymphfunc_ncit_c74017", 
            "value": "lymphfunc_ncit_c74017_val",
            "value_type": "ontology"
        },
        {
            "assay": "lymphfunc_ncit_c88774", 
            "value": "lymphfunc_ncit_c88774_val",
            "value_type": "ontology"
        },
        {
            "assay": "lymphfunc_ncit_c88789", 
            "value": "lymphfunc_ncit_c88789_val",
            "value_type": "ontology"
        },
        {
            "assay": "lymphfunc_ncit_c17166", 
            "value": "lymphfunc_ncit_c17166_val",
            "value_type": "ontology"
        },
        {
            "assay": "lymphfunc_ncit_c85185", 
            "value": "lymphfunc_ncit_c85185_val",
            "value_type": "ontology"
        },
        {
            "assay": "lymphfunc_ncit_c34541", 
            "value": "lymphfunc_ncit_c34541_val",
            "value_type": "ontology"
        },
        {
            "assay": "lymphfunc_ncit_c77163", 
            "value": "lymphfunc_ncit_c77163_val",
            "value_type": "ontology"
        },
        {
            "assay": "lymphfunc_ncit_c116203", 
            "value": "lymphfunc_ncit_c116203_val",
            "value_type": "ontology"
        }
    ]
}