# src/rarelink/phenopackets/mappings/utils/mapping_config.py
from typing import Any, Dict, List, Union
import logging

logger = logging.getLogger(__name__)

class MappingConfig:
    """
    Class to handle all mapping configuration needs for the RareLink-Phenopackets engine.
    Provides standardized methods for accessing configuration values.
    """

    def __init__(self, config_dict: Dict[str, Any] = None):
        """
        Initialize with a configuration dictionary.
        
        Args:
            config_dict (Dict[str, Any], optional): Configuration dictionary
        """
        self.config = config_dict or {}
    
    def get_field_path(self, field_name: str, default: Any = None) -> Any:
        """
        Get a field path from the config.
        
        Args:
            field_name (str): Name of the field in the configuration
            default (Any, optional): Default value if field not found
            
        Returns:
            Any: Field path or default
        """
        return self.config.get(field_name, default)
    
    def get_mapping_block(self, block_name: str = "mapping_block", default: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Get a mapping block from the config.
        
        Args:
            block_name (str, optional): Name of the block, defaults to "mapping_block"
            default (Dict[str, Any], optional): Default value if block not found
            
        Returns:
            Dict[str, Any]: Mapping block or default
        """
        return self.config.get(block_name, default or {})
    
    def get_enum_classes(self, default: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Get enum classes from the config.
        
        Args:
            default (Dict[str, Any], optional): Default value if enum classes not found
            
        Returns:
            Dict[str, Any]: Enum classes or default
        """
        return self.config.get("enum_classes", default or {})
    
    def get_instruments(self) -> List[str]:
        """
        Get all instruments from the config.
        
        Returns:
            List[str]: List of instrument names
        """
        instruments = set()

        # Add instrument_name
        instrument_name = self.config.get("instrument_name")
        if isinstance(instrument_name, (list, set)):
            instruments.update(list(instrument_name))
        elif instrument_name:
            instruments.add(instrument_name)

        # Add redcap_repeat_instrument
        repeat_instrument = self.config.get("redcap_repeat_instrument")
        if repeat_instrument:
            instruments.add(repeat_instrument)
            
        # Add additional_instruments if present
        additional_instruments = self.config.get("additional_instruments", [])
        if additional_instruments:
            instruments.update(additional_instruments)

        # Filter out dummy instruments
        return [i for i in instruments if i and i != "__dummy__"]
    
    def is_multi_entity(self) -> bool:
        """
        Check if this configuration is for multiple entities.
        
        Returns:
            bool: True if multi-entity, False otherwise
        """
        return self.config.get("multi_entity", False)
    
    def update(self, updates: Dict[str, Any]) -> None:
        """
        Update the configuration with new values.
        
        Args:
            updates (Dict[str, Any]): Dictionary of updates
        """
        self.config.update(updates)
    
    def copy(self) -> 'MappingConfig':
        """
        Create a copy of this configuration.
        
        Returns:
            MappingConfig: Copy of this configuration
        """
        return MappingConfig({k: v for k, v in self.config.items()})
    
    def merge(self, other: Union[Dict[str, Any], 'MappingConfig']) -> 'MappingConfig':
        """
        Merge this configuration with another.
        
        Args:
            other (Union[Dict[str, Any], MappingConfig]): Configuration to merge with
            
        Returns:
            MappingConfig: New merged configuration
        """
        # Handle case where other is a MappingConfig
        if isinstance(other, MappingConfig):
            other_dict = other.config
        else:
            other_dict = other
            
        # Create a new configuration with merged values
        merged = self.copy()
        
        # Merge dictionaries with special handling for certain keys
        for key, value in other_dict.items():
            if key in merged.config and isinstance(merged.config[key], dict) and isinstance(value, dict):
                # Merge dictionaries
                merged.config[key] = {**merged.config[key], **value}
            elif key in merged.config and isinstance(merged.config[key], list) and isinstance(value, list):
                # Extend lists
                merged.config[key] = merged.config[key] + value
            elif key in merged.config and isinstance(merged.config[key], set) and (isinstance(value, set) or isinstance(value, list)):
                # Union sets
                merged.config[key] = merged.config[key].union(set(value))
            else:
                # Override other values
                merged.config[key] = value
                
        return merged