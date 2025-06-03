from typing import Optional, Dict, Any
import logging
import os
import requests
from urllib.parse import quote
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
BIOPORTAL_API_TOKEN = os.getenv("BIOPORTAL_API_TOKEN", "").strip()

def fetch_label_from_enum(code: str, enum_class: Any) -> Optional[str]:
    """
    Fetch a label from an Enum class.
    
    Args:
        code: The code to look up
        enum_class: The enum class
        
    Returns:
        The description or None if not found
    """
    if not code or not enum_class:
        return None
    
    try:
        enum_value = getattr(enum_class, code, None)
        if enum_value and hasattr(enum_value, 'description'):
            return enum_value.description
        return None
    except Exception as e:
        logger.debug(f"Error fetching from enum: {e}")
        return None

def fetch_label_from_dict(code: str, label_dict: Dict[str, str]) -> Optional[str]:
    """
    Fetch a label from a dictionary.
    
    Args:
        code: The code to look up
        label_dict: Dictionary mapping codes to labels
        
    Returns:
        The label or None if not found
    """
    return label_dict.get(code) if code and label_dict else None

def fetch_label_from_bioportal(code: str) -> Optional[str]:
    """
    Fetch a label from BioPortal API.
    
    Args:
        code: Code in standard format with prefix:id
        
    Returns:
        The label or None if not found
    """
    if not code or ":" not in code or not BIOPORTAL_API_TOKEN:
        return None
    
    try:
        # Split ontology prefix and identifier
        ontology, identifier = code.split(":", 1)
        
        ontology_map = {
            "ORPHA": {"api": "ORDO", "iri": f"http://www.orpha.net/ORDO/Orphanet_{identifier}"},
            "HGNC": {"api": "HGNC-NR", "iri": f"http://identifiers.org/hgnc/{identifier}"},
            "NCIT": {"api": "NCIT", "iri": f"http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#{identifier}"},
            "NCBITAXON": {"api": "NCBITAXON", "iri": f"http://purl.bioontology.org/ontology/NCBITAXON/{identifier}"},
            "HP": {"api": "HP", "iri": f"http://purl.obolibrary.org/obo/HP_{identifier.replace(':', '_')}"},
            "ICD10CM": {"api": "ICD10CM", "iri": identifier},  # Directly use identifier
            "SNOMEDCT": {"api": "SNOMEDCT", "iri": identifier},  # Directly use identifier
            "LOINC": {"api": "LOINC", "iri": identifier},  # Directly use identifier
            "MONDO": {"api": "MONDO", "iri": f"http://purl.obolibrary.org/obo/MONDO_{identifier.replace(':', '_')}"},
            "OMIM": {"api": "OMIM", "iri": f"http://purl.bioontology.org/ontology/OMIM/{identifier}"},
            "ECO": {"api": "ECO", "iri": f"http://purl.obolibrary.org/obo/ECO_{identifier}"},
            "UO": {"api": "UO", "iri": f"http://purl.obolibrary.org/obo/UO_{identifier}"},
            "VO": {"api": "VO", "iri": f"http://purl.obolibrary.org/obo/VO_{identifier}"},
            "GENO": {"api": "GENO", "iri": f"http://purl.obolibrary.org/obo/GENO_{identifier}"}
        }
                
        # Get API parameters
        mapping = ontology_map.get(ontology)
        if not mapping:
            # Default parameters for unsupported ontologies
            logger.debug(f"Unsupported ontology: {ontology}, using default parameters")
            api_ontology = ontology
            iri = identifier
        else:
            api_ontology = mapping["api"]
            iri = mapping["iri"]
        
        # Make API request
        encoded_iri = quote(iri, safe="")
        url = f"https://data.bioontology.org/ontologies/{api_ontology}/classes/{encoded_iri}?apikey={BIOPORTAL_API_TOKEN}"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("prefLabel")
        
        return None
    except Exception as e:
        logger.debug(f"Error fetching from BioPortal: {e}")
        return None

def fetch_label(code: str, enum_class: Any = None, label_dict: Dict[str, str] = None) -> Optional[str]:
    """
    Fetch a label using hierarchy of sources.
    
    Args:
        code: The code to look up
        enum_class: Optional enum class for lookup
        label_dict: Optional label dictionary
        
    Returns:
        The label or None if not found
    """
    if not code:
        return None
    
    # Priority 1: Enum class
    if enum_class:
        label = fetch_label_from_enum(code, enum_class)
        if label:
            return label
    
    # Priority 2: Label dictionary
    if label_dict:
        label = fetch_label_from_dict(code, label_dict)
        if label:
            return label
    
    # Priority 3: BioPortal API (only for codes with prefix:id format)
    if ":" in code:
        label = fetch_label_from_bioportal(code)
        if label:
            return label
    
    # Priority 4: Try processed code with BioPortal
    if ":" not in code:
        from .code_processing import process_code
        processed_code = process_code(code)
        if processed_code != code and ":" in processed_code:
            label = fetch_label_from_bioportal(processed_code)
            if label:
                return label
    
    return None