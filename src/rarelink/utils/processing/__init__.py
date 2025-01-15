"""
RareLink Utilities - Processing Module

This module contains all functions to preprocessing, enrich, and transform 
data for the required schemas, exports, and pipelines.

Submodules: 
- codes: contains all functions to process codes from REDCap or other 
unstructured formats to comply with Phenopackets or FHIR
- schemas: contains all functions to process entire schemas, such as the
REDCap JSON data into the LinkML RareLink-CDM schema.
"""



__all__ = [
    "codes",
    "schemas"
]