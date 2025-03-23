from typing import Dict, Any, List, Optional
import logging
from phenopackets import (
    Measurement, 
    OntologyClass, 
    Value, 
    Quantity, 
    TimeElement, 
    Procedure, 
    Age
)

from rarelink.phenopackets.mappings.base_mapper import BaseMapper

logger = logging.getLogger(__name__)

class MeasurementMapper(BaseMapper[Measurement]):
    """
    Mapper for Measurement entities in the Phenopacket schema.
    Always returns a list of Measurement objects for consistency.
    """
    
    def map(self, data: Dict[str, Any], **kwargs) -> List[Measurement]:
        """
        Map data to a list of Measurement entities.
        Overrides the base method to ensure a list is always returned.
        
        Args:
            data (Dict[str, Any]): Input data to map
            **kwargs: Additional mapping parameters
                - dob (str, optional): Date of birth for age calculations
            
        Returns:
            List[Measurement]: List of mapped Measurement entities
        """
        # Set multi_entity to True to ensure _map_multi_entity is called
        self.processor.mapping_config["multi_entity"] = True
        
        # Call the base map method which will call _map_multi_entity
        return super().map(data, **kwargs)
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> Optional[Measurement]:
        """
        Map data to a single Measurement entity.
        Note: This method is required by the BaseMapper interface but not directly used
        since we always return multiple entities.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (List[str]): List of instruments for field access
            **kwargs: Additional mapping parameters
                - dob (str, optional): Date of birth for age calculations
            
        Returns:
            Optional[Measurement]: Mapped Measurement entity or None
        """
        dob = kwargs.get('dob')
        
        # Get standard fields from the mapping configuration
        assay_field = self.processor.mapping_config.get("assay_field")
        value_field = self.processor.mapping_config.get("value_field")
        value_unit_field = self.processor.mapping_config.get("value_unit_field")
        time_observed_field = self.processor.mapping_config.get("time_observed_field")
        
        if not assay_field or not value_field:
            logger.debug("Required fields not found in mapping configuration")
            return None
        
        # Get field values
        assay_code = self.get_field(data, "assay_field", instruments=instruments)
        value_data = self.get_field(data, "value_field", instruments=instruments)
        
        if not assay_code or value_data is None:
            logger.debug("Required field values not found in data")
            return None
        
        # Process assay code
        processed_id = self.process_code(assay_code)
        assay_label = self.fetch_label(assay_code) or "Unknown Assay"
        
        # Create assay OntologyClass
        assay = OntologyClass(
            id=processed_id,
            label=assay_label
        )
        
        # Process value
        value = None
        try:
            value_numeric = float(value_data)
            
            # Get unit if available
            unit_code = None
            if value_unit_field:
                unit_code = self.get_field(data, "value_unit_field", instruments=instruments)
            
            if unit_code:
                unit_id = self.process_code(unit_code)
                unit_label = self.fetch_label(unit_code) or "Unknown Unit"
                unit = OntologyClass(id=unit_id, label=unit_label)
                quantity = Quantity(value=value_numeric, unit=unit)
            else:
                quantity = Quantity(value=value_numeric)
                
            value = Value(quantity=quantity)
        except (ValueError, TypeError):
            logger.warning(f"Could not convert value {value_data} to float")
            return None
        
        # Process time observed
        time_observed = None
        if time_observed_field and dob:
            time_value = self.get_field(data, "time_observed_field", instruments=instruments)
            if time_value:
                try:
                    iso_age = self.processor.convert_date_to_iso_age(time_value, dob)
                    if iso_age:
                        time_observed = TimeElement(age=Age(iso8601duration=iso_age))
                except Exception as e:
                    logger.error(f"Error processing time observed: {e}")
        
        # Process procedure fields
        procedure = None
        for i in range(1, 4):  # Check up to 3 procedure fields
            procedure_field_key = f"procedure_field_{i}"
            if procedure_field_key in self.processor.mapping_config:
                procedure_value = self.get_field(data, procedure_field_key, instruments=instruments)
                if procedure_value:
                    proc_id = self.process_code(procedure_value)
                    proc_label = self.fetch_label(procedure_value) or "Unknown Procedure"
                    procedure = Procedure(
                        code=OntologyClass(id=proc_id, label=proc_label)
                    )
                    break
        
        # Create and return the Measurement
        measurement = Measurement(
            assay=assay,
            value=value,
            time_observed=time_observed,
            procedure=procedure
        )
        
        return measurement
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> List[Measurement]:
        """
        Map data to multiple Measurement entities.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (List[str]): List of instruments for field access
            **kwargs: Additional mapping parameters
                - dob (str, optional): Date of birth for age calculations
            
        Returns:
            List[Measurement]: List of mapped Measurement entities
        """
        dob = kwargs.get('dob')
        measurements = []
        
        # Check for multi-measurement configuration
        multi_measurement = self.processor.mapping_config.get("multi_measurement", False)
        measurement_fields = self.processor.mapping_config.get("measurement_fields", [])
        
        instrument_name = self.processor.mapping_config.get("redcap_repeat_instrument")
        logger.debug(f"Processing measurements for instrument: {instrument_name}")
        
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
            for element in measurement_elements:
                # Try both direct access and nested "measurements" field
                element_data = element.get(instrument_name) or element.get("measurements")
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
                            
                        measurement = self._create_measurement_from_fields(
                            element_data, 
                            field_config,
                            dob
                        )
                        
                        if measurement:
                            measurements.append(measurement)
                            logger.debug(f"Added measurement for {field_config.get('assay')}")
                else:
                    # Use the single entity mapper for standard measurements
                    element_data_dict = {instrument_name: element_data}
                    measurement = self._map_single_entity(element_data_dict, instruments, dob=dob)
                    if measurement:
                        measurements.append(measurement)
            
            return measurements
            
        except Exception as e:
            logger.error(f"Error mapping measurements: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return []
    
    def _create_measurement_from_fields(self, data: Dict[str, Any], field_config: Dict[str, Any], dob: Optional[str] = None) -> Optional[Measurement]:
        """
        Create a measurement from field configuration with support for different value types.
        
        Args:
            data (Dict[str, Any]): Element data
            field_config (Dict[str, Any]): Field configuration with assay, value, unit, etc.
            dob (str, optional): Date of birth for age calculations
            
        Returns:
            Optional[Measurement]: A measurement object or None on failure
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
        assay_id = self.process_code(assay_code)
        assay_label = self.fetch_label(assay_code)
        
        # If no label found, extract from field name
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
            value_id = self.process_code(value_data)
            value_label = self.fetch_label(value_data)
            ontology_class = OntologyClass(id=value_id, label=value_label or "Unknown Value")
            value = Value(ontology_class=ontology_class)
            
        elif value_type == "dual":
            # Try interpretation field first, then fall back to numeric value
            interpretation_value = data.get(interpretation_field_name)
            numeric_value = data.get(value_field_name)
            
            if interpretation_value:
                # Use interpretation (categorical value)
                logger.debug(f"Using interpretation value: {interpretation_value}")
                interp_id = self.process_code(interpretation_value)
                interp_label = self.fetch_label(interpretation_value)
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
                        unit_id = self.process_code(unit_code)
                        unit_label = self.fetch_label(unit_code)
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
                
                # Get unit from either primary or alternative unit field
                unit_code = None
                if unit_field_name:
                    unit_code = data.get(unit_field_name)
                
                if not unit_code and unit_alt_field_name:
                    unit_code = data.get(unit_alt_field_name)
                
                if unit_code:
                    # Create unit with proper ontology
                    logger.debug(f"Processing unit code: {unit_code}")
                    unit_id = self.process_code(unit_code)
                    unit_label = self.fetch_label(unit_code)
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
        time_observed_field = self.processor.mapping_config.get("time_observed_field")
        time_observed = None
        
        if time_observed_field and dob and data.get(time_observed_field):
            try:
                time_observed_str = data.get(time_observed_field)
                dob_str = dob if isinstance(dob, str) else str(dob)
                
                iso_age = self.processor.convert_date_to_iso_age(time_observed_str, dob_str)
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