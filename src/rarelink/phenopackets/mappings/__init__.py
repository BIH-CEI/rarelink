"""
This module contains general mapping functions for the each
of the blocks in the Phenopackets schema.

"""

from .map_individual import map_individual
from .map_metadata import map_metadata
from .map_vital_status import map_vital_status
from .map_disease import map_diseases


__all__ = [
    "map_individual",
    "map_metadata",
    "map_vital_status",
    "map_diseases"

]