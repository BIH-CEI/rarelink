"""
Mapping function for infections_initial_form REDCap data to LinkML format for CIEINR.
"""

def map_infections(record):
    """
    Map REDCap record data to the InfectionsInitial LinkML class format.
    
    Args:
        record (dict): The REDCap record data
        
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        # Main infection type
        "type_of_infection": record.get("type_of_infection", ""),
        
        # Specific infection types
        "snomedct_61274003": record.get("snomedct_61274003", ""),  # Opportunistic Infection
        "snomedct_21483005": record.get("snomedct_21483005", ""),  # CNS Infection
        "snomedct_81745001": record.get("snomedct_81745001", ""),  # Eye Infection
        "snomedct_385383008": record.get("snomedct_385383008", ""),  # ENT Infection
        "snomedct_127856007": record.get("snomedct_127856007", ""),  # Skin and Soft Tissue Infection
        "snomedct_110522009": record.get("snomedct_110522009", ""),  # Bone and Joint Infection
        "snomedct_20139000": record.get("snomedct_20139000", ""),  # Respiratory Infection
        "snomedct_303699009": record.get("snomedct_303699009", ""),  # Gastrointestinal Infection
        "snomedct_21514008": record.get("snomedct_21514008", ""),  # Genitourinary Infections
        "snomedct_31099001": record.get("snomedct_31099001", ""),  # Systemic Infection
        
        # Additional infection data
        "infection_severity": record.get("infection_severity", ""),
        "infection_temp_pattern": record.get("infection_temp_pattern", ""),
        "infection_times_obseverd": record.get("infection_times_obseverd", ""),
        
        # Form completion status
        "infections_initial_form_complete": record.get("infections_initial_form_complete", "0")
    }