# src/cieinr/mappings/phenopackets/__init__.py
"""
CIEINR specific mapping to the Phenopacket schema blocks.
"""

from .mapping_dicts import mapping_dicts, get_mapping_by_name
from .label_dicts import label_dicts
from .individual import INDIVIDUAL_BLOCK
from .disease import DISEASE_BLOCK
from .phenotypes import CONDITIONS_FEATURES_BLOCK, INFECTIONS_FEATURES_BLOCK
from .medical_actions import (
    BASIC_PROCEDURE_BLOCK,
    INACTIVATE_VACCINE_BLOCK,
    LIVE_VACCINE_BLOCK,
)
from .genetics import INTERPRETATION_BLOCK, VARIATION_DESCRIPTOR_BLOCK
from .resources import CIEINR_CODE_SYSTEMS
from .combined import create_phenopacket_mappings

__all__ = [
    "mapping_dicts",
    "get_mapping_by_name",
    "label_dicts",
    "INDIVIDUAL_BLOCK",
    "DISEASE_BLOCK",
    "CONDITIONS_FEATURES_BLOCK",
    "INFECTIONS_FEATURES_BLOCK",
    "INTERPRETATION_BLOCK",
    "VARIATION_DESCRIPTOR_BLOCK",
    "BASIC_PROCEDURE_BLOCK",
    "INACTIVATE_VACCINE_BLOCK",
    "LIVE_VACCINE_BLOCK",
    "CIEINR_CODE_SYSTEMS",
    "create_phenopacket_mappings"
]