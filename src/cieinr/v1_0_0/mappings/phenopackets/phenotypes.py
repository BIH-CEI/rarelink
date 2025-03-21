# In src/cieinr/v1_0_0/mappings/phenopackets/phenotypes.py

PHENOTYPIC_FEATURES_BLOCK = {
    # Both instruments need to be supported in the default block
    "redcap_repeat_instrument": None,  # Will be overridden by processing logic
    
    # Essential type fields that explicitly map to condition/disease/phenotype concepts
    # These should be the ONLY fields that generate phenotypic features
    
    # Infections form type fields (with explicit prefixes for clarity)
    "type_field": "infections_initial_form.snomedct_61274003",
    "type_field_2": "infections_initial_form.snomedct_21483005",
    "type_field_3": "infections_initial_form.snomedct_81745001",
    "type_field_4": "infections_initial_form.snomedct_385383008",
    "type_field_5": "infections_initial_form.snomedct_127856007",
    "type_field_6": "infections_initial_form.snomedct_110522009",
    "type_field_7": "infections_initial_form.snomedct_20139000",
    "type_field_8": "infections_initial_form.snomedct_303699009",
    "type_field_9": "infections_initial_form.snomedct_21514008",
    "type_field_10": "infections_initial_form.snomedct_31099001",
    "type_field_11": "infections_initial_form.other_infection_hpo",
    "type_field_12": "infections_initial_form.other_infection_mondo",
    
    # Conditions form type fields (to be used when processing that form)
    "type_field_20": "patients_systemic_or_organ_specific_conditions.snomedct_128477000",
    "type_field_21": "patients_systemic_or_organ_specific_conditions.snomedct_95320005",
    "type_field_22": "patients_systemic_or_organ_specific_conditions.snomedct_118938008",
    "type_field_23": "patients_systemic_or_organ_specific_conditions.snomedct_50043002",
    "type_field_24": "patients_systemic_or_organ_specific_conditions.snomedct_49601007",
    "type_field_25": "patients_systemic_or_organ_specific_conditions.mondo_0005570",
    "type_field_26": "patients_systemic_or_organ_specific_conditions.snomedct_928000",
    "type_field_27": "patients_systemic_or_organ_specific_conditions.snomedct_119292006",
    "type_field_28": "patients_systemic_or_organ_specific_conditions.snomedct_362969004",
    "type_field_29": "patients_systemic_or_organ_specific_conditions.snomedct_42030000",
    "type_field_30": "patients_systemic_or_organ_specific_conditions.condition_other_hp",
    
    # Modifier fields - these should NOT generate phenotypic features themselves
    "excluded_field": None,
    "onset_date_fields": ["infection_date", "infection_date_2", "infection_date_3"],
    "resolution_field": None,
    "severity_field": "infection_severity",
    "modifier_field_1": "type_of_infection",
    "modifier_field_2": "infection_temp_pattern",
    
    # Flag to disable fallback field scanning to prevent picking up non-type fields
    "enable_field_scanning": False,
    
    # Multi-onset support
    "multi_onset": True
}

INFECTIONS_FEATURES_BLOCK = {
    "redcap_repeat_instrument": "infections_initial_form",
    # Type fields for various infection types
    "type_field": "infections_initial_form.snomedct_61274003",
    "type_field_2": "infections_initial_form.snomedct_21483005",
    "type_field_3": "infections_initial_form.snomedct_81745001",
    "type_field_4": "infections_initial_form.snomedct_385383008",
    "type_field_5": "infections_initial_form.snomedct_127856007",
    "type_field_6": "infections_initial_form.snomedct_110522009",
    "type_field_7": "infections_initial_form.snomedct_20139000",
    "type_field_8": "infections_initial_form.snomedct_303699009",
    "type_field_9": "infections_initial_form.snomedct_21514008",
    "type_field_10": "infections_initial_form.snomedct_31099001",
    "type_field_11": "infections_initial_form.other_infection_hpo",
    "type_field_12": "infections_initial_form.other_infection_mondo",
    # Onset date fields
    "onset_date_fields": [
        "infections_initial_form.infection_date", 
        "infections_initial_form.infection_date_2", 
        "infections_initial_form.infection_date_3", 
        "infections_initial_form.infection_date_4", 
        "infections_initial_form.infection_date_5", 
        "infections_initial_form.infection_date_6", 
        "infections_initial_form.infection_date_7", 
        "infections_initial_form.infection_date_8", 
        "infections_initial_form.infection_date_9", 
        "infections_initial_form.infection_date_10"
    ],
    # Severity and modifiers
    "severity_field": "infections_initial_form.infection_severity",
    "modifier_field_1": "infections_initial_form.type_of_infection",
    "modifier_field_2": "infections_initial_form.infection_temp_pattern",
    "modifier_field_4": "infections_initial_form.causing_agent_viral",
    "modifier_field_5": "infections_initial_form.causing_agent_bacterial",
    "modifier_field_6": "infections_initial_form.causing_agent_mycotic",
    "modifier_field_7": "infections_initial_form.causing_organism_other",
    # Multi-onset support
    "multi_onset": True,
    # Data model type
    "data_model": "infections"
}

CONDITIONS_FEATURES_BLOCK = {
    "redcap_repeat_instrument": "patients_systemic_or_organ_specific_conditions",
    # Type fields for various condition types
    "type_field": "patients_systemic_or_organ_specific_conditions.snomedct_128477000",
    "type_field_1": "patients_systemic_or_organ_specific_conditions.snomedct_95320005",
    "type_field_2": "patients_systemic_or_organ_specific_conditions.snomedct_118938008",
    "type_field_3": "patients_systemic_or_organ_specific_conditions.snomedct_50043002",
    "type_field_4": "patients_systemic_or_organ_specific_conditions.snomedct_49601007",
    "type_field_5": "patients_systemic_or_organ_specific_conditions.mondo_0005570",
    "type_field_6": "patients_systemic_or_organ_specific_conditions.snomedct_928000",
    "type_field_7": "patients_systemic_or_organ_specific_conditions.snomedct_119292006",
    "type_field_8": "patients_systemic_or_organ_specific_conditions.snomedct_362969004",
    "type_field_9": "patients_systemic_or_organ_specific_conditions.snomedct_42030000",
    "type_field_10": "patients_systemic_or_organ_specific_conditions.snomedct_55342001",
    "type_field_11": "patients_systemic_or_organ_specific_conditions.snomedct_85828009",
    "type_field_12": "patients_systemic_or_organ_specific_conditions.hp_0025142",
    "type_field_13": "patients_systemic_or_organ_specific_conditions.snomedct_5294002",
    "type_field_14": "patients_systemic_or_organ_specific_conditions.condition_other_hp",
    # Onset and severity fields
    "onset_date_field": "patients_systemic_or_organ_specific_conditions.condition_date_1",
    "severity_field": "patients_systemic_or_organ_specific_conditions.condition_severity",
    # Modifier fields
    "modifier_field_1": "patients_systemic_or_organ_specific_conditions.type_of_condition",
    "modifier_field_2": "patients_systemic_or_organ_specific_conditions.hp_0012539_modifier",
    "modifier_field_3": "patients_systemic_or_organ_specific_conditions.hp_0012189_modifier",
    "modifier_field_4": "patients_systemic_or_organ_specific_conditions.hp_0005523_modifier",
    "modifier_field_5": "patients_systemic_or_organ_specific_conditions.condition_temp_pattern",
    # Evidence field
    "evidence_field": "patients_systemic_or_organ_specific_conditions.mondo_0005265_evidence",
    # Data model type
    "data_model": "conditions"
}