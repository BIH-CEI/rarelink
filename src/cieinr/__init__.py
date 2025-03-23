"""
CIEINR: Canadian Inborn Errors of Immunity National Registry

This package provides tools for:
1. Managing and processing CIEINR data model
2. Converting REDCap records to LinkML schema
3. Generating GA4GH Phenopackets from structured data
"""
from cieinr._version import __version__
from cieinr.config import Config

__all__ = ["Config", "__version__"]