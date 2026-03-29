# tests/phenopackets/adapter/test_ontology_routing_adapter.py
"""
Tests for the ontology routing adapter.

Three tests cover the essential behaviour:
  1. HP-coded elements route to phenotypicFeatures (unchanged)
  2. MONDO-coded elements route to diseases (normalized)
  3. Elements with no routable code are skipped without error

Uses the exact data shape from the CIEINR test fixture.
"""

from rarelink.phenopackets.adapter.ontology_routing_adapter import (
    apply_ontology_routing,
    get_routed_disease_dicts,
    get_routed_phenotypic_elements,
)

# ---------------------------------------------------------------------------
# Shared config and fixture
# ---------------------------------------------------------------------------

ROUTING_CONFIG = {
    "ontology_routing": {
        "enabled": True,
        "instruments": ["infections_initial_form"],
        "scan_fields": {
            "infections_initial_form": [
                "snomedct_21483005",   # CNS → HP codes
                "snomedct_127856007",  # Skin → HP or MONDO
                "snomedct_20139000",   # Respiratory → HP codes
            ],
        },
        "onset_fields": {
            "infections_initial_form": ["infection_date", "infection_date_2"],
        },
    }
}

# Three infections elements:
#   #1 — HP code     → phenotypicFeatures
#   #2 — MONDO code  → diseases
#   #3 — SNOMED value (no routable prefix) → skipped
RECORD = {
    "record_id": "test_1",
    "repeated_elements": [
        {
            "redcap_repeat_instrument": "infections_initial_form",
            "redcap_repeat_instance": 1,
            "infections_initial_form": {
                "type_of_infection": "snomedct_21483005",
                "snomedct_21483005": "hp_0002383",        # HP → phenotypicFeatures
                "infection_severity": "hp_0012826",
                "infection_date": "2022-02-01",
            },
        },
        {
            "redcap_repeat_instrument": "infections_initial_form",
            "redcap_repeat_instance": 2,
            "infections_initial_form": {
                "type_of_infection": "snomedct_127856007",
                "snomedct_127856007": "mondo_0043653",    # MONDO → diseases
                "infection_severity": "hp_0012826",
                "infection_date": "2023-02-01",
            },
        },
        {
            "redcap_repeat_instrument": "infections_initial_form",
            "redcap_repeat_instance": 3,
            "infections_initial_form": {
                "type_of_infection": "snomedct_20139000",
                "snomedct_20139000": "snomedct_233604007",  # SNOMED → skip
                "infection_date": "2024-01-01",
            },
        },
    ],
}


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_hp_element_routes_to_phenotypic_features():
    """HP-coded element ends up in phenotypicFeatures, unchanged."""
    data = apply_ontology_routing(RECORD, ROUTING_CONFIG)
    pf = get_routed_phenotypic_elements(data)

    assert len(pf) == 1
    assert pf[0]["redcap_repeat_instance"] == 1
    assert pf[0]["infections_initial_form"]["snomedct_21483005"] == "hp_0002383"


def test_mondo_element_routes_to_diseases_normalized():
    """MONDO-coded element ends up in diseases, normalized to term_field_1 convention."""
    data = apply_ontology_routing(RECORD, ROUTING_CONFIG)
    diseases = get_routed_disease_dicts(data)

    assert len(diseases) == 1
    d = diseases[0]
    assert d["term_field_1"] == "mondo_0043653"
    assert d["onset_date_field"] == "2023-02-01"
    assert d["__source_instance"] == 2


def test_element_with_no_routable_code_is_skipped():
    """Element with an unrecognised prefix is not routed and original data is untouched."""
    data = apply_ontology_routing(RECORD, ROUTING_CONFIG)

    # Only HP (instance 1) and MONDO (instance 2) were routed
    assert len(get_routed_phenotypic_elements(data)) == 1
    assert len(get_routed_disease_dicts(data)) == 1

    # Original list untouched — no mutation
    assert len(data["repeated_elements"]) == 3