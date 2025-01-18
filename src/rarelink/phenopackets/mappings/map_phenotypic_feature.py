import logging
from phenopackets import PhenotypicFeature, OntologyClass, TimeElement, Evidence
from rarelink.utils.processor import DataProcessor
from google.protobuf.timestamp_pb2 import Timestamp

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
    
    # Fetching and preparation
    # --------------------------------------------------------------------------
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
            phenotypic_feature_data = phenotypic_feature_element.get(
                                                    "phenotypic_feature")
            if not phenotypic_feature_data:
                logger.warning("No phenotypic feature data found in "
                                "this element. Skipping.")
                continue
            
            # PhenotypicFeature.type
            # ------------------------------------------------------------------
            type_field = phenotypic_feature_data.get(
                processor.mapping_config["type_field"])
            type_field_label = processor.fetch_label(type_field)
            type = OntologyClass(
                id=type_field, 
                label=type_field_label)
            

            excluded_value = phenotypic_feature_data.get(
                processor.mapping_config["excluded_field"])
            excluded = None
            if excluded_value:
                mapped_value = processor.fetch_mapping_value(
                    "phenotypic_feature_status", excluded_value)
                if mapped_value == "true":
                    excluded = True
                elif mapped_value == "false":
                    excluded = False
                else:
                    excluded = None
            
            # PhenotypicFeature.onset ( -> prefer date over category)
            # ------------------------------------------------------------------
            onset_date= phenotypic_feature_data.get(
                processor.mapping_config["onset_date_field"])
            onset_age_field = phenotypic_feature_data.get(
                processor.mapping_config["onset_age_field"])
            onset = None 
            
            if onset_date:
                try:
                    timestamp = processor.process_date(onset_date)
                    if isinstance(timestamp, Timestamp):
                        onset = TimeElement(timestamp=timestamp)
                    else:
                        raise TypeError(
                            "Processed date is not a Timestamp object.")
                except Exception as e:
                    logger.error(f"Error processing onset date: {e}")
            
            if not onset and onset_age_field:
                try:
                    onset_label = processor.fetch_label(
                        onset_age_field, enum_class="AgeOfOnset")
                    onset_age = processor.process_code(
                        onset_age_field)
                    if onset_label:
                        onset = TimeElement(
                            ontology_class=OntologyClass(
                                id=onset_age,
                                label=onset_label)
                        )
                except Exception as e:
                    logger.error(f"Error processing onset age: {e}")
                    
            # PhenotypicFeature.resolution
            # ------------------------------------------------------------------
            resolution = None
            resolution_field = phenotypic_feature_data.get(
                processor.mapping_config["resolution_field"])
            if resolution_field: 
                try:
                    resolution_timestamp = processor.process_date(
                                                        resolution_field)
                    if isinstance(resolution_timestamp, Timestamp):
                        resolution = TimeElement(timestamp=resolution_timestamp)
                    else:
                        raise TypeError(
                            "Processed date is not a Timestamp object.")
                except Exception as e:
                    logger.error(f"Error processing resolution date: {e}")

            # PhenotypicFeature.severity
            # ------------------------------------------------------------------
            severity = None
            severity_field = phenotypic_feature_data.get(
                processor.mapping_config["severity_field"])
            severity_id = processor.process_code(severity_field)
            severity_label = processor.fetch_label(severity_field, 
                                                enum_class="PhenotypeSeverity")
            severity = OntologyClass(
                id=severity_id,
                label=severity_label
            )
            
            # PhenotypicFeature.evidence
            # ------------------------------------------------------------------
            evidence_id = phenotypic_feature_data.get(
                processor.mapping_config["evidence_field"]
            )
            if evidence_id:  
                evidence_label = processor.fetch_label(evidence_id)
                evidence = Evidence(
                    evidence_code=OntologyClass(
                        id=evidence_id,
                        label=evidence_label
                    )
                )
                evidence_list = [evidence]
            else:
                evidence_list = None

            # PhenotypicFeature.modifiers
            # ------------------------------------------------------------------
            modifiers = []
            # First Modifier: TemporalPattern
            modifier_temp_pattern_field = processor.mapping_config.get(
                "modifier_temp_pattern_field")
            if modifier_temp_pattern_field:
                temp_pattern_id = phenotypic_feature_data.get(
                    modifier_temp_pattern_field)
                if temp_pattern_id:
                    temp_pattern_label = processor.fetch_label(
                        temp_pattern_id, enum_class="TemporalPattern")
                    modifiers.append(OntologyClass(
                        id=processor.process_code(temp_pattern_id),
                        label=temp_pattern_label
                    ))
                        
            # Other Modifiers: Clinical Modifiers 1 -3, Causing Agent [NCBITaxon] 
            # and BodySite [SNOMEDCT]
            modifier_fields = [
                processor.mapping_config.get("modifier_field_1"),
                processor.mapping_config.get("modifier_field_2"),
                processor.mapping_config.get("modifier_field_3"),
                processor.mapping_config.get("modifier_field_4"),
                processor.mapping_config.get("modifier_field_5")
            ]

            for field in modifier_fields:
                modifier_id = phenotypic_feature_data.get(field)
                if modifier_id:
                    modifier_label = processor.fetch_label(modifier_id)
                    modifiers.append(OntologyClass(
                        id=modifier_id,
                        label=modifier_label
                    ))

            if not modifiers:
                modifiers = None

            # Create PhenotypicFeature
            # ------------------------------------------------------------------            
            phenotypic_feature = PhenotypicFeature(
                type=type,
                excluded=excluded,
                onset=onset,
                resolution=resolution,
                severity=severity,
                evidence=evidence_list,
                modifiers=modifiers
            )
            
            phenotypic_features.append(phenotypic_feature)
        
        return phenotypic_features
                    
    except Exception as e:
        logger.error(f"Failed to map phenotypic feature: {e}")
        raise

            
    
