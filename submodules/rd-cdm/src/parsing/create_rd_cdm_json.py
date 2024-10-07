import json
import os
from datetime import datetime

from data_model.utils import json_serializer

def load_json(file_path):
    """
    Utility function to load a JSON file.

    Args:
        file_path (str): The path to the JSON file to be loaded.

    Returns:
        dict: The loaded JSON data or None if the file could not be found 
        or has invalid JSON format.
    """
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in {file_path}: {e.msg}")
        return None

def create_final_rd_cdm_json(version):
    """
    Combine CodeSystems, DataElements, and ValueSets into one final RD CDM JSON file.

    This function combines the contents of separate JSON files for code systems, 
    data elements, and value sets into a single comprehensive JSON document. It 
    also adds metadata including the current creation date and author.

    Args:
        version (str): The version of the RD CDM (e.g., "v2_0_0_dev0").

    Returns:
        dict: The combined RD CDM JSON structure, or None if any components fail 
        to load.
    """
    # Define the paths to the individual JSON files
    base_path = f"res/{version}/"
    codesystems_file = os.path.join(base_path, f"rd_cdm_codesystems_{version}.json")
    data_elements_file = os.path.join(base_path, f"rd_cdm_data_elements_{version}.json")
    value_sets_file = os.path.join(base_path, f"rd_cdm_value_sets_{version}.json")
    
    # Load the individual JSON files
    code_systems = load_json(codesystems_file)
    data_elements = load_json(data_elements_file)
    value_sets = load_json(value_sets_file)
    
    # Check if all files were loaded successfully
    if code_systems is None or data_elements is None or value_sets is None:
        print(f"Failed to load one or more components for version {version}.")
        return None
    
    # Get the current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Build the final combined RD CDM JSON
    rd_cdm_json = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Schema RD CDM Data Model",
        "version": version,
        "description": "The ontology-based Rare Disease Common Data Model (RD CDM) to enable international registry use, HL7 FHIR, and GA4GH Phenopackets.",
        "metadata": {
            "author": "Author Name",  # Replace with your metadata logic
            "creationDate": current_date,  # Automatically use today's date
        },
        "codeSystems": code_systems.get("CodeSystems", []),
        "dataElements": data_elements.get("dataElements", []),
        "valueSets": value_sets.get("valueSets", [])
    }
    
    # Write the final JSON file
    output_path = os.path.join(base_path, f"rd_cdm_{version}.json")
    with open(output_path, "w") as json_file:
        json.dump(rd_cdm_json, json_file, default=json_serializer, indent=2)
        print(f"Final RD CDM JSON created successfully: {output_path}")
    
    return rd_cdm_json
# Run the function for the desired version
if __name__ == "__main__":
    create_final_rd_cdm_json("v2_0_0_dev0")
