import logging
from typing import List, Dict, Any, Optional
from phenopackets import PhenotypicFeature, OntologyClass, TimeElement, Evidence, Age
from cieinr.adapter.multi_onset import multi_onset_adapter
from rarelink.utils.processor import DataProcessor

logger = logging.getLogger(__name__)

def map_phenotypic_features(
    data: dict, 
    processor: DataProcessor,
    dob: str = None
) -> list:
    """
    Maps phenotype data to the Phenopacket schema PhenotypicFeature block.
    Handles multiple data models and structures.
    
    Args:
        data (dict): Input data from any schema.
        processor (DataProcessor): Handles all data processing logic.
        dob (str, optional): The individual's date of birth for age calculations.
    
    Returns:
        list: A list of Phenopacket PhenotypicFeature blocks.
    """
    # Get configuration for different instruments and their mappings
    mapping_config = processor.mapping_config
    
    # Extract the primary instrument
    primary_instrument = mapping_config.get("redcap_repeat_instrument", "")
    
    # Check for instrument-specific configurations
    instrument_configs = mapping_config.get("instrument_configs", {})
    
    # Check for simple list of additional instruments
    additional_instruments = mapping_config.get("additional_instruments", [])
    
    # If we have neither explicit instrument configs nor primary/additional instruments
    if not instrument_configs and not primary_instrument and not additional_instruments:
        logger.debug("No instruments configured for phenotypic features")
        return []
    
    try:
        all_features = []
        
        # Case 1: Using advanced instrument-specific configurations
        if instrument_configs:
            logger.debug(f"Using instrument-specific configs for {len(instrument_configs)} instruments")
            
            for instrument_name, config in instrument_configs.items():
                # Create a temporary processor with the instrument-specific config
                temp_processor = DataProcessor(
                    mapping_config={
                        **mapping_config,  # Base config
                        **config,         # Instrument-specific overrides
                        "redcap_repeat_instrument": instrument_name,
                        "current_instrument": instrument_name
                    }
                )
                
                # Map features using the temp processor
                features = _map_instrument_features(data, temp_processor, dob)
                
                if features:
                    all_features.extend(features)
                    logger.debug(f"Added {len(features)} features from instrument {instrument_name}")
        
        # Case 2: Using simple primary/additional instrument list
        else:
            # Combine all instruments
            all_instruments = [primary_instrument] + additional_instruments
            all_instruments = [i for i in all_instruments if i and i != "__dummy__"]
            
            if not all_instruments:
                logger.debug("No valid instrument names for phenotypic features")
                return []
            
            logger.debug(f"Processing {len(all_instruments)} instruments: {all_instruments}")
            
            # Process each instrument
            for instrument_name in all_instruments:
                # Store the current instrument in the processor
                processor.mapping_config["current_instrument"] = instrument_name
                
                # Map features for this instrument
                features = _map_instrument_features(data, processor, dob)
                
                if features:
                    all_features.extend(features)
                    logger.debug(f"Added {len(features)} features from instrument {instrument_name}")
        
        logger.debug(f"Total phenotypic features mapped: {len(all_features)}")
        return all_features
            
    except Exception as e:
        logger.error(f"Failed to map phenotypic feature: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        return []

def _map_instrument_features(data: dict, processor: DataProcessor, dob: str = None) -> List[PhenotypicFeature]:
    """
    Maps features for a specific instrument.
    
    Args:
        data (dict): Input data
        processor (DataProcessor): Processor with instrument-specific config
        dob (str, optional): Date of birth
        
    Returns:
        List[PhenotypicFeature]: List of mapped features
    """
    instrument_name = processor.mapping_config.get("current_instrument", 
                     processor.mapping_config.get("redcap_repeat_instrument", ""))
    
    # Determine the data model
    data_model = _determine_data_model(processor, instrument_name)
    logger.debug(f"Using data model: {data_model} with instrument: {instrument_name}")
    
    # Map features based on the detected data model
    if data_model == "infections":
        return _map_infections(data, processor, dob)
    elif data_model == "standard":
        return _map_standard_phenotypic_features(data, processor, dob)
    else:
        logger.warning(f"Unknown data model for phenotypic features: {data_model}")
        return []

def _determine_data_model(processor: DataProcessor, instrument_name: str) -> str:
    """
    Determines which data model to use based on configuration and instrument name.
    
    Args:
        processor (DataProcessor): The data processor with mapping configuration
        instrument_name (str): Name of the instrument
        
    Returns:
        str: Data model identifier ("infections", "standard", or "unknown")
    """
    # Check if this instrument has an explicit data model specified
    explicit_model = processor.mapping_config.get("data_model")
    if explicit_model:
        logger.debug(f"Using explicitly defined data model: {explicit_model}")
        return explicit_model
    
    # Check for multiple type fields (CIEINR/infections model)
    has_multiple_type_fields = any(
        f"type_field_{i}" in processor.mapping_config 
        for i in range(2, 11)
    )
    
    # Check instrument name for infection indicators
    is_infection_instrument = (
        "infection" in instrument_name.lower() or
        "infections_initial_form" == instrument_name
    )
    
    if has_multiple_type_fields or is_infection_instrument:
        return "infections"
    else:
        return "standard"

def _map_infections(data: dict, processor: DataProcessor, dob: str = None) -> List[PhenotypicFeature]:
    """Maps infection data to PhenotypicFeature objects."""
    instrument_name = processor.mapping_config.get("current_instrument",
                      processor.mapping_config.get("redcap_repeat_instrument"))
                      
    logger.debug(f"Mapping infections from instrument: {instrument_name}")
    
    phenotypic_features = []
    
    # Get data elements based on whether we're dealing with repeating elements
    data_elements = _get_data_elements(data, instrument_name)
    
    if not data_elements:
        logger.debug(f"No data elements found for infections with instrument: {instrument_name}")
        return []
    
    logger.debug(f"Found {len(data_elements)} infection elements")
    
    # Process each infection element
    for element_data in data_elements:
        # Log the element data keys for debugging
        logger.debug(f"Infection element data keys: {list(element_data.keys())}")
        
        # Try to extract infection types from multiple type fields
        infection_types = _get_infection_types(element_data, processor)
        
        if not infection_types:
            logger.debug("No infection types found in element")
            continue
        
        logger.debug(f"Found infection types: {infection_types}")
        
        for type_value in infection_types:
            features = multi_onset_adapter(_create_phenotypic_feature, type_value, element_data, processor, dob)
            if features:
                phenotypic_features.extend(features)
    
    return phenotypic_features

def _map_standard_phenotypic_features(data: dict, processor: DataProcessor, dob: str = None) -> List[PhenotypicFeature]:
    """Maps standard phenotypic feature data to PhenotypicFeature objects."""
    instrument_name = processor.mapping_config.get("current_instrument", 
                      processor.mapping_config.get("redcap_repeat_instrument"))
    
    phenotypic_features = []
    
    # Get data elements based on whether we're dealing with repeating elements
    data_elements = _get_data_elements(data, instrument_name)
    
    if not data_elements:
        logger.debug(f"No data elements found for phenotypic features with instrument: {instrument_name}")
        return []
    
    logger.debug(f"Found {len(data_elements)} phenotypic feature elements for instrument: {instrument_name}")
    
    # Process each feature element
    for element_data in data_elements:
        # Get the primary feature type
        type_field_path = processor.mapping_config.get("type_field")
        if not type_field_path:
            logger.debug("No type field configured")
            continue
            
        # Log the element data keys for debugging
        logger.debug(f"Element data keys: {list(element_data.keys())}")
        
        type_value = _get_field_value(element_data, type_field_path)
        if not type_value:
            logger.debug(f"No value found for type field '{type_field_path}'")
            continue
        logger.debug(f"Found type value: {type_value}")

        # Use the adapter to create one or more features per phenotype code.
        features = multi_onset_adapter(_create_phenotypic_feature, type_value, 
                                       element_data, processor, dob)
        if features:
            phenotypic_features.extend(features)

    
    return phenotypic_features

def _get_data_elements(data: dict, instrument_name: str) -> List[Dict[str, Any]]:
    """
    Extracts the relevant data elements from the input data.
    
    Args:
        data (dict): Input data
        instrument_name (str): Name of the instrument
        
    Returns:
        List[Dict[str, Any]]: List of data elements to process
    """
    elements = []
    
    # Check if we're dealing with repeated elements
    repeated_elements = data.get("repeated_elements", [])
    
    if repeated_elements:
        # Filter elements by instrument name
        elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        
        # Process each element to get the actual data
        processed_elements = []
        for element in elements:
            # Key for the actual phenotypic feature data - can be the instrument name
            # or a standardized name like "phenotypic_feature"
            possible_keys = [
                instrument_name, 
                "phenotypic_feature",  # RareLink CDM specific
                "clinical_phenotype",  # Possible alternative
                "phenotype_data"       # Possible alternative
            ]
            
            # Try each possible key
            element_data = None
            for key in possible_keys:
                if key in element:
                    element_data = element[key]
                    logger.debug(f"Found data using key: {key}")
                    break
            
            # If no data found using keys, use the element itself
            if not element_data:
                element_data = element
                
            if element_data:
                processed_elements.append(element_data)
                
        return processed_elements
    
    # If no repeated elements, check if the instrument data is directly in the main data
    elif instrument_name in data:
        return [data[instrument_name]]
    
    # Check for standardized phenotypic keys in main data
    elif any(key in data for key in ["phenotypic_feature", "clinical_phenotype", "phenotype_data"]):
        for key in ["phenotypic_feature", "clinical_phenotype", "phenotype_data"]:
            if key in data:
                return [data[key]]
    
    # Check if the data itself is the element (common in CIEINR)
    elif any(k.startswith(("snomedct_", "hp_")) for k in data.keys()):
        return [data]
    
    return []

def _get_infection_types(data: dict, processor: DataProcessor) -> List[str]:
    """
    Extracts infection type values from the data, handling multiple type fields.
    
    Args:
        data (dict): The data to extract from
        processor (DataProcessor): The data processor
        
    Returns:
        List[str]: List of infection type values
    """
    type_values = []
    
    # Get all type field configurations
    type_fields = {}
    
    # Get the primary type field
    primary_type_field = processor.mapping_config.get("type_field")
    if primary_type_field:
        type_fields["primary"] = primary_type_field
    
    # Get numbered type fields
    for i in range(1, 31):  # Support up to 30 numbered type fields
        field_key = f"type_field_{i}" if i > 1 else "type_field"
        if field_key in processor.mapping_config:
            field_path = processor.mapping_config[field_key]
            if field_path:
                type_fields[field_key] = field_path
    
    # Process all type fields
    logger.debug(f"Checking {len(type_fields)} type fields for values")
    for field_key, field_path in type_fields.items():
        value = _get_field_value(data, field_path)
        if value:
            logger.debug(f"Found value '{value}' for type field '{field_key}'")
            type_values.append(value)
    
    # If no values found with explicit type fields, try scanning for fields
    if not type_values:
        scan_patterns = processor.mapping_config.get("scan_patterns", [
            "infection_", "disease_", "phenotype_", "symptom_", "finding_"
        ])
        
        for field_name, value in data.items():
            # Check if field matches any scan pattern and has a non-empty string value
            if isinstance(value, str) and value and any(pattern in field_name.lower() for pattern in scan_patterns):
                logger.debug(f"Found scan match: field '{field_name}' with value '{value}'")
                type_values.append(value)
    
    # Debug logging
    if not type_values:
        logger.debug(f"No type values found in data with keys: {list(data.keys())[:10]}...")
        if len(data.keys()) > 10:
            logger.debug(f"(and {len(data.keys()) - 10} more keys)")
    
    return type_values

def _create_phenotypic_feature(
    feature_type: str, 
    feature_data: dict,
    processor: DataProcessor,
    dob: str = None
) -> Optional[PhenotypicFeature]:
    """
    Creates a phenotypic feature object from the given data.
    
    Args:
        feature_type (str): The type value for the feature
        feature_data (dict): The data for the feature
        processor (DataProcessor): The data processor
        dob (str, optional): Date of birth for age calculations
        
    Returns:
        Optional[PhenotypicFeature]: The created phenotypic feature or None
    """
    # PhenotypicFeature.type
    # ------------------------------------------------------------------
    type_id = processor.process_code(feature_type)
    type_label = processor.fetch_label(feature_type)
    
    feature_type_obj = OntologyClass(
        id=type_id,
        label=type_label or "Unknown Phenotypic Feature"
    )
    
    # PhenotypicFeature.excluded
    # ------------------------------------------------------------------
    excluded = _extract_excluded_status(feature_data, processor)
    
    # PhenotypicFeature.onset
    # ------------------------------------------------------------------
    onset = _extract_onset(feature_data, processor, dob)
    
    # PhenotypicFeature.resolution
    # ------------------------------------------------------------------
    resolution = _extract_resolution(feature_data, processor, dob)
    
    # PhenotypicFeature.severity
    # ------------------------------------------------------------------
    severity = _extract_severity(feature_data, processor)
    
    # PhenotypicFeature.evidence
    # ------------------------------------------------------------------
    evidence = _extract_evidence(feature_data, processor)
    
    # PhenotypicFeature.modifiers
    # ------------------------------------------------------------------
    modifiers = _extract_modifiers(feature_data, processor)
    
    # Create the PhenotypicFeature
    # ------------------------------------------------------------------
    phenotypic_feature = PhenotypicFeature(
        type=feature_type_obj,
        excluded=excluded,
        onset=onset,
        resolution=resolution,
        severity=severity,
        evidence=evidence,
        modifiers=modifiers if modifiers else None
    )
    
    return phenotypic_feature

def _extract_excluded_status(data: dict, processor: DataProcessor) -> Optional[bool]:
    """Extracts the excluded status from the data."""
    excluded = None
    excluded_field = processor.mapping_config.get("excluded_field")
    
    if excluded_field:
        excluded_value = _get_field_value(data, excluded_field)
        if excluded_value:
            mapped_value = processor.fetch_mapping_value(
                "phenotypic_feature_status", excluded_value)
            if mapped_value == "true":
                excluded = True
            elif mapped_value == "false":
                excluded = False
                
    return excluded

def _extract_onset(data: dict, processor: DataProcessor, dob: str = None) -> Optional[TimeElement]:
    """Extracts onset information from the data."""
    onset = None
    onset_date_field = processor.mapping_config.get("onset_date_field")
    onset_age_field = processor.mapping_config.get("onset_age_field")
    
    # Try onset date first if DOB is available
    if onset_date_field and dob:
        onset_date = _get_field_value(data, onset_date_field)
        if onset_date:
            try:
                # Handle various date formats - similar to how it's done in map_measurements
                # Ensure onset_date is a string in proper ISO format
                if not isinstance(onset_date, str):
                    onset_date_str = onset_date.ToDatetime().isoformat() \
                        if hasattr(onset_date, "ToDatetime") \
                        else str(onset_date)
                else:
                    onset_date_str = onset_date
                
                # Ensure dob is a string in proper ISO format
                if not isinstance(dob, str):
                    dob_str = dob.ToDatetime().isoformat() \
                        if hasattr(dob, "ToDatetime") \
                        else str(dob)
                else:
                    dob_str = dob
                
                # Log the formatted date strings
                logger.debug(f"Formatted onset date: {onset_date_str}, dob: {dob_str}")
                
                # Calculate ISO age
                iso_age = processor.convert_date_to_iso_age(onset_date_str, dob_str)
                if iso_age:
                    logger.debug(f"Converted onset date to ISO age: {iso_age}")
                    onset = TimeElement(age=Age(iso8601duration=iso_age))
                else:
                    logger.debug(f"Failed to convert onset date {onset_date_str} to ISO age")
            except Exception as e:
                logger.error(f"Error processing onset date for ISO age: {e}")
                import traceback
                logger.debug(traceback.format_exc())
    
    # Try onset age ontology if no date or date processing failed
    if not onset and onset_age_field:
        onset_age_value = _get_field_value(data, onset_age_field)
        if onset_age_value:
            onset_label = processor.fetch_label(onset_age_value, "AgeOfOnset")
            onset_id = processor.process_code(onset_age_value)
            if onset_label:
                onset = TimeElement(
                    ontology_class=OntologyClass(
                        id=onset_id,
                        label=onset_label
                    )
                )
                
    return onset

def _extract_resolution(data: dict, processor: DataProcessor, dob: str = None) -> Optional[TimeElement]:
    """Extracts resolution information from the data."""
    resolution = None
    resolution_field = processor.mapping_config.get("resolution_field")
    
    if resolution_field and dob:
        resolution_date = _get_field_value(data, resolution_field)
        if resolution_date:
            try:
                # Handle various date formats - similar to how it's done in map_measurements
                # Ensure resolution_date is a string in proper ISO format
                if not isinstance(resolution_date, str):
                    resolution_date_str = resolution_date.ToDatetime().isoformat() \
                        if hasattr(resolution_date, "ToDatetime") \
                        else str(resolution_date)
                else:
                    resolution_date_str = resolution_date
                
                # Ensure dob is a string in proper ISO format
                if not isinstance(dob, str):
                    dob_str = dob.ToDatetime().isoformat() \
                        if hasattr(dob, "ToDatetime") \
                        else str(dob)
                else:
                    dob_str = dob
                
                # Log the formatted date strings
                logger.debug(f"Formatted resolution date: {resolution_date_str}, dob: {dob_str}")
                
                # Calculate ISO age
                iso_age = processor.convert_date_to_iso_age(resolution_date_str, dob_str)
                if iso_age:
                    logger.debug(f"Converted resolution date to ISO age: {iso_age}")
                    resolution = TimeElement(age=Age(iso8601duration=iso_age))
                else:
                    logger.debug(f"Failed to convert resolution date {resolution_date_str} to ISO age")
            except Exception as e:
                logger.error(f"Error processing resolution date for ISO age: {e}")
                import traceback
                logger.debug(traceback.format_exc())
                
    return resolution

def _extract_severity(data: dict, processor: DataProcessor) -> Optional[OntologyClass]:
    """Extracts severity information from the data."""
    severity = None
    severity_field = processor.mapping_config.get("severity_field")
    
    if severity_field:
        severity_value = _get_field_value(data, severity_field)
        if severity_value:
            severity_id = processor.process_code(severity_value)
            severity_label = processor.fetch_label(severity_value, "PhenotypeSeverity")
            if severity_label:
                severity = OntologyClass(
                    id=severity_id,
                    label=severity_label
                )
                
    return severity

def _extract_evidence(data: dict, processor: DataProcessor) -> Optional[List[Evidence]]:
    """Extracts evidence information from the data."""
    evidence_list = None
    evidence_field = processor.mapping_config.get("evidence_field")
    
    if evidence_field:
        evidence_value = _get_field_value(data, evidence_field)
        if evidence_value:
            evidence_id = processor.process_code(evidence_value)
            evidence_label = processor.fetch_label(evidence_value)
            evidence = Evidence(
                evidence_code=OntologyClass(
                    id=evidence_id,
                    label=evidence_label or "Unknown Evidence"
                )
            )
            evidence_list = [evidence]
            
    return evidence_list

def _extract_modifiers(data: dict, processor: DataProcessor) -> List[OntologyClass]:
    """Extracts modifier information from the data."""
    modifiers = []
    
    for i in range(1, 6):
        modifier_field = processor.mapping_config.get(f"modifier_field_{i}")
        if not modifier_field:
            continue
            
        modifier_value = _get_field_value(data, modifier_field)
        if modifier_value:
            modifier_id = processor.process_code(modifier_value)
            modifier_label = processor.fetch_label(modifier_value)
            if modifier_label:
                modifiers.append(OntologyClass(
                    id=modifier_id,
                    label=modifier_label
                ))
                
    return modifiers

def _get_field_value(data: dict, field_path: str) -> Any:
    """
    Get a field value from data, handling direct and nested access.
    
    Args:
        data (dict): The data to extract from
        field_path (str): Field path, can be simple or dotted
        
    Returns:
        Any: The field value or None if not found
    """
    if not field_path or not data:
        return None
        
    # Direct field access
    if "." not in field_path:
        return data.get(field_path)
        
    # Nested field access
    parts = field_path.split(".", 1)
    if len(parts) == 2 and parts[0] in data:
        nested_data = data.get(parts[0])
        if isinstance(nested_data, dict):
            return nested_data.get(parts[1])
            
    # Try matching the exact path
    if field_path in data:
        return data[field_path]
    
    return None