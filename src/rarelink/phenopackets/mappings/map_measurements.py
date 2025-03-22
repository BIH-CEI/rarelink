import logging
from typing import List, Any, Optional, Dict
from phenopackets import (
    Measurement, 
    OntologyClass, 
    Value, 
    Quantity, 
    TimeElement, 
    Procedure, 
    Age
)
from rarelink.utils.processor import DataProcessor
from rarelink.utils.loading import _get_multi_instrument_field_value

logger = logging.getLogger(__name__)

def map_measurements(data: dict, processor: DataProcessor, dob: str = None) -> list:
    """
    Maps measurement data to the Phenopacket schema Measurement block.
    Enhanced to support multi-instrument, multi-measurement configurations.

    Args:
        data (dict): Input data.
        processor (DataProcessor): Handles all data processing logic.
        dob (str, optional): Date of birth for age calculations.

    Returns:
        list: A list of Phenopacket Measurement blocks.
    """
    mapping_config = processor.mapping_config
    
    # Check if this is a multi-instrument configuration (similar to phenotypicFeatures)
    if isinstance(mapping_config.get("measurements"), list):
        logger.debug("Using multi-instrument measurement configuration")
        all_measurements = []
        
        # Process each instrument configuration
        for config in mapping_config.get("measurements", []):
            # Create a new processor for this configuration
            instrument_processor = DataProcessor(mapping_config=config.get("mapping_block", {}))
            instrument_processor.enable_debug(getattr(processor, 'debug_mode', False))
            
            # Apply additional configuration
            for key, value in config.items():
                if key != "mapping_block":
                    instrument_processor.mapping_config[key] = value
                    
            # Add enum classes if present
            if "enum_classes" in config:
                for prefix, enum_class in config.get("enum_classes", {}).items():
                    instrument_processor.add_enum_class(prefix, enum_class)
                    
            # Map measurements for this instrument
            measurements = _map_instrument_measurements(data, instrument_processor, dob)
            if measurements:
                all_measurements.extend(measurements)
                logger.debug(f"Added {len(measurements)} measurements from {config.get('instrument_name')}")
                
        return all_measurements
    
    # Standard single instrument approach
    return _map_instrument_measurements(data, processor, dob)

def _map_instrument_measurements(data: dict, processor: DataProcessor, dob: str = None) -> List[Measurement]:
    """
    Maps measurement data for a specific instrument.
    Enhanced to support multi-measurement configurations.
    
    Args:
        data (dict): Input data dictionary.
        processor (DataProcessor): Data processor with mapping configuration.
        dob (str, optional): Date of birth for age calculations.
        
    Returns:
        List[Measurement]: List of mapped measurements.
    """
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
    multi_measurement = processor.mapping_config.get("multi_measurement", False)
    measurement_fields = processor.mapping_config.get("measurement_fields", [])
    
    logger.debug(f"Processing measurements for instrument: {instrument_name}")
    logger.debug(f"Multi-measurement mode: {multi_measurement}")
    
    try:
        # Get repeated elements if available
        repeated_elements = data.get("repeated_elements", [])
        
        # Filter relevant measurement elements
        measurement_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        
        # If no repeated elements, try direct access
        if not measurement_elements and instrument_name in data:
            measurement_elements = [{"redcap_repeat_instrument": instrument_name, instrument_name: data[instrument_name]}]
            
        logger.debug(f"Found {len(measurement_elements)} elements for instrument {instrument_name}")
        
        # Process all measurement elements
        measurements = []
        for element in measurement_elements:
            element_data = element.get(instrument_name)
            if not element_data:
                logger.debug(f"No data found for element with instrument {instrument_name}")
                continue
                
            # Handle multi-measurement
            if multi_measurement and measurement_fields:
                # Process measurements field by field
                for field_config in measurement_fields:
                    # Skip if assay field is missing
                    assay_field = field_config.get("assay")
                    if not assay_field or not element_data.get(assay_field):
                        continue
                        
                    # Skip if value field is missing or empty
                    value_field = field_config.get("value")
                    if not value_field or not element_data.get(value_field):
                        continue
                        
                    measurement = _create_measurement_from_fields(
                        element_data, 
                        processor, 
                        dob,
                        field_config
                    )
                    
                    if measurement:
                        measurements.append(measurement)
                        logger.debug(f"Added measurement for {field_config.get('assay')}")
            else:
                # Standard single measurement approach (RareLinkCDM compatibility)
                measurement = _create_standard_measurement(element_data, processor, dob)
                if measurement:
                    measurements.append(measurement)
                    
        logger.debug(f"Returning {len(measurements)} measurements for instrument {instrument_name}")
        return measurements
        
    except Exception as e:
        logger.error(f"Error mapping measurements for instrument {instrument_name}: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        return []

def _create_measurement_from_fields(data, processor, dob, field_config):
    """
    Create a measurement from field configuration with support for different value types.
    
    Args:
        data (dict): Element data.
        processor (DataProcessor): Data processor.
        dob (str): Date of birth.
        field_config (dict): Field configuration with assay, value, unit, etc.
        
    Returns:
        Measurement: A measurement object or None.
    """
    if not field_config or not field_config.get("assay"):
        return None
        
    # Extract field names from configuration
    assay_field_name = field_config.get("assay")
    value_field_name = field_config.get("value")
    interpretation_field_name = field_config.get("interpretation")
    unit_field_name = field_config.get("unit")
    unit_alt_field_name = field_config.get("unit_alt")
    value_type = field_config.get("value_type", "quantity").lower()
    
    # Get actual values from the data
    assay_code = data.get(assay_field_name)
    
    # Skip if assay is missing
    if not assay_code:
        return None
    
    # Create assay - using the code from the base field
    logger.debug(f"Processing assay code: {assay_code} from field {assay_field_name}")
    assay_id = processor.process_code(assay_code)
    assay_label = processor.fetch_label(assay_code)
    
    # If no label found, extract from field name (e.g., "lympheno_loinc_8122_4" → "8122_4")
    if not assay_label:
        parts = assay_field_name.split('_')
        if len(parts) >= 3:
            assay_label = f"{parts[-2]}_{parts[-1]}"
            
    assay = OntologyClass(id=assay_id, label=assay_label or "Unknown Assay")
    
    # Create value based on value_type
    value = None
    
    if value_type == "ontology":
        # Create OntologyClass value
        value_data = data.get(value_field_name)
        if not value_data:
            return None
            
        logger.debug(f"Processing ontology value: {value_data}")
        value_id = processor.process_code(value_data)
        value_label = processor.fetch_label(value_data)
        ontology_class = OntologyClass(id=value_id, label=value_label or "Unknown Value")
        value = Value(ontology_class=ontology_class)
        
    elif value_type == "dual":
        # Try interpretation field first, then fall back to numeric value
        interpretation_value = data.get(interpretation_field_name)
        numeric_value = data.get(value_field_name)
        
        if interpretation_value:
            # Use interpretation (categorical value)
            logger.debug(f"Using interpretation value: {interpretation_value}")
            interp_id = processor.process_code(interpretation_value)
            interp_label = processor.fetch_label(interpretation_value)
            ontology_class = OntologyClass(id=interp_id, label=interp_label or "Unknown Interpretation")
            value = Value(ontology_class=ontology_class)
        elif numeric_value:
            # Fall back to numeric value with unit
            try:
                logger.debug(f"Using numeric value: {numeric_value}")
                value_numeric = float(numeric_value)
                
                # Get unit from either primary or alternative unit field
                unit_code = data.get(unit_field_name)
                if not unit_code and unit_alt_field_name:
                    unit_code = data.get(unit_alt_field_name)
                
                if unit_code:
                    logger.debug(f"Using unit: {unit_code}")
                    unit_id = processor.process_code(unit_code)
                    unit_label = processor.fetch_label(unit_code)
                    unit = OntologyClass(id=unit_id, label=unit_label or "Unknown Unit")
                    quantity = Quantity(value=value_numeric, unit=unit)
                else:
                    quantity = Quantity(value=value_numeric)
                    
                value = Value(quantity=quantity)
            except (ValueError, TypeError):
                logger.warning(f"Could not convert value {numeric_value} to float")
                return None
        else:
            # No value available
            return None
            
    else:
        # Create Quantity value (default)
        value_data = data.get(value_field_name)
        if not value_data:
            return None
            
        try:
            value_numeric = float(value_data)
            quantity = None
            
            # Get unit from either primary or alternative unit field
            unit_code = None
            if unit_field_name:
                unit_code = data.get(unit_field_name)
            
            if not unit_code and unit_alt_field_name:
                unit_code = data.get(unit_alt_field_name)
            
            if unit_code:
                # Create unit with proper ontology
                logger.debug(f"Processing unit code: {unit_code}")
                unit_id = processor.process_code(unit_code)
                unit_label = processor.fetch_label(unit_code)
                unit = OntologyClass(id=unit_id, label=unit_label or "Unknown Unit")
                quantity = Quantity(value=value_numeric, unit=unit)
            else:
                # Unit-less quantity
                quantity = Quantity(value=value_numeric)
                
            value = Value(quantity=quantity)
        except (ValueError, TypeError):
            logger.warning(f"Could not convert value {value_data} to float")
            return None
    
    # Get time observed (date)
    time_observed_field = processor.mapping_config.get("time_observed_field")
    time_observed = None
    
    if time_observed_field and dob and data.get(time_observed_field):
        try:
            time_observed_str = data.get(time_observed_field)
            dob_str = dob if isinstance(dob, str) else str(dob)
            
            iso_age = processor.convert_date_to_iso_age(time_observed_str, dob_str)
            if iso_age:
                time_observed = TimeElement(age=Age(iso8601duration=iso_age))
        except Exception as e:
            logger.error(f"Error processing time observed: {e}")
    
    # Create the measurement
    measurement = Measurement(
        assay=assay,
        value=value,
        time_observed=time_observed
    )
    
    return measurement

def _create_standard_measurement(data, processor, dob):
    """
    Create measurement using standard RareLink CDM field mappings.
    
    Args:
        data (dict): Element data.
        processor (DataProcessor): Data processor.
        dob (str): Date of birth.
        
    Returns:
        Measurement: A measurement object or None.
    """
    # Standard fields from original implementation
    assay_field_name = processor.mapping_config.get("assay_field")
    value_field_name = processor.mapping_config.get("value_field")
    value_unit_field_name = processor.mapping_config.get("value_unit_field")
    time_observed_field = processor.mapping_config.get("time_observed_field")
    
    # Get procedure fields
    procedure_fields = []
    for i in range(1, 4):
        field = processor.mapping_config.get(f"procedure_field_{i}")
        if field:
            procedure_fields.append(field)
    
    # Skip if field names are missing
    if not assay_field_name or not value_field_name:
        return None
        
    # Get the actual values from data
    assay_code = data.get(assay_field_name)
    value_data = data.get(value_field_name)
    unit_code = value_unit_field_name and data.get(value_unit_field_name)
    
    # Skip if values are missing
    if not assay_code or not value_data:
        return None
    
    # Create assay
    logger.debug(f"Processing standard assay code: {assay_code}")
    assay_id = processor.process_code(assay_code)
    assay_label = processor.fetch_label(assay_code)
    assay = OntologyClass(id=assay_id, label=assay_label or "Unknown Assay")
    
    # Create value and quantity
    try:
        value_numeric = float(value_data)
        quantity = None
        
        if unit_code:
            logger.debug(f"Processing standard unit code: {unit_code}")
            unit_id = processor.process_code(unit_code)
            unit_label = processor.fetch_label(unit_code)
            unit = OntologyClass(id=unit_id, label=unit_label or "Unknown Unit")
            quantity = Quantity(value=value_numeric, unit=unit)
        else:
            quantity = Quantity(value=value_numeric)
            
        value = Value(quantity=quantity)
    except (ValueError, TypeError):
        logger.warning(f"Could not convert value {value_data} to float")
        return None
    
    # Get time observed (date)
    time_observed = None
    if time_observed_field and dob and data.get(time_observed_field):
        try:
            time_observed_str = data.get(time_observed_field)
            dob_str = dob if isinstance(dob, str) else str(dob)
            
            iso_age = processor.convert_date_to_iso_age(time_observed_str, dob_str)
            if iso_age:
                time_observed = TimeElement(age=Age(iso8601duration=iso_age))
        except Exception as e:
            logger.error(f"Error processing time observed: {e}")
    
    # Create procedure
    procedure = None
    for field in procedure_fields:
        if data.get(field):
            proc_id = processor.process_code(data.get(field))
            proc_label = processor.fetch_label(data.get(field))
            procedure = Procedure(
                code=OntologyClass(id=proc_id, label=proc_label or "Unknown Procedure")
            )
            break
    
    # Create measurement
    measurement = Measurement(
        assay=assay,
        value=value,
        time_observed=time_observed,
        procedure=procedure
    )
    
    return measurement