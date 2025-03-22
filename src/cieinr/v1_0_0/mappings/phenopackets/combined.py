from typing import Dict, Any
from cieinr.v1_0_0.mappings.phenopackets import (
    DISEASE_BLOCK, 
    INDIVIDUAL_BLOCK, 
    INFECTIONS_FEATURES_BLOCK,
    CONDITIONS_FEATURES_BLOCK,
    BASIC_PROCEDURE_BLOCK,
    INACTIVATE_VACCINE_BLOCK,
    LIVE_VACCINE_BLOCK,
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
            "instrument_name": {"basic_form", "patient_demographics_initial_form"},
            "mapping_block": DISEASE_BLOCK,
            "enum_classes": {
                "mondo_": "cieinr.v1_0_0.python_schemas.form_1_basic.IUIS2024MONDOEnum"
            }
        },
        # separate configurations for each phenotypic feature type: Infections & Conditions
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
                # Disable multi-onset for conditions
                "multi_onset": False,
                # Disable field scanning
                "enable_field_scanning": False,
                # Enum classes
                "enum_classes": {
                    "type_of_condition": "cieinr.v1_0_0.python_schemas.form_4_conditions.ConditionTypeEnum",
                    "snomedct_95320005": "cieinr.v1_0_0.python_schemas.form_4_conditions.SkinConditionEnum",
                    "snomedct_118938008": "cieinr.v1_0_0.python_schemas.form_4_conditions.DentalConditionEnum",
                    "snomedct_50043002": "cieinr.v1_0_0.python_schemas.form_4_conditions.SinoPulmonaryConditionEnum",
                    "snomedct_49601007": "cieinr.v1_0_0.python_schemas.form_4_conditions.CardiovascularConditionEnum",
                    "mondo_0005570": "cieinr.v1_0_0.python_schemas.form_4_conditions.HematologicLymphoidConditionEnum",
                    "snomedct_928000": "cieinr.v1_0_0.python_schemas.form_4_conditions.MusculoskeletalConditionEnum",
                    "snomedct_119292006": "cieinr.v1_0_0.python_schemas.form_4_conditions.GastrointestinalConditionEnum",
                    "mondo_0005265_evidence": "cieinr.v1_0_0.python_schemas.form_4_conditions.IBDEvidenceEnum",
                    "snomedct_362969004": "cieinr.v1_0_0.python_schemas.form_4_conditions.EndocrineMetabolicConditionEnum",
                    "snomedct_42030000": "cieinr.v1_0_0.python_schemas.form_4_conditions.GenitourinaryConditionEnum",
                    "snomedct_55342001": "cieinr.v1_0_0.python_schemas.form_4_conditions.NeoplasticConditionEnum",
                    "snomedct_85828009": "cieinr.v1_0_0.python_schemas.form_4_conditions.AutoimmuneConditionEnum",
                    "hp_0025142": "cieinr.v1_0_0.python_schemas.form_4_conditions.ConstitutionalConditionEnum",
                    "snomedct_5294002": "cieinr.v1_0_0.python_schemas.form_4_conditions.GrowthDevelopmentConditionEnum",
                    "modifier_field_3": "cieinr.v1_0_0.python_schemas.form_4_conditions.EBVStatusEnum",
                    "modifier_field_4": "cieinr.v1_0_0.python_schemas.form_4_conditions.EBVStatusEnum",
                    "modifier_field_5": "cieinr.v1_0_0.python_schemas.form_4_conditions.EBVStatusEnum"
                }
                
            }
        ],
        "procedures": {
                "instrument_name": "basic_form",
                "mapping_block": BASIC_PROCEDURE_BLOCK,
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
        "treatments": [
            {
                "instrument_name": "inactivated_vaccine_history_and_specific_immune_re", 
                "mapping_block": INACTIVATE_VACCINE_BLOCK,
                "enum_classes": 
                    {
                        "vo_": "cieinr.v1_0_0.python_schemas.form_6_inactivated_vaccines.InactivatedVaccineTypeEnum"
                    }
            },
            {
                "instrument_name": "live_vaccine_and_specific_immune_response",
                "mapping_block": LIVE_VACCINE_BLOCK,
                "enum_classes": 
                    {
                        "vo_": "cieinr.v1_0_0.python_schemas.form_7_live_vaccines.LiveVaccineTypeEnum"
                    }
            }       
        ],
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