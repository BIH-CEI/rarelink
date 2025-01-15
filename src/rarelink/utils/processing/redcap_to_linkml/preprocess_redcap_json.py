import json
from collections import defaultdict
from src.rarelink_cdm.v2_0_0_dev0.helpers import MAPPING_FUNCTIONS

def preprocess_flat_data(flat_data, mapping_functions):
    """
    Transforms flat REDCap data into structured JSON format compatible with the 
    RareLink-CDM LinkML schema. Allows modular addition of schemas via
    mapping_functions.

    Args:
        flat_data (list): Flat JSON data from REDCap.
        mapping_functions (dict): Dictionary of mapping functions for each schema.

    Returns:
        list: Transformed JSON data compatible with RareLink schema.
    """
    transformed_data = []

    # Group data by record_id
    records = defaultdict(list)
    for record in flat_data:
        records[record["record_id"]].append(record)

    for record_id, entries in records.items():
        # Base structure for the record
        record = {
            "record_id": record_id,
            "formal_criteria": None,
            "personal_information": None,
            "consent": None,
            "disability": None,
            "repeated_elements": []
        }

        for entry in entries:
            if entry["redcap_repeat_instrument"] == "":
                # Map non-repeating data using mapping functions
                for schema_name, mapper in mapping_functions.items():
                    if schema_name in ["formal_criteria", "personal_information", "consent", "disability"] and not record[schema_name]:
                        record[schema_name] = mapper(entry)
            else:
                # Handle repeating data
                repeated_element = {
                    "redcap_repeat_instrument": entry["redcap_repeat_instrument"],
                    "redcap_repeat_instance": int(entry["redcap_repeat_instance"])
                }
                if entry["redcap_repeat_instrument"] == "rarelink_3_patient_status":
                    repeated_element["patient_status"] = mapping_functions["patient_status"](entry)
                elif entry["redcap_repeat_instrument"] == "rarelink_4_care_pathway":
                    repeated_element["care_pathway"] = mapping_functions["care_pathway"](entry)
                elif entry["redcap_repeat_instrument"] == "rarelink_5_disease":
                    repeated_element["disease"] = mapping_functions["disease"](entry)
                elif entry["redcap_repeat_instrument"] == "rarelink_6_1_genetic_findings":
                    repeated_element["genetic_findings"] = mapping_functions["genetic_findings"](entry)
                elif entry["redcap_repeat_instrument"] == "rarelink_6_2_phenotypic_feature":
                    repeated_element["phenotypic_feature"] = mapping_functions["phenotypic_feature"](entry)
                elif entry["redcap_repeat_instrument"] == "rarelink_6_3_measurements":
                    repeated_element["measurements"] = mapping_functions["measurements"](entry)
                elif entry["redcap_repeat_instrument"] == "rarelink_6_4_family_history":
                    repeated_element["family_history"] = mapping_functions["family_history"](entry)
                record["repeated_elements"].append(repeated_element)

        transformed_data.append(record)

    return transformed_data


def main(flat_data_file, output_file):
    """
    Reads flat data, processes it, and writes the transformed JSON to a file.

    Args:
        flat_data_file (str): Path to the input flat JSON data file.
        output_file (str): Path to the output transformed JSON data file.
    """
    # Load flat data from JSON
    with open(flat_data_file, "r") as infile:
        flat_data = json.load(infile)

    # Transform the flat data
    transformed_data = preprocess_flat_data(flat_data, MAPPING_FUNCTIONS)

    # Save the transformed data to a new JSON file
    with open(output_file, "w") as outfile:
        json.dump(transformed_data, outfile, indent=2)

    print(f"Transformed data has been saved to {output_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Preprocess flat data for RareLink schema.")
    parser.add_argument("flat_data_file", help="Path to the input flat JSON data file")
    parser.add_argument("output_file", help="Path to the output transformed JSON data file")

    args = parser.parse_args()
    main(args.flat_data_file, args.output_file)
