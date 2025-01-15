import pytest
from rarelink.utils.processing.codes import (
    fetch_label_directly,
    batch_fetch_labels,
)

@pytest.mark.parametrize("code, expected_label", [
    ("HP:0000118", "Phenotypic abnormality"),
    ("ICD10CM:G46.4", "Cerebellar stroke syndrome"), 
    ("ORPHA:84", "Fanconi anemia"),
    ("SNOMEDCT:106221001", "Genetic finding"),  
    ("MONDO:0019391", "Fanconi anemia"),
    ("OMIM:601622", "TWIST FAMILY bHLH TRANSCRIPTION FACTOR 1"),
    ("LOINC:62374-4", "Human reference sequence assembly release number:ID:Pt:Bld/Tiss:Nom:Molgen"),
    ("Thesaurus:C3262", "Neoplasm"),
    ("NCBITAXON:1279", "Staphylococcus"),
    ("HGNC:4238", "GFI1B"),
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
    label = fetch_label_directly(code)
    
    assert label == expected_label, f"Label for {code} was {label}, expected {expected_label}"

@pytest.mark.parametrize("codes, expected_labels", [
    ([
        "HP:0000118", 
        "ICD10CM:G46.4",
        "ORPHA:84",  
        "SNOMEDCT:106221001",  
        "MONDO:0019391", 
        "OMIM:601622",  
        "LOINC:62374-4",  
        "Thesaurus:C3262",  
        "NCBITAXON:1279",  
        "HGNC:4238", 
        "ECO:0000180", 
        "UO:0000276", 
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
        "amount per container",
    ])
])
def test_batch_fetch_labels(codes, expected_labels):
    """
    Tests the `batch_fetch_labels` function by verifying it returns correct
    labels for multiple ontology codes in a single call.
    """
    labels = batch_fetch_labels(codes)
    assert labels == expected_labels, f"Labels were {labels}, expected {expected_labels}"
