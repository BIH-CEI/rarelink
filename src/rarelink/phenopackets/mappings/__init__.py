"""
This module contains general mapping functions for the each
of the blocks in the Phenopackets schema.

"""

from .map_individual import map_individual
from .map_metadata import map_metadata
from .map_vital_status import map_vital_status
from .map_disease import map_diseases
from .map_interpretation import map_interpretations
from .map_variation_descriptor import map_variation_descriptor
from .map_phenotypic_feature import map_phenotypic_features
from .map_measurements import map_measurements
from .map_medical_action import map_medical_actions


__all__ = [
    "map_individual",
    "map_metadata",
    "map_vital_status",
    "map_diseases",
    "map_interpretations",
    "map_variation_descriptor",
    "map_phenotypic_features",
    "map_measurements",
    "map_medical_actions"
]