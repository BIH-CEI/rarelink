"""
RareLink Utilities - Loading Module

This module contains all loading functions necesary in 
Modules:
- schema_loader: Contains functions for loading LinkML schema YAML definitions.
- multiple_instruments: Contains functions for accessing data across multiple instruments.
- multiple_map: Contains generic mapping functions for multi-instrument entities.

Exports:
- load_schema: Function to load a schema from its YAML definition.
- _get_field_value: Function to get a field value from data, handling direct and nested access.
- _get_multi_instrument_field_value: Function to retrieve field values across multiple instruments.
- generic_map_entities: Generic mapping function for various entity types across instruments.
    
"""

from .fetch_redcap_data import fetch_redcap_data
from .schema_loader import load_schema
from .project_and_schema import load_project_and_schema_info
from .nested_json_data import get_nested_field  
from .label_from_enum import fetch_description_from_label_dict
from .highest_instance import get_highest_instance
from .multiple_instruments import _get_field_value
# Import the fixed versions of these functions from module's root to override existing ones
from rarelink.utils.loading.fixed_field_access import _get_multi_instrument_field_value, generic_map_entities

__all__ = [
    "load_schema",
    "fetch_redcap_data",
    "load_project_and_schema_info",
    "get_nested_field",
    "fetch_description_from_label_dict",
    "get_highest_instance",
    "_get_multi_instrument_field_value",
    "_get_field_value",
    "generic_map_entities"
]