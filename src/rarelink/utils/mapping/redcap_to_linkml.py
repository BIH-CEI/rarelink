"""
Utility for transforming flat REDCap data into structured JSON format compatible 
with a LinkML schema. This function is generalized to work with dynamically 
provided mapping functions.
"""

from collections import defaultdict

def redcap_to_linkml(flat_data, mapping_functions):
    """
    Transforms flat REDCap data into structured JSON format.

    Args:
        flat_data (list): Flat JSON data from REDCap.
        mapping_functions (dict): Dictionary of mapping functions for each schema.

    Returns:
        list: Transformed JSON data structured according to the mapping functions.
    """
    records = defaultdict(list)

    # Group data by record_id
    for record in flat_data:
        records[record["record_id"]].append(record)

    transformed_data = []

    for record_id, entries in records.items():
        record = {"record_id": record_id, "repeated_elements": []}

        for entry in entries:
            if entry["redcap_repeat_instrument"] == "":
                # Map non-repeating data using mapping functions
                for schema_name, mapper in mapping_functions.items():
                    if schema_name not in record:
                        record[schema_name] = mapper(entry)
            else:
                # Handle repeating data
                repeated_element = {
                    "redcap_repeat_instrument": entry["redcap_repeat_instrument"],
                    "redcap_repeat_instance": int(entry["redcap_repeat_instance"]),
                }
                mapper = mapping_functions.get(entry["redcap_repeat_instrument"])
                if mapper:
                    repeated_element["data"] = mapper(entry)
                record["repeated_elements"].append(repeated_element)

        transformed_data.append(record)

    return transformed_data
