from rarelink.utils.processor import DataProcessor
import logging
from phenopackets import (
    VariationDescriptor,
    OntologyClass,
    Expression,
    GeneDescriptor,
    Extension
    # VcfRecord
)

logger = logging.getLogger(__name__)

def map_variation_descriptor(data: dict, processor: DataProcessor) -> dict:
    """
    Maps variant data to a dictionary of VariationDescriptors keyed by 
    redcap_repeat_instance.

    Args:
        data (dict): Input data for variants.
        processor (DataProcessor): Handles field processing.

    Returns:
        dict: A dictionary with `redcap_repeat_instance` as the key and 
              VariationDescriptor as the value.
    """
    # Fetching and preparation
    # --------------------------------------------------------------------------
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")

    try:
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.warning("No repeated elements found in the data.")
            return {}

        variation_descriptors = {}

        for variation_descriptor_element in repeated_elements:
            if variation_descriptor_element.get("redcap_repeat_instrument") \
                != instrument_name:
                continue

            # Extract redcap_repeat_instance
            redcap_repeat_instance = variation_descriptor_element.get(
                "redcap_repeat_instance")
            if not redcap_repeat_instance:
                logger.warning("No redcap_repeat_instance found in element.")
                continue

            variation_descriptor_data = variation_descriptor_element.get(
                "genetic_findings")
            if not variation_descriptor_data:
                logger.warning(f"No genetic findings data found in element: \
                    {variation_descriptor_element}. Skipping.")
                continue

            # Unique ID
            # ------------------------------------------------------------------
            id = processor.generate_unique_id()

            # VariationDescriptor.expressions
            # ------------------------------------------------------------------
            expressions = [
                Expression(syntax="hgvs", value=expression_value)
                for expression_value in [
                    variation_descriptor_data.get(
                        processor.mapping_config[field_key])
                    for field_key in ["expression_field_1", 
                                      "expression_field_2",
                                      "expression_field_3"]
                    if variation_descriptor_data.get(
                        processor.mapping_config[field_key])
                ]
            ]

            # VariationDescriptor.allelic_state
            # ------------------------------------------------------------------
            allelic_state_id = (
                variation_descriptor_data.get(processor.mapping_config[
                    "allelic_state_field_2"])
                if variation_descriptor_data.get(processor.mapping_config[
                    "allelic_state_field_1"]) == "loinc_48019_4_other"
                else variation_descriptor_data.get(processor.mapping_config[
                    "allelic_state_field_1"])
            )
            allelic_state_label = (
                processor.fetch_label(allelic_state_id, enum_class="Zygosity")
                or processor.fetch_label(allelic_state_id)
            )
            allelic_state = OntologyClass(
                id=processor.process_code(allelic_state_id),
                label=allelic_state_label
            )

            # VariationDescriptor.structural_type
            # ------------------------------------------------------------------
            structural_type_id = (
                variation_descriptor_data.get(processor.mapping_config[
                    "structural_type_field_2"])
                if variation_descriptor_data.get(processor.mapping_config[
                    "structural_type_field_1"]) == "loinc_48019_4_other"
                else variation_descriptor_data.get(processor.mapping_config[
                    "structural_type_field_1"])
            )
            structural_type_label = (
                processor.fetch_label(structural_type_id,
                                      enum_class="DNAChangeType")
                or processor.fetch_label(structural_type_id)
            )
            structural_type = OntologyClass(
                id=processor.process_code(structural_type_id),
                label=structural_type_label
            )

            # VariationDescriptor.gene_context
            # ------------------------------------------------------------------
            value_id_string = variation_descriptor_data.get(
                processor.mapping_config["value_id_field"], None)
            value_id = processor.normalize_hgnc_id(value_id_string)
            gene_context = GeneDescriptor(value_id=value_id, 
                symbol=processor.fetch_label(value_id)) if value_id else None

            # VariationDescriptor.extensions = Unvalidated Genetic Mutation String
            # ------------------------------------------------------------------
            value = variation_descriptor_data.get(processor.mapping_config[
                "expression_string_field"], None)
            extensions = [Extension(name="Unvalidated Genetic Mutation String",
                                    value=value)] if value else None

            # Create VariationDescriptor
            # ------------------------------------------------------------------
            variation_descriptor = VariationDescriptor(
                id=id,
                expressions=expressions,
                allelic_state=allelic_state,
                structural_type=structural_type,
                gene_context=gene_context,
                extensions=extensions
            )

            variation_descriptors[redcap_repeat_instance] = variation_descriptor

        return variation_descriptors

    except Exception as e:
        logger.error(f"Failed to map variation descriptors: {e}")
        raise
