import json
import pytest
from jsonschema import validate, ValidationError
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Schema file paths
CODE_SYSTEMS_SCHEMA = "schemas/rd_cdm_code_systems_schema.json"
DATA_ELEMENTS_SCHEMA = "schemas/rd_cdm_data_elements_schema.json"
VALUE_SETS_SCHEMA = "schemas/rd_cdm_value_sets_schema.json"
FULL_MODEL_SCHEMA = "schemas/rd_cdm_v2_0_0_dev0_schema.json"

# JSON files and corresponding schemas for validation
JSON_FILES_AND_SCHEMAS = [
    ("res/v2_0_0_dev0/rd_cdm_codesystems_v2_0_0_dev0.json", CODE_SYSTEMS_SCHEMA),
    ("res/v2_0_0_dev0/rd_cdm_data_elements_v2_0_0_dev0.json", DATA_ELEMENTS_SCHEMA),
    ("res/v2_0_0_dev0/rd_cdm_value_sets_v2_0_0_dev0.json", VALUE_SETS_SCHEMA),
    ("res/v2_0_0_dev0/rd_cdm_v2_0_0_dev0.json", FULL_MODEL_SCHEMA),
]

@pytest.mark.parametrize("json_file,schema_file", JSON_FILES_AND_SCHEMAS)
def test_validate_json_file(json_file, schema_file):
    """
    Validate JSON file against its corresponding schema.

    This function tests each JSON file by validating it against the appropriate
    JSON schema. If validation fails, it provides detailed error messages
    indicating where and why the validation failed.
    
    Args:
        json_file (str): Path to the JSON file to be validated.
        schema_file (str): Path to the schema file used for validation.
    """
    try:
        with open(schema_file, "r") as sf:
            schema = json.load(sf)

        with open(json_file, "r") as jf:
            data = json.load(jf)

        validate(instance=data, schema=schema)

    except FileNotFoundError:
        pytest.fail(f"File not found: {json_file}")

    except json.JSONDecodeError as e:
        pytest.fail(f"Invalid JSON format in {json_file}: {e.msg}")

    except ValidationError as e:
        print(f"Validation failed for {json_file}: {e.message}")
        print(f"Error in data element: {e.instance}")
        print(f"Error in schema part: {e.schema}")
        print(f"Validation path: {e.path}")
        pytest.fail(f"Validation failed for {json_file}: {e.message}")
