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
from rarelink.utils.loading import get_nested_field

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

    def fetch_label(self, code: str):
        return fetch_label_directly(code)

    def get_mapping(self, mapping_name: str):
        return get_mapping_by_name(mapping_name)
