import os
from dotenv import load_dotenv
from .cieinr_phenopackets_mappings import CIEINR_RESOURCES

def create_phenopacket_mappings():
    """
    Create a comprehensive mapping configuration for Phenopacket creation.
    
    Returns:
        Dict: Mapping configurations for Phenopacket generation
    """
    # Load environment variables
    load_dotenv()
    
    return {
        "individual": {
            "instrument_name": "patient_demographics_initial_form",
            "mapping_block": {
                "id_field": "record_id",
                "date_of_birth_field": "patient_demographics_initial_form.snomedct_184099003",
                "time_at_last_encounter_field": "patient_demographics_initial_form.visit_date_demographics"
            },
        },
        "vitalStatus": {
            "instrument_name": "noVitalStatusIncluded",
        },
        "diseases": {
            "instrument_name": "basic_form",
            "mapping_block": {
                "term_field_1": "basic_form.iei_deficiency_basic"
            }
        },
        "metadata": {
           # "code_systems": CIEINR_RESOURCES
            },
        }
    