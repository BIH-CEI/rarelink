from typing import Any, Dict, List, Optional
from rarelink.utils.processor.processor import DataProcessor
import logging
from phenopackets import OntologyClass, Evidence, TimeElement, Age
from rarelink.utils.loading import _get_multi_instrument_field_value

logger = logging.getLogger(__name__)

def _get_field_value(data: dict, field_path: str) -> Any:
    """
    Gets a field value from a dict, supporting multiple data structures.
    Enhanced to handle different nested data scenarios.
    
    Args:
        data (dict): Input data.
        field_path (str): Field path (e.g., "patient.birthdate" or "infections_initial_form.field").
    
    Returns:
        Any: The field value or None.
    """
    if not field_path or not data:
        return None
        
    # Case 1: Direct field access (no dot notation)
    if "." not in field_path:
        # Try direct access first
        if field_path in data:
            return data.get(field_path)
            
        # For repeated elements, check inside each instrument block
        for key, value in data.items():
            if isinstance(value, dict) and field_path in value:
                return value.get(field_path)
                
        return None
        
    # Case 2: Path with instrument prefix (instrument.field)
    instrument, field = field_path.split(".", 1)
    
    # First try: Look for instrument as a separate block
    if instrument in data and isinstance(data[instrument], dict):
        return data[instrument].get(field)
    
    # Second try: For flat data without instrument keys, try the field directly
    if field in data:
        return data.get(field)
    
    # Third try: For repeated_elements data where instrument is the record key
    if "repeated_elements" in data:
        for element in data["repeated_elements"]:
            if element.get("redcap_repeat_instrument") == instrument:
                # Check if field exists directly in element
                if field in element:
                    return element.get(field)
                # Or inside a nested instrument dictionary
                if instrument in element and isinstance(element[instrument], dict):
                    return element[instrument].get(field)
                # Last resort - check any dictionary inside
                for key, value in element.items():
                    if isinstance(value, dict) and field in value:
                        return value.get(field)
    
    # Not found
    return None

def _get_single_type(data: dict, processor: DataProcessor, all_instruments: List[str] = None) -> List[str]:
    """
    Extracts a single type value from data using the configured 'type_field'.
    Enhanced to support multi-instrument field access.
    
    Args:
        data (dict): Input element data.
        processor (DataProcessor): Data processor.
        all_instruments (List[str], optional): List of all instruments for field lookup.
    
    Returns:
        List[str]: List with a single type value if found, else an empty list.
    """
    type_field = processor.mapping_config.get("type_field")
    if not type_field:
        logger.debug("No type field configured")
        return []
    
    value = None
    
    # Try multi-instrument lookup first if available
    if all_instruments and hasattr(processor, 'mapping_config') and 'all_instruments' in processor.mapping_config:
        # Use the full data and all instruments for lookup
        full_data = processor.mapping_config.get('full_data', {})
        value = _get_multi_instrument_field_value(
            data=full_data,
            instruments=all_instruments,
            field_paths=[type_field]
        )
    
    # If not found or multi-instrument lookup not available, use direct field access
    if value is None:
        value = _get_field_value(data, type_field)
    
    if not value:
        logger.debug(f"No value found for type field '{type_field}'")
        return []
    
    logger.debug(f"Found type value: {value}")
    return [value]

def _determine_data_model(processor: DataProcessor, instrument_name: str) -> str:
    """
    Determines which data model to use based on configuration and instrument name.
    Updated to recognize systemic/organ-specific conditions instruments.
    
    Args:
        processor (DataProcessor): Data processor.
        instrument_name (str): Name of the instrument.
    
    Returns:
        str: "infections", "conditions", "rarelink_cdm", or specified model.
    """
    # Check for explicitly defined model in the configuration
    explicit_model = processor.mapping_config.get("data_model")
    if explicit_model:
        logger.debug(f"Using explicitly defined data model: {explicit_model}")
        return explicit_model
    
    # Check for multiple type fields which suggests a multi-field form
    has_multiple_type_fields = any(f"type_field_{i}" in processor.mapping_config for i in range(2, 20))
    
    # Check instrument name patterns
    is_infection = (
        "infection" in instrument_name.lower() or 
        instrument_name == "infections_initial_form"
    )
    
    is_condition = (
        "systemic" in instrument_name.lower() or
        "organ_specific" in instrument_name.lower() or
        "patients_systemic_or_organ_specific_conditions" == instrument_name
    )
    
    # Determine model based on checks
    if is_infection:
        return "infections"
    elif is_condition:
        return "conditions"
    elif has_multiple_type_fields:
        # If multiple type fields but not identified as infections or conditions,
        # default to multi-field type
        return "multi_field"
    else:
        return "rarelink_cdm"

def _get_data_elements(data: dict, instrument_name: str) -> List[Dict[str, Any]]:
    """
    Extracts the data elements to process for a given instrument.
    Enhanced to properly handle nested data structures.
    
    Args:
        data (dict): Input data.
        instrument_name (str): Name of the instrument.
    
    Returns:
        List[Dict[str, Any]]: List of data elements.
    """
    logger.debug(f"Looking for data elements with instrument: {instrument_name}")
    logger.debug(f"Data keys: {list(data.keys()) if isinstance(data, dict) else 'not a dict'}")
    
    elements = []
    
    # Check for repeated_elements structure
    if isinstance(data, dict) and "repeated_elements" in data:
        repeated_elements = data["repeated_elements"]
        logger.debug(f"Found repeated_elements with {len(repeated_elements)} items")
        
        # Filter elements for the target instrument
        for element in repeated_elements:
            if element.get("redcap_repeat_instrument") == instrument_name:
                # Extract the actual instrument data
                if instrument_name in element and isinstance(element[instrument_name], dict):
                    logger.debug(f"Found element with instrument {instrument_name} and keys: {list(element[instrument_name].keys())}")
                    elements.append(element[instrument_name])
                else:
                    logger.debug(f"Element has instrument {instrument_name} but no nested data")
        
        if not elements:
            logger.debug(f"No elements found for instrument {instrument_name} in repeated_elements")
    else:
        logger.debug("No repeated_elements found in data")
    
    # If no elements found, try direct access
    if not elements and instrument_name in data and isinstance(data[instrument_name], dict):
        logger.debug(f"Found direct instrument data with keys: {list(data[instrument_name].keys())}")
        elements.append(data[instrument_name])
    
    # If we still haven't found anything, as a fallback check if the data itself has relevant fields
    if not elements and isinstance(data, dict):
        for field in ["snomedct_21483005", "snomedct_61274003", "mondo_0005570", "snomedct_362969004"]:
            if field in data:
                logger.debug(f"Found field {field} directly in data, treating data itself as an element")
                elements.append(data)
                break
    
    logger.debug(f"Returning {len(elements)} data elements for instrument {instrument_name}")
    return elements

def _get_infection_types(data: dict, processor: DataProcessor, all_instruments: List[str] = None) -> List[str]:
    """
    Extracts infection type values from the data.
    Refactored to support nested REDCap data structure.
    
    Args:
        data (dict): The data element to extract from (already extracted from the full data).
        processor (DataProcessor): The data processor with mapping configuration.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        
    Returns:
        List[str]: A list of infection type values.
    """
    # Define infection type fields to check
    infection_type_fields = [
        "snomedct_61274003",   # Opportunistic infections
        "snomedct_21483005",   # CNS infections
        "snomedct_81745001",   # Eye infections
        "snomedct_385383008",  # ENT infections
        "snomedct_127856007",  # Skin/soft tissue
        "snomedct_110522009",  # Bone/joint
        "snomedct_20139000",   # Respiratory
        "snomedct_303699009",  # GI
        "snomedct_21514008",   # GU
        "snomedct_31099001",   # Systemic
        "other_infection_hpo",
        "other_infection_mondo"
    ]
    
    # Storage for found type values
    type_values = []
    
    # Log the data keys for debugging
    logger.debug(f"Examining data: {list(data.keys()) if isinstance(data, dict) else 'not a dict'}")
    
    # Check each field directly in the data (since _map_features already extracted the right element)
    if isinstance(data, dict):
        for field in infection_type_fields:
            if field in data and data[field]:
                value = data[field]
                logger.debug(f"Found field '{field}' with value '{value}'")
                
                if isinstance(value, str) and (
                    value.startswith("hp_") or 
                    value.startswith("mondo_") or 
                    value.startswith("snomedct_") or
                    ":" in value
                ):
                    logger.debug(f"✅ Found valid infection type value '{value}' for field '{field}'")
                    type_values.append(value)
                else:
                    logger.debug(f"❌ Value '{value}' for field '{field}' is not a valid type code")
    
    # Log the final result
    logger.debug(f"Final infection type values: {type_values}")
    return type_values

def _get_condition_types(data: dict, processor: DataProcessor, all_instruments: List[str] = None) -> List[str]:
    """
    Extracts condition type values from the data.
    Refactored to support nested REDCap data structure.
    
    Args:
        data (dict): The data element to extract from (already extracted from the full data).
        processor (DataProcessor): The data processor with mapping configuration.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        
    Returns:
        List[str]: A list of condition type values.
    """
    # Define condition type fields to check
    condition_type_fields = [
        "snomedct_128477000",  # Systemic condition
        "snomedct_95320005",   # Allergy
        "snomedct_118938008",  # Neoplasm
        "snomedct_50043002",   # Endocrine disorder
        "snomedct_49601007",   # Cardiovascular disorder
        "mondo_0005570",       # Autoimmune disorder
        "snomedct_928000",     # Gastrointestinal disorder
        "snomedct_119292006",  # Genitourinary disorder
        "snomedct_362969004",  # Metabolic disorder
        "snomedct_42030000",   # Renal system disorder
        "snomedct_55342001",   # Skeletal disorder
        "snomedct_85828009",   # Trauma
        "hp_0025142",          # Constitutional symptom
        "snomedct_5294002",    # Developmental delay
        "condition_other_hp"
    ]
    
    # Storage for found type values
    type_values = []
    
    # Log the data keys for debugging
    logger.debug(f"Examining condition data: {list(data.keys()) if isinstance(data, dict) else 'not a dict'}")
    
    # Check each field directly in the data (since _map_features already extracted the right element)
    if isinstance(data, dict):
        for field in condition_type_fields:
            if field in data and data[field]:
                value = data[field]
                logger.debug(f"Found field '{field}' with value '{value}'")
                
                if isinstance(value, str) and (
                    value.startswith("hp_") or 
                    value.startswith("mondo_") or 
                    value.startswith("snomedct_") or
                    ":" in value
                ):
                    logger.debug(f"✅ Found valid condition type value '{value}' for field '{field}'")
                    type_values.append(value)
                else:
                    logger.debug(f"❌ Value '{value}' for field '{field}' is not a valid type code")
    
    # Log the final result
    logger.debug(f"Final condition type values: {type_values}")
    return type_values

def _extract_excluded_status(
    data: dict, 
    processor: DataProcessor,
    all_instruments: List[str] = None,
    data_context: dict = None
) -> Optional[bool]:
    """
    Extracts excluded status from the data.
    Enhanced to support multi-instrument field access.
    
    Args:
        data (dict): The data to extract from.
        processor (DataProcessor): The data processor.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        data_context (dict, optional): Additional data context for field lookup.
        
    Returns:
        Optional[bool]: True if excluded, False if not, None if not specified.
    """
    excluded = None
    field = processor.mapping_config.get("excluded_field")
    if field:
        val = None
        
        # Try multi-instrument lookup first if available
        if all_instruments and data_context:
            val = _get_multi_instrument_field_value(
                data=data_context,
                instruments=all_instruments,
                field_paths=[field]
            )
        
        # If not found or multi-instrument lookup not available, use direct field access
        if val is None:
            val = _get_field_value(data, field)
        
        if val:
            mapped = processor.fetch_mapping_value("phenotypic_feature_status", val)
            if mapped == "true":
                excluded = True
            elif mapped == "false":
                excluded = False
    return excluded

def _extract_onset(
    data: dict, 
    processor: DataProcessor, 
    dob: str = None, 
    all_instruments: List[str] = None,
    data_context: dict = None
) -> Optional[TimeElement]:
    """
    Extracts onset information from the data.
    Enhanced to support multi-instrument field access.
    
    Args:
        data (dict): The data to extract from.
        processor (DataProcessor): The data processor.
        dob (str, optional): Date of birth for age calculations.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        data_context (dict, optional): Additional data context for field lookup.
        
    Returns:
        Optional[TimeElement]: Onset time element or None.
    """
    onset = None
    field = processor.mapping_config.get("onset_date_field")
    alt_field = processor.mapping_config.get("onset_age_field")
    
    if field and dob:
        val = None
        
        # Try multi-instrument lookup first if available
        if all_instruments and data_context:
            val = _get_multi_instrument_field_value(
                data=data_context,
                instruments=all_instruments,
                field_paths=[field]
            )
        
        # If not found or multi-instrument lookup not available, use direct field access
        if val is None:
            val = _get_field_value(data, field)
        
        if val:
            try:
                onset_str = val if isinstance(val, str) else (val.ToDatetime().isoformat() if hasattr(val, "ToDatetime") else str(val))
                dob_str = dob if isinstance(dob, str) else (dob.ToDatetime().isoformat() if hasattr(dob, "ToDatetime") else str(dob))
                logger.debug(f"Formatted onset date: {onset_str}, dob: {dob_str}")
                iso_age = processor.convert_date_to_iso_age(onset_str, dob_str)
                if iso_age:
                    onset = TimeElement(age=Age(iso8601duration=iso_age))
            except Exception as e:
                logger.error(f"Error processing onset date: {e}")
    
    if not onset and alt_field:
        alt_val = None
        
        # Try multi-instrument lookup first if available
        if all_instruments and data_context:
            alt_val = _get_multi_instrument_field_value(
                data=data_context,
                instruments=all_instruments,
                field_paths=[alt_field]
            )
        
        # If not found or multi-instrument lookup not available, use direct field access
        if alt_val is None:
            alt_val = _get_field_value(data, alt_field)
        
        if alt_val:
            label = processor.fetch_label(alt_val, "AgeOfOnset")
            pid = processor.process_code(alt_val)
            if label:
                onset = TimeElement(ontology_class=OntologyClass(id=pid, label=label))
    
    return onset

def _extract_resolution(
    data: dict, 
    processor: DataProcessor, 
    dob: str = None, 
    all_instruments: List[str] = None,
    data_context: dict = None
) -> Optional[TimeElement]:
    """
    Extracts resolution information from the data.
    Enhanced to support multi-instrument field access.
    
    Args:
        data (dict): The data to extract from.
        processor (DataProcessor): The data processor.
        dob (str, optional): Date of birth for age calculations.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        data_context (dict, optional): Additional data context for field lookup.
        
    Returns:
        Optional[TimeElement]: Resolution time element or None.
    """
    resolution = None
    field = processor.mapping_config.get("resolution_field")
    
    if field and dob:
        val = None
        
        # Try multi-instrument lookup first if available
        if all_instruments and data_context:
            val = _get_multi_instrument_field_value(
                data=data_context,
                instruments=all_instruments,
                field_paths=[field]
            )
        
        # If not found or multi-instrument lookup not available, use direct field access
        if val is None:
            val = _get_field_value(data, field)
        
        if val:
            try:
                res_str = val if isinstance(val, str) else (val.ToDatetime().isoformat() if hasattr(val, "ToDatetime") else str(val))
                dob_str = dob if isinstance(dob, str) else (dob.ToDatetime().isoformat() if hasattr(dob, "ToDatetime") else str(dob))
                logger.debug(f"Formatted resolution date: {res_str}, dob: {dob_str}")
                iso_age = processor.convert_date_to_iso_age(res_str, dob_str)
                if iso_age:
                    resolution = TimeElement(age=Age(iso8601duration=iso_age))
            except Exception as e:
                logger.error(f"Error processing resolution date: {e}")
    
    return resolution

def _extract_severity(
    data: dict, 
    processor: DataProcessor, 
    all_instruments: List[str] = None,
    data_context: dict = None
) -> Optional[OntologyClass]:
    """
    Extracts severity information from the data.
    Enhanced to support multi-instrument field access.
    
    Args:
        data (dict): The data to extract from.
        processor (DataProcessor): The data processor.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        data_context (dict, optional): Additional data context for field lookup.
        
    Returns:
        Optional[OntologyClass]: Severity ontology class or None.
    """
    severity = None
    field = processor.mapping_config.get("severity_field")
    
    if field:
        val = None
        
        # Try multi-instrument lookup first if available
        if all_instruments and data_context:
            val = _get_multi_instrument_field_value(
                data=data_context,
                instruments=all_instruments,
                field_paths=[field]
            )
        
        # If not found or multi-instrument lookup not available, use direct field access
        if val is None:
            val = _get_field_value(data, field)
        
        if val:
            sid = processor.process_code(val)
            label = processor.fetch_label(val, "PhenotypeSeverity")
            if label:
                severity = OntologyClass(id=sid, label=label)
    
    return severity

def _extract_evidence(
    data: dict, 
    processor: DataProcessor, 
    all_instruments: List[str] = None,
    data_context: dict = None
) -> Optional[List[Evidence]]:
    """
    Extracts evidence information from the data.
    Enhanced to support multi-instrument field access.
    
    Args:
        data (dict): The data to extract from.
        processor (DataProcessor): The data processor.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        data_context (dict, optional): Additional data context for field lookup.
        
    Returns:
        Optional[List[Evidence]]: List of evidence or None.
    """
    evidence_list = None
    field = processor.mapping_config.get("evidence_field")
    
    if field:
        val = None
        
        # Try multi-instrument lookup first if available
        if all_instruments and data_context:
            val = _get_multi_instrument_field_value(
                data=data_context,
                instruments=all_instruments,
                field_paths=[field]
            )
        
        # If not found or multi-instrument lookup not available, use direct field access
        if val is None:
            val = _get_field_value(data, field)
        
        if val:
            eid = processor.process_code(val)
            label = processor.fetch_label(val)
            evidence = Evidence(evidence_code=OntologyClass(id=eid, label=label or "Unknown Evidence"))
            evidence_list = [evidence]
    
    return evidence_list

def _extract_modifiers(
    data: dict, 
    processor: DataProcessor, 
    all_instruments: List[str] = None,
    data_context: dict = None
) -> List[OntologyClass]:
    """
    Extracts modifier information from the data.
    Enhanced to support multi-instrument field access.
    
    Args:
        data (dict): The data to extract from.
        processor (DataProcessor): The data processor.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        data_context (dict, optional): Additional data context for field lookup.
        
    Returns:
        List[OntologyClass]: List of modifiers.
    """
    modifiers = []
    
    for i in range(1, 10):
        field = processor.mapping_config.get(f"modifier_field_{i}")
        if not field:
            continue
        
        val = None
        
        # Try multi-instrument lookup first if available
        if all_instruments and data_context:
            val = _get_multi_instrument_field_value(
                data=data_context,
                instruments=all_instruments,
                field_paths=[field]
            )
        
        # If not found or multi-instrument lookup not available, use direct field access
        if val is None:
            val = _get_field_value(data, field)
        
        if val:
            mid = processor.process_code(val)
            label = processor.fetch_label(val)
            if label:
                modifiers.append(OntologyClass(id=mid, label=label))
    
    return modifiers