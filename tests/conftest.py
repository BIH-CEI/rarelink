
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

def set_bioportal_api_key():
    """
    Ensures the BioPortal API key is available for tests by setting it
    as an environment variable or creating the Oaklib configuration file.
    """
    # Fetch the API key from an environment variable or a secret
    api_key = os.getenv("BIOPORTAL_API_KEY")
    if not api_key:
        raise ValueError("BioPortal API key not found. Please set the BIOPORTAL_API_KEY environment variable.")

    # Option 1: Set the environment variable for Oaklib
    os.environ["BIOPORTAL_API_KEY"] = api_key

    # Option 2: Create the configuration file Oaklib expects
    config_dir = Path.home() / ".config" / "ontology-access-kit"
    config_dir.mkdir(parents=True, exist_ok=True)
    config_file = config_dir / "bioportal-apikey.txt"
    config_file.write_text(api_key)