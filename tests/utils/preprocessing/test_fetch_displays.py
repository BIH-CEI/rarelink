import pytest
from rarelink.utils.preprocessing.fetch_displays import fetch_display_for_code
import os
from dotenv import load_dotenv

load_dotenv()
bioportal_token = os.getenv("BIOPORTAL_API_TOKEN")

@pytest.mark.parametrize("code, expected_label", [
    ("MONDO:0019391", "Fanconi anemia"),  
    ("SNOMEDCT:106221001", "Genetic finding"), 
    ("HP:0000118", "Phenotypic abnormality"), 
])
def test_fetch_display_for_code(code, expected_label):
    """
    Tests the `fetch_display_for_code` function by verifying that it returns
    the correct label for given ontology codes.

    Args:
        code (str): The ontology code to fetch the display label for.
        expected_label (str): The expected label corresponding to the code.

    Raises:
        AssertionError: If the fetched label does not match the expected label.

    Example:
        Given the code "MONDO:0019391", the function should return "Fanconi anemia".
    """
    label = fetch_display_for_code(code, bioportal_token)
    assert label == expected_label, f"Label for {code} was {label}, expected {expected_label}"