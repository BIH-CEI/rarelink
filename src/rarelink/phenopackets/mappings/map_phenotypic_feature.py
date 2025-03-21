import logging
from typing import List, Optional, Callable, Tuple
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
    _get_condition_types,
    _get_single_type,
)

logger = logging.getLogger(__name__)

# This is a patch to be added to the map_phenotypic_features function in map_phenotypic_feature.py

def map_phenotypic_features(
    data: dict, 
    processor: DataProcessor,
    dob: str = None
) -> List[PhenotypicFeature]:
    """
    Maps phenotype data to Phenopacket PhenotypicFeature blocks with enhanced debugging.
    Supports multiple instruments and handles both infections and standard data models.
    
    Args:
        data (dict): Input data.
        processor (DataProcessor): Data processor with mapping configuration.
        dob (str, optional): Date of birth (for age calculations).
    
    Returns:
        List[PhenotypicFeature]: List of mapped phenotypic feature blocks.
    """
    mapping_config = processor.mapping_config
    
    # Store the full data for multi-instrument field access
    mapping_config['full_data'] = data
    
    # Check if this is a direct single instrument configuration
    current_instrument = mapping_config.get("current_instrument") or mapping_config.get("redcap_repeat_instrument")
    if current_instrument:
        logger.info(f"Processing single instrument: {current_instrument}")
        data_model = _determine_data_model(processor, current_instrument)
        logger.debug(f"Using data model: {data_model} with instrument: {current_instrument}")
        
        # Choose the type extractor based on the model
        if data_model == "infections":
            logger.debug(f"Using infection type extractor for {current_instrument}")
            type_extractor = _get_infection_types
        elif data_model == "conditions":
            logger.debug(f"Using condition type extractor for {current_instrument}") 
            type_extractor = _get_condition_types
        else:
            # Default to generic type extractor
            logger.debug(f"Using generic type extractor for {current_instrument}")
            type_extractor = _get_single_type
            
        # Extract all instrument names for multi-instrument field access
        all_instruments = mapping_config.get("all_instruments", [])
        if current_instrument and current_instrument not in all_instruments:
            all_instruments.append(current_instrument)
            
        # Map features for this instrument
        features = _map_features(data, processor, dob, type_extractor, all_instruments)
        logger.debug(f"Found {len(features)} features for instrument {current_instrument}")
        return features
    
    # Below this is the original multi-instrument handling which can remain as fallback
    # Get advanced instrument configs or a simple instrument list.
    instrument_configs = mapping_config.get("instrument_configs", {})
    instruments: List[Tuple[str, DataProcessor]] = []
    
    # Extract all instrument names for multi-instrument field access
    all_instruments = []
    
    # Handle instrument_name that might be a set/list
    instrument_name_config = mapping_config.get("instrument_name")
    if isinstance(instrument_name_config, (list, set)):
        all_instruments.extend(list(instrument_name_config))
    elif instrument_name_config:
        all_instruments.append(instrument_name_config)
    
    # Add primary instrument if not already included
    primary_instrument = mapping_config.get("redcap_repeat_instrument", "")
    if primary_instrument and primary_instrument not in all_instruments:
        all_instruments.append(primary_instrument)
    
    # Add additional instruments
    additional_instruments = mapping_config.get("additional_instruments", [])
    for inst in additional_instruments:
        if inst and inst not in all_instruments:
            all_instruments.append(inst)
    
    # Filter out invalid instruments
    all_instruments = [i for i in all_instruments if i and i != "__dummy__"]
    
    # Store all instruments in the mapping config for field access
    mapping_config["all_instruments"] = all_instruments
    
    logger.info(f"Processing {len(all_instruments)} instruments: {all_instruments}")
    
    # Set up processors for each instrument
    if instrument_configs:
        logger.debug(f"Using instrument-specific configs for {len(instrument_configs)} instruments")
        # Add each configured instrument
        for instrument_name, config in instrument_configs.items():
            # Don't add if instrument is not in our all_instruments list
            if instrument_name not in all_instruments:
                continue
                
            temp_proc = DataProcessor(mapping_config={
                **mapping_config,  # Base config
                **config,          # Instrument-specific overrides
                "redcap_repeat_instrument": instrument_name,
                "current_instrument": instrument_name,
                "all_instruments": all_instruments
            })
            instruments.append((instrument_name, temp_proc))
    
    # If we have no configured instruments, use our all_instruments list with the default processor
    if not instruments:
        logger.debug(f"Using default config for {len(all_instruments)} instruments")
        for instrument_name in all_instruments:
            processor_copy = DataProcessor(mapping_config=dict(processor.mapping_config))
            processor_copy.mapping_config["redcap_repeat_instrument"] = instrument_name
            processor_copy.mapping_config["current_instrument"] = instrument_name
            processor_copy.mapping_config["all_instruments"] = all_instruments
            instruments.append((instrument_name, processor_copy))
    
    all_features: List[PhenotypicFeature] = []
    
    # Process each instrument
    for instrument_name, proc in instruments:
        logger.debug(f"Using data model: {_determine_data_model(proc, instrument_name)} with instrument: {instrument_name}")
        model = _determine_data_model(proc, instrument_name)
        
        # Choose the type extractor based on the model
        if model == "infections":
            logger.debug(f"Using infection type extractor for {instrument_name}")
            type_extractor = _get_infection_types
        elif model == "conditions":
            logger.debug(f"Using condition type extractor for {instrument_name}") 
            type_extractor = _get_condition_types
        else:
            # Default to generic type extractor
            logger.debug(f"Using generic type extractor for {instrument_name}")
            type_extractor = _get_single_type
            
        # Map features for this instrument
        features = _map_features(data, proc, dob, type_extractor, all_instruments)
        if features:
            all_features.extend(features)
            logger.debug(f"Added {len(features)} features from instrument {instrument_name}")
        else:
            logger.debug(f"No features found for instrument {instrument_name}")
    
    logger.debug(f"Total phenotypic features mapped: {len(all_features)}")
    return all_features
def _create_phenotypic_feature(
    feature_type: str, 
    feature_data: dict,
    processor: DataProcessor,
    dob: str = None,
    all_instruments: List[str] = None
) -> Optional[PhenotypicFeature]:
    """
    Creates a PhenotypicFeature object from the given data.
    
    Args:
        feature_type (str): Type value.
        feature_data (dict): Data for the feature.
        processor (DataProcessor): Data processor.
        dob (str, optional): Date of birth.
        all_instruments (List[str], optional): List of all instruments for field lookup.
    
    Returns:
        Optional[PhenotypicFeature]: The feature, or None.
    """
    # Add the full data to the processor if it's not already there
    if hasattr(processor, 'mapping_config') and 'full_data' not in processor.mapping_config:
        processor.mapping_config['full_data'] = feature_data
    
    type_id = processor.process_code(feature_type)
    type_label = processor.fetch_label(feature_type)
    
    logger.debug(f"Creating feature for type: {feature_type} -> {type_id} ({type_label})")
    
    type_obj = OntologyClass(id=type_id, label=type_label or "Unknown Phenotypic Feature")
    
    # Extract feature properties with multi-instrument support
    excluded = _extract_excluded_status(feature_data, processor, all_instruments, data_context=feature_data)
    onset = _extract_onset(feature_data, processor, dob, all_instruments, data_context=feature_data)
    resolution = _extract_resolution(feature_data, processor, dob, all_instruments, data_context=feature_data)
    severity = _extract_severity(feature_data, processor, all_instruments, data_context=feature_data)
    evidence = _extract_evidence(feature_data, processor, all_instruments, data_context=feature_data)
    modifiers = _extract_modifiers(feature_data, processor, all_instruments, data_context=feature_data)
    
    # Check if multi-onset is enabled
    if processor.mapping_config.get("multi_onset", False):
        logger.debug(f"Multi-onset enabled for type {feature_type}")
        
        # Use the multi_onset_adapter to create multiple features if needed
        return multi_onset_adapter(
            mapping_func=lambda t, d, p, b: PhenotypicFeature(
                type=type_obj,
                excluded=excluded,
                onset=onset,
                resolution=resolution,
                severity=severity,
                evidence=evidence,
                modifiers=modifiers if modifiers else None
            ),
            feature_type=feature_type,
            feature_data=feature_data,
            processor=processor,
            dob=dob
        )[0]  # Return the first feature - multi_onset_adapter will be called again for each date
    else:
        # Create a standard single feature
        logger.debug(f"Creating standard single feature for type {feature_type}")
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
    type_extractor: Callable[[dict, DataProcessor, List[str]], List[str]],
    all_instruments: List[str] = None
) -> List[PhenotypicFeature]:
    """
    Generic function that extracts data elements and applies a type extractor to produce features.
    Enhanced to properly handle multi-onset fields.
    
    Args:
        data (dict): Input data.
        processor (DataProcessor): Processor with instrument-specific configuration.
        dob (str): Date of birth.
        type_extractor (callable): Function that extracts a list of type values from an element.
        all_instruments (List[str], optional): List of all instruments for field lookup.
    
    Returns:
        List[PhenotypicFeature]: List of phenotypic feature blocks.
    """
    features: List[PhenotypicFeature] = []
    instrument_name = processor.mapping_config.get("current_instrument", 
                        processor.mapping_config.get("redcap_repeat_instrument", ""))
    
    # Store full data in processor for multi-instrument field access
    processor.mapping_config['full_data'] = data
    
    # Get the data elements for this instrument
    data_elements = _get_data_elements(data, instrument_name)
    if not data_elements:
        logger.debug(f"No data elements found for instrument: {instrument_name}")
        return []
    
    logger.debug(f"Found {len(data_elements)} data elements for instrument: {instrument_name}")
    
    # Process each element
    for element in data_elements:
        # Extract type values using the provided extractor
        type_values = type_extractor(element, processor, all_instruments)
        if not type_values:
            logger.debug("No type values found in element")
            continue
        
        # Process each type value
        for t in type_values:
            try:
                # Check for multi-onset support
                multi_onset = processor.mapping_config.get("multi_onset", False)
                onset_fields = processor.mapping_config.get("onset_date_fields", [])
                
                if multi_onset and onset_fields:
                    logger.debug(f"Processing multi-onset for type {t}")
                    
                    # Extract all onset dates from the element
                    onset_dates = []
                    for field in onset_fields:
                        field_name = field.split(".")[-1] if "." in field else field
                        if field_name in element and element[field_name]:
                            onset_dates.append((field_name, element[field_name]))
                    
                    logger.debug(f"Found {len(onset_dates)} onset dates for type {t}")
                    
                    if onset_dates:
                        # Create a feature for each date
                        for field_name, date_value in onset_dates:
                            # Create a modified element with only this date
                            modified_element = element.copy()
                            
                            # Set all other date fields to empty
                            for other_field, _ in onset_dates:
                                if other_field != field_name:
                                    modified_element[other_field] = ""
                            
                            # Create the feature with just this date
                            feature = _create_phenotypic_feature(t, modified_element, processor, dob, all_instruments)
                            if feature:
                                features.append(feature)
                                logger.debug(f"Added feature with onset date {date_value} for type {t}")
                    else:
                        # No dates, create a single feature
                        feature = _create_phenotypic_feature(t, element, processor, dob, all_instruments)
                        if feature:
                            features.append(feature)
                            logger.debug(f"Added single feature (no dates) for type {t}")
                else:
                    # Standard single feature creation
                    feature = _create_phenotypic_feature(t, element, processor, dob, all_instruments)
                    if feature:
                        features.append(feature)
                        logger.debug(f"Added standard feature for type {t}")
            except Exception as e:
                logger.error(f"Error processing type {t}: {str(e)}")
                import traceback
                logger.debug(traceback.format_exc())
    
    return features