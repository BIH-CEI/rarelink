# src/rarelink/phenopackets/create.py
from phenopackets import Phenopacket
import logging
from typing import Dict, Any, Optional
import traceback

from rarelink.utils.processor import DataProcessor
from rarelink.phenopackets.mappings import (
    map_individual,
    map_vital_status,
    map_metadata,
    map_diseases,
    map_interpretations,
    map_variation_descriptor,
    map_phenotypic_features,
    map_measurements,
    map_medical_actions
)

logger = logging.getLogger(__name__)

def _add_enum_classes_to_processor(processor, enum_classes_config):
    """
    Add enum classes from the config to the processor.
    
    Args:
        processor (DataProcessor): The processor to add enum classes to
        enum_classes_config (dict): Configuration with prefix to enum class mappings
    """
    if not enum_classes_config:
        return
        
    for prefix, enum_class_or_path in enum_classes_config.items():
        if enum_class_or_path:
            processor.add_enum_class(prefix, enum_class_or_path)

def create_phenopacket(
    data: dict, 
    created_by: str, 
    mapping_configs: Optional[Dict[str, Any]] = None,
    debug: bool = False
) -> Phenopacket:
    """
    Creates a Phenopacket for an individual record with flexible mapping configurations.
    Enhanced to handle different data models, multiple instruments, and improve error tracking.

    Args:
        data (dict): Input data dictionary containing all data.
        created_by (str): Creator's name for metadata.
        mapping_configs (dict, optional): Dictionary of mapping configurations 
            for different Phenopacket blocks.
        debug (bool): Enable debug mode for verbose logging

    Returns:
        Phenopacket: A fully constructed Phenopacket.
    """
    # Validate and prepare mapping configurations
    if not mapping_configs:
        raise ValueError("Mapping configurations are required")

    # Set up debug mode
    logging_level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(logging_level)

    try:
        # Flexible mapping configuration with default fallbacks
        def get_mapping_config(block_name: str, default_instrument: str = "", required=False) -> Dict[str, Any]:
            """
            Retrieve mapping configuration with flexible handling
            
            Args:
                block_name (str): Name of the block (e.g., 'individual', 'diseases')
                default_instrument (str, optional): Default instrument name if not specified
                required (bool): Whether this mapping configuration is required
            
            Returns:
                Dict: Processed mapping configuration
            """
            block_config = mapping_configs.get(block_name, {})
            
            # If no instrument name is provided, use the default
            if 'instrument_name' not in block_config and default_instrument:
                block_config['instrument_name'] = default_instrument
            
            # Check if this is a required config
            if required and (not block_config or 'mapping_block' not in block_config):
                raise ValueError(f"Required mapping configuration '{block_name}' missing or incomplete")
                
            return block_config

        # Record ID --------------------------------------------------------------
        record_id = data.get("record_id", "unknown")
        if debug:
            logger.debug(f"Processing record ID: {record_id}")
            logger.debug(f"Data structure: {type(data)}")
            logger.debug(f"Top-level keys: {list(data.keys())}")

        # Individual Block ------------------------------------------------------
        try:
            individual_config = get_mapping_config("individual", required=True)
            
            if debug:
                logger.debug(f"Individual config: {individual_config}")
                
            individual_processor = DataProcessor(
                mapping_config=individual_config.get("mapping_block", {})
            )
            individual_processor.enable_debug(debug)
            
            # Add enum classes if present
            _add_enum_classes_to_processor(individual_processor, individual_config.get("enum_classes", {}))
            
            # Extract date of birth for subsequent blocks
            try:
                dob_field = individual_processor.get_field(data, "date_of_birth_field")
                dob_str = dob_field
                
                if debug:
                    logger.debug(f"Extracted DOB field: {dob_field}")
            except Exception as e:
                if debug:
                    logger.debug(f"Error extracting DOB: {e}")
                dob_str = None

            # Vital Status Block ----------------------------------------------------
            try:
                vital_status_config = get_mapping_config("vitalStatus")
                vital_status_processor = DataProcessor(
                    mapping_config=vital_status_config.get("mapping_block", {})
                )
                vital_status_processor.enable_debug(debug)
                
                # Add enum classes if present
                _add_enum_classes_to_processor(vital_status_processor, vital_status_config.get("enum_classes", {}))
                
                # Dynamically set instrument name
                if "instrument_name" in vital_status_config:
                    # Handle multiple instruments
                    instrument_name = vital_status_config.get("instrument_name")
                    if isinstance(instrument_name, (list, set)):
                        # For now, just use the first instrument if there are multiple
                        instrument_list = list(instrument_name)
                        if instrument_list:
                            vital_status_processor.mapping_config["instrument_name"] = instrument_list[0]
                    else:
                        vital_status_processor.mapping_config["instrument_name"] = instrument_name
                
                vital_status = map_vital_status(
                    data, 
                    vital_status_processor, 
                    dob=dob_str
                )
            except Exception as e:
                if debug:
                    logger.debug(f"Error mapping vital status: {e}")
                vital_status = None

            # Individual Block with Vital Status ------------------------------------
            individual = map_individual(
                data, 
                individual_processor, 
                vital_status=vital_status
            )
        except Exception as e:
            logger.error(f"Error in individual block processing: {e}")
            if debug:
                logger.error(traceback.format_exc())
            raise ValueError(f"Failed to create Individual block: {str(e)}")

        # Phenotypic Features Block --------------------------------------------
        try:
            phenotypic_feature_config = get_mapping_config("phenotypicFeatures")
            phenotypic_features = []
            
            # Multi-configuration approach (list of configurations)
            if isinstance(phenotypic_feature_config, list):
                logger.debug(f"Processing {len(phenotypic_feature_config)} phenotypic feature configurations")
                
                for index, config in enumerate(phenotypic_feature_config):
                    try:
                        # Create a processor for this specific config
                        feature_processor = DataProcessor(
                            mapping_config=config.get("mapping_block", {})
                        )
                        feature_processor.enable_debug(debug)
                        
                        # Copy configuration from the config to the processor
                        for key, value in config.items():
                            if key != "mapping_block":
                                feature_processor.mapping_config[key] = value
                        
                        # Add enum classes if present
                        _add_enum_classes_to_processor(feature_processor, config.get("enum_classes", {}))
                        
                        # Set the instrument name
                        instrument_name = config.get("instrument_name")
                        if isinstance(instrument_name, (list, set)):
                            # Copy the set/list to avoid modifying the original
                            feature_processor.mapping_config["instrument_names"] = list(instrument_name)
                            # For backwards compatibility, use the first instrument as the primary
                            if list(instrument_name):
                                feature_processor.mapping_config["redcap_repeat_instrument"] = list(instrument_name)[0]
                        else:
                            feature_processor.mapping_config["redcap_repeat_instrument"] = instrument_name
                        
                        # Process features for this configuration
                        logger.debug(f"Processing phenotypic features for instrument: {instrument_name}")
                        config_features = map_phenotypic_features(
                            data,
                            feature_processor,
                            dob=individual.date_of_birth
                        )
                        
                        if config_features:
                            phenotypic_features.extend(config_features)
                            logger.debug(f"Added {len(config_features)} features from config {index+1}")
                    except Exception as e:
                        logger.error(f"Error processing phenotypic feature config {index+1}: {e}")
                        if debug:
                            logger.debug(traceback.format_exc())
            # Single configuration approach (standard dictionary)
            else:
                # Original single configuration processing
                logger.debug("Using single phenotypic feature configuration")
                
                # Get the mapping block from the configuration
                mapping_block = phenotypic_feature_config.get("mapping_block", {})
                if not mapping_block:
                    logger.warning("No mapping block found in phenotypic feature configuration")
                
                # Create the processor with the mapping block
                phenotypic_feature_processor = DataProcessor(mapping_config=mapping_block)
                phenotypic_feature_processor.enable_debug(debug)
                
                # Add additional configuration properties
                for key, value in phenotypic_feature_config.items():
                    if key != "mapping_block":
                        phenotypic_feature_processor.mapping_config[key] = value
                
                # Add enum classes if present
                _add_enum_classes_to_processor(
                    phenotypic_feature_processor, 
                    phenotypic_feature_config.get("enum_classes", {})
                )
                
                # Handle instrument name(s)
                instrument_name = phenotypic_feature_config.get("instrument_name")
                if isinstance(instrument_name, (list, set)):
                    # Copy the set/list to avoid modifying the original
                    phenotypic_feature_processor.mapping_config["instrument_names"] = list(instrument_name)
                    # For backwards compatibility, use the first instrument as the primary
                    if list(instrument_name):
                        phenotypic_feature_processor.mapping_config["redcap_repeat_instrument"] = list(instrument_name)[0]
                else:
                    phenotypic_feature_processor.mapping_config["redcap_repeat_instrument"] = instrument_name
                
                # Map the phenotypic features
                phenotypic_features = map_phenotypic_features(
                    data,
                    phenotypic_feature_processor,
                    dob=individual.date_of_birth
                )
            
            if debug:
                logger.debug(f"Total phenotypic features: {len(phenotypic_features)}")
        except Exception as e:
            if debug:
                logger.debug(f"Error mapping phenotypic features: {e}")
                logger.debug(traceback.format_exc())
            phenotypic_features = []
        
        # Measurements Block ----------------------------------------------------
        try:
            measurement_config = get_mapping_config("measurements")
            measurements = []
            
            # Multi-configuration approach (list of configurations)
            if isinstance(measurement_config, list):
                logger.debug(f"Processing {len(measurement_config)} measurement configurations")
                
                for index, config in enumerate(measurement_config):
                    try:
                        # Create a processor for this specific config
                        measurement_processor = DataProcessor(
                            mapping_config=config.get("mapping_block", {})
                        )
                        measurement_processor.enable_debug(debug)
                        
                        # Copy configuration from the config to the processor
                        for key, value in config.items():
                            if key != "mapping_block":
                                measurement_processor.mapping_config[key] = value
                        
                        # Add enum classes if present
                        _add_enum_classes_to_processor(measurement_processor, config.get("enum_classes", {}))
                        
                        # Set the instrument name
                        instrument_name = config.get("instrument_name")
                        if isinstance(instrument_name, (list, set)):
                            # Copy the set/list to avoid modifying the original
                            measurement_processor.mapping_config["instrument_names"] = list(instrument_name)
                            # For backwards compatibility, use the first instrument as the primary
                            if list(instrument_name):
                                measurement_processor.mapping_config["redcap_repeat_instrument"] = list(instrument_name)[0]
                        else:
                            measurement_processor.mapping_config["redcap_repeat_instrument"] = instrument_name
                        
                        # Process measurements for this configuration
                        logger.debug(f"Processing measurements for instrument: {instrument_name}")
                        config_measurements = map_measurements(
                            data,
                            measurement_processor,
                            dob=individual.date_of_birth
                        )
                        
                        if config_measurements:
                            measurements.extend(config_measurements)
                            logger.debug(f"Added {len(config_measurements)} measurements from config {index+1}")
                    except Exception as e:
                        logger.error(f"Error processing measurement config {index+1}: {e}")
                        if debug:
                            logger.debug(traceback.format_exc())
            # Single configuration approach (standard dictionary)
            else:
                # Original single configuration processing
                logger.debug("Using single measurement configuration")
                
                # Get the mapping block from the configuration
                mapping_block = measurement_config.get("mapping_block", {})
                if not mapping_block:
                    logger.warning("No mapping block found in measurement configuration")
                
                # Create the processor with the mapping block
                measurement_processor = DataProcessor(mapping_config=mapping_block)
                measurement_processor.enable_debug(debug)
                
                # Add additional configuration properties
                for key, value in measurement_config.items():
                    if key != "mapping_block":
                        measurement_processor.mapping_config[key] = value
                
                # Add enum classes if present
                _add_enum_classes_to_processor(
                    measurement_processor, 
                    measurement_config.get("enum_classes", {})
                )
                
                # Handle instrument name(s)
                instrument_name = measurement_config.get("instrument_name")
                if isinstance(instrument_name, (list, set)):
                    # Copy the set/list to avoid modifying the original
                    measurement_processor.mapping_config["instrument_names"] = list(instrument_name)
                    # For backwards compatibility, use the first instrument as the primary
                    if list(instrument_name):
                        measurement_processor.mapping_config["redcap_repeat_instrument"] = list(instrument_name)[0]
                else:
                    measurement_processor.mapping_config["redcap_repeat_instrument"] = instrument_name
                
                # Map the measurements
                measurements = map_measurements(
                    data,
                    measurement_processor,
                    dob=individual.date_of_birth
                )
            
            if debug:
                logger.debug(f"Total measurements: {len(measurements)}")
        except Exception as e:
            if debug:
                logger.debug(f"Error mapping measurements: {e}")
                logger.debug(traceback.format_exc())
            measurements = []

        # Medical Actions Block --------------------------------------------------------
        try:
            medical_actions = []
            
            # PROCEDURES: Process traditional medical procedures
            medical_action_config = get_mapping_config("procedures")
            if medical_action_config:
                medical_action_processor = DataProcessor(
                    mapping_config=medical_action_config.get("mapping_block", {})
                )
                medical_action_processor.enable_debug(debug)
                
                # Add enum classes if present
                _add_enum_classes_to_processor(medical_action_processor, medical_action_config.get("enum_classes", {}))
                
                # Handle instrument name(s)
                instrument_name = medical_action_config.get("instrument_name")
                if isinstance(instrument_name, (list, set)):
                    # Copy the set/list to avoid modifying the original
                    medical_action_processor.mapping_config["instrument_names"] = list(instrument_name)
                    # For backwards compatibility, use the first instrument as the primary
                    if list(instrument_name):
                        instrument_name_str = list(instrument_name)[0]
                        if instrument_name_str not in ["__dummy__", ""]:
                            medical_action_processor.mapping_config["redcap_repeat_instrument"] = instrument_name_str
                elif instrument_name and instrument_name not in ["__dummy__", ""]:
                    medical_action_processor.mapping_config["redcap_repeat_instrument"] = instrument_name
                
                # Add mapping dicts to the configuration
                if "mapping_dicts" in medical_action_config:
                    medical_action_processor.mapping_config.update(medical_action_config.get("mapping_dicts", {}))
                
                # Add enum classes to the configuration
                if "enum_classes" in medical_action_config:
                    medical_action_processor.mapping_config["enum_classes"] = medical_action_config.get("enum_classes", {})
                
                # Map procedures
                procedure_actions = map_medical_actions(
                    data, 
                    medical_action_processor,
                    dob=individual.date_of_birth
                )
                
                if procedure_actions:
                    medical_actions.extend(procedure_actions)
                    if debug:
                        logger.debug(f"Generated {len(procedure_actions)} procedure-based medical actions")
            
            # TREATMENTS: Process treatments (including vaccines)
            # Directly access treatments from mapping_configs to avoid dict structure issues
            treatments_config = mapping_configs.get("treatments")
            
            # Debug to see actual structure
            if debug:
                logger.debug(f"Treatments config structure: {type(treatments_config)}")
                if treatments_config:
                    try:
                        import json
                        # Try to create a safe representation for logging
                        logger.debug(f"Treatments config keys: {list(treatments_config.keys()) if isinstance(treatments_config, dict) else 'not a dict'}")
                    except Exception as e:
                        logger.debug(f"Could not log treatments config details: {e}")
            
            # Check if treatments_config exists
            if treatments_config:
                # Extract and process treatment configurations in a manner similar to phenotypic features
                
                # Handle treatments as a list like phenotypicFeatures
                if isinstance(treatments_config, list):
                    logger.debug("Treating treatments config as a list of configurations")
                    treatments_list = treatments_config
                # Handle special case of malformed dictionary structure (common with the way Python represents nested dicts)
                elif isinstance(treatments_config, dict):
                    logger.debug("Converting treatments dictionary to list of configurations")
                    treatments_list = []
                    
                    # Extract values that are actual configurations
                    try:
                        for key, value in treatments_config.items():
                            # If the value is a dictionary, it's a proper configuration
                            if isinstance(value, dict):
                                logger.debug(f"Adding treatment config from key {key}")
                                # Ensure instrument_name is set
                                if "instrument_name" not in value and not isinstance(key, dict):
                                    value["instrument_name"] = key
                                treatments_list.append(value)
                            # Special case: if the key itself is a dictionary (happens in some serialized formats)
                            elif isinstance(key, dict):
                                logger.debug("Found dictionary as key - adding to treatments list")
                                treatments_list.append(key)
                    except TypeError as e:
                        # Handle case where dict contains unhashable types
                        logger.warning(f"Error processing treatments dict: {e}")
                        try:
                            # Hacky way to extract dictionaries from the object if normal iteration fails
                            treatments_str = str(treatments_config)
                            logger.debug(f"Attempting to extract configs from: {treatments_str[:200]}")
                            if "{" in treatments_str:
                                # Try direct access to treatments config as a sequence
                                logger.debug("Trying to access treatments as a sequence")
                                try:
                                    # Try to iterate through it as a sequence
                                    for item in treatments_config:
                                        if isinstance(item, dict):
                                            logger.debug(f"Adding treatment item from sequence: {item.get('instrument_name', 'no-name')}")
                                            treatments_list.append(item)
                                except Exception as e2:
                                    logger.warning(f"Could not iterate treatments config: {e2}")
                        except Exception as str_err:
                            logger.warning(f"Could not process treatments config as string: {str_err}")
                else:
                    # Default to empty list if treatments_config is not a recognizable structure
                    logger.warning(f"Unrecognized treatments config type: {type(treatments_config)}")
                    treatments_list = []
                    
                # Process each treatment configuration in the list
                logger.debug(f"Processing {len(treatments_list)} treatment configurations")
                for i, treatment_config in enumerate(treatments_list):
                    try:
                        if debug:
                            logger.debug(f"Processing treatment config {i+1}: {treatment_config.get('instrument_name', 'unknown')}")
                        
                        # Create a processor for this treatment configuration
                        mapping_block = treatment_config.get("mapping_block", {})
                        treatment_processor = DataProcessor(mapping_config=mapping_block)
                        treatment_processor.enable_debug(debug)
                        
                        # Add any enum classes configured for this treatment
                        _add_enum_classes_to_processor(treatment_processor, treatment_config.get("enum_classes", {}))
                        
                        # Make sure enum classes from the mapping block are also added to the processor
                        # This is a key step to ensure proper label fetching
                        if "enum_classes" in mapping_block:
                            for prefix, enum_class_path in mapping_block.get("enum_classes", {}).items():
                                treatment_processor.add_enum_class(prefix, enum_class_path)
                                logger.debug(f"Added enum class for prefix '{prefix}' from mapping block")
                        
                        # Set the instrument name in the processor config
                        instrument_name = treatment_config.get("instrument_name")
                        if instrument_name:
                            treatment_processor.mapping_config["redcap_repeat_instrument"] = instrument_name
                        
                        # Copy over label_dicts if present
                        if "label_dicts" in treatment_config:
                            treatment_processor.mapping_config["label_dicts"] = treatment_config.get("label_dicts", {})
                        
                        # Process this treatment configuration
                        treatment_actions = map_medical_actions(
                            data,
                            treatment_processor,
                            dob=individual.date_of_birth
                        )
                        
                        # Add the resulting actions to our list - ONLY ONCE!
                        if treatment_actions:
                            medical_actions.extend(treatment_actions)
                            logger.debug(f"Added {len(treatment_actions)} actions from treatment config {i+1} for {instrument_name}")
                    except Exception as e:
                        logger.error(f"Error processing treatment config {i+1}: {e}")
                        if debug:
                            logger.debug(traceback.format_exc())
            
            if debug:
                logger.debug(f"Generated {len(medical_actions)} total medical actions")
        except Exception as e:
            if debug:
                logger.debug(f"Error mapping medical actions: {e}")
                logger.debug(traceback.format_exc())
            medical_actions = []

        # Disease Block ---------------------------------------------------------
        try:
            disease_config = get_mapping_config("diseases")
            disease_processor = DataProcessor(
                mapping_config=disease_config.get("mapping_block", {})
            )
            disease_processor.enable_debug(debug)
            
            # Add enum classes if present
            _add_enum_classes_to_processor(disease_processor, disease_config.get("enum_classes", {}))
            
            # Handle instrument name(s)
            instrument_name = disease_config.get("instrument_name")
            if isinstance(instrument_name, (list, set)):
                # Store the full list of instruments in the config for use by the mapper
                disease_processor.mapping_config["instrument_name"] = instrument_name
                # For backwards compatibility with repeated elements, use the first instrument
                if list(instrument_name):
                    instrument_name_str = list(instrument_name)[0]
                    if instrument_name_str not in ["__dummy__", ""]:
                        disease_processor.mapping_config["redcap_repeat_instrument"] = instrument_name_str
            elif instrument_name and instrument_name not in ["__dummy__", ""]:
                disease_processor.mapping_config["redcap_repeat_instrument"] = instrument_name
                disease_processor.mapping_config["instrument_name"] = instrument_name
            
            diseases = map_diseases(
                data, 
                disease_processor,
                dob=individual.date_of_birth
            )
            
            if debug:
                logger.debug(f"Generated {len(diseases)} diseases")
        except Exception as e:
            if debug:
                logger.debug(f"Error mapping diseases: {e}")
                logger.debug(traceback.format_exc())
            diseases = []
            
        # Genetics Block --------------------------------------------------------
        # Variation Descriptor
        try:
            variation_descriptor_config = get_mapping_config("variationDescriptor")
            variation_descriptor_processor = DataProcessor(
                mapping_config=variation_descriptor_config.get("mapping_block", {})
            )
            variation_descriptor_processor.enable_debug(debug)
            
            # Add enum classes if present
            _add_enum_classes_to_processor(variation_descriptor_processor, variation_descriptor_config.get("enum_classes", {}))
            
            # Handle instrument name(s)
            instrument_name = variation_descriptor_config.get("instrument_name")
            if isinstance(instrument_name, (list, set)):
                # Store the full list of instruments for reference
                variation_descriptor_processor.mapping_config["instrument_names"] = list(instrument_name)
                # For backwards compatibility, use the first instrument
                if list(instrument_name):
                    variation_descriptor_processor.mapping_config["redcap_repeat_instrument"] = list(instrument_name)[0]
            else:
                variation_descriptor_processor.mapping_config["redcap_repeat_instrument"] = instrument_name
            
            variation_descriptor = map_variation_descriptor(
                data,
                variation_descriptor_processor
            )
        except Exception as e:
            if debug:
                logger.debug(f"Error mapping variation descriptor: {e}")
                logger.debug(traceback.format_exc())
            variation_descriptor = {}
        
        # Interpretations
        try:
            interpretation_config = get_mapping_config("interpretations")
            interpretation_processor = DataProcessor(
                mapping_config=interpretation_config.get("mapping_block", {})
            )
            interpretation_processor.enable_debug(debug)
            
            # Add enum classes if present
            _add_enum_classes_to_processor(interpretation_processor, interpretation_config.get("enum_classes", {}))
            
            # Handle instrument name(s)
            instrument_name = interpretation_config.get("instrument_name")
            if isinstance(instrument_name, (list, set)):
                # Store the full list of instruments for reference
                interpretation_processor.mapping_config["instrument_names"] = list(instrument_name)
                # For backwards compatibility, use the first instrument
                if list(instrument_name):
                    interpretation_processor.mapping_config["redcap_repeat_instrument"] = list(instrument_name)[0]
            else:
                interpretation_processor.mapping_config["redcap_repeat_instrument"] = instrument_name
            
            interpretations = map_interpretations(
                data,
                interpretation_processor,
                subject_id=individual.id,
                variation_descriptor=variation_descriptor
            )
        except Exception as e:
            if debug:
                logger.debug(f"Error mapping interpretations: {e}")
                logger.debug(traceback.format_exc())
            interpretations = []
        
        # Metadata --------------------------------------------------------------
        try:
            metadata_config = mapping_configs.get("metadata", {})
            metadata = map_metadata(
                created_by=created_by,
                code_systems=metadata_config.get("code_systems")
            )
        except Exception as e:
            logger.error(f"Error creating metadata: {e}")
            if debug:
                logger.error(traceback.format_exc())
            raise ValueError(f"Failed to create metadata: {str(e)}")
        
        # Debug count of medical actions
        if debug:
            procedure_count = sum(1 for a in medical_actions if hasattr(a, 'procedure') and a.procedure)
            treatment_count = sum(1 for a in medical_actions if hasattr(a, 'treatment') and a.treatment)
            logger.debug(f"Final medical actions breakdown: {procedure_count} procedures + {treatment_count} treatments = {len(medical_actions)} total")

        # Construct Phenopacket -------------------------------------------------
        phenopacket = Phenopacket(
            id=record_id,
            subject=individual,
            phenotypic_features=phenotypic_features,
            measurements=measurements,
            diseases=diseases,
            medical_actions=medical_actions,
            meta_data=metadata,
            interpretations=interpretations
        )
        
        if debug:
            logger.debug(f"Successfully created phenopacket for record {record_id}")
            
        return phenopacket
     
    except Exception as e:
        logger.error(f"Error creating Phenopacket: {e}")
        if debug:
            logger.error(traceback.format_exc())
        raise