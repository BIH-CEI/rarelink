import json

def phenopacket_processing(input_file, output_file, process_function):
    """
    Process all values in a JSON file with the given function, keeping the structure intact.

    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to the output JSON file.
        process_function (callable): Function to process values. It must accept two arguments (value and prefix).

    Returns:
        None
    """
    # Helper function to recursively process dictionary values
    def process_data(data):
        if isinstance(data, dict):
            # Process dictionary values
            return {
                key: process_data(process_function(value, key.split("_")[0]) if isinstance(value, str) else value)
                for key, value in data.items()
            }
        elif isinstance(data, list):
            # Process list elements
            return [process_data(item) for item in data]
        else:
            # Return data unchanged if not a dict or list
            return data

    # Load the input JSON
    with open(input_file, "r") as infile:
        json_data = json.load(infile)

    # Process the JSON data
    processed_data = process_data(json_data)

    # Save the processed JSON to the output file
    with open(output_file, "w") as outfile:
        json.dump(processed_data, outfile, indent=2)

    print(f"Processed data has been saved to {output_file}")
