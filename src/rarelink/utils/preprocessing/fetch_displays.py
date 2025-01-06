from urllib.parse import quote
from oaklib import get_adapter
from typing import List, Optional
import os
import requests
from dotenv import load_dotenv

# Load the API token from the environment file
load_dotenv()
BIOPORTAL_API_TOKEN = os.getenv("BIOPORTAL_API_TOKEN")

if not BIOPORTAL_API_TOKEN:
    raise ValueError("BioPortal API token not found. Please set it in the .env file.")

adapter = get_adapter(f"bioportal:{BIOPORTAL_API_TOKEN}")

def fetch_label_directly(code):
    """
    Fetch the label for a specific code directly using the BioPortal API.

    Args:
        code (str): Ontology code (e.g., "Thesaurus:C3262", "NCBITAXON:1279").

    Returns:
        str: The label (preferred name) of the term if found, or None if not
        resolvable.
    """
    base_url = "https://data.bioontology.org/ontologies"
    
    # Split ontology prefix and identifier
    if ":" not in code:
        print(f"Invalid code format: {code}")
        return None
    
    ontology, identifier = code.split(":", 1)

    # Adjust ontology prefix and IRI for specific cases
    if ontology == "ORPHA":
        ontology = "ORDO"
        iri = f"http://www.orpha.net/ORDO/Orphanet_{identifier}"
    elif ontology == "HGNC":
        ontology = "HGNC-NR"
        iri = f"http://identifiers.org/hgnc/{identifier}"
    elif ontology == "Thesaurus":  # Map "Thesaurus" to "NCIT"
        ontology = "NCIT"
        iri = f"http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#{identifier}"
    elif ontology == "NCBITAXON":
        iri = f"http://purl.bioontology.org/ontology/NCBITAXON/{identifier}"
    else:
        print(f"Unsupported ontology: {ontology}")
        return None

    # Correctly encode the IRI for URL construction
    encoded_iri = quote(iri, safe="")  # Encodes special characters
    url = f"{base_url}/{ontology}/classes/{encoded_iri}?apikey={BIOPORTAL_API_TOKEN}"
    
    # Debugging: Print constructed URL
    print(f"Constructed URL: {url}")
    
    # Make the API request
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("prefLabel", None)
    else:
        print(f"Error fetching label for {code}. \
            Status code: {response.status_code}")
        return None

def list_ontologies():
    """
    Lists all available ontologies in BioPortal via Oaklib.
    """
    try:
        print("Fetching available ontologies from BioPortal...")
        ontologies = adapter.ontologies()
        print("Available Ontologies:")
        for ontology in ontologies:
            print(ontology)
    except Exception as e:
        print(f"Error listing ontologies: {e}")
    

def fetch_label_for_code(code: str) -> Optional[str]:
    """
    Fetch the label for a single ontology code using Oaklib and BioPortal.

    Args:
        code (str): The ontology code to resolve.

    Returns:
        str: The label for the code if found, otherwise None.
    """
    try:
        label = adapter.label(code)
        if label:
            print(f"Code: {code}, Label: {label}")
            return label
        else:
            print(f"Code {code} could not be resolved.")
            return None
    except Exception as e:
        print(f"Error fetching label for {code}: {e}")
        return None

def batch_fetch_labels(codes: List[str]) -> List[Optional[str]]:
    """
    Fetch labels for a batch of ontology codes.

    Args:
        codes (List[str]): List of ontology codes to resolve.

    Returns:
        List[Optional[str]]: A list of labels corresponding to the 
        provided codes.
    """
    labels = []
    for code in codes:
        # Use fetch_label_directly for specific ontologies
        if (
            code.startswith("ORPHA:")
            or code.startswith("HGNC:")
            or code.startswith("Thesaurus:")
            or code.startswith("NCBITAXON:")
        ):
            label = fetch_label_directly(code)
        else:
            label = fetch_label_for_code(code)
        labels.append(label)
    return labels
