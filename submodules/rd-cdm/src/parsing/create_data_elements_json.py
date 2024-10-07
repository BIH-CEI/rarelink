import json
import sys
import os
import importlib

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from data_model.utils import json_serializer
from src.data_model.data_elements import DataElement, DataElementModel
from src.data_model.base_types import CodeSystem, Coding

def load_data_element_definitions(version):
    """Dynamically load the data elements for a given version."""
    try:
        module = importlib.import_module(f"src.{version}.rd_cdm_{version}_data_elements")
        class_name = f"DATA_ELEMENTS_VERSIONS_{version.replace('.', '_').upper()}"
        version_class = getattr(module, class_name)
        return version_class.data_elements
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading data element module for {version}: {e}")
        return None

def create_data_elements_json(version):
    """
    Create a JSON file for the data elements of a specified version.

    This function generates a JSON file containing the data elements for a 
    given version of the data model. It first loads the data element definitions 
    using `load_data_element_definitions()`. The result is written as a JSON 
    file in the "res" folder under the respective version directory.

    Example:
    - For version "v2_0_0_dev0", the JSON will be created at:
      "res/v2_0_0_dev0/rd_cdm_data_elements_v2_0_0_dev0.json".

    :param version: A string representing the data model version (e.g., 
                    "v2_0_0_dev0").
    """

    data_elements = load_data_element_definitions(version)
    if data_elements is None:
        print(f"Failed to create data elements JSON for {version}.")
        return

    # Create a JSON structure for the data elements
    data_elements_json = {
        "version": version,  # Adding the version key to the root of the JSON
        "dataElements": [
            {
                "ordinal": de.ordinal,
                "section": de.section,
                "elementName": de.elementName,
                "elementCode": de.elementCode.code,
                "elementCodeSystem": de.elementCodeSystem if isinstance(de.elementCodeSystem, str) else de.elementCodeSystem.namespace_prefix,
                "dataType": de.dataType,
                "dataSpecification": de.dataSpecification,
                "valueSet": de.valueSet if isinstance(de.valueSet, str) else None,  # Directly use the string reference
                "fhirExpression_v4_0_1": de.fhirExpression_v4_0_1,
                "recommendedDataSpec_fhir": de.recommendedDataSpec_fhir,
                "phenopacketSchemaElement_v2_0": de.phenopacketSchemaElement_v2_0,
                "recommendedDataSpec_phenopackets": de.recommendedDataSpec_phenopackets,
                "description": de.description
            }
            for de in data_elements
        ]
    }

    # Write the JSON file to the res folder
    output_path = f"res/{version}/rd_cdm_data_elements_{version}.json"
    with open(output_path, "w") as json_file:
        json.dump(data_elements_json, json_file, default=json_serializer, indent=2)
        print(f"JSON file created successfully: {output_path}")


# Run the function for the versions you want
if __name__ == "__main__":
    create_data_elements_json("v2_0_0_dev0")
