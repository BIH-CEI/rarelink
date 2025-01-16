"""
RareLink-CDM v2.0.0.dev0 specific mapping to the Phenopacket schema Blocks

    
"""

from .mapping_dicts import mapping_dicts
from .label_dicts import label_dicts
from .individual import INDIVIDUAL_BLOCK
from .vitalstatus import VITAL_STATUS_BLOCK
from .disease import DISEASE_BLOCK
from .resources import RARELINK_CODE_SYSTEMS




__all__ = [
    "mapping_dicts",
    "label_dicts",
    "INDIVIDUAL_BLOCK",
    "VITAL_STATUS_BLOCK",
    "DISEASE_BLOCK",
    "RARELINK_CODE_SYSTEMS"
]