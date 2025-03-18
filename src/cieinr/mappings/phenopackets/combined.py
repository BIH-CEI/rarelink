from typing import Dict, Any

# Import mapping blocks and code systems
from .disease import DISEASE_BLOCK
from .individual import INDIVIDUAL_BLOCK, VITAL_STATUS_BLOCK
from .resources import CIEINR_CODE_SYSTEMS
from .mapping_dicts import mapping_dicts
from .label_dicts import label_dicts

def create_rarelink_phenopacket_mappings() -> Dict[str, Any]:
    """
    Create a comprehensive mapping configuration for Phenopacket creation.

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
        },
        "vitalStatus": {
            "instrument_name": "__dummy__"
        },
        "diseases": {
            "instrument_name": "basic_form",
            "mapping_block": DISEASE_BLOCK
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
        mappings (Dict[str, Any], optional): Mappings to use. Defaults to RareLink mappings.

    Returns:
        Dict[str, str]: The requested mapping or label dictionary
    """
    if mappings is None:
        mappings = create_rarelink_phenopacket_mappings()
    
    block_mappings = mappings.get(block_name, {})
    
    if mapping_type not in block_mappings:
        return {}
    
    return block_mappings[mapping_type].get(key, {})