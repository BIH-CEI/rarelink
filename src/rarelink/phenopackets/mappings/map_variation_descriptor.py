from rarelink.utils.processor import DataProcessor
import logging
from phenopackets import (
    VariationDescriptor,
    OntologyClass,
    Expression
    #GeneDescriptor
)

logger = logging.getLogger(__name__)

def map_variation_descriptor(data: dict, processor: DataProcessor) -> dict:
    """Maps variant data to the Phenopacket VariationDescriptor format.

    Args:
        data (dict): Input data for variant.
        processor (DataProcessor): Handles field processing.

    Returns:
        dict: Mapped variation descriptor structure.
    """
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")

    try:
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.warning("No repeated elements found in the data.")
            return []

        variation_descriptor_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]

        for variation_descriptor_element in variation_descriptor_elements:
            variation_descriptor_data = variation_descriptor_element.get(
                                                        "genetic_findings")
            if not variation_descriptor_data:
                logger.warning(f"No genetic findings data found in element: \
                    {variation_descriptor_element}. Skipping.")
                continue
            
        # unique ID
        id = processor.generate_unique_id()
        
        #  Expressions
        expressions = [
            Expression(syntax="hgvs", value=expression_value)
            for expression_value in [
                variation_descriptor_data.get(processor.mapping_config[field_key])
                for field_key in [
                    "expression_field_1",
                    "expression_field_2",
                    "expression_field_3"
                ]
                if variation_descriptor_data.get(processor.mapping_config[field_key])
            ]
        ]
        
        # Allelic State
        allelic_state_id = variation_descriptor_data.get(
                processor.mapping_config["allelic_state_field_1"] or
                processor.mapping_config["allelic_state_field_2"]
        )
        allelic_state = OntologyClass(
            id = processor.process_code(allelic_state_id),
            label = processor.fetch_label(allelic_state_id, enum_class="Zygosity")
        )
        
        # Structural Type
        structural_type_id = variation_descriptor_data.get(
                processor.mapping_config["structural_type_field"]
         )

        variation_descriptor = VariationDescriptor(
            id=id,
            expressions=expressions,
            allelic_state=allelic_state,
            # structural_type=structural_type,
            # gene_context=gene_context,
            # extensions=extensions
        )
            
        logger.info(f"Successfully mapped individual: {variation_descriptor}")
        return variation_descriptor

    
    except Exception as e:
        logger.error(f"Failed to map individual: {e}")
        raise
            

    
    #     "expression_field_1": "loinc_81290_9",
    # "expression_field_2": "loinc_48004_6",
    # "expression_field_3": "loinc_48005_3",
    # "allelic_state_field_1": "loinc_53034_5",
    # "allelic_state_field_2": "loinc_53034_5_other",
    # "structural_type_field": "loinc_48019_4",
    # # gene descriptor:
    # "value_id_field": "loinc_48018_6"