# src/rarelink/_versions.py
from __future__ import annotations

from importlib.metadata import version as _pkg_version

__all__ = [
    "RARELINK_VERSION",
    "RARELINK_LABEL",
    "DATA_DICT_VERSION",
    "DATA_DICT_LABEL",
    "FHIR_IG_VERSION",
    "FHIR_IG_LABEL",
]

# -------------------------------
# 1) RareLink package version
# -------------------------------
RARELINK_VERSION: str = _pkg_version("rarelink")
RARELINK_LABEL: str = RARELINK_VERSION.replace(".", "_")

# -------------------------------
# 2) REDCap data dictionary version
# -------------------------------
DATA_DICT_VERSION: str = RARELINK_VERSION
DATA_DICT_LABEL: str = "v" + DATA_DICT_VERSION.replace(".", "_")

# -------------------------------
# 3) FHIR IG version
# -------------------------------
FHIR_IG_VERSION: str = "2.0.0"
FHIR_IG_LABEL: str = FHIR_IG_VERSION
