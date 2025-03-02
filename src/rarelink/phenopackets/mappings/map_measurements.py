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
from rarelink.utils.processor import DataProcessor

logger = logging.getLogger(__name__)

def map_measurements(
    data: dict, 
    processor: DataProcessor,
    dob: str) -> list:
    """
    Maps phenotype data to the Phenopacket schema Disease block fetching the 
    data elements from the repeated elements in the input data.

    Args:
        data (dict): Input data from the RareLink-CDM schema (or similar).
        processor (DataProcessor): Handles all data processing logic.

    Returns:
        list: A list of Phenopacket PhenotypicFeature blocks.
    """

    # Fetching and preparation
    # --------------------------------------------------------------------------
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
    try:
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.warning("No repeated elements found in the data.")
            return []

        # Filter relevant phenotypic_feature elements
        measurement_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
    
        measurements = []
        for measurement_element in measurement_elements:
            measurement_data = measurement_element.get(
                                                    "measurements")
            if not measurement_data:
                logger.warning("No measurements data found in "
                                "this element. Skipping.")
                continue
            

            # Measurement.assay
            # ------------------------------------------------------------------
            assay = None
            assay_field = measurement_data.get(
                processor.mapping_config.get("assay_field"))
            
            if not assay_field:
                continue # Skip this instance but continue with others
            
            assay_id = processor.process_code(assay_field)
            assay_label = processor.fetch_label(assay_id)
            assay = OntologyClass(
                id=assay_id,
                label=assay_label
            )
    
            # Measurement Value
            # ------------------------------------------------------------------
            value_field = measurement_data.get(
                processor.mapping_config["value_field"])
            value_unit_field = measurement_data.get(
                processor.mapping_config["value_unit_field"])

            value_unit_id = processor.process_code(value_unit_field)

            quantity = None
            if value_field and value_unit_field:
                try:
                    value = float(value_field)
                    unit_label = processor.fetch_label(value_unit_id)
                    unit = OntologyClass(
                        id=value_unit_field,
                        label=unit_label
                    )
                    quantity = Quantity(
                        value=value,
                        unit=unit
                    )
                except ValueError:
                    logger.error(f"Failed to convert value_field to float: \
                        {value_field}")


            value = Value(
                quantity=quantity
            )        
        
            # Measurement.time_observed
            # ------------------------------------------------------------------
            time_observed_field = measurement_data.get(
                processor.mapping_config["time_observed_field"])
            time_observed = None
            if time_observed_field and dob:
                try:
                    # Ensure time_observed_field is a string
                    if not isinstance(time_observed_field, str):
                        time_observed_str = time_observed_field.ToDatetime().isoformat()\
                            if hasattr(time_observed_field, "ToDatetime") \
                                else str(time_observed_field)
                    else:
                        time_observed_str = time_observed_field

                    # Ensure dob is a string
                    if not isinstance(dob, str):
                        dob_str = dob.ToDatetime().isoformat() \
                            if hasattr(dob, "ToDatetime") else str(dob)
                    else:
                        dob_str = dob

                    iso_age = processor.convert_date_to_iso_age(
                        time_observed_str, dob_str)
                    time_observed = TimeElement(age=Age(iso8601duration=iso_age))
                except Exception as e:
                    logger.error(f"Error processing time observed: {e}")

            # Measurement.procedure
            # ------------------------------------------------------------------
            procedure_id = (
                measurement_data.get(
                    processor.mapping_config["procedure_field_1"]) or
                measurement_data.get(
                    processor.mapping_config["procedure_field_2"]) or
                measurement_data.get(
                    processor.mapping_config["procedure_field_3"])
            )
            procedure_label = processor.fetch_label(
                procedure_id) if procedure_id else None
            procedure = None
            if procedure_id:
                procedure = Procedure(
                    code=OntologyClass(
                        id=procedure_id,
                        label=procedure_label
                    )
                )
                  
            # Construct Measurement
            # ------------------------------------------------------------------
            measurement = Measurement(
                assay=assay,
                value=value,
                time_observed=time_observed,
                procedure=procedure
            )
            
            measurements.append(measurement)
        
        return measurements
                    
    except Exception as e:
        logger.error(f"Failed to map measurement: {e}")
        raise
