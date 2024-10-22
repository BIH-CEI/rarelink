
import os
from pathlib import Path


def pytest_ignore_collect(collection_path, config):
    # Ignore any conf.py file in the submodules
    if collection_path.name == "conf.py" and (
        "submodules/phenopacket_mapper/docs" in str(collection_path) or
        "submodules/rd-cdm/docs" in str(collection_path)
    ):
        return True
    return False