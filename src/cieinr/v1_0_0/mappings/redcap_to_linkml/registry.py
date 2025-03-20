"""
Registry of mapping functions for the CIEINR project.
This file defines the mapping from REDCap instruments to their LinkML schema equivalents.
"""

from .basic_form import map_basic_form
from .patient_demographics import map_patient_demographics  
from .infections import map_infections
from .genetics import map_genetic_findings

# Registry of mapping functions with configuration
MAPPING_FUNCTIONS = {
    "basic_form": {
        "mapper": map_basic_form,
        "is_repeating": False
    },
    "patient_demographics_initial_form": {
        "mapper": map_patient_demographics,
        "is_repeating": False
    },
    "infections_initial_form": {
        "mapper": map_infections,
        "is_repeating": True
    },
    "genetic_information": {
        "mapper": map_genetic_findings,
        "is_repeating": True,
        "output_key": "genetic_findings" 
    }
}