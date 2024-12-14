import json
from collections import defaultdict


def preprocess_flat_data(flat_data):
    """
    Transforms flat REDCap data into structured JSON format compatible with the RareLink schema.
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
            "formalCriteria": None,
            "personalInformation": None,
            "repeatedElements": []
        }

        for entry in entries:
            if entry["redcap_repeat_instrument"] == "":
                # Non-repeating data (formalCriteria or personalInformation)
                if not record["formalCriteria"]:
                    record["formalCriteria"] = {
                        "snomed_422549004": entry.get("snomed_422549004", ""),
                        "snomed_399423000": entry.get("snomed_399423000", ""),
                        "rarelink_1_formal_criteria_complete": entry.get(
                            "rarelink_1_formal_criteria_complete", ""
                        )
                    }
                if not record["personalInformation"]:
                    record["personalInformation"] = {
                        "snomed_184099003": entry.get("snomed_184099003", ""),
                        "snomed_281053000": entry.get("snomed_281053000", ""),
                        "snomed_1296886006": entry.get("snomed_1296886006", ""),
                        "snomed_263495000": entry.get("snomed_263495000", ""),
                        "snomed_370159000": entry.get("snomed_370159000", ""),
                        "rarelink_2_personal_information_complete": entry.get(
                            "rarelink_2_personal_information_complete", ""
                        )
                    }

                # Handle patient status if present but not repeated
                if "patient_status_date" in entry and entry["patient_status_date"]:
                    record["repeatedElements"].append({
                        "redcap_repeat_instrument": "rarelink_3_patient_status",
                        "redcap_repeat_instance": 1,  # Default for non-repeating
                        "patientStatus": {
                            "patient_status_date": entry.get("patient_status_date", ""),
                            "snomed_278844005": entry.get("snomed_278844005", ""),
                            "snomed_398299004": entry.get("snomed_398299004", ""),
                            "snomed_184305005": entry.get("snomed_184305005", ""),
                            "snomed_105727008": entry.get("snomed_105727008", ""),
                            "snomed_412726003": entry.get("snomed_412726003", ""),
                            "snomed_723663001": entry.get("snomed_723663001", ""),
                            "rarelink_3_patient_status_complete": entry.get(
                                "rarelink_3_patient_status_complete", ""
                            )
                        }
                    })
            else:
                # Repeating data
                record["repeatedElements"].append({
                    "redcap_repeat_instrument": entry["redcap_repeat_instrument"],
                    "redcap_repeat_instance": int(entry["redcap_repeat_instance"]),
                    "patientStatus": {
                        "patient_status_date": entry.get("patient_status_date", ""),
                        "snomed_278844005": entry.get("snomed_278844005", ""),
                        "snomed_398299004": entry.get("snomed_398299004", ""),
                        "snomed_184305005": entry.get("snomed_184305005", ""),
                        "snomed_105727008": entry.get("snomed_105727008", ""),
                        "snomed_412726003": entry.get("snomed_412726003", ""),
                        "snomed_723663001": entry.get("snomed_723663001", ""),
                        "rarelink_3_patient_status_complete": entry.get(
                            "rarelink_3_patient_status_complete", ""
                        )
                    }
                })

        transformed_data.append(record)

    return transformed_data


def main(flat_data_file, output_file):
    """
    Reads flat data, processes it, and writes the transformed JSON to a file.
    """
    # Load flat data from JSON
    with open(flat_data_file, "r") as infile:
        flat_data = json.load(infile)

    # Transform the flat data
    transformed_data = preprocess_flat_data(flat_data)

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
