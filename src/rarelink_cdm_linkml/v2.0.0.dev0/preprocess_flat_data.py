import json
from linkml_runtime.loaders import JSONLoader
from linkml_runtime.utils.yamlutils import YAMLRoot
from linkml_runtime.dumpers import JSONDumper
from linkml.validator import Validator
from pathlib import Path

# Preprocessing Function
def preprocess_flat_data(flat_data):
    transformed_data = {"aggregatedDataInstances": []}
    for record in flat_data:
        transformed_record = {
            "formalCriteria": {
                "record_id": record["record_id"],
                "redcap_repeat_instrument": record["redcap_repeat_instrument"],
                "redcap_repeat_instance": record["redcap_repeat_instance"],
                "snomed_422549004": record["snomed_422549004"],
                "snomed_399423000": record["snomed_399423000"],
                "rarelink_1_formal_criteria_complete": record["rarelink_1_formal_criteria_complete"],
            },
            "personalInformation": {
                "snomed_184099003": record["snomed_184099003"],
                "snomed_281053000": record["snomed_281053000"],
                "snomed_1296886006": record["snomed_1296886006"],
                "snomed_263495000": record["snomed_263495000"],
                "snomed_370159000": record["snomed_370159000"],
                "rarelink_2_personal_information_complete": record["rarelink_2_personal_information_complete"],
            },
        }
        transformed_data["aggregatedDataInstances"].append(transformed_record)
    return transformed_data

# Main script
def main(flat_data_file: Path, output_file: Path, schema_file: Path):
    # Load flat data
    with open(flat_data_file, "r") as f:
        flat_data = json.load(f)

    # Preprocess flat data into modular structure
    transformed_data = preprocess_flat_data(flat_data)

    # Save the transformed data
    with open(output_file, "w") as f:
        json.dump(transformed_data, f, indent=2)

    # Validate the transformed data
    validator = Validator(schema_file)
    results = validator.validate(output_file)
    
    # Print validation results
    if results.is_valid:
        print("Validation passed.")
    else:
        print("Validation failed:")
        for error in results.errors:
            print(f"- {error}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Process and validate flat data against the RareLink CDM schema.")
    parser.add_argument("flat_data_file", type=Path, help="Path to the flat JSON data file")
    parser.add_argument("output_file", type=Path, help="Path to save the transformed JSON data")
    parser.add_argument("schema_file", type=Path, help="Path to the RareLink CDM schema file")
    args = parser.parse_args()
    main(args.flat_data_file, args.output_file, args.schema_file)
