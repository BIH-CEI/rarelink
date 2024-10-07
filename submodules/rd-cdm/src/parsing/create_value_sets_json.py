import json
import sys
import os
import importlib
from data_model.utils import json_serializer
from src.data_model.value_set import ValueSet, ValueSetChoice
from src.data_model.base_types import Coding, CodeSystem

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def load_value_set_definitions(version):
    """
    Dynamically load the value sets for a specified version.

    This function imports the module containing the value sets for the given
    version and retrieves the value sets definitions.
    
    Args:
        version (str): The version of the value sets (e.g., "v2_0_0_dev0").

    Returns:
        list: The loaded value sets or None if the module or class is not found.
    """
    try:
        module = importlib.import_module(f"src.{version}.rd_cdm_{version}_value_sets")
        class_name = f"VALUE_SETS_VERSIONS_{version.replace('.', '_').upper()}"
        version_class = getattr(module, class_name)
        return version_class.value_sets
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading value set module for {version}: {e}")
        return None

def load_code_system_versions(version):
    """
    Dynamically load the code system versions for a specified version.

    This function imports the module containing the code system versions for
    the given version and retrieves the version information.
    
    Args:
        version (str): The version of the code systems (e.g., "v2_0_0_dev0").

    Returns:
        dict: The loaded code system versions or an empty dictionary if the
        module or class is not found.
    """
    try:
        module = importlib.import_module(f"src.{version}.rd_cdm_{version}_codesystems_versions")
        class_name = f"CODESYSTEMS_VERSIONS_{version.replace('.', '_').upper()}"
        version_class = getattr(module, class_name)
        return version_class.versions
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading code system version module for {version}: {e}")
        return {}

def create_value_set_json(version):
    """
    Create a JSON file for the value sets of a specified version.

    This function generates a JSON file that includes the value sets and their
    associated code systems and choices for the given version, and writes it to
    the appropriate output directory.

    Args:
        version (str): The version of the value sets to generate (e.g., "v2_0_0_dev0").
    """
    
    value_sets = load_value_set_definitions(version)
    if value_sets is None:
        print(f"Failed to create value set JSON for {version}.")
        return

    code_system_versions = load_code_system_versions(version)
    
    value_sets_json = {
        "version": version,
        "dataElements": [], 
        "valueSets": [
            {
                "valueSetName": vs.valueSetName,
                "valueSetOrigin": vs.valueSetOrigin,
                "valueSetLink": vs.valueSetLink,
                "display": vs.display,
                "valueSetCode": vs.valueSetCode.code if isinstance(
                    vs.valueSetCode, Coding) else None,
                "valueSetCodeSystem": [
                    {
                        "codeSystem": system.namespace_prefix,
                        "version": code_system_versions.get(
                            system.namespace_prefix, "unknown")
                    }
                    for system in vs.valueSetCodeSystem if isinstance(
                        vs.valueSetCodeSystem, list)
                ] if isinstance(vs.valueSetCodeSystem, list) else [
                    {
                        "codeSystem": vs.valueSetCodeSystem.namespace_prefix,
                        "version": code_system_versions.get(
                            vs.valueSetCodeSystem.namespace_prefix, "unknown")
                    }
                ] if isinstance(vs.valueSetCodeSystem, CodeSystem) else None,
                "valueSetChoices": [
                    {
                        "choiceDisplay": choice.choiceDisplay,
                        "choiceCode": choice.choiceCode.code if isinstance(
                            choice.choiceCode, Coding) else None,
                        "choiceCodeSystem": 
                            choice.choiceCodeSystem.namespace_prefix if 
                                isinstance(choice.choiceCodeSystem, CodeSystem)
                                    else None,
                        "choiceCodeSystemVersion": code_system_versions.get(
                            choice.choiceCodeSystem.namespace_prefix, "unknown"
                        ) if isinstance(choice.choiceCodeSystem, CodeSystem) 
                            else "unknown"
                    }
                    for choice in vs.valueSetChoices
                ]
            }
            for vs in value_sets
        ]
    }

    output_directory = f"res/{version}/"
    os.makedirs(output_directory, exist_ok=True)

    output_path = os.path.join(
        output_directory, f"rd_cdm_value_sets_{version}.json")
    with open(output_path, "w") as json_file:
        json.dump(value_sets_json, json_file, default=json_serializer, indent=2)
        print(f"JSON file created successfully: {output_path}")


# Example usage
if __name__ == "__main__":
    create_value_set_json("v2_0_0_dev0")
