from phenopackets import Phenopacket
import logging
import traceback
from typing import Dict, Any, Optional
from rarelink.utils.processor import DataProcessor
from rarelink.phenopackets.mappings.utils.common_utils import add_enum_classes_to_processor
from rarelink.rarelink_cdm import get_codesystems_container_class
from rarelink.phenopackets.mappings.metadata_mapper import collect_used_prefixes_from_blocks

from rarelink.phenopackets.mappings.individual_mapper import IndividualMapper
from rarelink.phenopackets.mappings.vital_status_mapper import VitalStatusMapper
from rarelink.phenopackets.mappings.phenotypic_feature_mapper import PhenotypicFeatureMapper
from rarelink.phenopackets.mappings.measurement_mapper import MeasurementMapper
from rarelink.phenopackets.mappings.medical_action_mapper import MedicalActionMapper
from rarelink.phenopackets.mappings.disease_mapper import DiseaseMapper
from rarelink.phenopackets.mappings.variation_descriptor_mapper import VariationDescriptorMapper
from rarelink.phenopackets.mappings.interpretation_mapper import InterpretationMapper
from rarelink.phenopackets.mappings.metadata_mapper import MetadataMapper
from rarelink.phenopackets.adapter.ontology_routing_adapter import (
    should_route,
    apply_ontology_routing,
    get_routed_phenotypic_elements,
    get_routed_disease_dicts,
)

logger = logging.getLogger(__name__)

def create_phenopacket(
    data: dict,
    created_by: str,
    mapping_configs: Optional[Dict[str, Any]] = None,
    debug: bool = False
) -> Phenopacket:
    """
    Creates a Phenopacket for an individual record with flexible mapping
    configurations.

    Args:
        data (dict): Input record data.
        created_by (str): Creator's name (written into MetaData).
        mapping_configs (dict): Mapping configurations for all blocks.
        debug (bool): Enable verbose debug logging.

    Returns:
        Phenopacket: The fully constructed Phenopacket.
    """
    if not mapping_configs:
        raise ValueError("Mapping configurations are required.")

    logging_level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(logging_level)

    try:
        record_id = data.get("record_id", "unknown")
        if debug:
            logger.debug(f"Processing record ID: {record_id}")

        # Ontology routing (opt-in)
        if should_route(mapping_configs):
            data = apply_ontology_routing(data, mapping_configs)
            logger.debug(
                f"[routing] phenotypicFeatures: "
                f"{len(get_routed_phenotypic_elements(data))}, "
                f"diseases: {len(get_routed_disease_dicts(data))}"
            )

        # ── Helper: build a DataProcessor from a named config block ──────────
        def create_processor(block: str, required: bool = False):
            config = mapping_configs.get(block, {})
            if isinstance(config, list):
                config = config[0]
            if required and not config:
                raise ValueError(
                    f"Required mapping configuration '{block}' missing."
                )
            mapping_block = config.get("mapping_block", {}).copy()
            for key, value in config.items():
                if key != "mapping_block":
                    mapping_block[key] = value
            if "instrument_name" in mapping_block:
                inst = mapping_block["instrument_name"]
                if not isinstance(inst, str):
                    inst_list = (
                        [str(x) for x in inst]
                        if isinstance(inst, (list, set))
                        else [str(inst)]
                    )
                    mapping_block["instrument_name"] = inst_list
                else:
                    mapping_block["instrument_name"] = [inst]
            if (
                "instrument_name" in mapping_block
                and "redcap_repeat_instrument" not in mapping_block
            ):
                mapping_block["redcap_repeat_instrument"] = (
                    mapping_block["instrument_name"][0]
                )
            processor = DataProcessor(mapping_config=mapping_block)
            processor.enable_debug(debug)
            add_enum_classes_to_processor(
                processor, config.get("enum_classes", {})
            )
            return processor, config

        # ── Individual & Vital Status ────────────────────────────────────────
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

        # ── Phenotypic Features ──────────────────────────────────────────────
        phenotypic_features = []
        phenotypic_config = mapping_configs.get("phenotypicFeatures")
        full_data = data

        # if ontology_routing is active
        routed_pf = get_routed_phenotypic_elements(data)
        if routed_pf:
            base_pf_config = (
                phenotypic_config[0]
                if isinstance(phenotypic_config, list) and phenotypic_config
                else phenotypic_config or {}
            )
            routed_pf_config = _build_routed_pf_config(base_pf_config, routed_pf)

            if isinstance(phenotypic_config, list):
                phenotypic_config = list(phenotypic_config) + [routed_pf_config]
            elif phenotypic_config:
                phenotypic_config = [phenotypic_config, routed_pf_config]
            else:
                phenotypic_config = [routed_pf_config]

        if isinstance(phenotypic_config, list):
            logger.debug(
                f"Processing {len(phenotypic_config)} phenotypic feature "
                f"configurations"
            )
            for i, config in enumerate(phenotypic_config):
                try:
                    proc = DataProcessor(
                        mapping_config=config.get("mapping_block", {}).copy()
                    )
                    proc.mapping_config["full_data"] = full_data
                    for key, value in config.items():
                        if key != "mapping_block":
                            proc.mapping_config[key] = value
                    if (
                        "instrument_name" in proc.mapping_config
                        and "redcap_repeat_instrument"
                        not in proc.mapping_config
                    ):
                        proc.mapping_config["redcap_repeat_instrument"] = (
                            proc.mapping_config["instrument_name"]
                        )
                    proc.enable_debug(debug)
                    add_enum_classes_to_processor(
                        proc, config.get("enum_classes", {})
                    )
                    feature_mapper = PhenotypicFeatureMapper(proc)
                    feats = feature_mapper.map(
                        data, dob=dob_field
                    )
                    if feats:
                        phenotypic_features.extend(feats)
                        logger.debug(
                            f"Added {len(feats)} features from config {i + 1}"
                        )
                except Exception as e:
                    logger.error(
                        f"Error processing phenotypic feature config "
                        f"{i + 1}: {e}"
                    )
                    if debug:
                        logger.debug(traceback.format_exc())
        else:
            proc, _ = create_processor("phenotypicFeatures")
            proc.mapping_config["full_data"] = full_data
            feature_mapper = PhenotypicFeatureMapper(proc)
            phenotypic_features = feature_mapper.map(
                data, dob=dob_field
            )

        if debug:
            logger.debug(f"Total phenotypic features: {len(phenotypic_features)}")

        # Deduplicate features (guard against multi-config overlap)
        processed_features = []
        feature_types_seen = set()
        for feature in phenotypic_features:
            if not feature or not feature.type or not feature.type.id:
                continue
            feature_key = (
                feature.type.id,
                str(getattr(feature.onset, "age", None))
                if hasattr(feature, "onset")
                else None,
                hash(tuple(sorted([m.id for m in feature.modifiers])))
                if hasattr(feature, "modifiers") and feature.modifiers
                else None,
            )
            if feature_key not in feature_types_seen:
                feature_types_seen.add(feature_key)
                processed_features.append(feature)
        phenotypic_features = processed_features

        # ── Measurements ─────────────────────────────────────────────────────
        measurements = []
        measurement_config = mapping_configs.get("measurements")
        if isinstance(measurement_config, list):
            logger.debug(
                f"Processing {len(measurement_config)} measurement configurations"
            )
            for i, config in enumerate(measurement_config):
                try:
                    proc = DataProcessor(
                        mapping_config=config.get("mapping_block", {}).copy()
                    )
                    for key, value in config.items():
                        if key != "mapping_block":
                            proc.mapping_config[key] = value
                    if (
                        "instrument_name" in proc.mapping_config
                        and "redcap_repeat_instrument"
                        not in proc.mapping_config
                    ):
                        proc.mapping_config["redcap_repeat_instrument"] = (
                            proc.mapping_config["instrument_name"]
                        )
                    proc.enable_debug(debug)
                    add_enum_classes_to_processor(
                        proc, config.get("enum_classes", {})
                    )
                    measurement_mapper = MeasurementMapper(proc)
                    meas = measurement_mapper.map(
                        data, dob=dob_field
                    )
                    if meas:
                        measurements.extend(meas)
                        logger.debug(
                            f"Added {len(meas)} measurements from config {i + 1}"
                        )
                except Exception as e:
                    logger.error(
                        f"Error processing measurement config {i + 1}: {e}"
                    )
                    if debug:
                        logger.debug(traceback.format_exc())
        else:
            proc, _ = create_processor("measurements")
            measurement_mapper = MeasurementMapper(proc)
            measurements = measurement_mapper.map(
                data, dob=dob_field
            )
        if debug:
            logger.debug(f"Total measurements: {len(measurements)}")

        # ── Medical Actions ───────────────────────────────────────────────────
        medical_actions = []
        proc_processor, _ = create_processor("medical_actions")
        medical_action_mapper = MedicalActionMapper(proc_processor)
        proc_actions = medical_action_mapper.map(
            data, dob=dob_field
        )
        if proc_actions:
            medical_actions.extend(proc_actions)
            logger.debug(
                f"Added {len(proc_actions)} procedure-based medical actions"
            )

        treatments_config = mapping_configs.get("treatments")
        if treatments_config:
            if isinstance(treatments_config, list):
                for i, config in enumerate(treatments_config):
                    try:
                        proc, _ = create_processor("treatments")
                        for key, value in config.items():
                            if key != "mapping_block":
                                proc.mapping_config[key] = value
                        proc.enable_debug(debug)
                        add_enum_classes_to_processor(
                            proc, config.get("enum_classes", {})
                        )
                        treatment_mapper = MedicalActionMapper(proc)
                        treat_actions = treatment_mapper.map(
                            data, dob=dob_field
                        )
                        if treat_actions:
                            medical_actions.extend(treat_actions)
                            logger.debug(
                                f"Added {len(treat_actions)} treatment actions "
                                f"from config {i + 1}"
                            )
                    except Exception as e:
                        logger.error(
                            f"Error processing treatment config {i + 1}: {e}"
                        )
                        if debug:
                            logger.debug(traceback.format_exc())
            elif isinstance(treatments_config, dict):
                proc, _ = create_processor("treatments")
                treatment_mapper = MedicalActionMapper(proc)
                treat_actions = treatment_mapper.map(
                    data, dob=dob_field
                )
                if treat_actions:
                    medical_actions.extend(treat_actions)
                    logger.debug(
                        f"Added {len(treat_actions)} treatment actions"
                    )

        if debug:
            logger.debug(f"Total medical actions: {len(medical_actions)}")

        # ── Diseases ─────────────────────────────────────────────────────────
        disease_processor, _ = create_processor("diseases")
        disease_mapper = DiseaseMapper(disease_processor)
        diseases = disease_mapper.map(data, dob=dob_field)

        # if ontology_routing is active
        routed_diseases = get_routed_disease_dicts(data)
        if routed_diseases:
            logger.debug(
                f"Processing {len(routed_diseases)} ontology-routed disease(s)"
            )
            for routed_dict in routed_diseases:
                try:
                    routed_proc, _ = create_processor("diseases")
                    routed_data = _inject_routed_disease(
                        data, routed_dict, routed_proc
                    )
                    routed_disease_mapper = DiseaseMapper(routed_proc)
                    routed_result = routed_disease_mapper.map(
                        routed_data, dob=dob_field
                    )
                    if routed_result:
                        diseases.extend(
                            routed_result
                            if isinstance(routed_result, list)
                            else [routed_result]
                        )
                        logger.debug(
                            f"Added routed disease from "
                            f"{routed_dict.get('__source_instrument')} "
                            f"#{routed_dict.get('__source_instance')}"
                        )
                except Exception as e:
                    logger.error(
                        f"Error processing routed disease "
                        f"({routed_dict.get('__source_instrument')} "
                        f"#{routed_dict.get('__source_instance')}): {e}"
                    )
                    if debug:
                        logger.debug(traceback.format_exc())

        if debug:
            logger.debug(f"Total diseases: {len(diseases)}")

        # ── Genetics ─────────────────────────────────────────────────────────
        var_processor, _ = create_processor("variationDescriptor")
        variation_mapper = VariationDescriptorMapper(var_processor)
        variation_descriptors = variation_mapper.map(data)

        interp_processor, _ = create_processor("interpretations")
        interpretation_mapper = InterpretationMapper(interp_processor)
        interpretations = interpretation_mapper.map(
            data,
            subject_id=individual.id,
            variation_descriptors=variation_descriptors,
        )

        # ── Metadata ──────────────────────────────────────────────────────────
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
            logger.debug(
                f"[metadata] used CURIE prefixes: {sorted(used_prefixes)}"
            )

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
            interpretations=interpretations,
        )
        if debug:
            logger.debug(
                f"Successfully created phenopacket for record {record_id}"
            )
        return phenopacket

    except Exception as e:
        logger.error(f"Error creating Phenopacket: {e}")
        if debug:
            logger.error(traceback.format_exc())
        raise


# ---------------------------------------------------------------------------
# Private helpers — only used by create_phenopacket
# ---------------------------------------------------------------------------

def _build_routed_pf_config(
    base_config: Dict[str, Any],
    routed_elements: list,
) -> Dict[str, Any]:
    """
    Build a minimal phenotypicFeatures mapping config for HP-routed elements.

    The config inherits onset/severity/modifier field-name conventions from
    the first existing phenotypicFeatures block so the PhenotypicFeatureMapper
    knows which fields to read from the routed elements.

    The instrument name is set to the instrument of the first routed element,
    so the mapper looks in the right sub-dict of each repeated_elements entry.
    """
    # Detect the instrument from the first routed element
    instrument = (
        routed_elements[0].get("redcap_repeat_instrument", "__routed__")
        if routed_elements
        else "__routed__"
    )

    # Keys to inherit from the base config's mapping_block
    _INHERIT = {
        "onset_date_field", "onset_date_fields", "onset_age_field",
        "resolution_field", "severity_field", "evidence_field",
        "modifier_temp_pattern_field",
        *(f"modifier_field_{i}" for i in range(1, 10)),
    }

    base_block = (
        base_config.get("mapping_block", {})
        if isinstance(base_config, dict)
        else {}
    )
    inherited = {k: v for k, v in base_block.items() if k in _INHERIT}

    return {
        "instrument_name": instrument,
        "mapping_block": {
            "redcap_repeat_instrument": instrument,
            "multi_onset": base_block.get("multi_onset", False),
            **inherited,
        },
        "enum_classes": (
            base_config.get("enum_classes", {})
            if isinstance(base_config, dict)
            else {}
        ),
        "data_model": (
            base_config.get("data_model", "")
            if isinstance(base_config, dict)
            else ""
        ),
    }


def _inject_routed_disease(
    data: Dict[str, Any],
    routed_dict: Dict[str, Any],
    processor,
) -> Dict[str, Any]:
    """
    Produce a data view that makes the normalized routed_dict visible to
    the DiseaseMapper via its normal field-access path.

    The DiseaseMapper reads ``term_field_1`` and ``onset_date_field`` from
    the processor's mapping_config, then looks them up against the record
    data.  We temporarily override those keys in the processor config to
    point at fixed sentinel field names, then return a synthetic data dict
    that contains those sentinel values.

    This approach requires no changes to DiseaseMapper itself.
    """
    # Overlay the routed values directly onto the processor's mapping config
    # using the term_field_1 / onset_date_field convention.
    processor.mapping_config["term_field_1"] = "__routed_term__"
    processor.mapping_config["onset_date_field"] = "__routed_onset__"

    # Build a synthetic record that DiseaseMapper can traverse normally
    synthetic = dict(data)
    synthetic["__routed_term__"] = routed_dict.get("term_field_1")
    synthetic["__routed_onset__"] = routed_dict.get("onset_date_field")
    return synthetic