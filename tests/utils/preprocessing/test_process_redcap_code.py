from rarelink.utils.code_processing import process_code

def test_process_redcap_code():
    test_cases = [
        # General prefix-case
        ("UO_1234", "UO:1234"),
        # Already formatted
        ("HP:0004322", "HP:0004322"),
        # Special case for LOINC
        ("loinc_81304_8", "LOINC:81304-8"),
        # Special case for ICD10CM
        ("icd10cm_r51_1", "ICD10CM:R51.1"),
        # Mixed-case for ICD11
        ("ICD11_a02_0", "ICD11:A02.0"),
        # Special case for MONDO
        ("mondo_1234567", "MONDO:1234567"),
        # Orphanet example
        ("ordo_56789", "ORDO:56789"),
        # Human Phenotype Ontology
        ("hp_1234567", "HP:1234567"),
        # Already formatted for OMIM
        ("OMIM:246300", "OMIM:246300"),
        # National Cancer Institute Thesaurus
        ("ncit_987654", "NCIT:987654"),
        # Sequence Ontology
        ("so_0001234", "SO:0001234"),
        # HL7 FHIR
        ("hl7fhir_567", "HL7FHIR:567"),
        # GA4GH
        ("ga4gh_789", "GA4GH:789"),
    ]

    for code, expected in test_cases:
        assert process_code(code) == expected
