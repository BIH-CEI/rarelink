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
from rarelink.utils.loading import get_nested_field, fetch_label_from_enum

class DataProcessor:
    def __init__(self, mapping_config: dict):
        self.mapping_config = mapping_config

    def get_field(self, data: dict, field_name: str):
        return get_nested_field(data, self.mapping_config[field_name])

    def process_date(self, date_input: str):
        return date_to_timestamp(date_input)

    def process_time_element(self, date_input: str):
        return create_time_element_from_date(date_input)

    def process_code(self, code: str):
        return process_redcap_code(code)

    def fetch_label(self, code: str, enum_class=None):
        """
        Fetches the label for a given code. If an enum class is provided,
        it fetches the label directly from the value set.

        Args:
            code (str): The code for which to fetch the label.
            enum_class (EnumDefinitionImpl): The EnumDefinition class to 
            fetch labels from.

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
            enum_class (EnumDefinitionImpl): The EnumDefinition class to 
            fetch labels from.

        Returns:
            str: The label (description) for the code, or None if not found.
        """
        label = fetch_label_from_enum(enum_class, code)
        if label:
            return label
        else:
            return None

    def get_mapping(self, mapping_name: str):
        return get_mapping_by_name(mapping_name)
