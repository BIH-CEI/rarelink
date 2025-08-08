"""
Tests for rd-cdm YAML normalization and schema building with version overlay.

We avoid network/dynamic imports by writing a temp code_systems.yaml
and monkeypatching the path resolver.
"""
from pathlib import Path
import yaml

from rarelink.cdm.codegen import (
    build_schema_with_versions,
)

def test_build_schema_with_versions_overlays_only_versions(tmp_path: Path, monkeypatch):
    """
    Ensure schema keeps exact enum keys/URLs/descriptions and only changes code_set_version
    from RD-CDM's code_systems.yaml.
    """
    # Minimal rd-cdm-ish structure:
    data = {
        "code_systems": [
            {"key": "HP", "name": "Human Phenotype Ontology", "url": "https://www.human-phenotype-ontology.org", "version": "2025-01-01"},
            {"key": "SNOMEDCT", "name": "SNOMED", "url": "http://snomed.info/sct", "version": "2025-02-02"},
            {"key": "NCIT", "name": "NCI Thesaurus", "url": "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl", "version": "24.06"},
        ]
    }
    inst_dir = tmp_path / "rd_cdm" / "instances" / "v2_0_2"
    inst_dir.mkdir(parents=True)
    y = inst_dir / "code_systems.yaml"
    y.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    def fake_path(ver: str) -> Path:
        assert ver == "v2_0_2"
        return y

    monkeypatch.setattr("rarelink.cdm.codegen._rdcdm_code_systems_yaml", fake_path)

    schema = build_schema_with_versions("v2_0_2")
    enums = schema["enums"]

    assert enums["HP"]["code_set"] == "https://www.human-phenotype-ontology.org"
    assert enums["HP"]["code_set_version"] == "2025-01-01"

    assert enums["SNOMEDCT"]["code_set"] == "http://snomed.info/sct"
    assert enums["SNOMEDCT"]["code_set_version"] == "2025-02-02"

    assert enums["NCIT"]["code_set"].startswith("http://ncicb")
    assert enums["NCIT"]["code_set_version"] == "24.06"

    # GA4GH (not provided) remains blank version but exists in base schema
    assert "GA4GH" in enums
    assert enums["GA4GH"]["code_set_version"] == ""
