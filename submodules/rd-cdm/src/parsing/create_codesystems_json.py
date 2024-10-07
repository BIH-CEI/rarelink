import json
import sys
import os
import importlib

# Add src directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from data_model.utils import json_serializer
from src.data_model.codesystems import CodeSystems 

def load_code_system_versions(version):
    """
    Load code system versions for the specified data model version.

    This function dynamically imports a Python module that holds the versioned
    code systems for a given data model version (e.g., "v2_0_0_dev0"). Each version
    is stored in a class containing a dictionary mapping code system names to
    their respective version numbers.

    :param version: A string representing the version of the code systems 
                    to load (e.g., "v2_0_0_dev0").
    :return: A dictionary with the code system versions for the given version, 
             or None if the module or class is not found.
    """
    try:
        # Dynamically import the version-specific module
        module = importlib.import_module(f"src.{version}.rd_cdm_{version}_codesystems_versions")
        class_name = f"CODESYSTEMS_VERSIONS_{version.replace('.', '_').upper()}"
        version_class = getattr(module, class_name)
        return version_class.versions
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading version module for {version}: {e}")
        return None

def create_codesystem_json(version):
    """
    Create a JSON file for the code systems of a specified version.

    This function generates a JSON file containing the code systems for a 
    given version of the data model. It first loads the code system versions 
    using `load_code_system_versions()`, then it uses `CodeSystems` to fetch 
    all code systems. The result is written as a JSON file in the "res" folder 
    under the respective version directory.

    :param version: A string representing the data model version (e.g., 
                    "v2_0_0_dev0").
    """

    # Load code system versions for the specified version
    versions = load_code_system_versions(version)
    if versions is None:
        print(f"Failed to create code system JSON for {version}.")
        return

    # Access all predefined code systems using the CodeSystems class
    code_systems = CodeSystems.get_all_code_systems()

    # Generate the JSON structure
    code_systems_json = {
        "version": version,
        "CodeSystems": [
            {
                "codeSystemName": cs.name,
                "namespace_prefix": cs.namespace_prefix,
                "version": versions.get(cs.namespace_prefix, "unknown"), 
                "url": cs.url,
                "synonyms": cs.synonyms
            } for cs in code_systems.values()
        ]
    }

    # Ensure the output directory exists
    output_directory = f"res/{version}/"
    os.makedirs(output_directory, exist_ok=True)

    # Write the JSON file to the res folder
    output_path = os.path.join(output_directory, f"rd_cdm_codesystems_{version}.json")
    with open(output_path, "w") as json_file:
        json.dump(code_systems_json, json_file, default=json_serializer, indent=2)
        print(f"JSON file created successfully: {output_path}")


if __name__ == "__main__":
    create_codesystem_json("v2_0_0_dev0")
