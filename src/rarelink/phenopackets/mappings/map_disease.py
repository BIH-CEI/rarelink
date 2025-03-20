import logging
from phenopackets import Disease, OntologyClass, TimeElement, Age
from rarelink.utils.processor import DataProcessor
from rarelink.utils.loading import (
    _get_multi_instrument_field_value, 
    generic_map_entities
)

logger = logging.getLogger(__name__)

def map_diseases(
    data: dict, 
    processor: DataProcessor,
    dob: str = None
    ) -> list:
    """
    Maps disease data to the Phenopacket schema Disease block.
    Enhanced to handle both repeating and non-repeating elements, properly process codes,
    and support fields from multiple instruments.

    Args:
        data (dict): Input data from any schema.
        processor (DataProcessor): Handles all data processing logic.
        dob (str, optional): Date of birth for age calculations.

    Returns:
        list: A list of Phenopacket Disease blocks.
    """
    # Initialize list for diseases
    diseases = []
    
    # Extract all instruments from the configuration
    instruments = []
    
    # Check for specific instrument names
    instrument_name = processor.mapping_config.get("instrument_name")
    if isinstance(instrument_name, (list, set)):
        instruments.extend(list(instrument_name))
    elif instrument_name:
        instruments.append(instrument_name)
        
    # Add the redcap_repeat_instrument if it's not already included
    repeat_instrument = processor.mapping_config.get("redcap_repeat_instrument")
    if repeat_instrument and repeat_instrument not in instruments:
        instruments.append(repeat_instrument)
    
    if not instruments:
        logger.debug("No instruments configured for disease mapping.")
        return []
    
    try:
        logger.debug(f"Looking for disease data using instruments: {instruments}")
        
        # CASE 1: Try to find term data in the direct instrument sections
        for instrument in instruments:
            if instrument in data:
                logger.debug(f"Found direct top-level section: {instrument}")
                instrument_data = data[instrument]
                
                # Create a disease using this instrument's data and all instruments for field lookup
                disease = _create_disease_block(data, processor, dob, instruments)
                
                if disease:
                    diseases.append(disease)
                    logger.debug(f"Created disease from top-level section: {disease.term.id}")
                    return diseases
                
        # CASE 2: Try repeating elements if no direct disease found
        if not diseases and "repeated_elements" in data:
            logger.debug(f"Looking in repeated elements for instruments: {instruments}")
            repeated_elements = data.get("repeated_elements", [])
            
            if repeated_elements:
                # Check each repeating instrument
                for instrument in instruments:
                    disease_elements = [
                        element for element in repeated_elements
                        if element.get("redcap_repeat_instrument") == instrument
                    ]
                    
                    if disease_elements:
                        logger.debug(f"Found {len(disease_elements)} disease elements for instrument {instrument}")
                        for element in disease_elements:
                            # Get the instrument data
                            instrument_data = element.get(instrument)
                            
                            # Create a copy of the full data but replace the instrument data with this element's data
                            element_data = data.copy()
                            if instrument_data:
                                element_data[instrument] = instrument_data
                            
                            # Try to create a disease
                            disease = _create_disease_block(element_data, processor, dob, instruments)
                            if disease:
                                diseases.append(disease)
                                logger.debug(f"Created disease from repeated element: {disease.term.id}")
        
        # CASE 3: If still no diseases, try the generic mapper as a last resort
        if not diseases:
            logger.debug("Attempting to extract disease across multiple instruments using generic mapper")
            try:
                # Make sure the instruments are in the processor config for the generic mapper
                processor.mapping_config["instrument_name"] = instruments
                
                diseases = generic_map_entities(
                    data=data,
                    processor=processor,
                    dob=dob,
                    mapping_type="diseases",
                    create_entity_func=lambda d, p, b: _create_disease_block(d, p, b, instruments)
                )
                if diseases:
                    logger.debug(f"Successfully created {len(diseases)} diseases using generic mapper")
            except Exception as e:
                logger.error(f"Error using generic mapper: {e}")
                import traceback
                logger.debug(traceback.format_exc())
                
        return diseases

    except Exception as e:
        logger.error(f"Failed to map diseases: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        return []

def _create_disease_block(data, processor, dob, instruments=None):
    """
    Create a Disease block from the provided data.
    Enhanced to use multiple instruments for field access.
    
    Args:
        data (dict): Input data dictionary.
        processor (DataProcessor): The data processor.
        dob (str): Date of birth for age calculations.
        instruments (list): List of instruments to search for fields.
        
    Returns:
        Disease: A fully constructed Disease block or None.
    """
    try:
        logger.debug(f"Creating disease block using instruments: {instruments}")
        
        # Term - try multiple fields in order
        term_id = None
        term_field_keys = []
        
        # Build a list of all term field keys to check
        for i in range(1, 6):
            field_key = f"term_field_{i}"
            if field_key in processor.mapping_config and processor.mapping_config[field_key]:
                term_field_keys.append(field_key)
                
        if not term_field_keys:
            logger.debug("No term field keys found in mapping configuration.")
            return None
            
        logger.debug(f"Term field keys to check: {term_field_keys}")
        
        # Try each term field
        for field_key in term_field_keys:
            field_path = processor.mapping_config[field_key]
            if not field_path:
                continue
                
            # Use multi-instrument field access
            if instruments:
                term_id = _get_multi_instrument_field_value(
                    data=data,
                    instruments=instruments,
                    field_paths=[field_path]
                )
                
                if term_id:
                    logger.debug(f"Found disease term ID using multi-instrument lookup: {term_id} from {field_path}")
                    break
        
        if not term_id:
            logger.debug(f"No disease term ID found in any fields: {term_field_keys}")
            return None
            
        logger.debug(f"Using disease term ID: {term_id}")
        
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
            excluded_value = _get_multi_instrument_field_value(
                data=data,
                instruments=instruments,
                field_paths=[excluded_field]
            )
                
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
            onset_date = _get_multi_instrument_field_value(
                data=data,
                instruments=instruments,
                field_paths=[onset_date_field]
            )
                
            if onset_date:
                try:
                    # Handle various date formats
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
            onset_category = _get_multi_instrument_field_value(
                data=data,
                instruments=instruments,
                field_paths=[onset_category_field]
            )
                
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
            primary_site_id = _get_multi_instrument_field_value(
                data=data,
                instruments=instruments,
                field_paths=[primary_site_field]
            )
                
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