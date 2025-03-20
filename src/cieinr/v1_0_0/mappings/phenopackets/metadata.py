"""Module for generating Phenopacket metadata.

This module adapts RareLink's metadata mapping for CIEINR.
"""

from datetime import datetime
from typing import Dict, Any, Optional, List

# Import RareLink metadata mapping for reuse
from rarelink.phenopackets.mappings.map_metadata import map_metadata as rarelink_map_metadata
from phenopackets import MetaData, Resource

# Code systems container for CIEINR
CIEINR_CODE_SYSTEMS_CONTAINER = [
    {
        "id": "hp",
        "name": "Human Phenotype Ontology",
        "url": "http://purl.obolibrary.org/obo/hp.owl",
        "version": "2023-06-04",
        "namespace_prefix": "HP",
        "iri_prefix": "http://purl.obolibrary.org/obo/HP_"
    },
    {
        "id": "mondo",
        "name": "Mondo Disease Ontology",
        "url": "http://purl.obolibrary.org/obo/mondo.owl",
        "version": "2024-09-03",
        "namespace_prefix": "MONDO",
        "iri_prefix": "http://purl.obolibrary.org/obo/MONDO_"
    },
    {
        "id": "ncit",
        "name": "NCI Thesaurus",
        "url": "http://purl.obolibrary.org/obo/ncit.owl",
        "version": "24.04e",
        "namespace_prefix": "NCIT",
        "iri_prefix": "http://purl.obolibrary.org/obo/NCIT_"
    },
    {
        "id": "snomedct",
        "name": "SNOMED Clinical Terms",
        "url": "http://snomed.info/sct",
        "version": "2023-03",
        "namespace_prefix": "SNOMEDCT",
        "iri_prefix": "http://snomed.info/id/"
    },
    {
        "id": "ncbitaxon",
        "name": "NCBI Taxonomy",
        "url": "http://purl.obolibrary.org/obo/ncbitaxon.owl",
        "version": "2023-04-01",
        "namespace_prefix": "NCBITaxon",
        "iri_prefix": "http://purl.obolibrary.org/obo/NCBITaxon_"
    }
]

def map_cieinr_metadata(created_by: Optional[str] = None) -> MetaData:
    """
    Generate metadata for a CIEINR Phenopacket.
    
    Args:
        created_by: Optional name of the creator
        
    Returns:
        MetaData: A Phenopacket MetaData block
    """
    created_time = datetime.utcnow().isoformat() + "Z"
    resources = []
    
    # Convert our code systems to proper Resource objects
    for cs in CIEINR_CODE_SYSTEMS_CONTAINER:
        resource = Resource(
            id=cs["id"],
            name=cs["name"],
            url=cs["url"],
            version=cs["version"],
            namespace_prefix=cs["namespace_prefix"],
            iri_prefix=cs.get("iri_prefix", "")
        )
        resources.append(resource)
    
    # Create the metadata
    metadata = MetaData(
        created_by=created_by or "CIEINR Data Team",
        created=created_time,
        resources=resources,
        phenopacket_schema_version="2.0"
    )
    
    return metadata