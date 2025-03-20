"""
This module contains the adapter functions for the RareLink-Phenopacket 
engine, e.g. to handle multi-onset features.
"""

from .multi_onset import multi_onset_adapter

__all__ = [
    "multi_onset_adapter"
    
]