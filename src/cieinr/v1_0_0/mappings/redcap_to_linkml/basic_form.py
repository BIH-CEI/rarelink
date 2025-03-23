"""
Mapping function for basic_form REDCap data to LinkML format for CIEINR.
"""

def map_basic_form(record):
    """
    Map REDCap record data to the BasicForm LinkML class format.
    
    Args:
        record (dict): The REDCap record data
        
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "iei_deficiency_basic": record.get("iei_deficiency_basic", ""),
        "basic_form_complete": record.get("basic_form_complete", "0"),
        "igrt_basic": record.get("igrt_basic", ""),
        "hct_basic_form": record.get("hct_basic_form", "")
        
    }