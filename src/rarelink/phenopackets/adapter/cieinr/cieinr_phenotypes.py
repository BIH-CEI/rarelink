

from typing import List
from rarelink.utils.processor import DataProcessor


def get_infection_types(data: dict, processor: DataProcessor, all_instruments: List[str] = None) -> List[str]:
    """
    Extracts infection type values from the data.
    
    Args:
        data (dict): The data element to extract from.
        processor (DataProcessor): The data processor.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        
    Returns:
        List[str]: A list of infection type values.
    """
    # Define infection type fields to check
    infection_type_fields = [
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
    ]
    
    # Override with configuration if available
    if processor.mapping_config.get("type_fields"):
        infection_type_fields = processor.mapping_config.get("type_fields")
    
    # Storage for found type values
    type_values = []
    
    # Check each field directly in the data
    if isinstance(data, dict):
        for field in infection_type_fields:
            if field in data and data[field]:
                value = data[field]
                
                if isinstance(value, str) and (
                    value.startswith("hp_") or 
                    value.startswith("mondo_") or 
                    value.startswith("snomedct_") or
                    ":" in value
                ):
                    type_values.append(value)
    
    return type_values

def get_condition_types(data: dict, processor: DataProcessor, all_instruments: List[str] = None) -> List[str]:
    """
    Extracts condition type values from the data.
    
    Args:
        data (dict): The data element to extract from.
        processor (DataProcessor): The data processor.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        
    Returns:
        List[str]: A list of condition type values.
    """
    # Define condition type fields to check
    condition_type_fields = [
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
    ]
    
    # Override with configuration if available
    if processor.mapping_config.get("type_fields"):
        condition_type_fields = processor.mapping_config.get("type_fields")
    
    # Storage for found type values
    type_values = []
    
    # Check each field directly in the data
    if isinstance(data, dict):
        for field in condition_type_fields:
            if field in data and data[field]:
                value = data[field]
                
                if isinstance(value, str) and (
                    value.startswith("hp_") or 
                    value.startswith("mondo_") or 
                    value.startswith("snomedct_") or
                    ":" in value
                ):
                    type_values.append(value)
    
    return type_values