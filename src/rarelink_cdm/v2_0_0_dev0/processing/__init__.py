"""
Processing Module

This module provides data transformation utilities for preprocessing and converting REDCap data
to and from hierarchical LinkML-compatible formats.

Modules:
- preprocess_redcap_json: Preprocesses flat REDCap JSON data into a hierarchical structure.
- transform_to_redcap_json: Transforms hierarchical LinkML-compatible data back to REDCap JSON format.

Exports:
- preprocess_redcap_data: Function to preprocess flat REDCap JSON data.
- transform_to_redcap_json: Function to transform hierarchical data back to REDCap JSON.
"""

# Importing functions from individual modules
from .preprocess_redcap_json import preprocess_flat_data
from .transform_to_redcap_json import transform_to_redcap_json
from .map_to_linkml_schema import MAPPING_FUNCTIONS

__all__ = [
    "preprocess_flat_data",
    "transform_to_redcap_json",
    "MAPPING_FUNCTIONS"
]
