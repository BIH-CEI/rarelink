import json
from collections import defaultdict


# Schema-specific mappers
def map_formal_criteria(entry):
    """
    Maps a flat REDCap entry to the FormalCriteria schema.
    """
    return {
        "snomed_422549004": entry.get("snomed_422549004", ""),
        "snomed_399423000": entry.get("snomed_399423000", ""),
        "rarelink_1_formal_criteria_complete": entry.get("rarelink_1_formal_criteria_complete", "")
    }


def map_personal_information(entry):
    """
    Maps a flat REDCap entry to the PersonalInformation schema.
    """
    return {
        "snomed_184099003": entry.get("snomed_184099003", ""),
        "snomed_281053000": entry.get("snomed_281053000", ""),
        "snomed_1296886006": entry.get("snomed_1296886006", ""),
        "snomed_263495000": entry.get("snomed_263495000", ""),
        "snomed_370159000": entry.get("snomed_370159000", ""),
        "rarelink_2_personal_information_complete": entry.get("rarelink_2_personal_information_complete", "")
    }


def map_patient_status(entry):
    """
    Maps a flat REDCap entry to the PatientStatus schema.
    """
    return {
        "patient_status_date": entry.get("patient_status_date", ""),
        "snomed_278844005": entry.get("snomed_278844005", ""),
        "snomed_398299004": entry.get("snomed_398299004", ""),
        "snomed_184305005": entry.get("snomed_184305005", ""),
        "snomed_105727008": entry.get("snomed_105727008", ""),
        "snomed_412726003": entry.get("snomed_412726003", ""),
        "snomed_723663001": entry.get("snomed_723663001", ""),
        "rarelink_3_patient_status_complete": entry.get("rarelink_3_patient_status_complete", "")
    }


def map_care_pathway(entry):
    """
    Maps a flat REDCap entry to the CarePathway schema.
    """
    return {
        "hl7fhir_enc_period_start": entry.get("hl7fhir_enc_period_start", ""),
        "hl7fhir_enc_period_end": entry.get("hl7fhir_enc_period_end", ""),
        "snomed_305058001": entry.get("snomed_305058001", ""),
        "hl7fhir_encounter_class": entry.get("hl7fhir_encounter_class", "")
    }


# Modular mapping dispatcher
MAPPING_FUNCTIONS = {
    "formal_criteria": map_formal_criteria,
    "personal_information": map_personal_information,
    "patient_status": map_patient_status,
    "care_pathway": map_care_pathway
}


def preprocess_flat_data(flat_data, mapping_functions):
    """
    Transforms flat REDCap data into structured JSON format compatible with the 
    RareLink-CDM LinkML schema. Allows modular addition of schemas via
    mapping_functions.

    Args:
        flat_data (list): Flat JSON data from REDCap.
        mapping_functions (dict): Dictionary of mapping functions for each schema.

    Returns:
        list: Transformed JSON data compatible with RareLink schema.
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
            "formal_criteria": None,
            "personal_information": None,
            "repeated_elements": []
        }

        for entry in entries:
            if entry["redcap_repeat_instrument"] == "":
                # Map non-repeating data using mapping functions
                for schema_name, mapper in mapping_functions.items():
                    if schema_name in ["formal_criteria", "personal_information"] and not record[schema_name]:
                        record[schema_name] = mapper(entry)
            else:
                # Handle repeating data
                repeated_element = {
                    "redcap_repeat_instrument": entry["redcap_repeat_instrument"],
                    "redcap_repeat_instance": int(entry["redcap_repeat_instance"])
                }
                if entry["redcap_repeat_instrument"] == "rarelink_3_patient_status":
                    repeated_element["patient_status"] = mapping_functions["patient_status"](entry)
                elif entry["redcap_repeat_instrument"] == "rarelink_4_care_pathway":
                    repeated_element["care_pathway"] = mapping_functions["care_pathway"](entry)
                record["repeated_elements"].append(repeated_element)

        transformed_data.append(record)

    return transformed_data


def main(flat_data_file, output_file):
    """
    Reads flat data, processes it, and writes the transformed JSON to a file.

    Args:
        flat_data_file (str): Path to the input flat JSON data file.
        output_file (str): Path to the output transformed JSON data file.
    """
    # Load flat data from JSON
    with open(flat_data_file, "r") as infile:
        flat_data = json.load(infile)

    # Transform the flat data
    transformed_data = preprocess_flat_data(flat_data, MAPPING_FUNCTIONS)

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
