# processor.py
from typing import Any, Dict, List, Optional, Union
import logging
import uuid
import importlib
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

from ..field_access import get_field_value, get_multi_instrument_field_value
from ..code_processing import process_code, normalize_hgnc_id
from ..label_fetching import (
    fetch_label, 
    fetch_label_from_enum, 
    fetch_label_from_dict, 
    fetch_label_from_bioportal
)
from ..date_handling import convert_date_to_iso_age, date_to_timestamp
from rarelink_cdm import import_from_latest

logger = logging.getLogger(__name__)

class DataProcessor:
    """
    Data processor for phenopacket mapping that delegates to utility functions.
    """
    
    def __init__(self, mapping_config: Dict[str, Any]):
        self.mapping_config = mapping_config or {}
        self.debug_mode = False
        self.enum_classes = {}
    
    def enable_debug(self, enabled: bool = True) -> None:
        """Enable debug mode for verbose logging"""
        self.debug_mode = enabled
    
    def get_field(self, 
                 data: Dict[str, Any], 
                 field_name: str, 
                 default_value: Any = None) -> Any:
        """Get a field value using the mapping configuration"""
        field_path = self.mapping_config.get(field_name)
        if not field_path:
            if self.debug_mode:
                logger.debug(f"Field '{field_name}' not found in mapping config")
            return default_value
        
        return get_field_value(data, field_path, default_value)
    
    def get_multi_instrument_field(self,
                                  data: Dict[str, Any],
                                  field_name: str,
                                  default_value: Any = None) -> Any:
        """Get a field value across multiple instruments"""
        field_path = self.mapping_config.get(field_name)
        if not field_path:
            if self.debug_mode:
                logger.debug(f"Field '{field_name}' not found in mapping config")
            return default_value
        
        # Get instruments from config
        instruments = self._get_instruments()
        if not instruments:
            if self.debug_mode:
                logger.debug("No instruments found in mapping config")
            return get_field_value(data, field_path, default_value)
        
        return get_multi_instrument_field_value(
            data, instruments, [field_path], default_value)
    
    def _get_instruments(self) -> List[str]:
        """Get instruments from mapping config"""
        instruments = []
        
        # Get instrument_name(s)
        instrument_name = self.mapping_config.get("instrument_name")
        if isinstance(instrument_name, (list, set)):
            instruments.extend(list(instrument_name))
        elif instrument_name:
            instruments.append(instrument_name)
        
        # Add redcap_repeat_instrument if present
        repeat_instrument = self.mapping_config.get("redcap_repeat_instrument")
        if repeat_instrument and repeat_instrument not in instruments:
            instruments.append(repeat_instrument)
        
        return instruments
    
    def process_code(self, code: str) -> Optional[str]:
        """Process a code to standard ontology format"""
        return process_code(code)
    
    def normalize_hgnc_id(self, value: str) -> str:
        """Normalize an HGNC identifier"""
        return normalize_hgnc_id(value)
    
    def fetch_label(self, code: str, enum_class: Any = None) -> Optional[str]:
        """Fetch a label for a code"""
        if not code:
            return None
        
        # If enum_class is a string, try to get the actual class
        if isinstance(enum_class, str) and enum_class in self.enum_classes:
            enum_obj = self.enum_classes[enum_class]
        else:
            enum_obj = enum_class
        
        # Try hierarchical label fetching with enum class
        return fetch_label(code, enum_obj)
    
    def fetch_label_from_enum(self, code: str, enum_class) -> Optional[str]:
        """Fetch a label from an enum class"""
        return fetch_label_from_enum(code, enum_class)
    
    def fetch_label_from_dict(self, code: str, label_dict: Dict[str, str]) -> Optional[str]:
        """Fetch a label from a dictionary"""
        return fetch_label_from_dict(code, label_dict)
    
    def fetch_label_from_bioportal(self, code: str) -> Optional[str]:
        """Fetch a label from BioPortal API"""
        return fetch_label_from_bioportal(code)
    
    def add_enum_class(self, prefix: str, enum_class_or_path) -> None:
        """Add an enum class for label lookups"""
        if not enum_class_or_path:
            return
        
        if isinstance(enum_class_or_path, str):
            # Import the class from the path
            try:
                module_path, class_name = enum_class_or_path.rsplit('.', 1)
                module = importlib.import_module(module_path)
                enum_class = getattr(module, class_name)
                self.enum_classes[prefix] = enum_class
            except Exception as e:
                logger.error(f"Failed to import enum class: {e}")
        else:
            # Use the provided class directly
            self.enum_classes[prefix] = enum_class_or_path
    
    def fetch_mapping_value(
        self,
        mapping_name: str,
        code: str,
        default_value: Any = None
    ) -> Any:
        """Fetch a mapping value from the latest rarelink_cdm version."""
        if not code:
            return default_value

        try:
            mod = import_from_latest("mappings.phenopackets.mapping_dicts")
            get_mapping_by_name = getattr(mod, "get_mapping_by_name")
            mapping = get_mapping_by_name(mapping_name)
            return mapping.get(code, default_value)
        except Exception as e:
            if self.debug_mode:
                logger.error(f"Error fetching mapping value: {e}")
            return default_value
    
    def convert_date_to_iso_age(self, 
                              event_date: Union[str, datetime], 
                              dob: Union[str, datetime]) -> Optional[str]:
        """Convert dates to ISO8601 duration string"""
        return convert_date_to_iso_age(event_date, dob)
    
    def date_to_timestamp(self, 
                        date_input: Union[str, datetime]) -> Optional[Timestamp]:
        """Convert a date to a Protobuf Timestamp"""
        return date_to_timestamp(date_input)
    
    @staticmethod
    def generate_unique_id(length: int = 30) -> str:
        """Generate a unique ID"""
        return uuid.uuid4().hex[:length]