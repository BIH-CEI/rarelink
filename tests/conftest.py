def pytest_ignore_collect(collection_path, config):
    path_str = str(collection_path)

    # Ignore conf.py files in specific docs folders
    if collection_path.name == "conf.py" and (
        "submodules/phenopacket_mapper/docs" in path_str or
        "submodules/rd-cdm/docs" in path_str
    ):
        return True

    # Ignore any files in the rarelink/rarelink_cdm/datamodel folder
    if "rarelink/rarelink_cdm/datamodel" in path_str:
        return True

    # Ignore all files in the rd-cdm submodule
    if "submodules/rd-cdm" in path_str:
        return True

    return False
