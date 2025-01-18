"""
Processing Utilities for RareLink

This package contains modules and functions for data processing related to REDCap and other data sources.
"""

# Explicitly define all modules and functions to be exposed
from .codes import (
    add_prefix_to_code,
    process_redcap_code,
    fetch_label_directly,
    fetch_label_for_code,
    batch_fetch_labels,
    convert_to_boolean,
)

__all__ = [
    "add_prefix_to_code",
    "process_redcap_code",
    "fetch_label_directly",
    "fetch_label_for_code",
    "batch_fetch_labels",
    "convert_to_boolean",
]