# src/cieinr/mappings/phenopackets/combined.py
from typing import Dict, Any

# Use absolute imports instead of relative ones
from cieinr.mappings.phenopackets.disease import DISEASE_BLOCK
from cieinr.mappings.phenopackets.individual import INDIVIDUAL_BLOCK
from cieinr.mappings.phenopackets.phenotypes import PHENOTYPIC_FEATURES_BLOCK
from cieinr.mappings.phenopackets.procedure import PROCEDURE_BLOCK
from cieinr.mappings.phenopackets.resources import CIEINR_CODE_SYSTEMS
from cieinr.mappings.phenopackets.mapping_dicts import mapping_dicts
from cieinr.mappings.phenopackets.label_dicts import label_dicts

def create_phenopacket_mappings() -> Dict[str, Any]:
    """
    Create a comprehensive mapping configuration for CIEINR Phenopacket creation.

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
            "instrument_name": "basic_form",
            "mapping_block": DISEASE_BLOCK,
            "label_dicts": {
                "AgeAtOnset": label_dicts.get("AgeAtOnset", {})
            },
            "mapping_dicts": {
                "map_disease_verification_status": mapping_dict_lookup.get("map_disease_verification_status", {})
            },
            "enum_classes": {
                # Reference the IUIS2024MONDOEnum class by import path
                "mondo_": "cieinr.datamodel.form_1_basic.IUIS2024MONDOEnum"
            }
        },
        "phenotypicFeatures": {
            # Map infections_initial_form to phenotypic features
            "instrument_name": "infections_initial_form",
            "mapping_block": PHENOTYPIC_FEATURES_BLOCK,
            "label_dicts": {
                "TemporalPattern": label_dicts.get("TemporalPattern", {}),
                "PhenotypeSeverity": label_dicts.get("PhenotypeSeverity", {})
            },
            "mapping_dicts": {
                "phenotypic_feature_status": mapping_dict_lookup.get("phenotypic_feature_status", {})
            },
            "enum_classes": {}
        },
        "procedures": {
            "instrument_name": "basic_form",
            "mapping_block": PROCEDURE_BLOCK
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