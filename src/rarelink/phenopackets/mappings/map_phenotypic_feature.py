import logging
from typing import List, Optional, Callable
from phenopackets import PhenotypicFeature, OntologyClass
from rarelink.utils.processor import DataProcessor
from rarelink.phenopackets.adapter.multi_onset import multi_onset_adapter
from rarelink.phenopackets.mappings.utils.utils_phenotypic_feature import (
    _extract_evidence,
    _extract_excluded_status,
    _extract_modifiers,
    _extract_onset,
    _extract_resolution,
    _extract_severity,
    _determine_data_model,
    _get_data_elements,
    _get_infection_types,
    _get_single_type    
)

logger = logging.getLogger(__name__)

def map_phenotypic_features(
    data: dict, 
    processor: DataProcessor,
    dob: str = None
) -> List[PhenotypicFeature]:
    """
    Maps phenotype data to Phenopacket PhenotypicFeature blocks.
    Supports multiple instruments and handles both infections and standard data models.
    
    Args:
        data (dict): Input data.
        processor (DataProcessor): Data processor with mapping configuration.
        dob (str, optional): Date of birth (for age calculations).
    
    Returns:
        List[PhenotypicFeature]: List of mapped phenotypic feature blocks.
    """
    mapping_config = processor.mapping_config
    # Get advanced instrument configs or a simple instrument list.
    instrument_configs = mapping_config.get("instrument_configs", {})
    instruments: List[tuple[str, DataProcessor]] = []
    
    if instrument_configs:
        logger.debug(f"Using instrument-specific configs for {len(instrument_configs)} instruments")
        for instrument_name, config in instrument_configs.items():
            temp_proc = DataProcessor(mapping_config={
                **mapping_config,  # Base config
                **config,          # Instrument-specific overrides
                "redcap_repeat_instrument": instrument_name,
                "current_instrument": instrument_name
            })
            instruments.append((instrument_name, temp_proc))
    else:
        primary_instrument = mapping_config.get("redcap_repeat_instrument", "")
        additional_instruments = mapping_config.get("additional_instruments", [])
        all_instruments = [primary_instrument] + additional_instruments
        all_instruments = [i for i in all_instruments if i and i != "__dummy__"]
        if not all_instruments:
            logger.debug("No valid instrument names for phenotypic features")
            return []
        logger.debug(f"Processing {len(all_instruments)} instruments: {all_instruments}")
        for instrument_name in all_instruments:
            # Use the same processor for all instruments in this case.
            processor.mapping_config["current_instrument"] = instrument_name
            instruments.append((instrument_name, processor))
    
    all_features: List[PhenotypicFeature] = []
    # Process each instrument
    for instrument_name, proc in instruments:
        proc.mapping_config["current_instrument"] = instrument_name
        model = _determine_data_model(proc, instrument_name)
        logger.debug(f"Using data model: {model} with instrument: {instrument_name}")
        # Choose the type extractor based on the model
        type_extractor: Callable[[dict, DataProcessor], List[str]] = (
            _get_infection_types if model == "infections" else _get_single_type
        )
        features = _map_features(data, proc, dob, type_extractor)
        if features:
            all_features.extend(features)
            logger.debug(f"Added {len(features)} features from instrument {instrument_name}")
    
    logger.debug(f"Total phenotypic features mapped: {len(all_features)}")
    return all_features

def _create_phenotypic_feature(
    feature_type: str, 
    feature_data: dict,
    processor: DataProcessor,
    dob: str = None
) -> Optional[PhenotypicFeature]:
    """
    Creates a PhenotypicFeature object from the given data.
    
    Args:
        feature_type (str): Type value.
        feature_data (dict): Data for the feature.
        processor (DataProcessor): Data processor.
        dob (str, optional): Date of birth.
    
    Returns:
        Optional[PhenotypicFeature]: The feature, or None.
    """
    type_id = processor.process_code(feature_type)
    type_label = processor.fetch_label(feature_type)
    type_obj = OntologyClass(id=type_id, label=type_label or "Unknown Phenotypic Feature")
    
    excluded = _extract_excluded_status(feature_data, processor)
    onset = _extract_onset(feature_data, processor, dob)
    resolution = _extract_resolution(feature_data, processor, dob)
    severity = _extract_severity(feature_data, processor)
    evidence = _extract_evidence(feature_data, processor)
    modifiers = _extract_modifiers(feature_data, processor)
    
    return PhenotypicFeature(
        type=type_obj,
        excluded=excluded,
        onset=onset,
        resolution=resolution,
        severity=severity,
        evidence=evidence,
        modifiers=modifiers if modifiers else None
    )


def _map_features(
    data: dict,
    processor: DataProcessor,
    dob: str,
    type_extractor: Callable[[dict, DataProcessor], List[str]]
) -> List[PhenotypicFeature]:
    """
    Generic function that extracts data elements and applies a type extractor to produce features.
    
    Args:
        data (dict): Input data.
        processor (DataProcessor): Processor with instrument-specific configuration.
        dob (str): Date of birth.
        type_extractor (callable): Function that extracts a list of type values from an element.
    
    Returns:
        List[PhenotypicFeature]: List of phenotypic feature blocks.
    """
    features: List[PhenotypicFeature] = []
    instrument_name = processor.mapping_config.get("current_instrument", 
                        processor.mapping_config.get("redcap_repeat_instrument", ""))
    data_elements = _get_data_elements(data, instrument_name)
    if not data_elements:
        logger.debug(f"No data elements found for instrument: {instrument_name}")
        return []
    logger.debug(f"Found {len(data_elements)} data elements for instrument: {instrument_name}")
    for element in data_elements:
        # Extract type values using the provided extractor.
        type_values = type_extractor(element, processor)
        if not type_values:
            logger.debug("No type values found in element")
            continue
        for t in type_values:
            feats = multi_onset_adapter(_create_phenotypic_feature, t, element, processor, dob)
            features.extend(feats)
    return features
