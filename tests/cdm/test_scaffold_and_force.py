"""
Scaffold behavior: clone previous version → new version, then allow --force re-run
without 'copying onto myself' errors or __pycache__ collisions.
"""
from pathlib import Path

from rarelink.cdm.codegen import scaffold_version_package

def test_scaffold_force_overwrite(tmp_path: Path, monkeypatch):
    """
    Create a fake previous version, scaffold a new version, and re-run with force=True.
    """
    root = tmp_path / "rarelink_cdm"
    prev = root / "v2_0_2"
    (prev / "schema_definitions").mkdir(parents=True)
    (prev / "python_datamodel").mkdir(parents=True)
    (prev / "schema_definitions" / "rarelink_types.yaml").write_text("id: x\nname: rarelink_types\nimports:\n- linkml:types\n", encoding="utf-8")
    (prev / "python_datamodel" / "__init__.py").write_text("# old init", encoding="utf-8")
    (prev / "__init__.py").write_text("# old top init", encoding="utf-8")

    # First run: v2_0_2 from v2_0_2
    res1 = scaffold_version_package("v2_0_2", root, from_version="v2_0_2", force=False)  # noqa: F841
    assert (root / "v2_0_2").exists()
    assert (root / "v2_0_2" / "schema_definitions" / "rarelink_code_systems.yaml").exists()
    assert (root / "v2_0_2" / "python_datamodel" / "rarelink_code_systems.py").exists()

    # Second run with force should delete and recreate cleanly
    res2 = scaffold_version_package("v2_0_2", root, from_version="v2_0_2", force=True)  # noqa: F841
    assert (root / "v2_0_2" / "python_datamodel" / "rarelink_code_systems.py").exists()
