from typing import Dict, Any, Optional
import logging
from phenopackets import (
    VariationDescriptor,
    OntologyClass,
    Expression,
    GeneDescriptor,
    Extension
)

from rarelink.phenopackets.mappings.base_mapper import BaseMapper

logger = logging.getLogger(__name__)

class VariationDescriptorMapper(BaseMapper[Dict[str, VariationDescriptor]]):
    """
    Mapper for VariationDescriptor entities in the Phenopacket schema.
    Maps variant data to a dictionary of VariationDescriptors keyed by redcap_repeat_instance.
    """
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> Optional[Dict[str, VariationDescriptor]]:
        """
        Map data to a dictionary of VariationDescriptor entities.
        The dictionary is keyed by redcap_repeat_instance.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (list): List of instruments for field access
            **kwargs: Additional mapping parameters
            
        Returns:
            Optional[Dict[str, VariationDescriptor]]: Dictionary of mapped VariationDescriptor entities
                                                      or None on failure
        """
        try:
            # Get the instrument name from the configuration or the provided instruments
            instrument_name = self.processor.mapping_config.get("redcap_repeat_instrument")
            if not instrument_name and instruments:
                instrument_name = instruments[0]
            
            if not instrument_name:
                logger.warning("No instrument name found for variation descriptor mapping")
                return {}
                
            # Find repeated elements for the specified instrument
            repeated_elements = data.get("repeated_elements", [])
            if not repeated_elements:
                logger.warning("No repeated elements found in the data")
                return {}
                
            # Filter elements for the target instrument
            variation_elements = [
                element for element in repeated_elements
                if element.get("redcap_repeat_instrument") == instrument_name
            ]
            
            if not variation_elements:
                logger.warning(f"No elements found for instrument {instrument_name}")
                return {}
                
            # Dictionary to store the mapped variation descriptors
            variation_descriptors = {}
            
            # Process each element
            for element in variation_elements:
                # Extract redcap_repeat_instance
                instance_id = element.get("redcap_repeat_instance")
                if not instance_id:
                    logger.warning("No redcap_repeat_instance found in element")
                    continue
                    
                # Get the genetic findings data
                genetic_data = element.get("genetic_findings")
                if not genetic_data:
                    logger.warning(f"No genetic findings data found in element {instance_id}")
                    continue
                    
                # Map this element to a VariationDescriptor
                variation_descriptor = self._map_variation_descriptor(genetic_data, instance_id)
                if variation_descriptor:
                    variation_descriptors[instance_id] = variation_descriptor
                    
            logger.debug(f"Mapped {len(variation_descriptors)} variation descriptors")
            return variation_descriptors
                
        except Exception as e:
            logger.error(f"Error mapping variation descriptors: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return {}
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> list:
        """
        Map data to multiple VariationDescriptor entities.
        
        Note: This method is required by the BaseMapper interface but not directly used
        for VariationDescriptorMapper, which returns a dictionary instead.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (list): List of instruments for field access
            **kwargs: Additional mapping parameters
            
        Returns:
            list: Empty list as this mapper doesn't return a list of entities
        """
        logger.warning("VariationDescriptorMapper._map_multi_entity called, but this mapper returns a dictionary")
        return []
        
    def map(self, data: Dict[str, Any], **kwargs) -> Dict[str, VariationDescriptor]:
        """
        Override the base map method to ensure we always return a dictionary.
        
        Args:
            data (Dict[str, Any]): Input data to map
            **kwargs: Additional mapping parameters
            
        Returns:
            Dict[str, VariationDescriptor]: Dictionary of mapped VariationDescriptor entities
        """
        result = super().map(data, **kwargs)
        
        # If the result is None (on error), return an empty dict
        if result is None:
            return {}
            
        return result
    
    def _map_variation_descriptor(self, variation_data: Dict[str, Any], instance_id: str) -> Optional[VariationDescriptor]:
        """
        Map a single variation element to a VariationDescriptor.
        
        Args:
            variation_data (Dict[str, Any]): Genetic findings data
            instance_id (str): The redcap_repeat_instance
            
        Returns:
            Optional[VariationDescriptor]: Mapped VariationDescriptor or None on failure
        """
        try:
            # Generate a unique ID
            descriptor_id = self.processor.generate_unique_id()
            
            # Extract expressions
            expressions = self._extract_expressions(variation_data)
            
            # Extract allelic state
            allelic_state = self._extract_allelic_state(variation_data)
            
            # Extract structural type
            structural_type = self._extract_structural_type(variation_data)
            
            # Extract gene context
            gene_context = self._extract_gene_context(variation_data)
            
            # Extract extensions
            extensions = self._extract_extensions(variation_data)
            
            # Create the VariationDescriptor
            return VariationDescriptor(
                id=descriptor_id,
                expressions=expressions,
                allelic_state=allelic_state,
                structural_type=structural_type,
                gene_context=gene_context,
                extensions=extensions
            )
            
        except Exception as e:
            logger.error(f"Error mapping variation descriptor for instance {instance_id}: {e}")
            return None
    
    def _extract_expressions(self, variation_data: Dict[str, Any]) -> list:
        """Extract expression values from variation data"""
        expressions = []
        
        # Check each expression field
        for field_key in ["expression_field_1", "expression_field_2", "expression_field_3"]:
            field_path = self.processor.mapping_config.get(field_key)
            if not field_path:
                continue
                
            value = variation_data.get(field_path)
            if value:
                expressions.append(Expression(syntax="hgvs", value=value))
                
        return expressions
    
    def _extract_allelic_state(self, variation_data: Dict[str, Any]) -> Optional[OntologyClass]:
        """Extract allelic state from variation data"""
        # Get field paths from configuration
        primary_field = self.processor.mapping_config.get("allelic_state_field_1")
        alt_field = self.processor.mapping_config.get("allelic_state_field_2")
        
        if not primary_field:
            return None
            
        # Get primary field value
        primary_value = variation_data.get(primary_field)
        if not primary_value:
            return None
            
        # Check if we should use the alternative field
        allelic_state_id = primary_value
        if primary_value == "loinc_48019_4_other" and alt_field:
            alt_value = variation_data.get(alt_field)
            if alt_value:
                allelic_state_id = alt_value
        
        # Get label
        allelic_state_label = (
            self.fetch_label(allelic_state_id, enum_class="Zygosity") or
            self.fetch_label(allelic_state_id) or
            "Unknown Allelic State"
        )
        
        # Process ID
        processed_id = self.process_code(allelic_state_id)
        
        return OntologyClass(
            id=processed_id,
            label=allelic_state_label
        )
    
    def _extract_structural_type(self, variation_data: Dict[str, Any]) -> Optional[OntologyClass]:
        """Extract structural type from variation data"""
        # Get field paths from configuration
        primary_field = self.processor.mapping_config.get("structural_type_field_1")
        alt_field = self.processor.mapping_config.get("structural_type_field_2")
        
        if not primary_field:
            return None
            
        # Get primary field value
        primary_value = variation_data.get(primary_field)
        if not primary_value:
            return None
            
        # Check if we should use the alternative field
        structural_type_id = primary_value
        if primary_value == "loinc_48019_4_other" and alt_field:
            alt_value = variation_data.get(alt_field)
            if alt_value:
                structural_type_id = alt_value
        
        # Get label
        structural_type_label = (
            self.fetch_label(structural_type_id, enum_class="DNAChangeType") or
            self.fetch_label(structural_type_id) or
            "Unknown Structural Type"
        )
        
        # Process ID
        processed_id = self.process_code(structural_type_id)
        
        return OntologyClass(
            id=processed_id,
            label=structural_type_label
        )
    
    def _extract_gene_context(self, variation_data: Dict[str, Any]) -> Optional[GeneDescriptor]:
        """Extract gene context from variation data"""
        field = self.processor.mapping_config.get("value_id_field")
        if not field:
            return None
            
        value_id_string = variation_data.get(field)
        if not value_id_string:
            return None
            
        # Normalize HGNC ID
        value_id = self.processor.normalize_hgnc_id(value_id_string)
        if not value_id:
            return None
            
        # Get gene symbol
        symbol = self.fetch_label(value_id)
        
        return GeneDescriptor(
            value_id=value_id,
            symbol=symbol
        )
    
    def _extract_extensions(self, variation_data: Dict[str, Any]) -> Optional[list]:
        """Extract extensions from variation data"""
        field = self.processor.mapping_config.get("expression_string_field")
        if not field:
            return None
            
        value = variation_data.get(field)
        if not value:
            return None
            
        return [Extension(
            name="Unvalidated Genetic Mutation String",
            value=value
        )]