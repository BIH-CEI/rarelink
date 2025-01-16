from rarelink.utils.processing.dates import (
    date_to_timestamp, 
    create_time_element_from_date
)
from rarelink.utils.processing.codes import (
    process_redcap_code, 
    fetch_label_directly
)
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets.mapping_dicts import (
    get_mapping_by_name
)
from rarelink.utils.loading import get_nested_field, fetch_description_from_label_dict
import logging

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, mapping_config: dict):
        self.mapping_config = mapping_config

    def get_field(self, data: dict, field_name: str):
        """
        Fetches a field value from nested input data based on the mapping configuration.

        Args:
            data (dict): Input data dictionary.
            field_name (str): The name of the field to fetch.

        Returns:
            Any: The value of the requested field or None if not found.
        """
        field_path = self.mapping_config.get(field_name)
        if field_path is None:
            logger.warning(f"Field '{field_name}' not found in mapping_config.")
            return None
        return get_nested_field(data, field_path)


    def process_date(self, date_input: str):
        """
        Converts a date string into a timestamp.

        Args:
            date_input (str): The date string to process.

        Returns:
            int: The timestamp representation of the date.
        """
        return date_to_timestamp(date_input)

    def process_time_element(self, date_input: str):
        """
        Converts a date string into a time element.

        Args:
            date_input (str): The date string to process.

        Returns:
            dict: A dictionary representing the time element.
        """
        return create_time_element_from_date(date_input)

    def process_code(self, code: str):
        """
        Processes a REDCap code into the expected format.

        Args:
            code (str): The code to process.

        Returns:
            str: The processed code.
        """
        return process_redcap_code(code)

    def fetch_label(self, code: str, enum_class=None):
        """
        Fetches the label (description) for a given code.

        Args:
            code (str): The code for which to fetch the label.
            enum_class (EnumDefinitionImpl, optional): The EnumDefinition class to fetch labels from.

        Returns:
            str: The label (description) for the code, or None if not found.
        """
        if enum_class:
            return self.load_label(code, enum_class)
        return fetch_label_directly(code)

    def load_label(self, code: str, enum_class):
        """
        Loads the label for a given code from an EnumDefinition class.

        Args:
            code (str): The code for which to load the label.
            enum_class (EnumDefinitionImpl): The EnumDefinition class to fetch labels from.

        Returns:
            str: The label (description) for the code, or None if not found.
        """
        try:
            return fetch_description_from_label_dict(enum_class, code)
        except KeyError:
            return None

    def fetch_mapping_value(self, mapping_name: str, code: str):
        """
        Fetches the mapped value for a code using the specified mapping name.

        Args:
            mapping_name (str): The name of the mapping to use.
            code (str): The code to look up in the mapping.

        Returns:
            str: The mapped value, or None if not found.
        """
        try:
            mapping = get_mapping_by_name(mapping_name)
            return mapping.get(code, None)
        except KeyError:
            return None

    def get_mapping(self, mapping_name: str):
        """
        Retrieves a mapping dictionary by its name.

        Args:
            mapping_name (str): The name of the mapping to retrieve.

        Returns:
            dict: The mapping dictionary.
        """
        return get_mapping_by_name(mapping_name)
