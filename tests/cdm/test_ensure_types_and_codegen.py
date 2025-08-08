"""
End-to-end-ish test: writes schema, ensures rarelink_types.yaml exists,
and runs PythonGenerator to produce dataclasses.
"""
from pathlib import Path
import yaml

from rarelink.cdm.codegen import (
    generate_python_classes,
    _ensure_rarelink_types
)

def test_generate_python_classes(tmp_path: Path, monkeypatch):
    """
    Build a tiny schema on disk and run the LinkML Python generator.
    """
    # Build a schema with at least HP present
    schema = {
        "id": "https://github.com/BIH-CEI/RareLink/code_systems_data",
        "name": "code_systems_data",
        "prefixes": {"linkml": "https://w3id.org/linkml/"},
        "imports": ["linkml:types"],
        "default_range": "string",
        "enums": {
            "HP": {"description": "Human Phenotype Ontology", "code_set": "https://www.human-phenotype-ontology.org", "code_set_version": "2025-01-01"}
        },
        "classes": {
            "CodeSystemsContainer": {
                "attributes": {
                    "hpo": {"description": "Human Phenotype Ontology", "range": "HP", "required": True}
                }
            }
        },
    }

    schema_dir = tmp_path / "pkg" / "schema_definitions"
    schema_dir.mkdir(parents=True)
    schema_path = schema_dir / "rarelink_code_systems.yaml"
    schema_path.write_text(yaml.safe_dump(schema, sort_keys=False), encoding="utf-8")

    # Ensure rarelink_types.yaml exists (stubbed by helper)
    _ensure_rarelink_types(schema_dir)

    datamodel_dir = tmp_path / "pkg" / "datamodel"
    mod_path = generate_python_classes(schema_path, datamodel_dir)

    assert mod_path.exists()
    text = mod_path.read_text(encoding="utf-8")
    assert "class CodeSystemsContainer" in text
