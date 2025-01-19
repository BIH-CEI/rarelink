from urllib.parse import quote
from oaklib import get_adapter
from typing import List, Optional
import os
import requests
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

def get_bioportal_adapter():
    """
    Initializes and returns the BioPortal adapter.
    Ensures that the API token is loaded and processed correctly.
    """
    token = os.getenv("BIOPORTAL_API_TOKEN", "").strip()
    if not token:
        raise ValueError(
            "BioPortal API token not found or is empty. Please set it in the .env file.")
    
    adapter = get_adapter(f"bioportal:{token}")
    if not adapter:
        raise RuntimeError("Failed to initialize BioPortal adapter.")
    
    # Ensure the API key has no trailing spaces
    adapter.api_key = adapter.api_key.strip()
    return adapter

adapter = get_bioportal_adapter()


def fetch_label_directly(code: str) -> Optional[str]:
    """
    Fetch the label for a specific code directly using the BioPortal API.

    Args:
        code (str): Ontology code (e.g., "HP:0000118", "ICD10CM:G46.4").

    Returns:
        str: The label (preferred name) of the term if found, or None if not resolvable.
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
        print(f"Unsupported ontology: {ontology}")
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
        print(f"Error fetching label for {code}. Status code: {response.status_code}")
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
    Fetch the label for a single ontology code using the BioPortal adapter.

    Args:
        code (str): The ontology code to resolve.

    Returns:
        str: The label for the code if found, otherwise None.
    """
    try:
        print(f"Attempting to fetch label for code: {code}")
        label = adapter.label(code)  # Use the adapter to fetch the label
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
        List[Optional[str]]: A list of labels corresponding to the provided codes.
    """
    labels = []
    for code in codes:
        try:
            label = fetch_label_directly(code)
            labels.append(label)
        except Exception as e:
            print(f"Error processing code {code}: {e}")
            labels.append(None)
    return labels
