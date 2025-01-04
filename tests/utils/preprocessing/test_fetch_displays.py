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
    ("ICD10CM:G46.4", "Cerebellar stroke syndrome"),
    ("ORPHA:84", "Fanconi anemia"),
    ("SNOMEDCT:106221001", "Genetic finding"),
    ("MONDO:0019391", "Fanconi anemia"),
    ("OMIM:601622", "TWIST FAMILY bHLH TRANSCRIPTION FACTOR 1"),
    ### 
    ("LOINC:62374-4", "Human reference sequence assembly release number:ID:Pt:Bld/Tiss:Nom:Molgen"),
   # ("NCIT:C3262", "Genetic Marker"),
   # ("NCBITAXON:1279", "Staphylococcus"),
   # ("HGNC_NR:4238", "GFI1B"),
    ("ECO:0000180", "clinical study evidence"),
    ("UO:0000276", "amount per container"),
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
    if code.startswith("ORPHA:"):
        label = fetch_label_directly(code)
    else:
        label = fetch_label_for_code(code)

    if expected_label is None:
        assert label is None, f"Expected None for {code}, but got {label}"
    else:
        assert label == expected_label, f"Label for {code} was {label}, expected {expected_label}"

# def test_batch_fetch_labels():
#     """
#     Tests the `batch_fetch_labels` function by verifying it returns correct
#     labels for multiple ontology codes in a single call.
#     """
#     codes = [
#         "MONDO:0019391",
#         "SNOMEDCT:106221001",
#         "HP:0000118",
#         "NCIT:C3262",
#         "Z82.3",
#         "HGNC:4238",
#         "ECO:0000180",
#         "UO:0000276",
#     ]
#     expected_labels = [
#         "Fanconi anemia",
#         "Genetic finding",
#         "Phenotypic abnormality",
#         "Genetic Marker",
#         "Cerebellar stroke syndrome",
#         "GFI1B",
#         "clinical study evidence",
#         "amount per container",
#     ]
#     labels = batch_fetch_labels(codes)
#     assert labels == expected_labels, f"Labels were {labels}, expected {expected_labels}"
