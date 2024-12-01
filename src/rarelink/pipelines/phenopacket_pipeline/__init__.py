"""This module implements the pipeline from REDCap data to phenopackets."""

from .phenopacket_pipeline import rarelink_cdm_phenopacket_pipeline

__all__ = [
    "rarelink_cdm_phenopacket_pipeline"
]
