import logging 

logger = logging.getLogger(__name__)

def get_highest_instance(data: list, instrument_name: str) -> dict:
    """
    Fetches the dictionary with the highest redcap_repeat_instance 
    for a specified redcap_repeat_instrument.

    Args:
        data (list): List of dictionaries from "repeated_elements".
        instrument_name (str): Name of the redcap_repeat_instrument to filter.

    Returns:
        dict: The dictionary with the highest redcap_repeat_instance, or None.
    """
    filtered_elements = [
        entry for entry in data if entry.get("redcap_repeat_instrument") == instrument_name
    ]
    if not filtered_elements:
        logger.warning(f"No entries found for instrument '{instrument_name}'.")
        return None

    return max(filtered_elements, key=lambda x: x.get("redcap_repeat_instance", 0), default=None)
