"""
RareLink Package.

This package contains all submodules and utilities for the RareLink project,
including the CLI and Common Data Model (CDM) implementations.
"""

# Import key components for easier access if needed
from .rarelink_cdm import preprocess_flat_data, load_schema, MAPPING_FUNCTIONS

__all__ = [
    "preprocess_flat_data",
    "load_schema",
    "MAPPING_FUNCTIONS"
]
