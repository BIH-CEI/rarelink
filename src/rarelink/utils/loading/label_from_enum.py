from rarelink_cdm.v2_0_0_dev0.datamodel import EnumDefinitionImpl

def fetch_label_from_enum(enum_class: EnumDefinitionImpl, code: str) -> str:
    """
    Fetches the label (description) for a given code from an EnumDefinitionImpl.

    Args:
        enum_class (EnumDefinitionImpl): The LinkML EnumDefinition class.
        code (str): The code for which to fetch the label.

    Returns:
        str: The label (description) for the code, or None if not found.
    """
    try:
        # Iterate over all attributes of the enum class
        for attr_name in dir(enum_class):
            if not attr_name.startswith("_"):  # Ignore private/internal attributes
                permissible_value = getattr(enum_class, attr_name, None)
                # Check if this is a permissible value and matches the code
                if (
                    hasattr(permissible_value, "text") and 
                    permissible_value.text == code
                ):
                    return permissible_value.description
    except Exception as e:
        print(f"Error fetching label for code '{code}' in enum '{enum_class.__name__}': {e}")
    return None  # Return None if no matching label is found
