import json
from collections import defaultdict

def redcap_to_linkml(flat_data_file, output_file, mapping_functions):
    """
    Transforms flat REDCap data into structured JSON format compatible with the 
    LinkML schema and saves the output to a file.

    Args:
        flat_data_file (str): Path to the input flat JSON data file.
        output_file (str): Path to the output transformed JSON data file.
        mapping_functions (dict): Dictionary of mapping functions for each schema.

    Returns:
        None
    """
    # Load flat data from JSON
    with open(flat_data_file, "r") as infile:
        flat_data = json.load(infile)

    transformed_data = []

    # Group data by record_id
    records = defaultdict(list)
    for record in flat_data:
        records[record["record_id"]].append(record)

    # Process records
    for record_id, entries in records.items():
        # Initialize the record structure with non-repeating sections first
        record = {
            "record_id": record_id,
        }

        # Add non-repeating data
        for entry in entries:
            if entry["redcap_repeat_instrument"] == "":
                for schema_name, config in mapping_functions.items():
                    if not config["is_repeating"] and schema_name not in record:
                        record[schema_name] = config["mapper"](entry)

        # Add repeating elements
        record["repeated_elements"] = []
        for entry in entries:
            if entry["redcap_repeat_instrument"] != "":
                repeated_instrument = entry["redcap_repeat_instrument"]
                repeated_element = {
                    "redcap_repeat_instrument": repeated_instrument,
                    "redcap_repeat_instance": int(entry["redcap_repeat_instance"]),
                }

                # Find schema name and apply the mapper
                for schema_name, config in mapping_functions.items():
                    if config["is_repeating"] and repeated_instrument.endswith(
                        schema_name):
                        repeated_element[schema_name] = config["mapper"](entry)

                record["repeated_elements"].append(repeated_element)

        transformed_data.append(record)

    # Save the transformed data
    with open(output_file, "w") as outfile:
        json.dump(transformed_data, outfile, indent=2)

    print(f"Transformed data has been saved to {output_file}")


if __name__ == "__main__":
    import argparse
    from rarelink_cdm.v2_0_0_dev0.mappings.redcap import MAPPING_FUNCTIONS

    parser = argparse.ArgumentParser(
        description="Transform flat REDCap data to LinkML schema.")
    parser.add_argument("flat_data_file", 
                        help="Path to the input flat JSON data file")
    parser.add_argument("output_file", 
                        help="Path to the output transformed JSON data file")

    args = parser.parse_args()
    redcap_to_linkml(args.flat_data_file, args.output_file, MAPPING_FUNCTIONS)
