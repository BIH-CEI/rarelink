from rarelink_cdm.v2_0_0_dev0.datamodel import Optional
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets import label_dicts

def fetch_description_from_label_dict(enum_name: str, code: str) -> Optional[str]:
    """
    Fetch the description for a specific code from a pre-defined label dictionary.

    Args:
        enum_name (str): The name of the enum (e.g., "GenderIdentity").
        code (str): The code for which to find the description.

    Returns:
        Optional[str]: The description if found, or None otherwise.
    """
    enum_dict = label_dicts.get(enum_name)
    if enum_dict:
        return enum_dict.get(code)
    return None