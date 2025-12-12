"""
Scaffold behavior: clone previous version → new version, then allow --force re-run
without 'copying onto myself' errors or __pycache__ collisions.
"""
from pathlib import Path

from rarelink.rd_cdm.codegen import scaffold_version_package
from rarelink._versions import RD_CDM_LABEL


def test_scaffold_force_overwrite(tmp_path: Path, monkeypatch):
    """
    Create a fake previous version, scaffold a new version, and re-run with force=True.
    """
    root = tmp_path / "rarelink_cdm"
    prev = root / RD_CDM_LABEL
    (prev / "schema_definitions").mkdir(parents=True)
    (prev / "python_datamodel").mkdir(parents=True)
    (prev / "schema_definitions" / "rarelink_types.yaml").write_text(
        "id: x\nname: rarelink_types\nimports:\n- linkml:types\n",
        encoding="utf-8",
    )
    (prev / "python_datamodel" / "__init__.py").write_text(
        "# old init",
        encoding="utf-8",
    )
    (prev / "__init__.py").write_text("# old top init", encoding="utf-8")

    # First run: scaffold RD_CDM_LABEL from RD_CDM_LABEL
    res1 = scaffold_version_package(
        RD_CDM_LABEL,
        root,
        from_version=RD_CDM_LABEL,
        force=False,
    )  # noqa: F841
    assert (root / RD_CDM_LABEL).exists()
    assert (root / RD_CDM_LABEL / "schema_definitions" / "rarelink_code_systems.yaml").exists()
    assert (root / RD_CDM_LABEL / "python_datamodel" / "rarelink_code_systems.py").exists()

    # Second run with force should delete and recreate cleanly
    res2 = scaffold_version_package(
        RD_CDM_LABEL,
        root,
        from_version=RD_CDM_LABEL,
        force=True,
    )  # noqa: F841
    assert (root / RD_CDM_LABEL / "python_datamodel" / "rarelink_code_systems.py").exists()
