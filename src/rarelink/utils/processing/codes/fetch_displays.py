# src/rarelink/utils/processing/codes/fetch_displays.py
from urllib.parse import quote
from oaklib import get_adapter
from typing import List, Optional
import os
import requests
from dotenv import load_dotenv
import logging

# Logger
logger = logging.getLogger(__name__)

# Load the environment variables
load_dotenv()

def get_bioportal_adapter():
    """
    Initializes and returns the BioPortal adapter.
    Ensures that the API token is loaded and processed correctly.
    """
    token = os.getenv("BIOPORTAL_API_TOKEN", "").strip()
    if not token:
        logger.warning(
            "BioPortal API token not found or is empty. Please set it in the .env file.")
        return None
    
    try:
        adapter = get_adapter(f"bioportal:{token}")
        if not adapter:
            logger.warning("Failed to initialize BioPortal adapter.")
            return None
        
        # Ensure the API key has no trailing spaces
        adapter.api_key = adapter.api_key.strip()
        return adapter
    except Exception as e:
        logger.warning(f"Error initializing BioPortal adapter: {e}")
        return None

# Initialize adapter once
try:
    adapter = get_bioportal_adapter()
except Exception as e:
    logger.warning(f"Error initializing adapter: {e}")
    adapter = None


def fetch_label_directly(code: str) -> Optional[str]:
    """
    Fetch the label for a specific code directly using the BioPortal API.
    Enhanced to better handle different code formats.

    Args:
        code (str): Ontology code (e.g., "HP:0000118", "mondo_0007843").

    Returns:
        str: The label (preferred name) of the term if found, or None if not resolvable.
    """
    if not code:
        return None
        
    # Pre-process code to standard format
    processed_code = preprocess_code(code)
    if not processed_code:
        return None
    
    # Check if we have a valid adapter
    if not adapter:
        logger.debug("BioPortal adapter not available")
        return None
    
    base_url = "https://data.bioontology.org/ontologies"

    # Split ontology prefix and identifier
    if ":" not in processed_code:
        logger.debug(f"Invalid code format after processing: {processed_code}")
        return None

    try:
        ontology, identifier = processed_code.split(":", 1)

        # Adjust ontology prefix and IRI for specific cases
        if ontology == "ORPHA":
            ontology = "ORDO"
            iri = f"http://www.orpha.net/ORDO/Orphanet_{identifier}"
        elif ontology == "HGNC":
            ontology = "HGNC-NR"
            iri = f"http://identifiers.org/hgnc/{identifier}"
        elif ontology == "NCIT":  # Map "Thesaurus" or "NCIT" to "NCIT"
            iri = f"http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#{identifier}"
        elif ontology == "NCBITAXON":
            iri = f"http://purl.bioontology.org/ontology/NCBITAXON/{identifier}"
        elif ontology == "HP":
            iri = f"http://purl.obolibrary.org/obo/HP_{identifier.replace(':', '_')}"
        elif ontology == "ICD10CM":
            iri = identifier  # Directly use the identifier
        elif ontology == "SNOMEDCT":
            iri = identifier  # Directly use the identifier
        elif ontology == "LOINC":
            iri = identifier 
        elif ontology == "MONDO":
            iri = f"http://purl.obolibrary.org/obo/MONDO_{identifier.replace(':', '_')}"
        elif ontology == "OMIM":
            iri = f"http://purl.bioontology.org/ontology/OMIM/{identifier}"
        elif ontology == "ECO":
            iri = f"http://purl.obolibrary.org/obo/ECO_{identifier}"
        elif ontology == "UO":
            iri = f"http://purl.obolibrary.org/obo/UO_{identifier}"
        else:
            logger.debug(f"Unsupported ontology: {ontology}")
            return None

        # Correctly encode the IRI for URL construction
        encoded_iri = quote(iri, safe="")
        url = f"{base_url}/{ontology}/classes/{encoded_iri}?apikey={adapter.api_key}"

        # Make the API request
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("prefLabel", None)
        else:
            logger.debug(f"Error fetching label for {code}. Status code: {response.status_code}")
            return None
    except Exception as e:
        logger.debug(f"Error in fetch_label_directly for {code}: {e}")
        return None

def preprocess_code(code: str) -> str:
    """
    Preprocess code string to standard format (with colon separator).
    
    Args:
        code (str): Code to process (e.g., "mondo_0007843")
        
    Returns:
        str: Processed code (e.g., "MONDO:0007843")
    """
    if not code:
        return None
        
    # Handle prefixes without colon
    prefixes = {
        "mondo_": "MONDO:",
        "hp_": "HP:",
        "ncit_": "NCIT:",
        "snomedct_": "SNOMEDCT:",
        "orpha_": "ORPHA:",
        "omim_": "OMIM:",
        "icd10_": "ICD10:",
        "icd11_": "ICD11:",
        "loinc_": "LOINC:"
    }
    
    # Handle with or without colon
    if ":" in code:
        # Already has a colon, just uppercase prefix
        prefix, rest = code.split(":", 1)
        return f"{prefix.upper()}:{rest}"
    
    # Check for underscores
    for prefix, replacement in prefixes.items():
        if code.lower().startswith(prefix):
            return f"{replacement}{code[len(prefix):]}"
            
    return code  # Return original if no match


def list_ontologies():
    """
    Lists all available ontologies in BioPortal via Oaklib.
    """
    if not adapter:
        logger.warning("BioPortal adapter not available")
        return
        
    try:
        logger.info("Fetching available ontologies from BioPortal...")
        ontologies = adapter.ontologies()
        logger.info("Available Ontologies:")
        for ontology in ontologies:
            logger.info(ontology)
    except Exception as e:
        logger.error(f"Error listing ontologies: {e}")

def fetch_label_for_code(code: str) -> Optional[str]:
    """
    Fetch the label for a single ontology code using the BioPortal adapter.

    Args:
        code (str): The ontology code to resolve.

    Returns:
        str: The label for the code if found, otherwise None.
    """
    if not adapter:
        logger.debug("BioPortal adapter not available")
        return None
        
    try:
        # Preprocess the code to standard format
        processed_code = preprocess_code(code)
        if not processed_code:
            return None
            
        logger.debug(f"Attempting to fetch label for code: {processed_code}")
        label = adapter.label(processed_code)  # Use the adapter to fetch the label
        if label:
            logger.debug(f"Code: {processed_code}, Label: {label}")
            return label
        else:
            logger.debug(f"Code {processed_code} could not be resolved.")
            return None
    except Exception as e:
        logger.debug(f"Error fetching label for {code}: {e}")
        return None

def batch_fetch_labels(codes: List[str]) -> List[Optional[str]]:
    """
    Fetch labels for a batch of ontology codes.

    Args:
        codes (List[str]): List of ontology codes to resolve.

    Returns:
        List[Optional[str]]: A list of labels corresponding to the provided codes.
    """
    labels = []
    for code in codes:
        try:
            label = fetch_label_directly(code)
            labels.append(label)
        except Exception as e:
            logger.debug(f"Error processing code {code}: {e}")
            labels.append(None)
    return labels