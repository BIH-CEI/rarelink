import pytest

from rarelink.preprocessing import preprocess_redcap_code


@pytest.fixture
def resources():
    return [
        "CodeSystem(name='SNOMED CT', namespace_prefix='SNOMED')",
        "CodeSystem(name='MONDO', namespace_prefix='MONDO')",
    ]

@pytest.mark.parametrize("input, expected", [
    ("snomed_410605003", "Coding(system=CodeSystem(name='SNOMED CT', namespace_prefix='SNOMED'), code='410605003')"),
    ("mondo_0968976", "Coding(system=CodeSystem(name='MONDO', namespace_prefix='MONDO'), code='0968976')"),
])
def test_preprocess_redcap_code(input, resources, expected):
    assert preprocess_redcap_code(input, resources) == expected

