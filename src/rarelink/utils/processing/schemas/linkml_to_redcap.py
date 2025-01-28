import json
from rarelink.utils.processing.codes import remove_prefix_from_code

def process_redcap_to_linkml(record, processing_rules):
    """
    Applies reverse processing rules to convert REDCap fields back to LinkML format.

    Args:
        record (dict): A single record to process.
        processing_rules (dict): Dictionary of reverse processing rules.

    Returns:
        dict: The processed record.
    """
    for field, processing_function in processing_rules.items():
        if field in record and record[field] is not None:
            record[field] = processing_function(record[field])
    return record


def linkml_to_redcap(input_file, output_file, template, reverse_processing_rules):
    """
    Transforms nested JSON data from input_file into a flattened REDCap-like 
    structure with all variables included, even if empty, based on a template,
    and applies reverse processing rules.

    Args:
        input_file (str): Path to the input JSON file with nested structure.
        output_file (str): Path to the output JSON file to store flattened data.
        template (dict): Template dictionary with all possible keys initialized 
        with empty values.
        reverse_processing_rules (dict): Dictionary of reverse processing rules.
    """
    # Validate template
    if not isinstance(template, dict):
        raise ValueError("Template must be a dictionary with key-value pairs.")

    # Load the input data
    with open(input_file, 'r') as file:
        data = json.load(file)

    final_records = []

    for record in data:
        # Initialize the base record using the template
        base_record = template.copy()
        base_record.update({
            "record_id": record.get("record_id", ""),
            "redcap_repeat_instrument": "",
            "redcap_repeat_instance": ""
        })

        # Flatten the base level of the record (non-repeating data)
        for key, value in record.items():
            if isinstance(value, dict):  # Handle nested fields
                for sub_key, sub_value in value.items():
                    if sub_key in base_record:
                        base_record[sub_key] = sub_value
            elif not isinstance(value, list):  # Skip repeated elements
                if key in base_record:
                    base_record[key] = value

        # Apply reverse processing rules to the non-repeating base record
        base_record = process_redcap_to_linkml(base_record, reverse_processing_rules)

        # Add the non-repeating base record to the final records first
        final_records.append(base_record)

        # Process repeating elements
        for key, value in record.items():
            if isinstance(value, list):  # Handle repeated elements
                for repeated in value:
                    repeated_record = template.copy()
                    repeated_record.update({
                        "record_id": record["record_id"],
                        "redcap_repeat_instrument": repeated.get(
                            "redcap_repeat_instrument", ""),
                        "redcap_repeat_instance": repeated.get(
                            "redcap_repeat_instance", ""),
                    })
                    for repeated_key, repeated_value in repeated.items():
                        if repeated_key not in ["redcap_repeat_instrument", 
                                                "redcap_repeat_instance"]:
                            if isinstance(repeated_value, dict):
                                for sub_key, sub_value in repeated_value.items():
                                    if sub_key in repeated_record:
                                        repeated_record[sub_key] = sub_value
                            else:
                                repeated_record[repeated_key] = repeated_value

                    # Apply reverse processing rules to repeated records
                    repeated_record = process_redcap_to_linkml(repeated_record, reverse_processing_rules)

                    # Append repeated records after non-repeating
                    final_records.append(repeated_record)

    # Write the final data to the output file
    with open(output_file, 'w') as file:
        json.dump(final_records, file, indent=4)