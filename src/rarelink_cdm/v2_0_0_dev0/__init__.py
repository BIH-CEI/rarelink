"""
RareLink CDM v2.0.0 Development Package.

This package contains all modules and definitions for RareLink CDM version 2.0.0.dev0,
including:

- Schema definitions (`schema_definitions`)
- Data processing utilities (`processing`)
- Helper functions and configurations (`helpers`)
- Data models for Python-based interaction (`datamodel`)

Modules:
    - schema_definitions: YAML schema files defining RareLink structures.
    - processing: Scripts for preprocessing and transforming REDCap data.
    - helpers: Utility functions for schema loading, field mappings, and other helpers.
    - datamodel: Generated Python classes based on LinkML schema definitions.

Exports:
    - FIELD_MAPPINGS (from helpers.field_mappings)
    - load_schema (from helpers.schema_loader)
"""

from .helpers.schema_loader import load_schema
from .processing import preprocess_flat_data, MAPPING_FUNCTIONS

__all__ = [
    "load_schema",
    "preprocess_flat_data",
    "MAPPING_FUNCTIONS"
]

__version__ = "2.0.0.dev0"
