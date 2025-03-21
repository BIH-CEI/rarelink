from typing import Dict, Any
from cieinr.v1_0_0.mappings.phenopackets import (
    DISEASE_BLOCK, 
    INDIVIDUAL_BLOCK, 
    INFECTIONS_FEATURES_BLOCK,
    CONDITIONS_FEATURES_BLOCK,
    PROCEDURE_BLOCK,
    CIEINR_CODE_SYSTEMS,
    INTERPRETATION_BLOCK, 
    VARIATION_DESCRIPTOR_BLOCK,
    mapping_dicts,
    label_dicts
)

def create_phenopacket_mappings() -> Dict[str, Any]:
    """
    Create a comprehensive mapping configuration for CIEINR Phenopacket creation.
    Now supports multiple instruments per mapping block.

    Returns:
        Dict[str, Any]: Combined mapping configurations
    """
    # Process mapping_dicts into a more accessible dictionary
    mapping_dict_lookup = {
        mapping['name']: mapping['mapping'] 
        for mapping in mapping_dicts
    }

    # Create a comprehensive mapping structure
    return {
        "individual": {
            "instrument_name": "patient_demographics_initial_form",
            "mapping_block": INDIVIDUAL_BLOCK,
            "label_dicts": {
                "GenderIdentity": label_dicts.get("GenderIdentity", {})
            },
            "mapping_dicts": {
                "map_sex": mapping_dict_lookup.get("map_sex", {}),
                "map_karyotypic_sex": mapping_dict_lookup.get("map_karyotypic_sex", {})
            },
            "enum_classes": {}
        },
        "diseases": {
            # Using a set for multiple instruments
            "instrument_name": {"basic_form", "patient_demographics_initial_form"},
            "mapping_block": DISEASE_BLOCK,
            "enum_classes": {
                "mondo_": "cieinr.v1_0_0.python_schemas.form_1_basic.IUIS2024MONDOEnum"
            }
        },
        # Use separate configurations for each phenotypic feature type 
        # Instead of using instrument_configs which might not be processed correctly
        "phenotypicFeatures": [
            # Infections config
            {
                "instrument_name": "infections_initial_form",
                "mapping_block": INFECTIONS_FEATURES_BLOCK,
                "data_model": "infections",
                "label_dicts": {
                    "TemporalPattern": label_dicts.get("TemporalPattern", {}),
                    "PhenotypeSeverity": label_dicts.get("PhenotypeSeverity", {})
                },
                "mapping_dicts": {
                    "phenotypic_feature_status": mapping_dict_lookup.get("phenotypic_feature_status", {})
                },
                # Explicit list of type fields to scan
                "type_fields": [
                    "snomedct_61274003",   # Opportunistic infections
                    "snomedct_21483005",   # CNS infections
                    "snomedct_81745001",   # Eye infections
                    "snomedct_385383008",  # ENT infections
                    "snomedct_127856007",  # Skin/soft tissue
                    "snomedct_110522009",  # Bone/joint
                    "snomedct_20139000",   # Respiratory
                    "snomedct_303699009",  # GI
                    "snomedct_21514008",   # GU
                    "snomedct_31099001",   # Systemic
                    "other_infection_hpo",
                    "other_infection_mondo"
                ],
                # Enable multi-onset for infections
                "multi_onset": True,
                # Disable field scanning
                "enable_field_scanning": False,
                # Enum classes
                "enum_classes": {
                    "type_of_infection": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.InfectionTypeEnum",
                    "snomedct_61274003": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.OpportunisticInfectionEnum",
                    "snomedct_21483005": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.CNSInfectionEnum",
                    "snomedct_81745001": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.EyeInfectionEnum",
                    "snomedct_385383008": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.ENTInfectionEnum",
                    "snomedct_127856007": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.SkinInfectionEnum",
                    "snomedct_110522009": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.BoneJointInfectionEnum",
                    "snomedct_20139000": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.RespiratoryInfectionEnum",
                    "snomedct_303699009": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.GIInfectionEnum",
                    "snomedct_21514008": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.GUInfectionEnum",
                    "snomedct_31099001": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.SystemicInfectionEnum",
                    "infection_severity": "cieinr.v1_0_0.python_schemas.form_3_infections_initial.InfectionSeverityEnum",
                }
            },
            # Conditions config
            {
                "instrument_name": "patients_systemic_or_organ_specific_conditions",
                "mapping_block": CONDITIONS_FEATURES_BLOCK,
                "data_model": "conditions",
                "label_dicts": {
                    "TemporalPattern": label_dicts.get("TemporalPattern", {}),
                    "PhenotypeSeverity": label_dicts.get("PhenotypeSeverity", {})
                },
                "mapping_dicts": {
                    "phenotypic_feature_status": mapping_dict_lookup.get("phenotypic_feature_status", {})
                },
                # Explicit list of type fields to scan
                "type_fields": [
                    "snomedct_128477000",  # Systemic condition
                    "snomedct_95320005",   # Allergy
                    "snomedct_118938008",  # Neoplasm
                    "snomedct_50043002",   # Endocrine disorder
                    "snomedct_49601007",   # Cardiovascular disorder
                    "mondo_0005570",       # Autoimmune disorder
                    "snomedct_928000",     # Gastrointestinal disorder
                    "snomedct_119292006",  # Genitourinary disorder
                    "snomedct_362969004",  # Metabolic disorder
                    "snomedct_42030000",   # Renal system disorder
                    "snomedct_55342001",   # Skeletal disorder
                    "snomedct_85828009",   # Trauma
                    "hp_0025142",          # Constitutional symptom
                    "snomedct_5294002",    # Developmental delay
                    "condition_other_hp"
                ],
                # Disable multi-onset for conditions
                "multi_onset": False,
                # Disable field scanning
                "enable_field_scanning": False,
                # Enum classes
                "enum_classes": {
                    "type_of_condition": "cieinr.v1_0_0.python_schemas.form_4_conditions.ConditionTypeEnum"
                }
            }
        ],
        "procedures": {
            "instrument_name": "basic_form",
            "mapping_block": PROCEDURE_BLOCK,
            "label_dicts": {
                "ProcedureType": label_dicts.get("ProcedureType", {})
            },
            "mapping_dicts": {
                "procedure_status": mapping_dict_lookup.get("procedure_status", {})
            },
            "enum_classes": {
                "ncit_c62710": "cieinr.v1_0_0.python_schemas.form_1_basic.IGRTStatusEnumBasicForm",
                "ncit_c15431": "cieinr.v1_0_0.python_schemas.form_1_basic.HCTStatusEnumBasicForm"
            }
        },
        "variationDescriptor": {
            "instrument_name": "genetic_information",
            "mapping_block": VARIATION_DESCRIPTOR_BLOCK,
            "label_dicts": {
                "Zygosity": label_dicts.get("Zygosity", {}),
                "DNAChangeType": label_dicts.get("DNAChangeType", {}),
                "ReferenceGenome": label_dicts.get("ReferenceGenome", {})
            },
            "mapping_dicts": {}
        },
        "interpretations": {
            "instrument_name": "genetic_information",
            "mapping_block": INTERPRETATION_BLOCK,
            "label_dicts": {},
            "mapping_dicts": {
                "map_progress_status": mapping_dict_lookup.get("map_progress_status", {}),
                "map_interpretation_status": mapping_dict_lookup.get("map_interpretation_status", {}),
                "map_acmg_classification": mapping_dict_lookup.get("map_acmg_classification", {}),
                "map_therapeutic_actionability": mapping_dict_lookup.get("map_therapeutic_actionability", {})
            },
            "enum_classes": {
                # Reference the IUIS2024MONDOEnum class by import path
                "mondo_": "cieinr.v1_0_0.python_schemas.form_1_basic.IUIS2024MONDOEnum"
            }
        },
        "metadata": {
            "code_systems": CIEINR_CODE_SYSTEMS
        }
    }
    

def get_mapping_for_block(
    block_name: str, 
    mapping_type: str, 
    key: str, 
    mappings: Dict[str, Any] = None
) -> Dict[str, str]:
    """
    Retrieve a specific mapping or label dictionary from the comprehensive mappings.

    Args:
        block_name (str): Name of the block (e.g., 'individual', 'diseases')
        mapping_type (str): Type of mapping ('label_dicts' or 'mapping_dicts')
        key (str): Specific mapping or label key (e.g., 'map_sex', 'GenderIdentity')
        mappings (Dict[str, Any], optional): Mappings to use. Defaults to CIEINR mappings.

    Returns:
        Dict[str, str]: The requested mapping or label dictionary
    """
    if mappings is None:
        mappings = create_phenopacket_mappings()
    
    block_mappings = mappings.get(block_name, {})
    
    if mapping_type not in block_mappings:
        return {}
    
    return block_mappings[mapping_type].get(key, {})