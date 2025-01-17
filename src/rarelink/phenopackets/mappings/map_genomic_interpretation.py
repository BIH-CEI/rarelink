from rarelink.utils.processor import DataProcessor
import logging
from phenopackets import (
    GenomicInterpretation, 
    VariantInterpretation,
    VariationDescriptor
)

logger = logging.getLogger(__name__)

def map_genomic_interpretations(
    data: dict, 
    processor: DataProcessor,
    subject_id: str,
    variation_descriptor: VariationDescriptor = None) -> dict:
    """
    Maps multiple genomic interpretation to the required format.

    Args:
        data (dict): Input data for genomic interpretation.
        processor (DataProcessor): Handles field processing.

    Returns:
        dict: Mapped genomic interpretation structure.
    """

    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
    
    try:
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.warning("No repeated elements found in the data.")
            return []

        genomic_interpretation_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        
        genomic_interpretations = []
        
        for genomic_interpretation_element in genomic_interpretation_elements:
            genomic_interpretation_data = genomic_interpretation_element.get(
                                                        "genetic_findings")
            if not genomic_interpretation_data:
                logger.warning("No interpretation data found in "
                               "this element. Skipping.")
                continue

            # id
            subject_or_biosample_id = subject_id

            # interpretation status
            interpretation_status_field=genomic_interpretation_data.get(
                processor.mapping_config["interpretation_status_field"])
            interpretation_status = processor.fetch_mapping_value(
                "map_interpretation_status", interpretation_status_field) if \
                interpretation_status_field else "UNKNOWN_STATUS"
                
            # call: VariantInterpretation
            ## ACMG
            acmg_pathogenicity_classification_field = genomic_interpretation_data.get(
                processor.mapping_config["acmg_pathogenicity_classification_field"])
            acmg_pathogenicity_classification = processor.fetch_mapping_value(
                "map_acmg_classification", acmg_pathogenicity_classification_field) if \
                acmg_pathogenicity_classification_field else "NOT_PROVIDED"
            ## TherapeuticActionability
            therapeutic_actionability_field = genomic_interpretation_data.get(
                processor.mapping_config["therapeutic_actionability_field"])
            therapeutic_actionability = processor.fetch_mapping_value(
                "map_therapeutic_actionability", therapeutic_actionability_field) if \
                therapeutic_actionability_field else "UNKNOWN_ACTIONABILITY"    
            
            variant_interpretation = VariantInterpretation(
                acmg_pathogenicity_classification=acmg_pathogenicity_classification,
                therapeutic_actionability=therapeutic_actionability,
                variation_descriptor=variation_descriptor
                
            )
            
            # -> GenomicInterpretation Block
            genomic_interpretation = GenomicInterpretation(
                subject_or_biosample_id=subject_or_biosample_id,
                interpretation_status=interpretation_status,
                variant_interpretation = variant_interpretation
            )

            genomic_interpretations.append(genomic_interpretation)
        
        return genomic_interpretations
        
    except Exception as e:
        logger.error(f"Error mapping interpretation: {e}")
        raise
