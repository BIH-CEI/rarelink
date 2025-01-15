import json
from . import redcap_to_linkml


def process_redcap_data(input_file, mapping_functions, schema_name, output_dir):
    """
    Process REDCap data into the specified LinkML schema.

    Args:
        input_file (Path): Path to the input JSON file (e.g., REDCap records).
        mapping_functions (dict): Dictionary of mapping functions for processing.
        schema_name (str): Name of the LinkML schema.
        output_dir (Path): Directory to save the processed data.

    Returns:
        Path: Path to the processed JSON file.
    """
    with open(input_file, "r") as infile:
        flat_data = json.load(infile)

    # Use redcap_to_linkml to transform the data
    transformed_data = redcap_to_linkml(flat_data, mapping_functions)

    output_file = output_dir / f"{schema_name}_linkml.json"
    with open(output_file, "w") as outfile:
        json.dump(transformed_data, outfile, indent=2)
    return output_file
