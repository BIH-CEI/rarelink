# tests/phenopackets/test_utils.py
"""
Utilities for loading test data and configurations for Phenopackets tests.
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from rarelink_cdm import import_from_latest 

logger = logging.getLogger(__name__)

def get_test_data_dir() -> Path:
    """Get the path to the test data directory."""
    return Path(__file__).parent / "test_data"

def validate_json_file(file_path: Path) -> Tuple[bool, str]:
    """
    Validate a JSON file and provide diagnostic information if invalid.
    
    Args:
        file_path (Path): Path to the JSON file
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Try to parse the JSON
        json.loads(content)
        return True, "JSON is valid"
    
    except json.JSONDecodeError as e:
        # Extract the problematic line
        lines = content.split('\n')
        line_num = e.lineno - 1  # 0-based indexing
        
        # Show the problematic line and a few lines around it for context
        context_start = max(0, line_num - 2)
        context_end = min(len(lines), line_num + 3)
        
        context_lines = []
        for i in range(context_start, context_end):
            prefix = ">> " if i == line_num else "   "
            context_lines.append(f"{prefix}{i+1}: {lines[i]}")
        
        context = "\n".join(context_lines)
        
        error_message = (
            f"JSON error in {file_path.name}: {str(e)}\n"
            f"Error at line {e.lineno}, column {e.colno} (char {e.pos})\n"
            f"Context:\n{context}"
        )
        
        return False, error_message
    
    except Exception as e:
        return False, f"Error reading file {file_path}: {str(e)}"

def load_test_records() -> List[Dict[str, Any]]:
    """
    Load sample records from the test data directory.
    
    Returns:
        List[Dict[str, Any]]: List of sample records
    """
    # Try different possible filenames
    possible_files = [
        "sample_records.json",
        "sample_records_rarelink_cdm.json" 
    ]
    
    for filename in possible_files:
        test_data_path = get_test_data_dir() / filename
        if test_data_path.exists():
            # Validate the JSON before loading
            is_valid, message = validate_json_file(test_data_path)
            if not is_valid:
                logger.error(message)
                raise ValueError(f"Invalid JSON in {test_data_path}: {message}")
                
            try:
                with open(test_data_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading {test_data_path}: {e}")
                raise
    
    # If no file was found or loaded successfully
    raise FileNotFoundError(
        f"No sample records file found in {get_test_data_dir()}. "
        f"Expected one of: {', '.join(possible_files)}"
    )

def get_record_by_id(record_id: str) -> Optional[Dict[str, Any]]:
    """
    Get a specific record by ID.
    
    Args:
        record_id (str): ID of the record to retrieve
        
    Returns:
        Optional[Dict[str, Any]]: The record or None if not found
    """
    try:
        records = load_test_records()
        for record in records:
            if record.get("record_id") == record_id:
                return record
        logger.warning(f"Record with ID '{record_id}' not found in test data")
        return None
    except Exception as e:
        logger.error(f"Error getting record {record_id}: {e}")
        return None

# Rest of the file remains the same...
def get_rarelink_disease_config() -> Dict[str, Any]:
    """
    Get disease mapping configuration directly from RareLink CDM.
    """
    try:
        mod_disease = import_from_latest("mappings.phenopackets.disease")
        mod_mapping_dicts = import_from_latest("mappings.phenopackets.mapping_dicts")
        mod_label_dicts = import_from_latest("mappings.phenopackets.label_dicts")

        DISEASE_BLOCK = getattr(mod_disease, "DISEASE_BLOCK")
        mapping_dicts = getattr(mod_mapping_dicts, "mapping_dicts")
        label_dicts = getattr(mod_label_dicts, "label_dicts")

        disease_verification_mapping = {}
        for mapping_dict in mapping_dicts:
            if mapping_dict["name"] == "map_disease_verification_status":
                disease_verification_mapping = mapping_dict["mapping"]
                break

        age_at_onset_labels = label_dicts.get("AgeAtOnset", {})

        return {
            "mapping_block": DISEASE_BLOCK,
            "mapping_dicts": {
                "map_disease_verification_status": disease_verification_mapping
            },
            "label_dicts": {
                "AgeAtOnset": age_at_onset_labels
            }
        }
    except Exception:
        # Fallback remains unchanged
        return {
            "mapping_block": {
                "redcap_repeat_instrument": "rarelink_5_disease",
                "term_field_1": "snomedct_64572001_mondo",
                "term_field_2": "snomedct_64572001_ordo",
                "term_field_3": "snomedct_64572001_icd10cm",
                "term_field_4": "snomedct_64572001_icd11",
                "term_field_5": "snomedct_64572001_omim_p",
                "excluded_field": "loinc_99498_8",
                "onset_date_field": "snomedct_298059007",
                "onset_category_field": "snomedct_424850005",
                "primary_site_field": "snomedct_363698007"
            }
        }
        
def get_all_rarelink_configs() -> Dict[str, Any]:
    """
    Get all mapping configurations directly from RareLink CDM.
    """
    try:
        mod_combined = import_from_latest("mappings.phenopackets.combined")
        create_rarelink_phenopacket_mappings = getattr(
            mod_combined, "create_rarelink_phenopacket_mappings"
        )
        return create_rarelink_phenopacket_mappings()
    except Exception:
        return {}

def get_disease_instances_from_record(record: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract all disease instances from a record.
    
    Args:
        record (Dict[str, Any]): Record to extract from
        
    Returns:
        List[Dict[str, Any]]: List of disease instances
    """
    disease_instances = []
    
    # Check for direct disease data
    if "rarelink_5_disease" in record:
        disease_instances.append(record["rarelink_5_disease"])
    
    # Check repeated elements
    if "repeated_elements" in record:
        for element in record["repeated_elements"]:
            if element.get("redcap_repeat_instrument") == "rarelink_5_disease" and "disease" in element:
                disease_instances.append(element["disease"])
    
    return disease_instances

def setup_processor_for_block(block_name: str) -> Tuple[Any, Dict[str, Any]]:
    """
    Set up a DataProcessor for a specific block.
    
    Args:
        block_name (str): Name of the block (e.g., 'diseases')
        
    Returns:
        Tuple[Any, Dict[str, Any]]: Processor and configuration dictionary
    """
    try:
        from rarelink.utils.processor import DataProcessor
        
        # Get configs from RareLink CDM
        all_configs = get_all_rarelink_configs()
        block_config = all_configs.get(block_name, {})
        
        # Create processor with mapping block
        processor = DataProcessor(
            mapping_config=block_config.get("mapping_block", {})
        )
        
        # Add enum classes if present
        enum_classes = block_config.get("enum_classes", {})
        for prefix, enum_class in enum_classes.items():
            processor.add_enum_class(prefix, enum_class)
        
        return processor, block_config
    except ImportError:
        raise ImportError("Failed to import required modules. Make sure rarelink is installed.")