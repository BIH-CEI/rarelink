"""Phenopackets mapping modules for CIEINR v1.0.0."""
from typing import Dict, Any

# Import mapping blocks and metadata
from .metadata import CIEINR_CODE_SYSTEMS_CONTAINER
from .mapping_blocks import (
    INDIVIDUAL_BLOCK, 
    DISEASE_BLOCK, 
    PHENOTYPIC_FEATURES_BLOCK, 
    VITAL_STATUS_BLOCK
)

def create_cieinr_phenopacket_mappings() -> Dict[str, Any]:
    """
    Create a comprehensive mapping configuration for Phenopacket creation from CIEINR data.

    Returns:
        Dict[str, Any]: Combined mapping configurations
    """
    return {
        "individual": {
            "instrument_name": "patient_demographics_initial_form",
            "mapping_block": INDIVIDUAL_BLOCK,
        },
        "vitalStatus": {
            "instrument_name": "__dummy__",  # Special marker for our patched function
            "mapping_block": VITAL_STATUS_BLOCK
        },
        "diseases": {
            "instrument_name": "basic_form",
            "mapping_block": DISEASE_BLOCK
        },
        "phenotypicFeatures": {
            "instrument_name": "infections_initial_form",
            "mapping_block": PHENOTYPIC_FEATURES_BLOCK
        },
        "metadata": {
            "code_systems": CIEINR_CODE_SYSTEMS_CONTAINER
        }
    }

__all__ = [
    "generate_metadata",
    "INDIVIDUAL_BLOCK",
    "DISEASE_BLOCK",
    "PHENOTYPIC_FEATURES_BLOCK",
    "VITAL_STATUS_BLOCK",
    "CIEINR_CODE_SYSTEMS_CONTAINER",
    "create_cieinr_phenopacket_mappings"
]