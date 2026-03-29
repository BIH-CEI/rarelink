"""
This module contains the adapter functions for the RareLink-Phenopacket 
engine, e.g. to handle multi-onset features.
"""

from .multi_onset import multi_onset_adapter
from .ontology_routing_adapter import (
    apply_ontology_routing,
    get_routed_phenotypic_elements,
    get_routed_disease_dicts,
    check_prefix_placement,
)

__all__ = [
    "multi_onset_adapter",
    "apply_ontology_routing",
    "get_routed_phenotypic_elements",
    "get_routed_disease_dicts",
    "check_prefix_placement"
]