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

# Initialize the adapter
adapter = get_adapter(f"bioportal:{BIOPORTAL_API_TOKEN}")

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
        
def fetch_label_directly(code):
    """
    Fetch label directly using BioPortal API for cases where Oaklib fails.
    """
    if code.startswith("ORPHA:"):
        # Construct URL for BioPortal API
        base_url = "https://data.bioontology.org/ontologies/ORDO/classes/"
        iri = f"http://www.orpha.net/ORDO/Orphanet_{code.split(':')[1]}"
        url = f"{base_url}{iri.replace(':', '%3A').replace('/', '%2F')}?apikey={BIOPORTAL_API_TOKEN}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("prefLabel", None)
        else:
            return None
    return None

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
        List[Optional[str]]: A list of labels corresponding to the provided codes.
    """
    labels = []
    for code in codes:
        label = fetch_label_for_code(code)
        labels.append(label)
    return labels

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch ontology labels using Oaklib and BioPortal.")
    parser.add_argument("--list-ontologies", action="store_true", help="List available ontologies.")
    parser.add_argument("--codes", nargs="+", help="Ontology codes to fetch labels for.")
    
    args = parser.parse_args()

    if args.list_ontologies:
        list_ontologies()
    if args.codes:
        print("Fetching labels for provided codes...")
        batch_fetch_labels(args.codes)
