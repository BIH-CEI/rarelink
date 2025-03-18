# src/rarelink/utils/processor/processor.py
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
import uuid
import importlib
import sys
import json

# Define logger at module level
logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, mapping_config: dict):
        self.mapping_config = mapping_config
        self.debug_mode = False  # Add a debug mode flag
        self.fallback_values = {}  # Store fallback values for missing fields
        self.enum_classes = {}  # Store enum classes for label lookups

    # --------------------------------------
    # Field Fetching Methods
    # --------------------------------------

    def get_field(self, 
                  data: dict, 
                  field_name: str, 
                  highest_redcap_repeat_instance: bool = False,
                  default_value=None):
        """
        Fetches a field value from nested input data based on the
        mapping configuration with improved error handling and fallbacks.

        Args:
            data (dict): Input data dictionary.
            field_name (str): The name of the field to fetch.
            highest_redcap_repeat_instance (bool, optional): Whether to fetch  
                            the value from the highest redcap_repeat_instance.
            default_value: Value to return if field isn't found

        Returns:
            Any: The value of the requested field or default_value if not found.
        """
        # Import here to avoid circular import
        from rarelink.utils.loading import get_nested_field
        
        field_path = self.mapping_config.get(field_name)
        if field_path is None:
            if self.debug_mode:
                logger.warning(f"Field '{field_name}' not found in mapping_config.")
            return default_value

        if self.debug_mode:
            logger.debug(f"Resolving field '{field_name}' with path: {field_path}")
            logger.debug(f"Input data: {data}")

        try:
            # Try direct field access first
            if "." not in field_path and field_path in data:
                return data[field_path]
                
            # Try nested field resolution
            value = get_nested_field(
                data, field_path, highest_redcap_repeat_instance)
                
            if value is None and self.fallback_values.get(field_name):
                return self.fallback_values[field_name]
                
            return value
        except Exception as e:
            if self.debug_mode:
                logger.error(f"Failed to fetch field '{field_name}' with path '{field_path}': {e}")
            return default_value

    def set_fallback_value(self, field_name, value):
        """
        Sets a fallback value for a field if it's not found in the data.
        
        Args:
            field_name (str): The field name to set a fallback for
            value: The fallback value
        """
        self.fallback_values[field_name] = value

    def enable_debug(self, enabled=True):
        """Enable or disable debug mode for verbose logging"""
        self.debug_mode = enabled

    def add_enum_class(self, prefix, enum_class_or_path):
        """
        Add an Enum class for label lookups.
        
        Args:
            prefix (str): The prefix for codes that this enum handles (e.g., 'mondo_')
            enum_class_or_path: Either an actual enum class or a string path to import it
        """
        if enum_class_or_path is None:
            return
            
        if isinstance(enum_class_or_path, str):
            # Try to import the class from the path
            try:
                module_path, class_name = enum_class_or_path.rsplit('.', 1)
                module = importlib.import_module(module_path)
                enum_class = getattr(module, class_name)
                self.enum_classes[prefix] = enum_class
                if self.debug_mode:
                    logger.debug(f"Imported enum class {class_name} for prefix {prefix}")
            except Exception as e:
                logger.error(f"Failed to import enum class from {enum_class_or_path}: {e}")
        else:
            # Directly use the provided class
            self.enum_classes[prefix] = enum_class_or_path
            if self.debug_mode:
                logger.debug(f"Added enum class {enum_class_or_path.__name__} for prefix {prefix}")

    def prefer_non_empty_field(self, data: dict, fields: list, default_value=None):
        """
        Selects the first non-empty field from a list of fields.

        Args:
            data (dict): The input data dictionary.
            fields (list): List of field paths to check.
            default_value: Value to return if all fields are empty

        Returns:
            str: The value of the first non-empty field or default_value if all are empty.
        """
        for field in fields:
            if self.debug_mode:
                logger.debug(f"Attempting to resolve field: {field}")
            value = self.get_field(data, field)
            if isinstance(value, list):  # Handle repeated elements
                for item in value:
                    if item:
                        return item
            elif value:
                return value
        if self.debug_mode:
            logger.warning(f"All fields empty or not found: {fields}")
        return default_value

    # --------------------------------------
    # Data Processing Methods
    # --------------------------------------

    @staticmethod
    def process_date(date_input):
        """
        Converts a date string into a protobuf Timestamp with improved error handling.

        Args:
            date_input: The date string to process (in ISO8601 format) or None.

        Returns:
            Timestamp: A protobuf Timestamp object or None if input is invalid.
        """
        if not date_input:
            return None
            
        try:
            # Handle different date types
            if isinstance(date_input, datetime):
                dt = date_input
            elif isinstance(date_input, str):
                dt = datetime.fromisoformat(date_input.rstrip('Z'))
            else:
                logger.error(f"Unsupported date type: {type(date_input)}")
                return None
                
            # Set the day to "01" to only include year and month
            dt = dt.replace(day=1)
            timestamp = Timestamp()
            timestamp.FromDatetime(dt)
            return timestamp
        except Exception as e:
            logger.error(f"Error converting date to Timestamp: {e}")
            return None
        
    @staticmethod
    def convert_date_to_iso_age(event_date, dob):
        """
        Convert an event date and a date of birth into an ISO8601 duration string
        using only years and months (e.g., "P38Y7M").
        
        Args:
            event_date: The date of the event (e.g., onset), string or datetime
            dob: The individual's date of birth, string or datetime
            
        Returns:
            str: An ISO8601 duration string or None if conversion fails
        """
        if not event_date or not dob:
            return None
            
        try:
            # Convert both dates to datetime objects if they're strings
            if isinstance(dob, str):
                dob_dt = datetime.fromisoformat(dob.rstrip('Z'))
            else:
                dob_dt = dob
                
            if isinstance(event_date, str):
                event_date_dt = datetime.fromisoformat(event_date.rstrip('Z'))
            else:
                event_date_dt = event_date
                
            # Calculate the difference using relativedelta to get years and months
            delta = relativedelta(event_date_dt, dob_dt)
            # Build the ISO8601 duration string with only years and months
            iso_age = f"P{delta.years}Y{delta.months}M"
            return iso_age
        except Exception as e:
            logger.error(f"Error calculating ISO age: {e}")
            return None

    def process_code(self, code: str):
        """
        Processes a code into the expected format with enhanced ontology handling.

        Args:
            code (str): The code to process (e.g., "mondo_0007843").

        Returns:
            str: The processed code (e.g., "MONDO:0007843") or original code if processing fails.
        """
        if not code:
            return None
            
        # Handle common ontology prefix patterns
        patterns = {
            "mondo_": "MONDO:",
            "hp_": "HP:",
            "ncit_": "NCIT:",
            "snomedct_": "SNOMEDCT:",
            "orpha_": "ORPHA:",
            "omim_": "OMIM:",
            "icd10_": "ICD10:",
            "icd11_": "ICD11:",
            "loinc_": "LOINC:"
        }
        
        # Check for direct pattern matches first
        for prefix, replacement in patterns.items():
            if code.lower().startswith(prefix):
                # Extract the number part
                number_part = code[len(prefix):]
                # Return the correctly formatted code
                return f"{replacement}{number_part}"
            
        # If no direct match, try the standard processing
        try:
            # Import here to avoid circular import
            from rarelink.utils.processing.codes import process_redcap_code
            return process_redcap_code(code)
        except Exception as e:
            if self.debug_mode:
                logger.error(f"Error processing code '{code}': {e}")
            return code  # Return original code as fallback

    # --------------------------------------
    # Label and Mapping Methods
    # --------------------------------------

    def fetch_label_from_enum(self, code: str, enum_class):
        """
        Fetch a label from a Python Enum class that follows the LinkML pattern.
        
        Args:
            code (str): The code to look up (e.g., "mondo_0007843")
            enum_class: The enum class to look in
            
        Returns:
            str: The description (label) for the code, or None if not found
        """
        if not code or not enum_class:
            return None
            
        try:
            # Try to get the value as an attribute from the enum
            enum_value = getattr(enum_class, code, None)
            
            if enum_value and hasattr(enum_value, 'description'):
                # Return the description as the label
                if self.debug_mode:
                    logger.debug(f"Found label '{enum_value.description}' for code '{code}' in enum")
                return enum_value.description
                
            # No description found
            return None
        except Exception as e:
            if self.debug_mode:
                logger.error(f"Error fetching label from enum for code '{code}': {e}")
            return None

    def fetch_label(self, code: str, enum_class=None):
        """
        Fetches the label (description) for a given code with enhanced Enum support.

        Args:
            code (str): The code for which to fetch the label.
            enum_class (str or class, optional): Enum class or name for lookups

        Returns:
            str: The label (description) for the code, or None if not found.
        """
        if not code:
            return None
            
        # Case 1: Use specified enum class if provided
        if enum_class:
            if isinstance(enum_class, str):
                # It's the name of an enum class, try to load it from label dict
                return self.load_label(code, enum_class)
            else:
                # It's an actual enum class, use it directly
                return self.fetch_label_from_enum(code, enum_class)
            
        # Case 2: Try to find a matching enum class based on code prefix
        if hasattr(self, "enum_classes"):
            for prefix, enum_class in self.enum_classes.items():
                if code.lower().startswith(prefix.lower()):
                    label = self.fetch_label_from_enum(code, enum_class)
                    if label:
                        return label
        
        # Case 3: Try to fetch through label dictionaries
        try:
            # Import here to avoid circular import
            label = self.load_label(code, None)
            if label:
                return label
        except Exception:
            pass
            
        # Case 4: Try direct API lookup
        try:
            # Import here to avoid circular import
            from rarelink.utils.processing.codes import fetch_label_directly
            
            # Try with original code first
            label = fetch_label_directly(code)
            if label:
                return label
                
            # If that fails, try with processed code
            processed_code = self.process_code(code)
            if processed_code != code:
                return fetch_label_directly(processed_code)
                
            return None
        except Exception as e:
            if self.debug_mode:
                logger.error(f"Error fetching label for code '{code}': {e}")
            return None

    def load_label(self, code: str, enum_class):
        """
        Loads the label for a given code from an EnumDefinition class.

        Args:
            code (str): The code for which to load the label.
            enum_class (EnumDefinitionImpl): The EnumDefinition class to 
            fetch labels from.

        Returns:
            str: The label (description) for the code, or None if not found.
        """
        if not code:
            return None
            
        try:
            # Import here to avoid circular import
            from rarelink.utils.loading import fetch_description_from_label_dict
            return fetch_description_from_label_dict(enum_class, code)
        except KeyError:
            return None
        except Exception as e:
            if self.debug_mode:
                logger.error(f"Error loading label for code '{code}' from enum '{enum_class}': {e}")
            return None
        
    def fetch_mapping_value(self, mapping_name: str, code: str, default_value=None):
        """
        Fetches the mapped value for a code using the specified mapping name,
        with improved error handling.

        Args:
            mapping_name (str): The name of the mapping to use.
            code (str): The code to look up in the mapping.
            default_value: Default value to return if mapping fails

        Returns:
            str | bool | None: The mapped value or default_value if not found.
        """
        if not code:
            return default_value
            
        try:
            # Import here to avoid circular import
            from rarelink_cdm.v2_0_0_dev1.mappings.phenopackets.mapping_dicts import get_mapping_by_name
            mapping = get_mapping_by_name(mapping_name)
            value = mapping.get(code, default_value)
            return value
        except KeyError:
            return default_value
        except Exception as e:
            if self.debug_mode:
                logger.error(f"Error fetching mapping value for code '{code}' with mapping '{mapping_name}': {e}")
            return default_value

    # --------------------------------------
    # Utility Methods
    # --------------------------------------
    
    def dump_data(self, data, label="Data dump"):
        """Debug utility to dump data structure"""
        if self.debug_mode:
            logger.debug(f"--- {label} ---")
            logger.debug(json.dumps(data, indent=2, default=str))
            logger.debug("-------------------")

    # --------------------------------------
    # Generation Methods
    # --------------------------------------
    @staticmethod
    def generate_unique_id(length=30, used_ids=None) -> str:
        """
        Generates a unique random string of the specified length and ensures it is unique within a document.

        Args:
            length (int): The desired length of the unique ID. Default is 30.
            used_ids (set): A set of already-used IDs to ensure uniqueness.

        Returns:
            str: A unique random string of the specified length.
        """
        if used_ids is None:
            used_ids = set()  # Initialize if not provided

        while True:
            unique_id = uuid.uuid4().hex[:length]  # Generate a random ID
            if unique_id not in used_ids:  # Check uniqueness
                used_ids.add(unique_id)  # Mark as used
                return unique_id