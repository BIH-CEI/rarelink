"""
This module contains general mapping functions for the each
of the blocks in the Phenopackets schema.

"""

from .map_individual import map_individual
from .map_metadata import map_metadata


__all__ = [
    "map_individual",
    "map_metadata"

]