import logging
from rarelink.utils.processor import DataProcessor
from phenopackets import (
    Interpretation,
    OntologyClass,
    Diagnosis,
    GenomicInterpretation,
    VariantInterpretation,
    VariationDescriptor
)

logger = logging.getLogger(__name__)

def map_interpretations(
    data: dict, 
    processor: DataProcessor,
    subject_id: str,
    variation_descriptor: VariationDescriptor = None
) -> dict:
    """
    Maps interpretation details, including genomic interpretations grouped
    by diagnosis_id and redcap_repeat_instance.

    Args:
        data (dict): Input data for interpretation.
        processor (DataProcessor): Handles field processing.
        subject_id (str): The subject or biosample ID.
        variation_descriptor (VariationDescriptor): Variation descriptor 
        for genomic interpretation.

    Returns:
        dict: Mapped interpretation structure.
    """
    
    # Fetching and preparation
    # --------------------------------------------------------------------------
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
    
    try:
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.warning("No repeated elements found in the data.")
            return []

        interpretation_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        
        # Grouping interpreations by diagnosis_id
        # ----------------------------------------------------------------------
        interpretation_groups = {}

        for interpretation_element in interpretation_elements:
            interpretation_data = interpretation_element.get("genetic_findings")
            if not interpretation_data:
                logger.warning("No interpretation data found in this element.")
                continue
            
            # Genomic Diagnosis
            # ------------------------------------------------------------------
            diagnosis_id = (
                interpretation_data.get(processor.mapping_config[
                                                    "diagnosis_field_1"]) or
                interpretation_data.get(processor.mapping_config[
                                                    "diagnosis_field_2"]) or 
                interpretation_data.get(processor.mapping_config[
                                                    "diagnosis_field_3"])
            )
            diagnosis_label = processor.fetch_label(diagnosis_id)

            # Progress Status
            # ------------------------------------------------------------------
            progress_status_field = interpretation_data.get(
                processor.mapping_config["progress_status_field"])
            progress_status = processor.fetch_mapping_value(
                "map_progress_status", progress_status_field
            ) if progress_status_field else "UNKNOWN_PROGRESS"

            # Initialize interpretation group by `diagnosis_id`
            # ------------------------------------------------------------------
            if diagnosis_id not in interpretation_groups:
                interpretation_groups[diagnosis_id] = {
                    "diagnosis": Diagnosis(
                        disease=OntologyClass(
                            id=diagnosis_id,
                            label=diagnosis_label
                        ),
                        genomic_interpretations=[]
                    ),
                    "progress_status": progress_status
                }

            # Fetch `redcap_repeat_instance`
            # ------------------------------------------------------------------
            redcap_repeat_instance = interpretation_element.get(
                                                    "redcap_repeat_instance")
            if not redcap_repeat_instance:
                logger.warning("No redcap_repeat_instance found. Skipping.")
                continue

            # Check for existing genomic interpretations
            # ------------------------------------------------------------------
            existing_instances = {
                gi.subject_or_biosample_id for gi in interpretation_groups[
                    diagnosis_id]["diagnosis"].genomic_interpretations
            }
            if redcap_repeat_instance in existing_instances:
                continue

            # Match VariationDescriptor by redcap_repeat_instance
            # ------------------------------------------------------------------
            variation_descriptor_instance = variation_descriptor.get(
                redcap_repeat_instance)
            if not variation_descriptor_instance:
                logger.warning(f"No matching VariationDescriptor for \
                    redcap_repeat_instance: {redcap_repeat_instance}. Skipping.")
                continue
            
            # Create VariantInterpretation
            # ------------------------------------------------------------------
            variant_interpretation = VariantInterpretation(
                acmg_pathogenicity_classification=processor.fetch_mapping_value(
                    "map_acmg_classification",
                    interpretation_data.get(processor.mapping_config[
                        "acmg_pathogenicity_classification_field"])
                ) or "NOT_PROVIDED",
                therapeutic_actionability=processor.fetch_mapping_value(
                    "map_therapeutic_actionability",
                    interpretation_data.get(processor.mapping_config[
                        "therapeutic_actionability_field"])
                ) or "UNKNOWN_ACTIONABILITY",
                variation_descriptor=variation_descriptor_instance
            )

            # Create GenomicInterpretation
            # ------------------------------------------------------------------
            genomic_interpretation = GenomicInterpretation(
                subject_or_biosample_id=subject_id,
                interpretation_status=processor.fetch_mapping_value(
                    "map_interpretation_status",
                    interpretation_data.get(
                        processor.mapping_config["interpretation_status_field"])
                ) or "UNKNOWN_STATUS",
                variant_interpretation=variant_interpretation
            )

            interpretation_groups[diagnosis_id][
                "diagnosis"].genomic_interpretations.append(
                    genomic_interpretation)

        # Build interpretations
        # ----------------------------------------------------------------------
        interpretations = [
            Interpretation(
                id=subject_id,
                progress_status=group["progress_status"],
                diagnosis=group["diagnosis"]
            )
            for group in interpretation_groups.values()
        ]

        return interpretations
    
    except Exception as e:
        logger.error(f"Error mapping interpretation: {e}")
        raise
