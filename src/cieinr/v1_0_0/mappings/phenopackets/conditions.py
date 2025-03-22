# In src/cieinr/v1_0_0/mappings/phenopackets/phenotypes.py

PHENOTYPIC_FEATURES_BLOCK = {
    # Default block configuration with no specific instrument
    "redcap_repeat_instrument": None,  # Will be overridden by processing logic
    
    # Enable field scanning based on explicit fields only
    "enable_field_scanning": False,
    
    # Common fields for onset/resolution/severity
    "onset_date_field": None,  # Set per instrument
    "resolution_field": None,
    "severity_field": None,
    
    # Multi-onset support (will be configured per instrument)
    "multi_onset": False
}

INFECTIONS_FEATURES_BLOCK = {
    "redcap_repeat_instrument": "infections_initial_form",
    "data_model": "infections",
    
    # Type fields for infections
    "type_field": "snomedct_61274003",   # Opportunistic infections
    "type_field_2": "snomedct_21483005", # CNS infections
    "type_field_3": "snomedct_81745001", # Eye infections
    "type_field_4": "snomedct_385383008", # ENT infections
    "type_field_5": "snomedct_127856007", # Skin/soft tissue
    "type_field_6": "snomedct_110522009", # Bone/joint
    "type_field_7": "snomedct_20139000",  # Respiratory
    "type_field_8": "snomedct_303699009", # GI
    "type_field_9": "snomedct_21514008",  # GU
    "type_field_10": "snomedct_31099001", # Systemic
    "type_field_11": "other_infection_hpo",
    "type_field_12": "other_infection_mondo",
    
    # Onset date fields
    "onset_date_fields": [
        "infection_date", 
        "infection_date_2", 
        "infection_date_3", 
        "infection_date_4", 
        "infection_date_5", 
        "infection_date_6", 
        "infection_date_7", 
        "infection_date_8", 
        "infection_date_9", 
        "infection_date_10"
    ],
    
    # Severity and modifiers
    "severity_field": "infection_severity",
    "modifier_field_1": "type_of_infection",
    "modifier_field_2": "infection_temp_pattern",
    "modifier_field_3": "causing_agent_viral",
    "modifier_field_4": "causing_agent_bacterial",
    "modifier_field_5": "causing_agent_mycotic",
    "modifier_field_6": "causing_organism_other",
    
    # Enable multi-onset for infections
    "multi_onset": True,
    
    # Disable general field scanning to rely on explicit fields only
    "enable_field_scanning": False
}

CONDITIONS_FEATURES_BLOCK = {
    "redcap_repeat_instrument": "patients_systemic_or_organ_specific_conditions",
    "data_model": "conditions",
    
    # Type fields for conditions
    "type_field": "snomedct_128477000",   # Systemic condition
    "type_field_2": "snomedct_95320005",  # Allergy
    "type_field_3": "snomedct_118938008", # Neoplasm
    "type_field_4": "snomedct_50043002",  # Endocrine disorder
    "type_field_5": "snomedct_49601007",  # Cardiovascular disorder
    "type_field_6": "mondo_0005570",      # Autoimmune disorder
    "type_field_7": "snomedct_928000",    # Gastrointestinal disorder
    "type_field_8": "snomedct_119292006", # Genitourinary disorder
    "type_field_9": "snomedct_362969004", # Metabolic disorder
    "type_field_10": "snomedct_42030000", # Renal system disorder
    "type_field_11": "snomedct_55342001", # Skeletal disorder
    "type_field_12": "snomedct_85828009", # Trauma
    "type_field_13": "hp_0025142",        # Constitutional symptom
    "type_field_14": "snomedct_5294002",  # Developmental delay
    "type_field_15": "condition_other_hp",
    
    # Onset and severity fields
    "onset_date_field": "condition_date_1",
    "severity_field": "condition_severity",
    
    # Modifier fields
    "modifier_field_1": "type_of_condition",
    "modifier_field_2": "hp_0012539_modifier",
    "modifier_field_3": "hp_0012189_modifier",
    "modifier_field_4": "hp_0005523_modifier",
    "modifier_field_5": "condition_temp_pattern",
    
    # Evidence field
    "evidence_field": "mondo_0005265_evidence",
    
    # No multi-onset for conditions
    "multi_onset": False,
    
    # Disable general field scanning
    "enable_field_scanning": False
}
                # "type_of_condition": "cieinr.v1_0_0.python_schemas.form_4_conditions.ConditionTypeEnum",
                # "snomedct_95320005": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_118938008": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_50043002": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_49601007": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "mondo_0005570": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_928000": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_119292006": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "mondo_0005265_evidence": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_362969004": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_42030000": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_55342001": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_85828009": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "hp_0025142": "cieinr.v1_0_0.python_schemas.form_4_conditions.",
                # "snomedct_5294002": "cieinr.v1_0_0.python_schemas.form_4_conditions."
        #     }