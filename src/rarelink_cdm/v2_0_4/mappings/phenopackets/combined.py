from typing import Dict, Any

# Import mapping blocks and code systems
from rarelink_cdm.v2_0_4.mappings.phenopackets import (
    INDIVIDUAL_BLOCK,
    VITAL_STATUS_BLOCK,
    DISEASE_BLOCK,
    INTERPRETATION_BLOCK,
    VARIATION_DESCRIPTOR_BLOCK,
    PHENOTYPIC_FEATURES_BLOCK,
    MEASUREMENT_BLOCK,
    RARELINK_CODE_SYSTEMS,
    mapping_dicts,
    label_dicts
)

def create_rarelink_phenopacket_mappings() -> Dict[str, Any]:
    """
    Create a comprehensive mapping configuration for Phenopacket creation.
    Enhanced to support flexible configuration formats.

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
            "instrument_name": "rarelink_personal_information",
            "mapping_block": INDIVIDUAL_BLOCK,
            "mapping_dicts": {
                "map_sex": mapping_dict_lookup.get("map_sex", {}),
                "map_karyotypic_sex": mapping_dict_lookup.get("map_karyotypic_sex", {})
            },
            "enum_classes": {
                "SexAtBirth": "rarelink_cdm.v2_0_4.python_datamodel.SexAtBirth",
                "GenderIdentity": "rarelink_cdm.v2_0_4.python_datamodel.GenderIdentity",
                "KaryotypicSex": "rarelink_cdm.v2_0_4.python_datamodel.KaryotypicSex"
            }
        },
        "vitalStatus": {
            "instrument_name": "rarelink_3_patient_status",
            "mapping_block": VITAL_STATUS_BLOCK,
            "mapping_dicts": {
                "map_vital_status": mapping_dict_lookup.get("map_vital_status", {})
            }
        },
        "diseases": {
            "instrument_name": "rarelink_5_disease",
            "mapping_block": DISEASE_BLOCK,
            "mapping_dicts": {
                "map_disease_verification_status": mapping_dict_lookup.get("map_disease_verification_status", {})
            },
            "enum_classes": {
                "AgeAtDiagnosis": "rarelink_cdm.v2_0_4.python_datamodel.AgeAtDiagnosis",
                "AgeAtOnset": "rarelink_cdm.v2_0_4.python_datamodel.AgeAtOnset",
            }
        },
        # Standard single configuration for phenotypic features 
        # (can be processed by both the original and enhanced pipeline)
        "phenotypicFeatures": {
            "instrument_name": "rarelink_6_2_phenotypic_feature",
            "mapping_block": PHENOTYPIC_FEATURES_BLOCK,
            "mapping_dicts": {
                "phenotypic_feature_status": mapping_dict_lookup.get("phenotypic_feature_status", {})
            },
            "enum_classes": {
                "TemporalPattern": "rarelink_cdm.v2_0_4.python_datamodel.TemporalPattern",
                "AgeOfOnset": "rarelink_cdm.v2_0_4.python_datamodel.AgeOfOnset",
                "PhenotypeSeverity": "rarelink_cdm.v2_0_4.python_datamodel.PhenotypeSeverity"
            }
        },
        "measurements": {
            "instrument_name": "rarelink_6_3_measurements",
            "mapping_block": MEASUREMENT_BLOCK,
            "label_dicts": {},
            "mapping_dicts": {}
        },
        "variationDescriptor": {
            "instrument_name": "rarelink_6_1_genetic_findings",
            "mapping_block": VARIATION_DESCRIPTOR_BLOCK,
            "label_dicts": {
                "Zygosity": label_dicts.get("Zygosity", {}),
                "DNAChangeType": label_dicts.get("DNAChangeType", {}),
                "ReferenceGenome": label_dicts.get("ReferenceGenome", {})
            },
            "mapping_dicts": {}
        },
        "interpretations": {
            "instrument_name": "rarelink_6_1_genetic_findings",
            "mapping_block": INTERPRETATION_BLOCK,
            "label_dicts": {},
            "enum_classes": {
                "InterpretationProgressStatus": "rarelink_cdm.v2_0_4.python_datamodel.InterpretationProgressStatus",
                "InterpretationStatus": "rarelink_cdm.v2_0_4.python_datamodel.InterpretationStatus",
                "StructuralVariantMethod": "rarelink_cdm.v2_0_4.python_datamodel.StructuralVariantMethod",
                "ReferenceGenome": "rarelink_cdm.v2_0_4.python_datamodel.ReferenceGenome",
                "VariantExpressionType": "rarelink_cdm.v2_0_4.python_datamodel.VariantExpressionType",
                "Zygosity": "rarelink_cdm.v2_0_4.python_datamodel.Zygosity",
                "GenomicSourceClass": "rarelink_cdm.v2_0_4.python_datamodel.GenomicSourceClass",
                "DNAChangeType": "rarelink_cdm.v2_0_4.python_datamodel.DNAChangeType",
                "ClinicalSignificance": "rarelink_cdm.v2_0_4.python_datamodel.ClinicalSignificance",
                "TherapeuticActionability": "rarelink_cdm.v2_0_4.python_datamodel.TherapeuticActionability",
                "LevelOfEvidence": "rarelink_cdm.v2_0_4.python_datamodel.LevelOfEvidence"
            }
        },
        "metadata": {
            "code_systems": RARELINK_CODE_SYSTEMS
        }
    }

def create_phenopacket_mappings_for_model(model_name: str, 
                                        config_builder_func=None,
                                        **kwargs) -> Dict[str, Any]:
    """
    Generic function to create phenopacket mappings for any data model.
    
    Args:
        model_name (str): Name of the data model (e.g., 'rarelink_cdm', 'cieinr')
        config_builder_func (callable, optional): Function to build model-specific configurations
        **kwargs: Additional keyword arguments for the config builder
        
    Returns:
        Dict[str, Any]: Complete mapping configuration for the model
    """
    # Default to standard RareLink CDM mappings
    if model_name == "rarelink_cdm" or not config_builder_func:
        return create_rarelink_phenopacket_mappings()
    
    # Use the provided builder function for other data models
    return config_builder_func(**kwargs)

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
        mappings (Dict[str, Any], optional): Mappings to use. Defaults to RareLink mappings.

    Returns:
        Dict[str, str]: The requested mapping or label dictionary
    """
    if mappings is None:
        mappings = create_rarelink_phenopacket_mappings()
    
    block_mappings = mappings.get(block_name, {})
    
    # Handle both standard dictionary and list-based block configurations
    if isinstance(block_mappings, list):
        # For list-based configurations, combine all mappings of the requested type
        combined_mappings = {}
        for config in block_mappings:
            if mapping_type in config:
                combined_mappings.update(config[mapping_type].get(key, {}))
        return combined_mappings
    
    # Standard dictionary configuration
    if mapping_type not in block_mappings:
        return {}
    
    return block_mappings[mapping_type].get(key, {})