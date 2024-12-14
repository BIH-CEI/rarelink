import json


def transform_to_flat(hierarchical_data):
    """
    Transforms hierarchical RareLink-CDM data into a flat JSON format for REDCap.
    """
    flat_data = []

    for record in hierarchical_data:
        # Handle the base (non-repeated) record
        base_record = {
            "record_id": record.get("record_id", ""),
            "redcap_repeat_instrument": "",
            "redcap_repeat_instance": "",
        }

        # Add formal criteria fields
        formal_criteria = record.get("formalCriteria", {})
        base_record.update(formal_criteria)

        # Add personal information fields
        personal_information = record.get("personalInformation", {})
        base_record.update(personal_information)

        # If the record has patient status data that is NOT repeated, include it
        if "patient_status_date" in record:
            base_record.update({
                "patient_status_date": record.get("patient_status_date", ""),
                "snomed_278844005": record.get("snomed_278844005", ""),
                "snomed_398299004": record.get("snomed_398299004", ""),
                "snomed_184305005": record.get("snomed_184305005", ""),
                "snomed_105727008": record.get("snomed_105727008", ""),
                "snomed_412726003": record.get("snomed_412726003", ""),
                "snomed_723663001": record.get("snomed_723663001", ""),
                "rarelink_3_patient_status_complete": record.get("rarelink_3_patient_status_complete", ""),
            })

        flat_data.append(base_record)

        # Handle repeated elements
        repeated_elements = record.get("repeatedElements", [])
        for repeated in repeated_elements:
            repeated_record = {
                "record_id": record.get("record_id", ""),
                "redcap_repeat_instrument": repeated.get("redcap_repeat_instrument", ""),
                "redcap_repeat_instance": repeated.get("redcap_repeat_instance", ""),
                # Clear unrelated fields
                "snomed_422549004": "",
                "snomed_399423000": "",
                "rarelink_1_formal_criteria_complete": "",
                "snomed_184099003": "",
                "snomed_281053000": "",
                "snomed_1296886006": "",
                "snomed_263495000": "",
                "snomed_370159000": "",
                "rarelink_2_personal_information_complete": "",
            }

            # Add nested repeated element data (e.g., patientStatus)
            for key, value in repeated.items():
                if isinstance(value, dict):  # Nested section
                    repeated_record.update(value)

            flat_data.append(repeated_record)

    return flat_data


def main(hierarchical_file, flat_file):
    """
    Reads hierarchical JSON data, transforms it, and writes the flat JSON to a file.
    """
    # Load hierarchical data from JSON
    with open(hierarchical_file, "r") as infile:
        hierarchical_data = json.load(infile)

    # Transform hierarchical data to flat JSON
    flat_data = transform_to_flat(hierarchical_data)

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
