import json

def transform_to_redcap_json(hierarchical_data):
    """
    Transform hierarchical LinkML-compatible data back to flat REDCap JSON format.

    Args:
        hierarchical_data (list): A list of hierarchical JSON objects.

    Returns:
        list: A list of dictionaries representing flat REDCap JSON data.
    """
    flat_data = []

    for record in hierarchical_data:
        base_data = {key: value for key, value in record.items() if key not in ["repeatedElements"]}
        for repeated_element in record.get("repeatedElements", []):
            flat_entry = base_data.copy()
            flat_entry.update(repeated_element)
            flat_data.append(flat_entry)
        if not record.get("repeatedElements"):
            flat_data.append(base_data)

    return flat_data



def main(hierarchical_file, flat_file):
    """
    Reads hierarchical JSON data, transforms it, and writes the flat JSON to a file.
    """
    # Load hierarchical data from JSON
    with open(hierarchical_file, "r") as infile:
        hierarchical_data = json.load(infile)

    # Transform hierarchical data to flat JSON
    flat_data = transform_to_redcap_json(hierarchical_data)

    # Save the flat JSON data
    with open(flat_file, "w") as outfile:
        json.dump(flat_data, outfile, indent=2)

    print(f"Flat data has been saved to {flat_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Transform RareLink-CDM JSON to flat JSON for REDCap.")
    parser.add_argument("hierarchical_file", help="Path to the input hierarchical JSON data file")
    parser.add_argument("flat_file", help="Path to the output flat JSON data file")

    args = parser.parse_args()
    main(args.hierarchical_file, args.flat_file)
