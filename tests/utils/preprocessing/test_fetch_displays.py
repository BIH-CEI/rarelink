import pytest
from rarelink.utils.label_fetching import fetch_label_from_bioportal

@pytest.mark.parametrize("codes, expected_labels", [
    ([
        "HP:0000118", 
        "ICD10CM:G46.4",
        "ORPHA:84",  
        "SNOMEDCT:106221001",  
        "MONDO:0019391", 
        "OMIM:601622",  
        "LOINC:62374-4",  
        "NCIT:C3262",  
        "NCBITAXON:1279",  
        "HGNC:4238", 
        "ECO:0000180", 
        "UO:0000276", 
        "VO:0000654"
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
        "Measles virus vaccine"
    ])
])
def test_fetch_label_for_code(codes, expected_labels):
    """
    Tests the `fetch_label_for_code` function by verifying that it returns
    the correct label for given ontology codes.

    Args:
        codes (list): The list of ontology codes to fetch the display labels for.
        expected_labels (list): The list of expected labels corresponding to the codes.

    Raises:
        AssertionError: If any fetched label does not match the expected label.
    """
    for code, expected_label in zip(codes, expected_labels):
        label = fetch_label_from_bioportal(code)
        assert label == expected_label, f"Label for {code} was {label}, expected {expected_label}"


