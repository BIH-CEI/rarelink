"""
Mapping function for patient_demographics_initial_form REDCap data to LinkML format for CIEINR.
"""

def map_patient_demographics(record):
    """
    Map REDCap record data to the PatientDemographicsInitial LinkML class format.
    
    Args:
        record (dict): The REDCap record data
        
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "visit_date_demographics": record.get("visit_date_demographics", ""),
        "snomedct_184099003": record.get("snomedct_184099003", ""),  # Date of birth
        "snomedct_432213005": record.get("snomedct_432213005", ""),  # Date of diagnosis
        "snomedct_298059007": record.get("snomedct_298059007", ""),  # Date of symptom onset
        "patient_demographics_initial_form_complete": record.get("patient_demographics_initial_form_complete", "0")
    }