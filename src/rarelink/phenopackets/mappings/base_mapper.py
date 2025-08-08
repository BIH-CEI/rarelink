# src/rarelink/phenopackets/mappings/base_mapper.py
import logging
from typing import Any, Dict, List, Optional, TypeVar, Generic, Callable, Union
from rarelink.utils.processor import DataProcessor
from rarelink.utils.field_access import get_multi_instrument_field_value

# Define type variable for the return type of mappers
T = TypeVar('T')

logger = logging.getLogger(__name__)

class BaseMapper(Generic[T]):
    """
    Base class for all mappers in the RareLink-Phenopackets engine.
    Provides common functionality for field access, error handling, and entity creation.
    
    Type parameter T represents the type of entity this mapper creates.
    """
    
    def __init__(self, processor: DataProcessor):
        """
        Initialize the mapper with a data processor.
        
        Args:
            processor (DataProcessor): Processor for field access and data manipulation
        """
        self.processor = processor
        self.debug_mode = getattr(processor, 'debug_mode', False)
    
    def map(self, data: Dict[str, Any], **kwargs) -> Union[List[T], T, None]:
        """
        Map data to one or more entities of type T.
        
        Args:
            data (Dict[str, Any]): Input data to map
            **kwargs: Additional mapping parameters
            
        Returns:
            Union[List[T], T, None]: Mapped entity or list of entities or None on failure
        """
        try:
            # Extract mapping configuration from processor
            config = self.processor.mapping_config
            
            # Determine if this is a single or multi-entity mapper
            is_multi = config.get("multi_entity", False)
            
            # Extract instruments for field access
            instruments = self._get_instruments(config)
            
            # Store the instruments in the processor for field access
            if instruments:
                config["all_instruments"] = instruments
            
            # Map based on single or multi-entity configuration
            if is_multi:
                result = self._map_multi_entity(data, instruments, **kwargs)
                if result is None:
                    return []
                return result
            else:
                return self._map_single_entity(data, instruments, **kwargs)
                
        except Exception as e:
            logger.error(f"Error in {self.__class__.__name__}.map: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            # Return empty list for multi-entity mappers, None for single-entity mappers
            return [] if config.get("multi_entity", False) else None
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> Optional[T]:
        """
        Map data to a single entity. Override in subclasses.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (List[str]): List of instruments for field access
            **kwargs: Additional mapping parameters
            
        Returns:
            Optional[T]: Mapped entity or None on failure
        """
        raise NotImplementedError("Subclasses must implement _map_single_entity")
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> List[T]:
        """
        Map data to multiple entities. Override in subclasses.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (List[str]): List of instruments for field access
            **kwargs: Additional mapping parameters
            
        Returns:
            List[T]: List of mapped entities
        """
        raise NotImplementedError("Subclasses must implement _map_multi_entity")
    
    def get_field(self, 
                  data: Dict[str, Any], 
                  field_name: str, 
                  instruments: List[str] = None, 
                  default: Any = None) -> Any:
        """
        Get a field value from data using the field name from the mapping configuration.
        
        Args:
            data (Dict[str, Any]): Input data to extract from
            field_name (str): Name of the field in the mapping configuration
            instruments (List[str], optional): List of instruments for field access
            default (Any, optional): Default value if field not found
            
        Returns:
            Any: Field value or default
        """
        # Get the field path from the configuration
        field_path = self.processor.mapping_config.get(field_name)
        if not field_path:
            if self.debug_mode:
                logger.debug(f"Field '{field_name}' not found in mapping config")
            return default
        
        # Use multi-instrument field access if instruments provided
        if instruments:
            value = get_multi_instrument_field_value(
                data=data,
                instruments=instruments,
                field_paths=[field_path],
                default_value=default
            )
            if value is not None:
                return value
        
        # Fallback to processor's get_field method
        return self.processor.get_field(data, field_name, default)
    
    def safe_execute(self, 
                    func: Callable, 
                    error_msg: str, 
                    debug: bool = None, 
                    default_return: Any = None, 
                    **kwargs) -> Any:
        """
        Execute a function safely with standardized error handling.
        
        Args:
            func (Callable): Function to execute
            error_msg (str): Message to log on error
            debug (bool, optional): Whether to log debug info, defaults to self.debug_mode
            default_return (Any, optional): Value to return on error
            **kwargs: Arguments to pass to func
            
        Returns:
            Any: Function result or default_return on error
        """
        debug = self.debug_mode if debug is None else debug
        
        try:
            return func(**kwargs)
        except Exception as e:
            logger.error(f"{error_msg}: {e}")
            if debug:
                import traceback
                logger.debug(traceback.format_exc())
            return default_return
    
    def process_code(self, code: str) -> str:
        """Process a code using the processor"""
        return self.processor.process_code(code)
    
    def fetch_label(self, code: str, enum_class: Any = None) -> Optional[str]:
        """
        Fetch a label for a code using a hierarchical approach.
        
        Args:
            code (str): The code to look up
            enum_class (Any, optional): Enum class name (string) or actual enum class
            
        Returns:
            Optional[str]: The label or None if not found
        """
        if not code:
            return None
        
        # Get mapping configuration
        mapping_config = self.processor.mapping_config or {}
        
        # Step 1: Try label dictionaries from the configuration
        label_dicts = mapping_config.get("label_dicts", {})
        if label_dicts:
            # First, check if enum_class is a string that matches a dictionary name
            if isinstance(enum_class, str) and enum_class in label_dicts:
                specific_dict = label_dicts.get(enum_class, {})
                if code in specific_dict:
                    return specific_dict[code]
            
            # Next, try looking through all dictionaries
            for dict_name, label_dict in label_dicts.items():
                if code in label_dict:
                    return label_dict[code]
        
        # Step 2: Try enum classes from configuration
        enum_classes = getattr(self.processor, "enum_classes", {})
        if enum_classes:
            # If enum_class is provided as a string, get the actual class
            if isinstance(enum_class, str) and enum_class in enum_classes:
                enum_obj = enum_classes[enum_class]
                label = self.processor.fetch_label_from_enum(code, enum_obj)
                if label:
                    return label
                
            # If enum_class is provided as an actual class
            elif enum_class:
                label = self.processor.fetch_label_from_enum(code, enum_class)
                if label:
                    return label
                
            # Try prefix-based enum lookup 
            for prefix, enum_obj in enum_classes.items():
                if code.startswith(prefix):
                    label = self.processor.fetch_label_from_enum(code, enum_obj)
                    if label:
                        return label
        
        # Step 3: Finally, try BioPortal (most expensive option)
        # For codes with a colon format
        if ":" in code:
            label = self.processor.fetch_label_from_bioportal(code)
            if label:
                return label
        
        # For codes without a colon, try processing first
        else:
            processed_code = self.process_code(code)
            if processed_code != code and ":" in processed_code:
                label = self.processor.fetch_label_from_bioportal(processed_code)
                if label:
                    return label
        
        # Return None if no label found
        return None
    
    def fetch_mapping_value(self, mapping_name: str, code: str, default: Any = None) -> Any:
        """Fetch a mapping value using the processor"""
        return self.processor.fetch_mapping_value(mapping_name, code, default)
    
    def _get_instruments(self, config: Dict[str, Any] = None) -> List[str]:
        """
        Get instruments from the mapping configuration.
        
        Args:
            config (Dict[str, Any], optional): Mapping configuration, defaults to processor's config
            
        Returns:
            List[str]: List of instrument names
        """
        config = config or self.processor.mapping_config
        instruments = []
        
        # Get instrument_name(s)
        instrument_name = config.get("instrument_name")
        if isinstance(instrument_name, (list, set)):
            instruments.extend(list(instrument_name))
        elif instrument_name:
            instruments.append(instrument_name)
        
        # Add redcap_repeat_instrument if present
        repeat_instrument = config.get("redcap_repeat_instrument")
        if repeat_instrument and repeat_instrument not in instruments:
            instruments.append(repeat_instrument)
        
        # Filter out dummy instruments
        return [i for i in instruments if i and i != "__dummy__"]
    
    def map_genetics_to_geno_ontology(self, 
                             data: Dict[str, Any], 
                             instruments: List[str]) -> Optional[T]:
        """
        Map genetic data to a GENO ontology for Phenopacket-Analaysis tools.
        
        Args:
            data (Dict[str, Any]): Input genetic data
            instruments (List[str]): List of instruments for field access
            
        Returns:
            Optional[T]: Mapped genotype entity or None on failure
        """
        raise NotImplementedError("Subclasses must implement map_loinc_to_geno_ontology")