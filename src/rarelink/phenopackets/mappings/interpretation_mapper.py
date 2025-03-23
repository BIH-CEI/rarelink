from typing import Dict, Any, Optional, List, Union
import logging
from phenopackets import (
    Interpretation,
    OntologyClass,
    Diagnosis,
    GenomicInterpretation,
    VariantInterpretation,
    VariationDescriptor
)

from rarelink.phenopackets.mappings.base_mapper import BaseMapper

logger = logging.getLogger(__name__)

class InterpretationMapper(BaseMapper[Interpretation]):
    """
    Mapper for Interpretation entities in the Phenopacket schema.
    Maps interpretation details, including genomic interpretations grouped by diagnosis.
    """
    
    def map(self, data: Dict[str, Any], **kwargs) -> Union[List[Interpretation], None]:
        """
        Override the base map method to specify multi_entity mode.
        
        Args:
            data (Dict[str, Any]): Input data to map
            **kwargs: Additional mapping parameters
                - subject_id (str): The subject or biosample ID
                - variation_descriptors (Dict[str, VariationDescriptor]): Dictionary of
                                                                          variation descriptors
            
        Returns:
            Union[List[Interpretation], None]: List of mapped Interpretation entities or None on failure
        """
        # Set multi_entity to True to ensure _map_multi_entity is called
        self.processor.mapping_config["multi_entity"] = True
        
        # Call the base map method which will call _map_multi_entity
        return super().map(data, **kwargs)
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> Optional[Interpretation]:
        """
        Map data to a single Interpretation entity.
        
        This method should never be called directly since we're always returning
        multiple entities, but we need to implement it to satisfy the BaseMapper interface.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (list): List of instruments for field access
            **kwargs: Additional mapping parameters
                - subject_id (str): The subject or biosample ID
                - variation_descriptors (Dict[str, VariationDescriptor]): Dictionary of
                                                                          variation descriptors
            
        Returns:
            Optional[Interpretation]: None as this mapper always returns multiple entities
        """
        logger.warning("InterpretationMapper._map_single_entity called, but this mapper returns multiple entities")
        return None
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> List[Interpretation]:
        try:
            # Extract required parameters
            subject_id = kwargs.get('subject_id')
            # Instead of aborting if variation_descriptors is empty,
            # we simply set it to an empty dict.
            variation_descriptors = kwargs.get('variation_descriptors', {})

            # Validate required subject_id
            if not subject_id:
                logger.error("Subject ID is required for interpretation mapping")
                return []

            # Add this check right here to return empty list if no variation descriptors
            if not variation_descriptors:
                logger.warning("No variation descriptors provided, cannot create interpretations")
                return []
            
            # Get instrument name from configuration or instruments list
            instrument_name = self.processor.mapping_config.get("redcap_repeat_instrument")
            if not instrument_name and instruments:
                instrument_name = instruments[0]

            if not instrument_name:
                logger.warning("No instrument name found for interpretation mapping")
                return []

            # Find repeated elements for the specified instrument
            repeated_elements = data.get("repeated_elements", [])
            if not repeated_elements:
                logger.warning("No repeated elements found in the data")
                return []

            # Filter elements for the target instrument
            interpretation_elements = [
                element for element in repeated_elements
                if element.get("redcap_repeat_instrument") == instrument_name
            ]

            if not interpretation_elements:
                logger.warning(f"No elements found for instrument {instrument_name}")
                return []

            # Group interpretations by diagnosis using the provided (or empty) variation descriptors
            interpretation_groups = self._group_by_diagnosis(
                interpretation_elements,
                subject_id,
                variation_descriptors
            )

            # Build interpretations from groups
            interpretations = [
                Interpretation(
                    id=f"{subject_id}-interpretation-{i}",
                    progress_status=group["progress_status"],
                    diagnosis=group["diagnosis"]
                )
                for i, group in enumerate(interpretation_groups.values())
            ]

            logger.debug(f"Mapped {len(interpretations)} interpretations")
            return interpretations

        except Exception as e:
            logger.error(f"Error mapping interpretations: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return []

        
    def _group_by_diagnosis(
        self, 
        elements: List[Dict[str, Any]], 
        subject_id: str, 
        variation_descriptors: Dict[str, VariationDescriptor]
    ) -> Dict[str, Dict[str, Any]]:
        """
        Group interpretation elements by diagnosis.
        
        Args:
            elements (List[Dict[str, Any]]): Interpretation elements
            subject_id (str): The subject or biosample ID
            variation_descriptors (Dict[str, VariationDescriptor]): Dictionary of variation descriptors
            
        Returns:
            Dict[str, Dict[str, Any]]: Dictionary of grouped interpretations
        """
        interpretation_groups = {}
        
        for element in elements:
            # Get the genetic findings data
            genetic_data = element.get("genetic_findings")
            if not genetic_data:
                logger.warning("No interpretation data found in this element")
                continue
                
            # Genomic Diagnosis
            diagnosis_id = self._extract_diagnosis_id(genetic_data)
            if not diagnosis_id:
                logger.warning("No diagnosis ID found in element")
                continue
                
            # Progress Status
            progress_status = self._extract_progress_status(genetic_data)
            
            # Initialize the group if it doesn't exist
            if diagnosis_id not in interpretation_groups:
                # Get the diagnosis label
                diagnosis_label = self.fetch_label(diagnosis_id) or "Unknown Diagnosis"
                
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
                
            # Extract redcap_repeat_instance
            instance_id = element.get("redcap_repeat_instance")
            if not instance_id:
                logger.warning("No redcap_repeat_instance found in element")
                continue
                
            # Check if this instance already exists in the group
            existing_instances = [
                gi.subject_or_biosample_id 
                for gi in interpretation_groups[diagnosis_id]["diagnosis"].genomic_interpretations
            ]
            if str(instance_id) in existing_instances:
                logger.debug(f"Instance {instance_id} already exists in group {diagnosis_id}")
                continue
                
            # Get the variation descriptor for this instance
            variation_descriptor = variation_descriptors.get(instance_id)
            if not variation_descriptor:
                logger.warning(f"No variation descriptor found for instance {instance_id}")
                continue
                
            # Create genomic interpretation
            genomic_interpretation = self._create_genomic_interpretation(
                genetic_data, 
                subject_id, 
                instance_id, 
                variation_descriptor
            )
            
            if genomic_interpretation:
                interpretation_groups[diagnosis_id]["diagnosis"].genomic_interpretations.append(
                    genomic_interpretation
                )
                
        return interpretation_groups
    
    def _extract_diagnosis_id(self, genetic_data: Dict[str, Any]) -> Optional[str]:
        """
        Extract the diagnosis ID from genetic data.
        
        Args:
            genetic_data (Dict[str, Any]): Genetic findings data
            
        Returns:
            Optional[str]: Diagnosis ID or None if not found
        """
        # Try each diagnosis field in order
        for field_key in ["diagnosis_field_1", "diagnosis_field_2", "diagnosis_field_3"]:
            field_path = self.processor.mapping_config.get(field_key)
            if not field_path:
                continue
                
            value = genetic_data.get(field_path)
            if value:
                return self.process_code(value)
                
        return None
    
    def _extract_progress_status(self, genetic_data: Dict[str, Any]) -> str:
        """
        Extract the progress status from genetic data.
        
        Args:
            genetic_data (Dict[str, Any]): Genetic findings data
            
        Returns:
            str: Progress status or "UNKNOWN_PROGRESS" if not found
        """
        field_path = self.processor.mapping_config.get("progress_status_field")
        if not field_path:
            return "UNKNOWN_PROGRESS"
            
        value = genetic_data.get(field_path)
        if value:
            return self.fetch_mapping_value("map_progress_status", value) or "UNKNOWN_PROGRESS"
            
        return "UNKNOWN_PROGRESS"
    
    def _create_genomic_interpretation(
        self, 
        genetic_data: Dict[str, Any], 
        subject_id: str, 
        instance_id: str, 
        variation_descriptor: VariationDescriptor
    ) -> Optional[GenomicInterpretation]:
        """
        Create a genomic interpretation from genetic data.
        
        Args:
            genetic_data (Dict[str, Any]): Genetic findings data
            subject_id (str): The subject or biosample ID
            instance_id (str): The redcap_repeat_instance
            variation_descriptor (VariationDescriptor): Variation descriptor
            
        Returns:
            Optional[GenomicInterpretation]: Genomic interpretation or None on failure
        """
        try:
            # Create variant interpretation
            variant_interpretation = self._create_variant_interpretation(
                genetic_data, 
                variation_descriptor
            )
            
            if not variant_interpretation:
                return None
                
            # Get interpretation status
            status_field = self.processor.mapping_config.get("interpretation_status_field")
            status_value = genetic_data.get(status_field) if status_field else None
            interpretation_status = (
                self.fetch_mapping_value("map_interpretation_status", status_value)
                if status_value else "UNKNOWN_STATUS"
            )
            
            # Create genomic interpretation
            return GenomicInterpretation(
                subject_or_biosample_id=str(instance_id),  # Using instance_id to maintain uniqueness
                interpretation_status=interpretation_status,
                variant_interpretation=variant_interpretation
            )
            
        except Exception as e:
            logger.error(f"Error creating genomic interpretation: {e}")
            return None
    
    def _create_variant_interpretation(
        self, 
        genetic_data: Dict[str, Any], 
        variation_descriptor: VariationDescriptor
    ) -> Optional[VariantInterpretation]:
        """
        Create a variant interpretation from genetic data.
        
        Args:
            genetic_data (Dict[str, Any]): Genetic findings data
            variation_descriptor (VariationDescriptor): Variation descriptor
            
        Returns:
            Optional[VariantInterpretation]: Variant interpretation or None on failure
        """
        try:
            # Get ACMG classification
            acmg_field = self.processor.mapping_config.get("acmg_pathogenicity_classification_field")
            acmg_value = genetic_data.get(acmg_field) if acmg_field else None
            acmg_classification = (
                self.fetch_mapping_value("map_acmg_classification", acmg_value)
                if acmg_value else "NOT_PROVIDED"
            )
            
            # Get therapeutic actionability
            action_field = self.processor.mapping_config.get("therapeutic_actionability_field")
            action_value = genetic_data.get(action_field) if action_field else None
            therapeutic_actionability = (
                self.fetch_mapping_value("map_therapeutic_actionability", action_value)
                if action_value else "UNKNOWN_ACTIONABILITY"
            )
            
            # Create variant interpretation
            return VariantInterpretation(
                acmg_pathogenicity_classification=acmg_classification,
                therapeutic_actionability=therapeutic_actionability,
                variation_descriptor=variation_descriptor
            )
            
        except Exception as e:
            logger.error(f"Error creating variant interpretation: {e}")
            return None