# src/rarelink/phenopackets/mappings/map_medical_action.py
import logging
from typing import List, Any, Optional
from phenopackets import (
    MedicalAction,
    Procedure,
    Treatment,
    OntologyClass,
    TimeElement,
    Age,
    DoseInterval,
    Quantity
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
    Enhanced to handle both procedures and treatments (including vaccines).

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
        # Check if this is a treatment-specific processor by looking at the mapping block
        mapping_block = processor.mapping_config
        
        # Determine if this is a treatment processor based on specific fields
        is_treatment_processor = (
            'agent_field_1' in mapping_block or 
            'agent_field_2' in mapping_block or
            'cumulative_dose' in mapping_block
        )
        
        logger.debug(f"Processing medical actions with processor type: {'treatment' if is_treatment_processor else 'procedure'}")
        
        if is_treatment_processor:
            # This is a treatment-specific processor
            instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
            logger.debug(f"Processing treatment for instrument: {instrument_name}")
            
            # Map treatments directly
            treatment_actions = _map_treatments_direct(data, processor, dob)
            if treatment_actions:
                medical_actions.extend(treatment_actions)
                logger.debug(f"Added {len(treatment_actions)} treatment medical actions")
        else:
            # Standard procedure processor
            procedure_actions = _map_procedures(data, processor, dob)
            if procedure_actions:
                medical_actions.extend(procedure_actions)
                logger.debug(f"Added {len(procedure_actions)} procedure medical actions")
        
    except Exception as e:
        logger.error(f"Failed to map medical actions: {e}")
        import traceback
        logger.debug(traceback.format_exc())
    
    # Log the number of medical actions found
    if medical_actions:
        logger.debug(f"Generated {len(medical_actions)} total medical actions")
    else:
        logger.debug("No medical actions found in data. This is normal for some data models.")
        
    return medical_actions

def _map_procedures(
    data: dict, 
    processor: DataProcessor,
    dob: Optional[str] = None
) -> List[MedicalAction]:
    """
    Maps procedure data to MedicalAction blocks with procedure content.
    
    Args:
        data (dict): Input data from any schema.
        processor (DataProcessor): Handles all data processing logic.
        dob (str, optional): Date of birth for age calculations.
        
    Returns:
        List[MedicalAction]: A list of MedicalAction blocks with procedures.
    """
    medical_actions = []
    
    # Get the instrument name for repeated elements
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
    
    # Check for repeated elements
    repeated_elements = data.get("repeated_elements", [])
    if not repeated_elements:
        # If no repeated elements, try using the base data
        if instrument_name in data:
            repeated_elements = [data]
    
    # Filter repeated elements by instrument name
    procedure_elements = [
        element for element in repeated_elements
        if element.get("redcap_repeat_instrument") == instrument_name
    ]
    
    # If no filtered elements, use the original data
    if not procedure_elements and instrument_name in data:
        procedure_elements = [data]
    
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
                    
                    # Additional Medical Action fields could be added here:
                    # - action: OntologyClass
                    # - treatment_target: OntologyClass 
                    # - treatment_intent: OntologyClass
                    # - response_to_treatment: OntologyClass
                    # - adverse_events: List[OntologyClass]
                    # - treatment_termination_reason: OntologyClass
                    
                    medical_actions.append(medical_action)
                    logger.debug(f"Created medical action with procedure: {procedure_details}")

            except Exception as e:
                logger.error(f"Error processing procedure {procedure_key}: {e}")
                import traceback
                logger.debug(traceback.format_exc())
                
    return medical_actions

def _map_treatments_direct(
    data: dict, 
    processor: DataProcessor,
    dob: Optional[str] = None
) -> List[MedicalAction]:
    """
    Directly maps treatment data from the processor's mapping configuration.
    This is the optimized path for treatment-specific processors.
    
    Args:
        data (dict): Input data dictionary containing all elements.
        processor (DataProcessor): The processor with treatment-specific configuration.
        dob (str, optional): Date of birth for age calculations.
        
    Returns:
        List[MedicalAction]: A list of treatment-based medical actions.
    """
    medical_actions = []
    mapping_block = processor.mapping_config
    instrument_name = mapping_block.get("redcap_repeat_instrument")
    
    if not instrument_name:
        logger.debug("No instrument name found in mapping configuration")
        return []
    
    logger.debug(f"Directly mapping treatments for instrument: {instrument_name}")
    
    # Get all repeated elements
    repeated_elements = data.get("repeated_elements", [])
    if not repeated_elements:
        logger.debug("No repeated elements found in data")
        return []
    
    # Filter elements for this instrument
    instrument_elements = [
        element for element in repeated_elements
        if element.get("redcap_repeat_instrument") == instrument_name
    ]
    
    logger.debug(f"Found {len(instrument_elements)} elements for instrument {instrument_name}")
    
    # Track unique instances to prevent duplicates
    processed_instances = set()
    seen_agents = set()  # Track which agents we've already processed
    
    # Process each element for this instrument
    for element in instrument_elements:
        try:
            # Get instance ID to track uniqueness
            instance_id = element.get("redcap_repeat_instance")
            element_key = f"{instrument_name}:{instance_id}"
            
            # Skip if we've already processed this exact instance
            if element_key in processed_instances:
                logger.debug(f"Skipping duplicate instance: {element_key}")
                continue
                
            # Mark this instance as processed
            processed_instances.add(element_key)
            
            # Get the instrument-specific data
            instrument_data = element.get(instrument_name)
            if not instrument_data:
                logger.debug(f"No data found for instrument {instrument_name} in element")
                continue
                
            # Check which agent we're working with
            agent_field_1 = mapping_block.get("agent_field_1")
            agent_field_name = agent_field_1.split(".")[-1] if "." in agent_field_1 else agent_field_1
            agent_id = instrument_data.get(agent_field_name)
            
            # Skip if we've already seen this agent
            if agent_id in seen_agents:
                logger.debug(f"Skipping duplicate agent: {agent_id}")
                continue
                
            # Mark this agent as seen
            seen_agents.add(agent_id)
            
            # Create a treatment using the mapping block from the processor
            treatment = _create_treatment(
                instrument_data,
                mapping_block,
                processor,
                dob,
                instrument_name,
                element
            )
            
            if treatment:
                # Create a medical action with this treatment
                medical_action = MedicalAction(treatment=treatment)
                
                # Add adverse events (if available)
                adverse_events = _extract_adverse_events(
                    instrument_data,
                    mapping_block,
                    processor
                )
                
                if adverse_events:
                    medical_action.adverse_events.extend(adverse_events)
                
                # Add response to treatment (if available)
                responses = _extract_treatment_response(
                    instrument_data,
                    mapping_block,
                    processor
                )
                
                if responses:
                    # Check if we got a list of responses (new behavior)
                    if isinstance(responses, list) and responses:
                        # Use the first response as the primary one
                        medical_action.response_to_treatment.CopyFrom(responses[0])
                        if len(responses) > 1:
                            logger.debug(f"Found {len(responses)} responses, using the first one as primary response")
                    elif hasattr(responses, 'id') and hasattr(responses, 'label'):
                        # Handle the case where a single OntologyClass was returned (old behavior)
                        medical_action.response_to_treatment.CopyFrom(responses)
                    else:
                        logger.warning(f"Unexpected response format: {type(responses)}")
                
                # Add treatment target (if available)
                target_field = mapping_block.get("treatment_target_field")
                if target_field:
                    field_name = target_field.split(".")[-1] if "." in target_field else target_field
                    target_value = instrument_data.get(field_name)
                    
                    if target_value:
                        target_id = processor.process_code(target_value)
                        target_label = processor.fetch_label(target_value) or "Unknown Target"
                        target = OntologyClass(id=target_id, label=target_label)
                        medical_action.treatment_target.CopyFrom(target)
                
                # Add treatment intent (if available)
                intent_field = mapping_block.get("treatment_intent_field")
                if intent_field:
                    field_name = intent_field.split(".")[-1] if "." in intent_field else intent_field
                    intent_value = instrument_data.get(field_name)
                    
                    if intent_value:
                        intent_id = processor.process_code(intent_value)
                        intent_label = processor.fetch_label(intent_value) or "Unknown Intent"
                        intent = OntologyClass(id=intent_id, label=intent_label)
                        medical_action.treatment_intent.CopyFrom(intent)
                
                # Add the medical action to our list
                medical_actions.append(medical_action)
                logger.debug(f"Created medical action with treatment for instance {instance_id}")
        
        except Exception as e:
            logger.error(f"Error processing treatment element for {instrument_name}: {e}")
            import traceback
            logger.debug(traceback.format_exc())
    
    return medical_actions



def _create_treatment(
    instrument_data: dict,
    mapping_block: dict,
    processor: DataProcessor,
    dob: Optional[str] = None,
    instrument_name: str = "",
    full_element: dict = None
) -> Optional[Treatment]:
    """
    Creates a Treatment object from the provided data.
    
    Args:
        instrument_data (dict): Data for the treatment
        mapping_block (dict): Mapping configuration for this treatment type
        processor (DataProcessor): Data processor for code processing
        dob (str, optional): Date of birth for age calculations
        instrument_name (str, optional): Name of the instrument
        full_element (dict, optional): The complete element data
        
    Returns:
        Optional[Treatment]: The created treatment or None
    """
    # Extract agent information (primary + fallback)
    agent_id = None
    agent_field_1 = mapping_block.get("agent_field_1")
    agent_field_2 = mapping_block.get("agent_field_2")
    
    if agent_field_1:
        agent_field_name = agent_field_1.split(".")[-1] if "." in agent_field_1 else agent_field_1
        agent_id = instrument_data.get(agent_field_name)
    
    # If agent_id is "other", use the "other" field
    if agent_id == "other" and agent_field_2:
        other_field_name = agent_field_2.split(".")[-1] if "." in agent_field_2 else agent_field_2
        agent_id = instrument_data.get(other_field_name)
    
    if not agent_id:
        logger.debug("No agent ID found for treatment")
        return None
    
    # Show mapping block contents in debug mode
    logger.debug(f"Full mapping_block: {mapping_block}")
    
    # Process the code to proper ontology format
    processed_id = processor.process_code(agent_id)
    logger.debug(f"Processed agent term ID: {processed_id}")
    
    # Try to fetch the label using different methods
    agent_label = None
    
    # 1. Try direct lookup with original code
    agent_label = processor.fetch_label(agent_id)
    if agent_label:
        logger.debug(f"Found label using original code: {agent_label}")
        
    # 2. If that fails, try with the processed code
    if not agent_label and processed_id != agent_id:
        agent_label = processor.fetch_label(processed_id)
        if agent_label:
            logger.debug(f"Found label using processed code: {agent_label}")
    
    # 3. Try using label_dicts from mapping_block
    if not agent_label:
        label_dicts = mapping_block.get("label_dicts", {})
        agent_label_dict = label_dicts.get("agent_field_1")
        
        if agent_label_dict and agent_id in agent_label_dict:
            agent_label = agent_label_dict[agent_id]
            logger.debug(f"Found agent label from label_dict: {agent_label}")
    
    # 4. Try using Enum classes from the processor (this is the key part from map_diseases)
    if not agent_label and hasattr(processor, "enum_classes"):
        for prefix, enum_class in processor.enum_classes.items():
            if agent_id.lower().startswith(prefix.lower()):
                agent_label = processor.fetch_label_from_enum(agent_id, enum_class)
                if agent_label:
                    logger.debug(f"Found label using processor enum class: {agent_label}")
                    break
    
    # 5. Try using enum classes from mapping_block
    if not agent_label:
        enum_classes = mapping_block.get("enum_classes", {})
        # Try to match a prefix
        for prefix, enum_class_path in enum_classes.items():
            if agent_id.lower().startswith(prefix.lower()):
                try:
                    # Import the enum class
                    from importlib import import_module
                    parts = enum_class_path.rsplit('.', 1)
                    if len(parts) == 2:
                        module_path, class_name = parts
                        module = import_module(module_path)
                        
                        if hasattr(module, class_name):
                            enum_class = getattr(module, class_name)
                            agent_label = processor.fetch_label_from_enum(agent_id, enum_class)
                            if agent_label:
                                logger.debug(f"Found label from imported enum class: {agent_label}")
                                break
                except Exception as e:
                    logger.error(f"Error with enum lookup: {e}")
    
    # Use "Unknown Agent" as fallback if no label was found
    if not agent_label:
        agent_label = "Unknown Agent"
        logger.debug("Using default 'Unknown Agent' label")
    
    logger.debug(f"Final agent ID: {processed_id}, label: {agent_label}")
    
    agent = OntologyClass(
        id=processed_id,
        label=agent_label
    )
    
    # Extract cumulative dose
    cumulative_dose = None
    dose_field = mapping_block.get("cumulative_dose")
    
    if dose_field:
        dose_field_name = dose_field.split(".")[-1] if "." in dose_field else dose_field
        dose_value = instrument_data.get(dose_field_name)
        
        if dose_value:
            try:
                # Convert to float if possible
                dose_value = float(dose_value)
                
                # Create a Quantity with the dose value and proper unit
                quantity = Quantity(
                    value=dose_value,
                    unit=OntologyClass(
                        id="UO:0000307",  # Standard dose unit from Units Ontology
                        label="dose unit"
                    )
                )
                
                # Set the cumulative dose
                cumulative_dose = quantity
            except (ValueError, TypeError):
                logger.warning(f"Could not convert dose value '{dose_value}' to float")
    
    # Extract completion/administration date
    administration_date = None
    date_field_candidates = [
        "completion_of_inact_vax",
        "completion_live_vax"
    ]
    
    # Try each potential date field
    for date_field in date_field_candidates:
        date_value = instrument_data.get(date_field)
        if date_value:
            administration_date = date_value
            break
    
    # Convert administration date to TimeElement (age at administration)
    time_element = None
    if administration_date and dob:
        try:
            # Handle potentially problematic date format from 'seconds:' prefix
            if isinstance(dob, str) and "seconds:" in dob:
                # Parse seconds timestamp to datetime
                seconds_val = float(dob.replace("seconds:", "").strip())
                dob_dt = datetime.fromtimestamp(seconds_val)
                dob_str = dob_dt.strftime("%Y-%m-%d")
            else:
                dob_str = dob
                
            # Make sure administration_date is a proper date string
            if isinstance(administration_date, str):
                admin_date_str = administration_date
            else:
                # Handle other formats if needed
                admin_date_str = str(administration_date)
                
            logger.debug(f"Using dates for age calculation: admin date={admin_date_str}, dob={dob_str}")
                
            # Convert to ISO age (using safe approach for date handling)
            try:
                # Parse dates manually
                if isinstance(admin_date_str, str):
                    admin_dt = datetime.strptime(admin_date_str, "%Y-%m-%d")
                else:
                    # Handle Timestamp or other objects
                    logger.debug(f"Converting non-string admin date: {type(admin_date_str)}")
                    if hasattr(admin_date_str, 'ToDatetime'):
                        admin_dt = admin_date_str.ToDatetime()
                    else:
                        admin_dt = datetime.fromtimestamp(float(str(admin_date_str)))
                
                if isinstance(dob_str, str):
                    if "seconds:" in dob_str:
                        # Extract seconds value and convert to datetime
                        seconds_val = float(dob_str.replace("seconds:", "").strip())
                        birth_dt = datetime.fromtimestamp(seconds_val)
                    else:
                        birth_dt = datetime.strptime(dob_str, "%Y-%m-%d")
                else:
                    # Handle Timestamp or other objects
                    logger.debug(f"Converting non-string dob: {type(dob_str)}")
                    if hasattr(dob_str, 'ToDatetime'):
                        birth_dt = dob_str.ToDatetime()
                    else:
                        birth_dt = datetime.fromtimestamp(float(str(dob_str)))
                
                # Calculate age difference manually
                years = admin_dt.year - birth_dt.year
                months = admin_dt.month - birth_dt.month
                
                # Adjust for negative months
                if months < 0:
                    years -= 1
                    months += 12
                
                # Create ISO age string
                iso_age = f"P{years}Y{months}M"
                logger.debug(f"Calculated ISO age: {iso_age}")
                
                time_element = TimeElement(age=Age(iso8601duration=iso_age))
            except Exception as inner_e:
                logger.error(f"Error in manual date calculation: {inner_e}")
                # Fallback method if needed
        except Exception as e:
            logger.error(f"Error converting administration date to age: {e}")
    
    # Create the Treatment object
    treatment = Treatment(
        agent=agent,
        cumulative_dose=cumulative_dose
    )
    
    return treatment

def _extract_adverse_events(
    instrument_data: dict,
    mapping_block: dict,
    processor: DataProcessor
) -> List[OntologyClass]:
    """
    Extracts adverse events from treatment data.
    
    Args:
        instrument_data (dict): Data for the treatment
        mapping_block (dict): Mapping configuration
        processor (DataProcessor): Data processor
        
    Returns:
        List[OntologyClass]: List of adverse events as ontology classes
    """
    adverse_events = []
    
    # Check for primary adverse event field
    adverse_event_field = mapping_block.get("adverse_event_field")
    adverse_event_other_field = mapping_block.get("adverse_event_other_field")
    
    if adverse_event_field:
        # Get field name without instrument prefix
        field_name = adverse_event_field.split(".")[-1] if "." in adverse_event_field else adverse_event_field
        ae_value = instrument_data.get(field_name)
        
        if ae_value and not ae_value.endswith("_exluded"):  # Skip excluded AEs
            ae_id = processor.process_code(ae_value)
            ae_label = processor.fetch_label(ae_value) or "Unknown Adverse Event"
            
            adverse_events.append(OntologyClass(
                id=ae_id,
                label=ae_label
            ))
    
    # Process additional ("other") adverse event if present
    if adverse_event_other_field:
        field_name = adverse_event_other_field.split(".")[-1] if "." in adverse_event_other_field else adverse_event_other_field
        ae_other_value = instrument_data.get(field_name)
        
        if ae_other_value:
            ae_other_id = processor.process_code(ae_other_value)
            ae_other_label = processor.fetch_label(ae_other_value) or "Unknown Adverse Event"
            
            adverse_events.append(OntologyClass(
                id=ae_other_id,
                label=ae_other_label
            ))
    
    return adverse_events

def _extract_treatment_response(
    instrument_data: dict,
    mapping_block: dict,
    processor: DataProcessor
) -> List[OntologyClass]:
    """
    Extracts treatment responses from data, supporting multiple response fields.
    
    Args:
        instrument_data (dict): Data for the treatment
        mapping_block (dict): Mapping configuration
        processor (DataProcessor): Data processor
        
    Returns:
        List[OntologyClass]: List of treatment responses as ontology classes
    """
    responses = []
    
    # Find all response fields in the mapping block
    response_fields = {}
    for key, value in mapping_block.items():
        if key.startswith("response_field_") and value:
            try:
                # Extract the numeric suffix
                field_num = int(key.split("_")[-1])
                response_fields[field_num] = value
            except ValueError:
                # If the suffix isn't a number, skip it
                logger.warning(f"Invalid response field key format: {key}")
    
    # Process response fields in order (1, 2, 3, etc.)
    for field_num in sorted(response_fields.keys()):
        response_field = response_fields[field_num]
        logger.debug(f"Processing response field {field_num}: {response_field}")
        
        # Extract field name without instrument prefix
        field_name = response_field.split(".")[-1] if "." in response_field else response_field
        
        # Extract response value
        response_value = instrument_data.get(field_name)
        if not response_value:
            logger.debug(f"No value found for response field {field_num}")
            continue
        
        # Process response code and get label
        processed_response_id = processor.process_code(response_value)
        
        # Use the same label fetching approach as in other functions
        response_label = None
        
        # 1. Try direct lookup with original code
        response_label = processor.fetch_label(response_value)
        
        # 2. If that fails, try with the processed code
        if not response_label and processed_response_id != response_value:
            response_label = processor.fetch_label(processed_response_id)
        
        # 3. If still no label, try using label_dicts from mapping_block
        if not response_label:
            label_dicts = mapping_block.get("label_dicts", {})
            response_label_dict = label_dicts.get(f"response_field_{field_num}")
            
            if response_label_dict and response_value in response_label_dict:
                response_label = response_label_dict[response_value]
        
        # 4. Default to "Unknown Response" if no label was found
        if not response_label:
            response_label = "Unknown Response"
        
        response = OntologyClass(
            id=processed_response_id,
            label=response_label
        )
        
        responses.append(response)
        logger.debug(f"Added response {response.id} - {response.label}")
    
    return responses
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
                    iso_age = processor.convert_date_to_iso_age(procedure_date, dob)
                    if iso_age:
                        performed = TimeElement(
                            age=Age(iso8601duration=iso_age)
                        )
        except Exception as date_error:
            logger.warning(f"Could not calculate age at procedure: {date_error}")
    
    # Create the Procedure
    procedure = Procedure(
        code=code,
        performed=performed
        # Additional Procedure fields could be added here:
        # - body_site: OntologyClass
        # - procedure_type: OntologyClass
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
    
    # Split field path into parts if it contains a dot
    if "." in field_path:
        parts = field_path.split(".", 1)
        instrument, field = parts
        
        # Check if the instrument exists in data
        if instrument in data:
            if isinstance(data[instrument], dict):
                return data[instrument].get(field)
        
        # Try direct access as fallback
        return data.get(field_path)
    
    # Direct dictionary access
    return data.get(field_path)