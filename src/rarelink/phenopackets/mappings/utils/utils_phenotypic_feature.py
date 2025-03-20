from typing import Any, Dict, List, Optional
from rarelink.utils.processor.processor import DataProcessor
import logging
from phenopackets import OntologyClass, Evidence, TimeElement, Age

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

def _get_single_type(data: dict, processor: DataProcessor) -> List[str]:
    """
    Extracts a single type value from data using the configured 'type_field'.
    
    Args:
        data (dict): Input element data.
        processor (DataProcessor): Data processor.
    
    Returns:
        List[str]: List with a single type value if found, else an empty list.
    """
    type_field = processor.mapping_config.get("type_field")
    if not type_field:
        logger.debug("No type field configured")
        return []
    value = _get_field_value(data, type_field)
    if not value:
        logger.debug(f"No value found for type field '{type_field}'")
        return []
    return [value]

def _determine_data_model(processor: DataProcessor, instrument_name: str) -> str:
    """
    Determines which data model to use based on configuration and instrument name.
    
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
    has_multiple = any(f"type_field_{i}" in processor.mapping_config for i in range(2, 11))
    is_infection = ("infection" in instrument_name.lower() or instrument_name == "infections_initial_form")
    return "infections" if (has_multiple or is_infection) else "standard"

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

def _get_infection_types(data: dict, processor: DataProcessor) -> List[str]:
    """
    Extracts infection type values from the data, handling multiple type fields.
    
    Args:
        data (dict): The data to extract from.
        processor (DataProcessor): The data processor with mapping configuration.
        
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
        value = _get_field_value(data, field_path)
        if value:
            logger.debug(f"Found value '{value}' for type field '{key}'")
            type_values.append(value)
    
    # If no explicit type fields yielded a value, scan the keys using common patterns.
    if not type_values:
        scan_patterns = processor.mapping_config.get("scan_patterns", [
            "infection_", "disease_", "phenotype_", "symptom_", "finding_"
        ])
        for field_name, value in data.items():
            if isinstance(value, str) and value and any(pattern in field_name.lower() for pattern in scan_patterns):
                logger.debug(f"Found scan match: field '{field_name}' with value '{value}'")
                type_values.append(value)
    
    if not type_values:
        logger.debug(f"No type values found in data with keys: {list(data.keys())[:10]}")
    
    return type_values



def _extract_excluded_status(data: dict, processor: DataProcessor) -> Optional[bool]:
    excluded = None
    field = processor.mapping_config.get("excluded_field")
    if field:
        val = _get_field_value(data, field)
        if val:
            mapped = processor.fetch_mapping_value("phenotypic_feature_status", val)
            if mapped == "true":
                excluded = True
            elif mapped == "false":
                excluded = False
    return excluded

def _extract_onset(data: dict, processor: DataProcessor, dob: str = None) -> Optional[TimeElement]:
    onset = None
    field = processor.mapping_config.get("onset_date_field")
    alt_field = processor.mapping_config.get("onset_age_field")
    if field and dob:
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
        alt_val = _get_field_value(data, alt_field)
        if alt_val:
            label = processor.fetch_label(alt_val, "AgeOfOnset")
            pid = processor.process_code(alt_val)
            if label:
                onset = TimeElement(ontology_class=OntologyClass(id=pid, label=label))
    return onset

def _extract_resolution(data: dict, processor: DataProcessor, dob: str = None) -> Optional[TimeElement]:
    resolution = None
    field = processor.mapping_config.get("resolution_field")
    if field and dob:
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

def _extract_severity(data: dict, processor: DataProcessor) -> Optional[OntologyClass]:
    severity = None
    field = processor.mapping_config.get("severity_field")
    if field:
        val = _get_field_value(data, field)
        if val:
            sid = processor.process_code(val)
            label = processor.fetch_label(val, "PhenotypeSeverity")
            if label:
                severity = OntologyClass(id=sid, label=label)
    return severity

def _extract_evidence(data: dict, processor: DataProcessor) -> Optional[List[Evidence]]:
    evidence_list = None
    field = processor.mapping_config.get("evidence_field")
    if field:
        val = _get_field_value(data, field)
        if val:
            eid = processor.process_code(val)
            label = processor.fetch_label(val)
            evidence = Evidence(evidence_code=OntologyClass(id=eid, label=label or "Unknown Evidence"))
            evidence_list = [evidence]
    return evidence_list

def _extract_modifiers(data: dict, processor: DataProcessor) -> List[OntologyClass]:
    modifiers = []
    for i in range(1, 6):
        field = processor.mapping_config.get(f"modifier_field_{i}")
        if not field:
            continue
        val = _get_field_value(data, field)
        if val:
            mid = processor.process_code(val)
            label = processor.fetch_label(val)
            if label:
                modifiers.append(OntologyClass(id=mid, label=label))
    return modifiers
