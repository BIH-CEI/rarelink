import logging

logger = logging.getLogger(__name__)

def process_code(code: str) -> str:
    """
    Process a (REDCap) code to its standard ontology format.
    
    Args:
        code: The code to process (e.g., "mondo_0007843")
        
    Returns:
        The processed code (e.g., "MONDO:0007843") or original
    """
    if not code:
        return code
    
    # Check if already has colon format
    if ":" in code:
        prefix, rest = code.split(":", 1)
        prefix_upper = prefix.upper()
        
        # Special case for SNOMED -> SNOMEDCT
        if prefix_upper == "SNOMED":
            prefix_upper = "SNOMEDCT"
            
        return f"{prefix_upper}:{rest}"
    
    # Handle prefixes without colon
    prefixes = {
        "mondo_": "MONDO:",
        "hp_": "HP:",
        "ncit_": "NCIT:",
        "snomedct_": "SNOMEDCT:",
        "orpha_": "ORPHA:",
        "omim_": "OMIM:",
        "icd10cm_": "ICD10CM:",
        "icd10_": "ICD10:",
        "icd11_": "ICD11:",
        "icd9_": "ICD9:",
        "loinc_": "LOINC:",
        "uo_": "UO:",
        "vo_": "VO:"
    }
    
    # Check for underscore prefix
    for prefix, replacement in prefixes.items():
        if code.lower().startswith(prefix):
            rest = code[len(prefix):]
            
            # Special processing for certain ontologies
            if prefix == "ncit_" and rest.lower().startswith('c'):
                rest = rest.upper()
            elif prefix == "loinc_":
                if rest.lower().startswith('la'):
                    # Special handling for LOINC LA pattern
                    rest = rest.upper().replace('_', '-')
                else:
                    rest = rest.replace('_', '-').upper()
            elif prefix in ["icd10cm_", "icd11_", "icd10_", "icd9_"]:
                rest = rest.replace('_', '.').upper()
                
            return f"{replacement}{rest}"
    
    # If no known prefix found, but has underscore, try generic handling
    if "_" in code:
        prefix, rest = code.split("_", 1)
        prefix_upper = prefix.upper()
        
        # Special case handling for generic extraction
        if prefix_upper == "LOINC":
            if rest.lower().startswith('la'):
                rest = rest.upper().replace('_', '-')
            else:
                rest = rest.replace('_', '-').upper()
        elif prefix_upper == "NCIT" and rest.lower().startswith('c'):
            rest = rest.upper()
        elif prefix_upper in ["ICD10CM", "ICD11", "ICD10", "ICD9"]:
            rest = rest.replace('_', '.').upper()
        elif prefix_upper == "SNOMED":
            prefix_upper = "SNOMEDCT"
            
        return f"{prefix_upper}:{rest}"
    
    return code

def normalize_hgnc_id(value: str) -> str:
    """
    Normalize HGNC identifiers to standard format.
    
    Args:
        value: HGNC identifier in any format
        
    Returns:
        Normalized HGNC identifier or original value
    """
    if not value:
        return value
    
    value = str(value)
    
    # Already standard format
    if value.startswith("HGNC:"):
        return value
    
    # Extract from URL format
    if "HGNC:" in value:
        import re
        match = re.search(r'HGNC:(\d+)', value)
        if match:
            return f"HGNC:{match.group(1)}"
    
    # Handle numeric only
    if value.isdigit():
        return f"HGNC:{value}"
    
    return value

def add_prefix_to_code(code: str, prefix: str = "") -> str:
    """
    Adds a specific prefix to the REDCap code if not already present.

    Args:
        code (str): The original code (e.g., "G46.4", "62374-4").
        prefix (str): The prefix to add (e.g., "ICD10CM").

    Returns:
        str: The code with the appropriate prefix (e.g., "ICD10CM:G46.4").
    """
    if not code:
        return code 
    if prefix and not code.startswith(f"{prefix}:"):
        return f"{prefix}:{code}"
    return code


def remove_prefix_from_code(value, prefix):
    """
    Removes a specific prefix from the value if it exists.

    Args:
        value (str): The original value.
        prefix (str): The prefix to remove.

    Returns:
        str: The value without the prefix, or the original value if the prefix is not present.
    """
    if value and value.startswith(f"{prefix}:"):
        return value[len(prefix) + 1:]
    return value


def convert_to_boolean(value: str, mapping: dict) -> bool:
    """
    Converts a string value to a boolean based on a mapping.

    Args:
        value (str): String value to convert (e.g., "true", "false").
        mapping (dict): A dictionary mapping string values to booleans.

    Returns:
        bool: Converted boolean value or None if no match is found.
    """
    return mapping.get(value.lower(), None)
