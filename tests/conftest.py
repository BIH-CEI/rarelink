import os
from pathlib import Path

def pytest_ignore_collect(collection_path, config):
    path_str = str(collection_path)
    
    # Ignore conf.py files in specific docs folders
    if collection_path.name == "conf.py" and (
        "submodules/phenopacket_mapper/docs" in path_str or
        "submodules/rd-cdm/docs" in path_str
    ):
        return True

    # Ignore any files in the rarelink_cdm/v2_0_2/datamodel folder
    if "rarelink_cdm/v2_0_2/datamodel" in path_str:
        return True

    # Ignore all files in the rd-cdm submodule
    if "submodules/rd-cdm" in path_str:
        return True

    return False

def set_bioportal_api_key():
    """
    Ensures the BioPortal API key is available for tests by setting it
    as an environment variable
    """
    api_key = os.getenv("BIOPORTAL_API_KEY")
    if not api_key:
        raise ValueError("BioPortal API key not found. Please set the BIOPORTAL_API_KEY environment variable.")

    os.environ["BIOPORTAL_API_KEY"] = api_key
    config_dir = Path.home() / ".config" / "ontology-access-kit"
    config_dir.mkdir(parents=True, exist_ok=True)
    config_file = config_dir / "bioportal-apikey.txt"
    config_file.write_text(api_key)
