"""Each repeated element must map to its own entity."""
from __future__ import annotations

import pytest

from rarelink.phenopackets.mappings.disease_mapper import DiseaseMapper
from rarelink.phenopackets.mappings.phenotypic_feature_mapper import (
    PhenotypicFeatureMapper,
)
from rarelink.utils.label_fetching import set_label_dict
from rarelink.utils.processor import DataProcessor

DOB = "2020-01-05"
DISEASE_TERMS = ["ORPHA:459345", "MONDO:0019499", "ICD10CM:Z82.3", "MONDO:0002367"]
HPO_TERMS = ["HP:0001250", "HP:0001263", "HP:0000822", "HP:0001279"]


@pytest.fixture(autouse=True)
def _no_network():
    """Resolve labels locally so these tests never hit BioPortal."""
    set_label_dict({term: term for term in DISEASE_TERMS + HPO_TERMS})
    yield
    set_label_dict({})


def _record(instrument: str, inner_key: str, field: str, values: list[str]) -> dict:
    return {
        "record_id": "101",
        "personal_information": {"snomedct_184099003": DOB},
        "repeated_elements": [
            {
                "redcap_repeat_instrument": instrument,
                "redcap_repeat_instance": index + 1,
                inner_key: {field: value},
            }
            for index, value in enumerate(values)
        ],
    }


@pytest.mark.parametrize("inner_key", ["disease", "rarelink_5_disease"])
def test_each_repeated_disease_maps_to_its_own_term(inner_key):
    """Four distinct repeated diseases yield four distinct Disease terms."""
    record = _record("rarelink_5_disease", inner_key,
                     "snomedct_64572001_ordo", DISEASE_TERMS)
    config = {
        "instrument_name": "rarelink_5_disease",
        "redcap_repeat_instrument": "rarelink_5_disease",
        "term_field_1": "snomedct_64572001_ordo",
        "multi_entity": True,
    }

    diseases = DiseaseMapper(DataProcessor(config)).map(record, dob=DOB)

    assert [d.term.id for d in diseases] == DISEASE_TERMS


def test_each_repeated_phenotype_keeps_its_own_type():
    """Four distinct phenotype elements keep their own types."""
    record = _record("phenotypic_features", "phenotypic_features",
                     "hpo_term", HPO_TERMS)
    config = {
        "instrument_name": "phenotypic_features",
        "redcap_repeat_instrument": "phenotypic_features",
        "data_model": "custom",
        "type_field": "hpo_term",
        "multi_entity": True,
    }

    features = PhenotypicFeatureMapper(DataProcessor(config)).map(record, dob=DOB)

    assert [f.type.id for f in features] == HPO_TERMS


def test_type_field_and_type_fields_agree():
    """The singular and plural config spellings produce the same result."""
    record = _record("phenotypic_features", "phenotypic_features",
                     "hpo_term", HPO_TERMS)
    base = {
        "instrument_name": "phenotypic_features",
        "redcap_repeat_instrument": "phenotypic_features",
        "data_model": "custom",
        "multi_entity": True,
    }

    singular = PhenotypicFeatureMapper(
        DataProcessor({**base, "type_field": "hpo_term"})).map(record, dob=DOB)
    plural = PhenotypicFeatureMapper(
        DataProcessor({**base, "type_fields": ["hpo_term"]})).map(record, dob=DOB)

    assert [f.type.id for f in singular] == [f.type.id for f in plural]


def test_default_code_systems_container_yields_resources():
    """A default-constructed container still populates metaData.resources."""
    from rarelink.phenopackets.mappings.metadata_mapper import (
        _filter_fields_by_prefixes,
    )
    from rarelink.rarelink_cdm import get_codesystems_container_class

    container = get_codesystems_container_class()()
    resources = _filter_fields_by_prefixes(container, {"HP", "MONDO", "SNOMEDCT"})

    assert resources, "default CodeSystemsContainer produced no resources"
    assert all(r.name and r.version for r in resources)
    assert {r.namespace_prefix for r in resources} >= {"HP", "MONDO", "SNOMEDCT"}
