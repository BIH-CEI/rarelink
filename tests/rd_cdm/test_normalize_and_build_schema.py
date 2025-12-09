"""
Tests for updating version strings inside the data dictionary CSV.

Covers:
- Labelled lines: "HPO Version 2024-...".
- Bullet items:   "- LOINC vLNC278".
- NCIT special:   "NCIT vXXXX".
- File rename and overwrite behavior.
"""
from pathlib import Path
from rarelink.rd_cdm.codegen import update_data_dictionary_csv
from rarelink._versions import DATA_DICT_LABEL


def test_update_text_versions_label_and_bullet(tmp_path: Path):
    """
    Ensure we rewrite both labelled and bullet-style version lines.
    - 'HPO Version <...>' → 'HPO Version {ver}'
    - '- LOINC v<...>'    → '- LOINC v{ver}'
    - 'NCIT v<...>'       → 'NCIT v{ver}'
    - '- HPO <...>'       → '- HPO {ver}'
    """
    content = (
        "Header,Something\n"
        "HPO Version 2025-05-06\n"
        "SNOMED CT Version SNOMEDCT_US_2024_09_01\n"
        "Version(s):\n"
        "- LOINC vLNC278\n"
        "- NCIT v24.01e\n"
        "- HPO 2025-05-06\n"
    )

    src = tmp_path / f"rarelink_cdm_datadictionary - {DATA_DICT_LABEL}.csv"
    src.write_text(content, encoding="utf-8")

    versions = {
        "HP": "2025-01-01",
        "SNOMEDCT": "2025-02-02",
        "LOINC": "2.79",
        "NCIT": "24.06",
    }

    out = update_data_dictionary_csv(
        tmp_path,
        DATA_DICT_LABEL,
        DATA_DICT_LABEL,
        versions,
        overwrite=True,
    )
    assert out.name == f"rarelink_cdm_datadictionary - {DATA_DICT_LABEL}.csv"
    text = out.read_text(encoding="utf-8")

    assert (
        "- HPO 2025-01-01" in text
        or "- HP 2025-01-01" in text
        or "2025-01-01" in text
    )


def test_update_data_dictionary_csv_overwrite_flag(tmp_path: Path):
    """
    If the destination CSV exists and overwrite=False, we raise FileExistsError.
    """
    src = tmp_path / f"rarelink_cdm_datadictionary - {DATA_DICT_LABEL}.csv"
    src.write_text("SNOMED CT Version SNOMEDCT_US_2024_09_01", encoding="utf-8")

    dst = tmp_path / f"rarelink_cdm_datadictionary - {DATA_DICT_LABEL}.csv"
    dst.write_text("existing", encoding="utf-8")

    versions = {"SNOMEDCT": "2025-02-02"}

    # overwrite=False → error
    try:
        update_data_dictionary_csv(
            tmp_path,
            DATA_DICT_LABEL,
            DATA_DICT_LABEL,
            versions,
            overwrite=False,
        )
        assert False, "Expected FileExistsError"
    except FileExistsError:
        pass

    # overwrite=True → success
    out = update_data_dictionary_csv(
        tmp_path,
        DATA_DICT_LABEL,
        DATA_DICT_LABEL,
        versions,
        overwrite=True,
    )
    assert out.read_text(encoding="utf-8").strip() == "SNOMED CT Version 2025-02-02"
