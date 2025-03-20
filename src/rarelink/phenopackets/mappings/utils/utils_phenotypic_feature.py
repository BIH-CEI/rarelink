from typing import Any, Dict, List, Optional
from rarelink.utils.processor.processor import DataProcessor
import logging
from phenopackets import OntologyClass, Evidence, TimeElement, Age
from rarelink.utils.loading import _get_multi_instrument_field_value

logger = logging.getLogger(__name__)

def _get_field_value(data: dict, field_path: str) -> Any:
    """
    Gets a field value from a dict, supporting dot notation for nested keys.
    
    Args:
        data (dict): Input data.
        field_path (str): Field path (e.g., "patient.birthdate").
    
    Returns:
        Any: The field value or None.
    """
    if not field_path or not data:
        return None
    if "." not in field_path:
        return data.get(field_path)
    parts = field_path.split(".", 1)
    if parts[0] in data and isinstance(data.get(parts[0]), dict):
        return data.get(parts[0]).get(parts[1])
    return data.get(field_path)

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
        str: "infections", "standard", or "unknown".
    """
    explicit_model = processor.mapping_config.get("data_model")
    if explicit_model:
        logger.debug(f"Using explicitly defined data model: {explicit_model}")
        return explicit_model
    
    has_multiple = any(f"type_field_{i}" in processor.mapping_config for i in range(2, 20))
    is_infection = ("infection" in instrument_name.lower() or instrument_name == "infections_initial_form")
    
    # Add support for systemic/organ-specific conditions
    is_condition = (
        "systemic" in instrument_name.lower() or
        "organ_specific" in instrument_name.lower() or
        "patients_systemic_or_organ_specific_conditions" == instrument_name
    )
    
    return "infections" if (has_multiple or is_infection or is_condition) else "standard"

def _get_data_elements(data: dict, instrument_name: str) -> List[Dict[str, Any]]:
    """
    Extracts the data elements to process for a given instrument.
    
    Args:
        data (dict): Input data.
        instrument_name (str): Name of the instrument.
    
    Returns:
        List[Dict[str, Any]]: List of data elements.
    """
    elements = []
    repeated = data.get("repeated_elements", [])
    if repeated:
        filtered = [el for el in repeated if el.get("redcap_repeat_instrument") == instrument_name]
        processed = []
        for el in filtered:
            for key in [instrument_name, "phenotypic_feature", "clinical_phenotype", "phenotype_data"]:
                if key in el:
                    processed.append(el[key])
                    break
            else:
                processed.append(el)
        return processed
    elif instrument_name in data:
        return [data[instrument_name]]
    elif any(k in data for k in ["phenotypic_feature", "clinical_phenotype", "phenotype_data"]):
        for key in ["phenotypic_feature", "clinical_phenotype", "phenotype_data"]:
            if key in data:
                return [data[key]]
    elif any(k.startswith(("snomedct_", "hp_")) for k in data.keys()):
        return [data]
    return elements

def _get_infection_types(data: dict, processor: DataProcessor, all_instruments: List[str] = None) -> List[str]:
    """
    Extracts infection type values from the data, handling multiple type fields.
    Enhanced to support multi-instrument field access.
    
    Args:
        data (dict): The data to extract from.
        processor (DataProcessor): The data processor with mapping configuration.
        all_instruments (List[str], optional): List of all instruments for field lookup.
        
    Returns:
        List[str]: A list of infection type values.
    """
    type_values = []
    
    # Gather all type field keys from the processor config.
    type_fields = {}
    
    # Primary type field
    primary_type_field = processor.mapping_config.get("type_field")
    if primary_type_field:
        type_fields["primary"] = primary_type_field
    
    # Additional numbered type fields (support up to 30)
    for i in range(2, 31):
        key = f"type_field_{i}"
        if key in processor.mapping_config:
            field_path = processor.mapping_config[key]
            if field_path:
                type_fields[key] = field_path
    
    logger.debug(f"Checking {len(type_fields)} type fields for values")
    for key, field_path in type_fields.items():
        value = None
        
        # Try multi-instrument lookup first if available
        if all_instruments and hasattr(processor, 'mapping_config') and 'all_instruments' in processor.mapping_config:
            # Use the full data and all instruments for lookup
            full_data = processor.mapping_config.get('full_data', {})
            value = _get_multi_instrument_field_value(
                data=full_data,
                instruments=all_instruments,
                field_paths=[field_path]
            )
        
        # If not found or multi-instrument lookup not available, use direct field access
        if value is None:
            value = _get_field_value(data, field_path)
        
        if value:
            logger.debug(f"Found value '{value}' for type field '{key}'")
            type_values.append(value)
    
    # If no explicit type fields yielded a value, scan the keys using common patterns.
    if not type_values:
        scan_patterns = processor.mapping_config.get("scan_patterns", [
            "infection_", "disease_", "phenotype_", "symptom_", "finding_", "hp_", "type_of_"
        ])
        for field_name, value in data.items():
            if isinstance(value, str) and value and any(pattern in field_name.lower() for pattern in scan_patterns):
                logger.debug(f"Found scan match: field '{field_name}' with value '{value}'")
                type_values.append(value)
    
    if not type_values:
        logger.debug(f"No type values found in data with keys: {list(data.keys())[:10]}")
    
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