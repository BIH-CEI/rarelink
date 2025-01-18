from rarelink.utils.processor import DataProcessor

import logging
from phenopackets import (
    VariationDescriptor,
    OntologyClass,
    Expression,
    GeneDescriptor,
    Extension,
    VcfRecord
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
        
        # Fetching VCF Record fields
        # potentially integrate function with pyhgvs in future - for now 
        # we only pass the genome assemlbly (= reference genome)
        genome_assembly_id = variation_descriptor_data.get(
            processor.mapping_config["genome_assembly_field"]
        )
        genome_assembly = processor.fetch_label(genome_assembly_id, 
                                                enum_class="ReferenceGenome")
            
        vcf_record = VcfRecord(
            genome_assembly=genome_assembly,
            chrom="unknown",
            pos=0,
            ref="unknown",
            alt="unknown",
        )

        # Allelic State
        allelic_state_id = (
            variation_descriptor_data.get(
                processor.mapping_config["allelic_state_field_2"])
            if variation_descriptor_data.get(
                processor.mapping_config["allelic_state_field_1"]) == "loinc_48019_4_other"
            else variation_descriptor_data.get(
                processor.mapping_config["allelic_state_field_1"])
        )
        allelic_state_label = (
            processor.fetch_label(allelic_state_id, enum_class="Zygosity")
            or processor.fetch_label(allelic_state_id)
        )
        allelic_state = OntologyClass(
            id=processor.process_code(allelic_state_id),
            label=allelic_state_label
        )
        
        # Structural Type
        structural_type_id = (
            variation_descriptor_data.get(
                processor.mapping_config["structural_type_field_2"])
            if variation_descriptor_data.get(
                processor.mapping_config["structural_type_field_1"]) == "loinc_48019_4_other"
            else variation_descriptor_data.get(
                processor.mapping_config["structural_type_field_1"])
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

        # Gene Context
        value_id = variation_descriptor_data.get(
            processor.mapping_config["value_id_field"], None
        )

        if value_id:
            symbol = processor.fetch_label(value_id)
            gene_context = GeneDescriptor(
                value_id=value_id,
                symbol=symbol
            )
        else:
            gene_context = None
            
        # Extensions: (6.1.6) - Genetic Mutation String
            # to be discussed: This field allows users to enter unvalidated 
            # genetic mutation strings. We could allow this field to be added
            # to the Extensions field of the VariationDescriptor class.
            # expression_string_field
        value = variation_descriptor_data.get(
            processor.mapping_config["expression_string_field"], None
        )

        if value:
            extensions = [
                Extension(
                    name="Unvalidated Genetic Mutation String",
                    value=value
                )
            ]
        else:
            extensions = None
            
        # --> constructing VariationDescriptor
        variation_descriptor = VariationDescriptor(
            id=id,
            expressions=expressions,
            vcf_record=vcf_record,
            allelic_state=allelic_state,
            structural_type=structural_type,
            gene_context=gene_context,
            extensions=extensions
        )
            
        logger.info(f"Successfully mapped individual: {variation_descriptor}")
        return variation_descriptor

    
    except Exception as e:
        logger.error(f"Failed to map individual: {e}")
        raise