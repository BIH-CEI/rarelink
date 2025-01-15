"""
RareLink Utilities - Mapping Module

This module provides mappings functions to facilitate data transformations 
between schemas and models in the RareLink project.

Modules:

Exports:
- FIELD_MAPPINGS: A dictionary defining mappings of schema sections to 
field lists.

"""

from .map_entry import map_entry

__all__ = [
    "redcap_to_linkml",
    "map_entry"
]

