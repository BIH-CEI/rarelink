# src/rarelink/phenopackets/mappings/map_medical_action.py
import logging
from typing import List, Any, Optional
from phenopackets import (
    MedicalAction,
    Procedure,
    OntologyClass,
    TimeElement,
    Age
)
from datetime import datetime
from rarelink.utils.processor import DataProcessor

logger = logging.getLogger(__name__)

def map_medical_actions(
    data: dict, 
    processor: DataProcessor,
    dob: Optional[str] = None
) -> List[MedicalAction]:
    """
    Maps medical action data to the Phenopacket schema MedicalAction blocks.
    Handles both procedure and other medical action types.

    Args:
        data (dict): Input data from any schema.
        processor (DataProcessor): Handles all data processing logic.
        dob (str, optional): Date of birth for age calculations.

    Returns:
        List[MedicalAction]: A list of Phenopacket MedicalAction blocks.
    """
    # Initialize list for medical actions
    medical_actions = []
    
    try:
        # Get the instrument name for repeated elements
        instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
        
        # Check for repeated elements
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            # If no repeated elements, try using the base data
            repeated_elements = [data.get(instrument_name, {})]
        
        # Filter repeated elements by instrument name
        procedure_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        
        # If no filtered elements, use the original data
        if not procedure_elements:
            procedure_elements = [data.get(instrument_name, {})]
        
        # Process each procedure element
        for procedure_element in procedure_elements:
            # Identify procedure fields
            procedure_fields = {
                k: v for k, v in processor.mapping_config.items() 
                if k.startswith('procedure_field_') and isinstance(v, str)
            }
            
            logger.debug(f"Found procedure fields: {procedure_fields}")

            # Process each procedure field
            for procedure_key, field_path in procedure_fields.items():
                try:
                    # Extract procedure details
                    procedure_details = _get_field_value(procedure_element, field_path)
                    
                    # Skip if no procedure details
                    if not procedure_details:
                        logger.debug(f"No details found for procedure {procedure_key}: looking for {field_path}")
                        continue

                    # Check if procedure is performed
                    performed_field = processor.mapping_config.get('performed')
                    is_performed = (
                        performed_field is None or 
                        _get_field_value(procedure_element, performed_field) is not None
                    )

                    if not is_performed:
                        logger.debug(f"Procedure {procedure_key} not performed, skipping")
                        continue

                    # Create the procedure
                    procedure = _create_procedure(
                        {procedure_key: procedure_details}, 
                        processor, 
                        dob
                    )

                    # If procedure is successfully created, wrap it in a MedicalAction
                    if procedure:
                        medical_action = MedicalAction(procedure=procedure)
                        medical_actions.append(medical_action)
                        logger.debug(f"Created medical action with procedure: {procedure_details}")

                except Exception as e:
                    logger.error(f"Error processing procedure {procedure_key}: {e}")
                    import traceback
                    logger.debug(traceback.format_exc())

    except Exception as e:
        logger.error(f"Failed to map procedures: {e}")
        import traceback
        logger.debug(traceback.format_exc())
    
    # Log the number of medical actions found
    if medical_actions:
        logger.debug(f"Generated {len(medical_actions)} medical actions")
    else:
        logger.debug("No medical actions found in data. This is normal for some data models.")
        
    return medical_actions

def _create_procedure(
    procedure_data: dict, 
    processor: DataProcessor, 
    dob: Optional[str] = None
) -> Optional[Procedure]:
    """
    Creates a Procedure object from the provided data.
    
    Args:
        procedure_data (dict): Data for the procedure
        processor (DataProcessor): Handles field processing
        dob (str, optional): Date of birth for age calculations
        
    Returns:
        Optional[Procedure]: The created procedure or None
    """
    # Find the procedure code
    procedure_code = None
    procedure_label = None
    procedure_key = None
    
    # Get the first (and only) key-value pair
    for key, value in procedure_data.items():
        procedure_code = value
        procedure_key = key
        break
    
    # If no procedure code found, we can't create a procedure
    if not procedure_code:
        logger.debug("No procedure code found in data")
        return None
    
    # Try to fetch label using enum classes
    enum_classes = processor.mapping_config.get('enum_classes', {})
    procedure_label = None
    
    for prefix, enum_class_path in enum_classes.items():
        # Check if the code starts with the prefix
        if procedure_code.startswith(prefix):
            try:
                # Dynamically import the enum class
                module_path, class_name = enum_class_path.rsplit('.', 1)
                module = __import__(module_path, fromlist=[class_name])
                enum_class = getattr(module, class_name)
                
                # Use processor's fetch_label_from_enum method
                procedure_label = processor.fetch_label_from_enum(procedure_code, enum_class)
                
                if procedure_label:
                    break
            except Exception as e:
                logger.warning(f"Could not fetch label from enum class {enum_class_path}: {e}")
                
    # Process the code
    processed_code = processor.process_code(procedure_code)
    
    # Create the OntologyClass for the procedure code
    code = OntologyClass(
        id=processed_code,
        label=procedure_label or "Unknown Procedure"
    )
    
    # Calculate age at procedure if date of birth is available
    performed = None
    if dob:
        try:
            # Get procedure date field if available
            procedure_date_field = processor.mapping_config.get(f'{procedure_key}_date')
            if procedure_date_field:
                procedure_date = _get_field_value(procedure_data, procedure_date_field)
                if procedure_date:
                    dob_date = datetime.strptime(dob, "%Y-%m-%d")
                    procedure_date = datetime.strptime(procedure_date, "%Y-%m-%d")
                    age_at_procedure = (procedure_date - dob_date).days / 365.25
                    performed = TimeElement(
                        age=Age(iso8601duration=f'P{int(age_at_procedure)}Y')
                    )
        except (ValueError, TypeError) as date_error:
            logger.warning(f"Could not calculate age at procedure: {date_error}")
    
    # Create the Procedure
    procedure = Procedure(
        code=code,
        performed=performed
    )
    
    return procedure

def _get_field_value(data: dict, field_path: str) -> Any:
    """
    Get a field value from data, handling direct and nested access.
    
    Args:
        data (dict): The data to extract from
        field_path (str): Field path to extract
        
    Returns:
        Any: The field value or None if not found
    """
    # Handle None or empty inputs
    if not data or not field_path:
        return None
    
    # Direct dictionary access
    if isinstance(data, dict):
        return data.get(field_path)
    
    return None