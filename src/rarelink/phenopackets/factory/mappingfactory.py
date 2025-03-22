"""
Phenopacket Mapping Factory

This module provides a generic factory for creating phenopacket mappings
that work across different data models (RareLink CDM, CIEINR, etc.)
"""

from typing import Dict, Any
import importlib
import logging

logger = logging.getLogger(__name__)

class PhenopacketMappingFactory:
    """
    Factory class for creating phenopacket mappings for different data models.
    """
    
    @staticmethod
    def create_for_model(model_name: str, **kwargs) -> Dict[str, Any]:
        """
        Create phenopacket mappings for a specific data model.
        
        Args:
            model_name (str): Name of the data model (e.g., 'rarelink_cdm', 'cieinr')
            **kwargs: Additional arguments to pass to the model-specific builder
            
        Returns:
            Dict[str, Any]: Phenopacket mappings for the specified model
        """
        try:
            # Try to import the model-specific module
            module_path = f"{model_name}.v1_0_0.mappings.phenopackets.combined"
            mapping_module = importlib.import_module(module_path)
            
            # Check if the module has the expected function
            if hasattr(mapping_module, 'create_phenopacket_mappings'):
                return mapping_module.create_phenopacket_mappings(**kwargs)
            else:
                logger.warning(f"Module {module_path} does not have create_phenopacket_mappings function")
                
                # Fall back to rarelink_cdm if available
                try:
                    from rarelink_cdm.v2_0_0_dev1.mappings.phenopackets.combined import create_rarelink_phenopacket_mappings
                    logger.info("Falling back to rarelink_cdm mappings")
                    return create_rarelink_phenopacket_mappings()
                except ImportError:
                    logger.error("Failed to import fallback rarelink_cdm mappings")
                    raise
                    
        except ImportError:
            logger.warning(f"Could not import model-specific module for {model_name}")
            
            # Try fallback to rarelink_cdm
            try:
                from rarelink_cdm.v2_0_0_dev1.mappings.phenopackets.combined import create_rarelink_phenopacket_mappings
                logger.info("Using fallback rarelink_cdm mappings")
                return create_rarelink_phenopacket_mappings()
            except ImportError:
                logger.error("Failed to import fallback rarelink_cdm mappings")
                raise
    
    @staticmethod
    def convert_to_multi_instrument_format(
        config: Dict[str, Any], 
        block_name: str = "phenotypicFeatures"
    ) -> Dict[str, Any]:
        """
        Convert a single-instrument block configuration to a multi-instrument format.
        This helps maintain backward compatibility with code expecting the newer format.
        
        Args:
            config (Dict[str, Any]): Original mapping configuration
            block_name (str): Name of the block to convert (default: "phenotypicFeatures")
            
        Returns:
            Dict[str, Any]: Updated configuration with multi-instrument support
        """
        # Create a deep copy to avoid modifying the original
        updated_config = {k: v for k, v in config.items()}
        
        # Check if the block already has the multi-instrument format (list)
        if block_name in updated_config and not isinstance(updated_config[block_name], list):
            # Convert to a single-element list
            updated_config[block_name] = [updated_config[block_name]]
            
        return updated_config
    
    @staticmethod
    def merge_configurations(
        base_config: Dict[str, Any],
        override_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Merge two configurations, with override_config taking precedence.
        This is useful for applying customizations to a base configuration.
        
        Args:
            base_config (Dict[str, Any]): Base configuration
            override_config (Dict[str, Any]): Configuration with overrides
            
        Returns:
            Dict[str, Any]: Merged configuration
        """
        # Start with a copy of the base
        merged = {k: v for k, v in base_config.items()}
        
        # Apply overrides
        for key, value in override_config.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                # Recursively merge dictionaries
                merged[key] = PhenopacketMappingFactory.merge_configurations(merged[key], value)
            elif key in merged and isinstance(merged[key], list) and isinstance(value, list):
                # For lists, append new items
                merged[key] = merged[key] + value
            elif key in merged and isinstance(merged[key], set) and (isinstance(value, set) or isinstance(value, list)):
                # For sets, union them
                merged[key] = merged[key].union(set(value))
            else:
                # Otherwise just override
                merged[key] = value
                
        return merged


# Helper function to get the right mappings for a model
def get_phenopacket_mappings(model_name: str = "rarelink_cdm", **kwargs) -> Dict[str, Any]:
    """
    Get the phenopacket mappings for a specific data model.
    
    Args:
        model_name (str): Name of the data model (e.g., 'rarelink_cdm', 'cieinr')
        **kwargs: Additional arguments to pass to the model-specific builder
        
    Returns:
        Dict[str, Any]: Phenopacket mappings for the specified model
    """
    return PhenopacketMappingFactory.create_for_model(model_name, **kwargs)


# Helper function to get a specific mapping for a block
def get_mapping_for_block(
    block_name: str, 
    mapping_type: str, 
    key: str, 
    mappings: Dict[str, Any] = None,
    model_name: str = "rarelink_cdm"
) -> Dict[str, str]:
    """
    Retrieve a specific mapping or label dictionary from the mappings.
    
    Args:
        block_name (str): Name of the block (e.g., 'individual', 'diseases')
        mapping_type (str): Type of mapping ('label_dicts' or 'mapping_dicts')
        key (str): Specific mapping or label key (e.g., 'map_sex', 'GenderIdentity')
        mappings (Dict[str, Any], optional): Mappings to use
        model_name (str): Data model to use if mappings not provided
        
    Returns:
        Dict[str, str]: The requested mapping or label dictionary
    """
    if mappings is None:
        mappings = get_phenopacket_mappings(model_name)
    
    block_mappings = mappings.get(block_name, {})
    
    # Handle both standard dictionary and list-based block configurations
    if isinstance(block_mappings, list):
        # For list-based configurations, combine all mappings of the requested type
        combined_mappings = {}
        for config in block_mappings:
            if mapping_type in config:
                if isinstance(config[mapping_type], dict) and key in config[mapping_type]:
                    combined_mappings.update(config[mapping_type][key])
        return combined_mappings
    
    # Standard dictionary configuration
    if mapping_type not in block_mappings:
        return {}
    
    return block_mappings[mapping_type].get(key, {})