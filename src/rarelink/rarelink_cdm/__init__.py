from __future__ import annotations

from importlib import resources
from pathlib import Path

from rarelink._versions import DATA_DICT_LABEL
from .python_datamodel import CodeSystemsContainer

__all__ = [
    "CodeSystemsContainer",
    "get_codesystems_container_class",
    "get_data_dictionary_path",
]


def get_codesystems_container_class():
    """
    Return CodeSystemsContainer from the built-in CDM datamodel.
    """
    return CodeSystemsContainer


def get_data_dictionary_path() -> Path:
    """
    Return the path to the packaged RareLink-CDM data dictionary CSV.

    The file name is expected to follow the pattern:
        rarelink_cdm_datadictionary - vX_Y_Z.csv
    where X_Y_Z is derived from DATA_DICT_LABEL.
    """
    fname = f"rarelink_cdm_datadictionary - {DATA_DICT_LABEL}.csv"
    return resources.files("rarelink").joinpath("rarelink_cdm", fname)
