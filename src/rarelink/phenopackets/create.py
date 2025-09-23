# src/rarelink/phenopackets/create.py
from phenopackets import Phenopacket
import logging
import traceback
from typing import Dict, Any, Optional
from rarelink.utils.processor import DataProcessor
from rarelink.phenopackets.mappings.utils.common_utils import add_enum_classes_to_processor
from rarelink_cdm import get_codesystems_container_class
from rarelink.phenopackets.mappings.metadata_mapper import collect_used_prefixes_from_blocks

# Import new mapper classes
from rarelink.phenopackets.mappings.individual_mapper import IndividualMapper
from rarelink.phenopackets.mappings.vital_status_mapper import VitalStatusMapper
from rarelink.phenopackets.mappings.phenotypic_feature_mapper import PhenotypicFeatureMapper
from rarelink.phenopackets.mappings.measurement_mapper import MeasurementMapper
from rarelink.phenopackets.mappings.medical_action_mapper import MedicalActionMapper
from rarelink.phenopackets.mappings.disease_mapper import DiseaseMapper
from rarelink.phenopackets.mappings.variation_descriptor_mapper import VariationDescriptorMapper
from rarelink.phenopackets.mappings.interpretation_mapper import InterpretationMapper
from rarelink.phenopackets.mappings.metadata_mapper import MetadataMapper


logger = logging.getLogger(__name__)

def create_phenopacket(
    data: dict, 
    created_by: str, 
    mapping_configs: Optional[Dict[str, Any]] = None,
    debug: bool = False
) -> Phenopacket:
    """
    Creates a Phenopacket for an individual record with flexible mapping configurations.
    Refactored to use mapper classes for improved organization.
    
    Args:
        data (dict): Input data.
        created_by (str): Creator's name.
        mapping_configs (dict, optional): Mapping configurations for different blocks.
        debug (bool): Enable debug mode.
        
    Returns:
        Phenopacket: The constructed Phenopacket.
    """
    if not mapping_configs:
        raise ValueError("Mapping configurations are required.")

    # Set logging level
    logging_level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(logging_level)

    try:
        record_id = data.get("record_id", "unknown")
        if debug:
            logger.debug(f"Processing record ID: {record_id}")

        # --- Helper: Create a processor by merging outer keys ---
        def create_processor(block: str, required: bool = False):
            """
            Create a DataProcessor for a given block by merging the outer configuration keys
            into the mapping config. If the block configuration is a list, use its first element.
            Also, if 'instrument_name' is a collection, convert it to a list of strings and
            set 'redcap_repeat_instrument' to the first element.
            """
            config = mapping_configs.get(block, {})
            # If the configuration is a list, use the first element as the base config.
            if isinstance(config, list):
                config = config[0]
            if required and not config:
                raise ValueError(f"Required mapping configuration '{block}' missing.")
            # Start with a copy of the mapping block
            mapping_block = config.get("mapping_block", {}).copy()
            # Merge other keys from the outer config
            for key, value in config.items():
                if key != "mapping_block":
                    mapping_block[key] = value
            # Convert instrument_name to a list of strings if needed.
            if "instrument_name" in mapping_block:
                inst = mapping_block["instrument_name"]
                if not isinstance(inst, str):
                    # Convert set or list items to strings.
                    inst_list = [str(x) for x in inst] if isinstance(inst, (list, set)) else [str(inst)]
                    mapping_block["instrument_name"] = inst_list
                else:
                    mapping_block["instrument_name"] = [inst]  # wrap a single string in a list
            # Ensure that "redcap_repeat_instrument" is set to the first instrument.
            if "instrument_name" in mapping_block and "redcap_repeat_instrument" not in mapping_block:
                mapping_block["redcap_repeat_instrument"] = mapping_block["instrument_name"][0]
            processor = DataProcessor(mapping_config=mapping_block)
            processor.enable_debug(debug)
            add_enum_classes_to_processor(processor, config.get("enum_classes", {}))
            return processor, config


        # --- Individual & Vital Status ---
        individual_processor, _ = create_processor("individual", required=True)
        try:
            dob_field = individual_processor.get_field(data, "date_of_birth_field")
            if debug:
                logger.debug(f"Extracted DOB: {dob_field}")
        except Exception as e:
            if debug:
                logger.debug(f"Error extracting DOB: {e}")
            dob_field = None

        vital_status_processor, _ = create_processor("vitalStatus")
        vital_status_mapper = VitalStatusMapper(vital_status_processor)
        vital_status = vital_status_mapper.map(data, dob=dob_field)

        individual_mapper = IndividualMapper(individual_processor)
        individual = individual_mapper.map(data, vital_status=vital_status)

        # --- Phenotypic Features ---
        phenotypic_features = []
        phenotypic_config = mapping_configs.get("phenotypicFeatures")
        
        # Ensure we store the full data context for proper modifier scoping
        full_data = data  
        
        if isinstance(phenotypic_config, list):
            logger.debug(f"Processing {len(phenotypic_config)} phenotypic feature configurations")
            for i, config in enumerate(phenotypic_config):
                try:
                    # Start with base mapping block
                    proc = DataProcessor(mapping_config=config.get("mapping_block", {}).copy())
                    
                    # Set full_data for proper feature & modifier scoping
                    proc.mapping_config['full_data'] = full_data
                    
                    # Merge outer keys
                    for key, value in config.items():
                        if key != "mapping_block":
                            proc.mapping_config[key] = value
                    
                    # Ensure repeat instrument is set
                    if "instrument_name" in proc.mapping_config and "redcap_repeat_instrument" not in proc.mapping_config:
                        proc.mapping_config["redcap_repeat_instrument"] = proc.mapping_config["instrument_name"]
                    
                    proc.enable_debug(debug)
                    
                    # Add enum classes
                    add_enum_classes_to_processor(proc, config.get("enum_classes", {}))
                    
                    # Create mapper and map features
                    feature_mapper = PhenotypicFeatureMapper(proc)
                    feats = feature_mapper.map(data, dob=individual.date_of_birth)
                    
                    if feats:
                        # Ensure each feature has appropriate modifiers only
                        phenotypic_features.extend(feats)
                        logger.debug(f"Added {len(feats)} features from config {i+1}")
                except Exception as e:
                    logger.error(f"Error processing phenotypic feature config {i+1}: {e}")
                    if debug:
                        logger.debug(traceback.format_exc())
        else:
            # Single configuration case
            proc, _ = create_processor("phenotypicFeatures")
            
            # Set full_data for proper feature & modifier scoping
            proc.mapping_config['full_data'] = full_data
            
            feature_mapper = PhenotypicFeatureMapper(proc)
            phenotypic_features = feature_mapper.map(data, dob=individual.date_of_birth)
        
        if debug:
            logger.debug(f"Total phenotypic features: {len(phenotypic_features)}")
        
        # Validate and deduplicate features if needed
        processed_features = []
        feature_types_seen = set()
        
        for feature in phenotypic_features:
            # Skip invalid features
            if not feature or not feature.type or not feature.type.id:
                continue
                
            # For CIEINR/multi-instrument setups, deduplicate features by onset date
            # This handles cases where the same feature appears in multiple configs
            feature_key = (
                feature.type.id, 
                str(getattr(feature.onset, 'age', None)) if hasattr(feature, 'onset') else None,
                # Include a hash of modifiers if they exist
                hash(tuple(sorted([m.id for m in feature.modifiers]))) if hasattr(feature, 'modifiers') and feature.modifiers else None
            )
            
            if feature_key not in feature_types_seen:
                feature_types_seen.add(feature_key)
                processed_features.append(feature)
        
        phenotypic_features = processed_features
        
        # --- Measurements ---
        measurements = []
        measurement_config = mapping_configs.get("measurements")
        if isinstance(measurement_config, list):
            logger.debug(f"Processing {len(measurement_config)} measurement configurations")
            for i, config in enumerate(measurement_config):
                try:
                    proc = DataProcessor(mapping_config=config.get("mapping_block", {}).copy())
                    for key, value in config.items():
                        if key != "mapping_block":
                            proc.mapping_config[key] = value
                    if "instrument_name" in proc.mapping_config and "redcap_repeat_instrument" not in proc.mapping_config:
                        proc.mapping_config["redcap_repeat_instrument"] = proc.mapping_config["instrument_name"]
                    proc.enable_debug(debug)
                    add_enum_classes_to_processor(proc, config.get("enum_classes", {}))
                    measurement_mapper = MeasurementMapper(proc)
                    meas = measurement_mapper.map(data, dob=individual.date_of_birth)
                    if meas:
                        measurements.extend(meas)
                        logger.debug(f"Added {len(meas)} measurements from config {i+1}")
                except Exception as e:
                    logger.error(f"Error processing measurement config {i+1}: {e}")
                    if debug:
                        logger.debug(traceback.format_exc())
        else:
            proc, _ = create_processor("measurements")
            measurement_mapper = MeasurementMapper(proc)
            measurements = measurement_mapper.map(data, dob=individual.date_of_birth)
        if debug:
            logger.debug(f"Total measurements: {len(measurements)}")

        # --- Medical Actions (Procedures and Treatments) ---
        medical_actions = []
        proc_processor, _ = create_processor("procedures")
        medical_action_mapper = MedicalActionMapper(proc_processor)
        proc_actions = medical_action_mapper.map(data, dob=individual.date_of_birth)
        if proc_actions:
            medical_actions.extend(proc_actions)
            logger.debug(f"Added {len(proc_actions)} procedure-based medical actions")

        treatments_config = mapping_configs.get("treatments")
        if treatments_config:
            if isinstance(treatments_config, list):
                for i, config in enumerate(treatments_config):
                    try:
                        # Use the helper to get a base processor from the first element of the treatments list.
                        proc, _ = create_processor("treatments")
                        # Merge the specific treatment config overrides
                        for key, value in config.items():
                            if key != "mapping_block":
                                proc.mapping_config[key] = value
                        proc.enable_debug(debug)
                        add_enum_classes_to_processor(proc, config.get("enum_classes", {}))
                        treatment_mapper = MedicalActionMapper(proc)
                        treat_actions = treatment_mapper.map(data, dob=individual.date_of_birth)
                        if treat_actions:
                            medical_actions.extend(treat_actions)
                            logger.debug(f"Added {len(treat_actions)} treatment actions from config {i+1}")
                    except Exception as e:
                        logger.error(f"Error processing treatment config {i+1}: {e}")
                        if debug:
                            logger.debug(traceback.format_exc())
            elif isinstance(treatments_config, dict):
                proc, _ = create_processor("treatments")
                treatment_mapper = MedicalActionMapper(proc)
                treat_actions = treatment_mapper.map(data, dob=individual.date_of_birth)
                if treat_actions:
                    medical_actions.extend(treat_actions)
                    logger.debug(f"Added {len(treat_actions)} treatment actions")

        if debug:
            logger.debug(f"Total medical actions: {len(medical_actions)}")

        # --- Diseases ---
        disease_processor, _ = create_processor("diseases")
        disease_mapper = DiseaseMapper(disease_processor)
        diseases = disease_mapper.map(data, dob=individual.date_of_birth)
        if debug:
            logger.debug(f"Total diseases: {len(diseases)}")

        # --- Genetics: Variation Descriptor and Interpretations ---
        var_processor, _ = create_processor("variationDescriptor")
        variation_mapper = VariationDescriptorMapper(var_processor)
        variation_descriptors = variation_mapper.map(data)

        interp_processor, _ = create_processor("interpretations")
        interpretation_mapper = InterpretationMapper(interp_processor)
        interpretations = interpretation_mapper.map(
            data,
            subject_id=individual.id,
            variation_descriptors=variation_descriptors
        )

        # --- Metadata ---
        metadata_config = mapping_configs.get("metadata", {}) or {}
        code_systems = metadata_config.get("code_systems")
        if not code_systems:
            try:
                CodeSystemsContainerCls = get_codesystems_container_class()
                code_systems = CodeSystemsContainerCls()
            except Exception as e:
                logger.warning(f"Could not auto-load CodeSystemsContainer: {e}")
                code_systems = metadata_config.get("code_systems")

        used_prefixes = collect_used_prefixes_from_blocks(
            features=phenotypic_features,
            diseases=diseases,
            measurements=measurements,
            medical_actions=medical_actions,
            interpretations=interpretations,
            variation_descriptors=variation_descriptors,
        )
        if debug:
            logger.debug(f"[metadata] used CURIE prefixes: {sorted(used_prefixes)}")
            
        metadata = MetadataMapper(None).map(
            data={},                     
            created_by=created_by,
            code_systems=code_systems,
            used_prefixes=used_prefixes, 
        )
        
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
