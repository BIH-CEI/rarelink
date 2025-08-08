import json
from collections import defaultdict

# Process REDCap to Linkml 
# ------------------------

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
    import logging
    from rarelink_cdm import import_from_latest, import_from_version, get_latest_version

    parser = argparse.ArgumentParser(
        description="Transform flat REDCap data to LinkML schema."
    )
    parser.add_argument("flat_data_file", help="Path to the input flat JSON data file")
    parser.add_argument("output_file", help="Path to the output transformed JSON data file")
    parser.add_argument(
        "--cdm-version",
        help="Force a specific rarelink_cdm version (e.g., v2_0_2). Defaults to newest available.",
        default=None,
    )
    args = parser.parse_args()

    # Dynamically load mapping functions from the requested/latest CDM
    log = logging.getLogger(__name__)
    try:
        if args.cdm_version:
            mod = import_from_version(args.cdm_version, "mappings.redcap")
            log.info(f"Using rarelink_cdm mappings from {args.cdm_version}")
        else:
            # prefer truly importable newest
            latest = get_latest_version()
            try:
                mod = import_from_version(latest, "mappings.redcap")
                log.info(f"Using rarelink_cdm mappings from {latest}")
            except Exception:
                # fallback scan across versions
                mod = import_from_latest("mappings.redcap")
                log.info("Using rarelink_cdm mappings from newest importable version")
        MAPPING_FUNCTIONS = getattr(mod, "MAPPING_FUNCTIONS")
    except Exception as e:
        raise SystemExit(f"Failed to import MAPPING_FUNCTIONS from rarelink_cdm: {e}")

    redcap_to_linkml(args.flat_data_file, args.output_file, MAPPING_FUNCTIONS)



# Process LinkML to REDCap
# ------------------------

def process_redcap_to_linkml(record, processing_rules):
    """
    Applies reverse processing rules to convert REDCap fields back to LinkML format.
    """
    for field, processing_function in processing_rules.items():
        if field in record and record[field] is not None:
            record[field] = processing_function(record[field])
    return record


def linkml_to_redcap(input_file, output_file, template, reverse_processing_rules):
    """
    Transforms nested JSON data from input_file into a flattened REDCap-like structure
    with all variables, based on a template, and applies reverse processing rules.
    """
    if not isinstance(template, dict):
        raise ValueError("Template must be a dictionary with key-value pairs.")

    with open(input_file, 'r') as file:
        data = json.load(file)

    final_records = []

    for record in data:
        base_record = template.copy()
        base_record.update({
            "record_id": record.get("record_id", ""),
            "redcap_repeat_instrument": "",
            "redcap_repeat_instance": ""
        })

        # Flatten non-repeating level
        for key, value in record.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    if sub_key in base_record:
                        base_record[sub_key] = sub_value
            elif not isinstance(value, list):
                if key in base_record:
                    base_record[key] = value

        base_record = process_redcap_to_linkml(base_record, reverse_processing_rules)
        final_records.append(base_record)

        # Repeating elements
        for key, value in record.items():
            if isinstance(value, list):
                for repeated in value:
                    repeated_record = template.copy()
                    repeated_record.update({
                        "record_id": record.get("record_id", ""),
                        "redcap_repeat_instrument": repeated.get("redcap_repeat_instrument", ""),
                        "redcap_repeat_instance": repeated.get("redcap_repeat_instance", ""),
                    })
                    for rk, rv in repeated.items():
                        if rk not in ["redcap_repeat_instrument", "redcap_repeat_instance"]:
                            if isinstance(rv, dict):
                                for sk, sv in rv.items():
                                    if sk in repeated_record:
                                        repeated_record[sk] = sv
                            else:
                                repeated_record[rk] = rv

                    repeated_record = process_redcap_to_linkml(repeated_record, reverse_processing_rules)
                    final_records.append(repeated_record)

    with open(output_file, 'w') as file:
        json.dump(final_records, file, indent=4)