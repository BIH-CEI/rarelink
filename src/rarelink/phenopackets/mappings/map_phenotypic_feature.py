import logging
from phenopackets import PhenotypicFeature, OntologyClass # TimeElement
from rarelink.utils.processor import DataProcessor
# from google.protobuf.timestamp_pb2 import Timestamp

logger = logging.getLogger(__name__)

def map_phenotypic_features(
    data: dict, 
    processor: DataProcessor) -> list:
    """
    Maps phenotype data to the Phenopacket schema Disease block fetching the 
    data elements from the repeated elements in the input data.

    Args:
        data (dict): Input data from the RareLink-CDM schema (or similar).
        processor (DataProcessor): Handles all data processing logic.

    Returns:
        list: A list of Phenopacket PhenotypicFeature blocks.
    """
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
    
    try:
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.warning("No repeated elements found in the data.")
            return []

        # Filter relevant phenotypic_feature elements
        phenotypic_feature_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
    
        phenotypic_features = []
        for phenotypic_feature_element in phenotypic_feature_elements:
            phenotypic_feature_data = phenotypic_feature_element.get("phenotypic_feature")
            if not phenotypic_feature_data:
                logger.warning("No phenotypic feature data found in "
                                "this element. Skipping.")
                continue
            
            type_field = phenotypic_feature_data.get(
                processor.mapping_config["type_field"])
            type_field_label = processor.fetch_label(type_field)
            type = OntologyClass(
                id=type_field, 
                label=type_field_label)
            
            phenotypic_feature = PhenotypicFeature(
                type=type
            )
            
            phenotypic_features.append(phenotypic_feature)
        
        return phenotypic_features
                    
    except Exception as e:
        logger.error(f"Failed to map diseases: {e}")
        raise

            
            
            
#     "type_field": "snomed_8116006",
#     "excluded_field": "snomed_363778006",
#     "onset_field_2": "hp_0003674",
#     "onset_field_1": "snomed_8116006_onset",
#     "resolution_field": "snomed_8116006_resolution",
#     "modifier_temp_pattern_field_": "hp_0011008",
#     "severity_field": "hp_0012824",
#     "modifier_field_1": "hp_0012823_hp1",
#     "modifier_field_2": "hp_0012823_hp2",
#     "modifier_field_3": "hp_0012823_hp3",
#     "modifier_field_4": "hp_0012823_ncbitaxon",
#     "modifier_field_5": "hp_0012823_snomed",
#     "evidence_field": "phenotypicfeature_evidence"
# }


            
    
