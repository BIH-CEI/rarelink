import logging
from phenopackets import Disease, OntologyClass, TimeElement, Age
from rarelink.utils.processor import DataProcessor

logger = logging.getLogger(__name__)

def map_diseases(
    data: dict, 
    processor: DataProcessor,
    dob: str = None
    ) -> list:
    """
    Maps disease data to the Phenopacket schema Disease block.
    Enhanced to handle both repeating and non-repeating elements and properly process codes.

    Args:
        data (dict): Input data from any schema.
        processor (DataProcessor): Handles all data processing logic.
        dob (str, optional): Date of birth for age calculations.

    Returns:
        list: A list of Phenopacket Disease blocks.
    """
    # Initialize list for diseases
    diseases = []
    
    # Determine if we're dealing with a repeated instrument or direct fields
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument") or processor.mapping_config.get("instrument_name")
    
    try:
        # Check if we have a non-repeating element specified (like "basic_form")
        logger.debug(f"Looking for disease data, instrument_name: {instrument_name}")
        
        # CASE 1: Handle direct top-level section (e.g., "basic_form")
        # This is the most common case for primary disease data
        if instrument_name and instrument_name in data:
            logger.debug(f"Found direct top-level section: {instrument_name}")
            disease_data = data[instrument_name]
            disease = _create_disease_block(disease_data, processor, dob)
            if disease:
                diseases.append(disease)
                logger.debug(f"Created disease from top-level section: {disease.term.id}")
                return diseases
            
        # CASE 2: Handle repeated elements (e.g., multiple diseases in repeating instruments)
        if "repeated_elements" in data and instrument_name:
            logger.debug(f"Processing diseases from repeated instrument: {instrument_name}")
            repeated_elements = data.get("repeated_elements", [])
            
            if repeated_elements:
                disease_elements = [
                    element for element in repeated_elements
                    if element.get("redcap_repeat_instrument") == instrument_name
                ]
                
                if disease_elements:
                    logger.debug(f"Found {len(disease_elements)} disease elements")
                    for disease_element in disease_elements:
                        # Get the nested data for this instrument
                        if instrument_name in disease_element:
                            disease_data = disease_element.get(instrument_name)
                            if not disease_data:
                                logger.debug(f"Empty data found for instrument {instrument_name} in element")
                                continue
                        else:
                            # For the case where the data is nested under a key like "disease" within the element
                            instrument_data_key = _find_disease_data_key(disease_element, instrument_name)
                            if not instrument_data_key:
                                logger.debug(f"No matching data key found for instrument {instrument_name} in element")
                                continue
                            
                            disease_data = disease_element.get(instrument_data_key)
                            if not disease_data:
                                logger.debug(f"No data found for key {instrument_data_key} in element")
                                continue
                        
                        disease = _create_disease_block(disease_data, processor, dob)
                        if disease:
                            diseases.append(disease)
                            logger.debug(f"Created disease from repeated element: {disease.term.id}")
                else:
                    logger.debug(f"No elements found for instrument: {instrument_name}")
            else:
                logger.debug("No repeated elements found in data")
        
        # CASE 3: Handle non-repeating disease as fallback
        # This is needed when the instrument_name doesn't directly match a top-level key
        if not diseases:
            logger.debug("Attempting to extract disease from non-repeating fields")
            fallback_diseases = _process_nonrepeating_disease(data, processor, dob)
            if fallback_diseases:
                diseases.extend(fallback_diseases)
                
        return diseases

    except Exception as e:
        logger.error(f"Failed to map diseases: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        return []

def _find_disease_data_key(element, instrument_name):
    """
    Find the key that contains the disease data within an element.
    This handles cases where the instrument name may not directly match the data key.
    """
    # Common patterns for disease data keys
    possible_keys = [
        instrument_name, 
        instrument_name.lower(),
        "disease",  # For RareLink format
        instrument_name.split('_')[-1],  # Extract just the last part (e.g., "disease" from "rarelink_5_disease")
    ]
    
    for key in possible_keys:
        if key in element:
            return key
            
    return None

def _process_nonrepeating_disease(data, processor, dob):
    """Process disease data from non-repeating elements."""
    logger.debug("Processing non-repeating disease data")
    
    # Get the term field paths to determine instrument path
    instrument_path = None
    for i in range(1, 6):
        field_key = f"term_field_{i}"
        if field_key not in processor.mapping_config:
            continue
            
        field_path = processor.mapping_config[field_key]
        if not field_path:
            continue
            
        if "." in field_path:
            instrument_path = field_path.split(".", 1)[0]
            break
    
    if instrument_path and instrument_path in data:
        logger.debug(f"Found instrument path: {instrument_path}")
        disease_data = data.get(instrument_path)
        disease = _create_disease_block(disease_data, processor, dob)
        if disease:
            logger.debug(f"Created disease from instrument path: {disease.term.id}")
            return [disease]
    
    # Last resort - try to create from entire data structure
    logger.debug("Trying to create disease from entire data structure")
    disease = _create_disease_block(data, processor, dob)
    return [disease] if disease else []
            
def _create_disease_block(disease_data, processor, dob):
    """Create a Disease block from the provided data."""
    try:
        logger.debug(f"Creating disease block from data type: {type(disease_data)}")
        if isinstance(disease_data, dict):
            logger.debug(f"Data keys: {list(disease_data.keys())}")
        
        # Term - try multiple fields in order
        term_id = None
        for i in range(1, 6):  # Try term_field_1 through term_field_5
            field_key = f"term_field_{i}"
            if field_key not in processor.mapping_config:
                continue
                
            field_path = processor.mapping_config[field_key]
            if not field_path:
                continue
                
            # Handle direct and nested field access
            if "." in field_path:
                # Nested field
                parts = field_path.split(".", 1)
                if len(parts) == 2:
                    # If the first part is the same as our data key (e.g., "basic_form"),
                    # we just need to look at the second part
                    if disease_data and isinstance(disease_data, dict) and parts[1] in disease_data:
                        term_id = disease_data[parts[1]]
                        logger.debug(f"Found disease term ID in nested field {parts[1]}: {term_id}")
                        break
            else:
                # Handle dynamic field selection based on disease_coding in RareLink
                if disease_data and isinstance(disease_data, dict):
                    if "disease_coding" in disease_data and field_path.endswith(disease_data["disease_coding"]):
                        # If disease_coding matches the field suffix, use this field
                        if field_path in disease_data and disease_data[field_path]:
                            term_id = disease_data[field_path]
                            logger.debug(f"Found disease term ID using disease_coding match in field {field_path}: {term_id}")
                            break
                    elif field_path in disease_data and disease_data[field_path]:
                        # Direct field in the current data
                        term_id = disease_data[field_path]
                        logger.debug(f"Found disease term ID in direct field {field_path}: {term_id}")
                        break
        
        if not term_id:
            logger.debug(f"No disease term ID found in any configured fields. Fields checked: {[f'term_field_{i}' for i in range(1, 6) if f'term_field_{i}' in processor.mapping_config]}")
            return None
            
        logger.debug(f"Using raw disease term ID: {term_id}")
        
        # Process the code to proper ontology format
        processed_id = processor.process_code(term_id)
        logger.debug(f"Processed disease term ID: {processed_id}")
        
        # Try to fetch the label using different methods
        term_label = None
        
        # 1. Try direct lookup with original code
        term_label = processor.fetch_label(term_id)
        if term_label:
            logger.debug(f"Found label using original code: {term_label}")
            
        # 2. If that fails, try with the processed code
        if not term_label and processed_id != term_id:
            term_label = processor.fetch_label(processed_id)
            if term_label:
                logger.debug(f"Found label using processed code: {term_label}")
        
        # 3. Try using Enum classes in the processor
        if not term_label and hasattr(processor, "enum_classes"):
            for prefix, enum_class in processor.enum_classes.items():
                if term_id.lower().startswith(prefix.lower()):
                    term_label = processor.fetch_label_from_enum(term_id, enum_class)
                    if term_label:
                        logger.debug(f"Found label using enum class: {term_label}")
                        break
        
        # Create the ontology class with the processed ID and best label found
        term = OntologyClass(id=processed_id, label=term_label or "Unknown Disease")
        logger.debug(f"Created disease term: {term.id} - {term.label}")

        # Excluded status
        excluded = None
        excluded_field = processor.mapping_config.get("excluded_field")
        if excluded_field:
            excluded_value = _get_field_value(disease_data, excluded_field)
            if excluded_value:
                mapped_value = processor.fetch_mapping_value(
                    "map_disease_verification_status", excluded_value)
                logger.debug(f"Excluded value: {excluded_value}, Mapped value: {mapped_value}")
                if mapped_value == "true":
                    excluded = True
                elif mapped_value == "false":
                    excluded = False

        # Onset
        onset = None
        onset_date_field = processor.mapping_config.get("onset_date_field")
        onset_category_field = processor.mapping_config.get("onset_category_field")
        
        if onset_date_field and dob:
            onset_date = _get_field_value(disease_data, onset_date_field)
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
                        logger.debug(f"Converted disease onset date to ISO age: {iso_age}")
                        onset = TimeElement(age=Age(iso8601duration=iso_age))
                    else:
                        logger.debug(f"Failed to convert disease onset date {onset_date_str} to ISO age")
                except Exception as e:
                    logger.error(f"Error processing disease onset date for ISO age: {e}")
                    import traceback
                    logger.debug(traceback.format_exc())
        
        if not onset and onset_category_field:
            onset_category = _get_field_value(disease_data, onset_category_field)
            if onset_category:
                onset_label = processor.fetch_label(onset_category, enum_class="AgeAtOnset")
                onset_code = processor.process_code(onset_category)
                if onset_label:
                    onset = TimeElement(
                        ontology_class=OntologyClass(
                            id=onset_code, 
                            label=onset_label
                        )
                    )

        # Primary site
        primary_site = None
        primary_site_field = processor.mapping_config.get("primary_site_field")
        if primary_site_field:
            primary_site_id = _get_field_value(disease_data, primary_site_field)
            if primary_site_id:
                primary_site_label = processor.fetch_label(primary_site_id)
                primary_site = OntologyClass(
                    id=primary_site_id, 
                    label=primary_site_label or "Unknown Site"
                )

        # Create the Disease block
        disease = Disease(
            term=term,
            onset=onset,
            excluded=excluded,
            primary_site=primary_site
        )
        
        logger.debug(f"Successfully created disease block: {disease.term.id} - {disease.term.label}")
        return disease
        
    except Exception as e:
        logger.error(f"Error creating disease block: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        return None

def _get_field_value(data, field_path):
    """Get a field value from data, handling direct and nested access."""
    if not field_path or not data:
        return None
        
    # Direct field access
    if "." not in field_path:
        return data.get(field_path)
        
    # Nested field access
    parts = field_path.split(".", 1)
    if len(parts) == 2:
        # If parts[0] is missing, use parts[1] directly (this happens when instrument name is same as data key)
        if parts[0] not in data and parts[1] in data:
            return data.get(parts[1])
            
        # Normal case - nested dictionary
        if parts[0] in data:
            nested_data = data.get(parts[0])
            if isinstance(nested_data, dict):
                return nested_data.get(parts[1])
    
    # Try matching the exact path as a fallback
    if field_path in data:
        return data[field_path]
    
    return None