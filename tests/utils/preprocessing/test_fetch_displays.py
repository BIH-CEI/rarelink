import pytest
from rarelink.utils.preprocessing.fetch_displays import fetch_label_for_code, fetch_label_directly, batch_fetch_labels
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
bioportal_token = os.getenv("BIOPORTAL_API_TOKEN")

if not bioportal_token:
    raise ValueError("BioPortal API token not found. Please set it in the .env file.")

@pytest.mark.parametrize("code, expected_label", [
    ("HP:0000118", "Phenotypic abnormality"),
    ("ICD10CM:G46.4", "Cerebellar stroke syndrome"), # add prefix for processing
    ("ORPHA:84", "Fanconi anemia"),
    ("SNOMEDCT:106221001", "Genetic finding"), # add prefix for processing
    ("MONDO:0019391", "Fanconi anemia"),
    ("OMIM:601622", "TWIST FAMILY bHLH TRANSCRIPTION FACTOR 1"), # add prefix for processing
    ("LOINC:62374-4", "Human reference sequence assembly release number:ID:Pt:Bld/Tiss:Nom:Molgen"), # add prefix for processing
    ("Thesaurus:C3262", "Neoplasm"),
    ("NCBITAXON:1279", "Staphylococcus"), # add prefix for processing
    ("HGNC:4238", "GFI1B"),
    ("ECO:0000180", "clinical study evidence"),
    ("UO:0000276", "amount per container"), # convert prefix from UO_ to UO: for processing
])

def test_fetch_label_for_code(code, expected_label):
    """
    Tests the `fetch_label_for_code` function by verifying that it returns
    the correct label for given ontology codes.

    Args:
        code (str): The ontology code to fetch the display label for.
        expected_label (str): The expected label corresponding to the code.

    Raises:
        AssertionError: If the fetched label does not match the expected label.
    """
    # Use fetch_label_directly for specific cases
    if (
        code.startswith("ORPHA:")
        or code.startswith("HGNC:")
        or code.startswith("Thesaurus:")
        or code.startswith("NCBITAXON:")
    ):
        label = fetch_label_directly(code)
    else:
        label = fetch_label_for_code(code)

    # Validate the fetched label
    if expected_label is None:
        assert label is None, f"Expected None for {code}, but got {label}"
    else:
        assert label == expected_label, f"Label for {code} was {label}, expected {expected_label}"



@pytest.mark.parametrize("codes, expected_labels", [
    ([
        "HP:0000118",  # Directly resolvable
        "ICD10CM:G46.4",  # Prefixed for processing
        "ORPHA:84",  # ORDO
        "SNOMEDCT:106221001",  # Prefixed for processing
        "MONDO:0019391",  # Directly resolvable
        "OMIM:601622",  # Prefixed for processing
        "LOINC:62374-4",  # Prefixed for processing
        "Thesaurus:C3262",  # NCIT mapped
        "NCBITAXON:1279",  # Prefixed for processing
        "HGNC:4238",  # HGNC-NR
        "ECO:0000180",  # Directly resolvable
        "UO:0000276"  # Prefix converted
    ], [
        "Phenotypic abnormality",
        "Cerebellar stroke syndrome",
        "Fanconi anemia",
        "Genetic finding",
        "Fanconi anemia",
        "TWIST FAMILY bHLH TRANSCRIPTION FACTOR 1",
        "Human reference sequence assembly release number:ID:Pt:Bld/Tiss:Nom:Molgen",
        "Neoplasm",
        "Staphylococcus",
        "GFI1B",
        "clinical study evidence",
        "amount per container"
    ])
])
def test_batch_fetch_labels(codes, expected_labels):
    """
    Tests the `batch_fetch_labels` function by verifying it returns correct
    labels for multiple ontology codes in a single call.
    """
    labels = batch_fetch_labels(codes)
    assert labels == expected_labels, f"Labels were {labels}, expected {expected_labels}"

