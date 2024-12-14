import json
from ..helpers.field_mappings import FIELD_MAPPINGS


def preprocess_redcap_data(flat_data):
    """
    Preprocess flat REDCap JSON data into hierarchical LinkML-compatible data.
    
    Args:
        flat_data (list): A list of dictionaries representing flat REDCap JSON data.

    Returns:
        list: A list of hierarchical JSON objects.
    """
    hierarchical_data = {}

    for row in flat_data:
        record_id = row["record_id"]
        if record_id not in hierarchical_data:
            hierarchical_data[record_id] = {
                "record_id": record_id,
                "formalCriteria": {},
                "personalInformation": {},
                "repeatedElements": []
            }

        for schema, config in FIELD_MAPPINGS.items():
            section_data = {field: row[field] for field in config["fields"] if field in row}

            if config.get("repeated"):  # Handle repeated elements
                if row.get("redcap_repeat_instrument") == schema:
                    repeated_element = {
                        "redcap_repeat_instrument": row.get("redcap_repeat_instrument", ""),
                        "redcap_repeat_instance": row.get("redcap_repeat_instance", "")
                    }
                    repeated_element.update(section_data)
                    hierarchical_data[record_id]["repeatedElements"].append(repeated_element)
            else:  # Handle base sections
                hierarchical_data[record_id][schema] = section_data

    return list(hierarchical_data.values())


def main(flat_file, hierarchical_file):
    """
    Main function to preprocess flat data into hierarchical data.
    """
    # Load flat JSON data
    with open(flat_file, "r") as infile:
        flat_data = json.load(infile)

    # Transform flat data
    hierarchical_data = preprocess_redcap_data(flat_data)

    # Save hierarchical JSON data
    with open(hierarchical_file, "w") as outfile:
        json.dump(hierarchical_data, outfile, indent=2)

    print(f"Hierarchical data has been saved to {hierarchical_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Preprocess flat REDCap data to hierarchical JSON.")
    parser.add_argument("flat_file", help="Path to the input flat JSON data file")
    parser.add_argument("hierarchical_file", help="Path to the output hierarchical JSON data file")

    args = parser.parse_args()
    main(args.flat_file, args.hierarchical_file)
