"""
Codes Processing Submodule


This submodule contains all functions to process specific codes and codestrings
from various unstructured formats to the required format or enrichting these 
with their labels.

    
Exports: 
- 
-   
-    
    
"""

from .add_prefixes import add_prefix_to_code
from .process_redcap_code import process_redcap_code
from .fetch_displays import (
    fetch_label_directly, 
    fetch_label_for_code, 
    batch_fetch_labels
)
from .conversions import convert_to_boolean

__all__ = [
    "add_prefix_to_code",
    "process_redcap_code",
    "fetch_label_directly",
    "fetch_label_for_code",
    "batch_fetch_labels",
    "convert_to_boolean"
]