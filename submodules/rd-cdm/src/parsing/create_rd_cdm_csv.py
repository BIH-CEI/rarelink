import csv
import json
import os

def load_json(file_path):
    """
    Utility function to load a JSON file.

    Args:
        file_path (str): The path to the JSON file to be loaded.

    Returns:
        dict: The loaded JSON data or None if the file could not be found
        or has invalid JSON format.
    """
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in {file_path}: {e.msg}")
        return None

def create_individual_csvs(json_data, version, output_dir):
    """
    Generate individual CSV files for CodeSystems, DataElements, and ValueSets.

    Args:
        json_data (dict): The JSON data to be converted to CSV.
        version (str): The version of the RD CDM.
        output_dir (str): Directory where the CSV files will be saved.
    """
    # Create CSV for code systems
    csv_code_systems = os.path.join(
        output_dir, f"rd_cdm_codesystems_{version}.csv")
    with open(csv_code_systems, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["CodeSystemName", "NamespacePrefix", "Version", "URL", "Synonyms"]
        )
        for cs in json_data.get("codeSystems", []):
            writer.writerow([
                cs.get("codeSystemName"), 
                cs.get("namespace_prefix"), 
                cs.get("version"), 
                cs.get("url"), 
                ",".join(cs.get("synonyms", []))
            ])

    # Create CSV for data elements
    csv_data_elements = os.path.join(
        output_dir, f"rd_cdm_data_elements_{version}.csv")
    with open(csv_data_elements, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Ordinal", "Section", "ElementName", "ElementCode", 
             "ElementCodeSystem", "DataType"]
        )
        for de in json_data.get("dataElements", []):
            writer.writerow([
                de.get("ordinal"), 
                de.get("section"), 
                de.get("elementName"), 
                de.get("elementCode"), 
                de.get("elementCodeSystem"), 
                de.get("dataType")
            ])

    # Create CSV for value sets
    csv_value_sets = os.path.join(
        output_dir, f"rd_cdm_value_sets_{version}.csv")
    with open(csv_value_sets, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["ValueSetName", "ValueSetOrigin", "ValueSetLink", "Display", 
             "ValueSetCode", "ValueSetCodeSystem", "ValueSetChoices"]
        )
        for vs in json_data.get("valueSets", []):
            value_set_code_systems = ";".join(
                [f"{cs['codeSystem']} (v{cs['version']})" 
                 for cs in vs.get("valueSetCodeSystem", [])]
            )
            value_set_choices = ";".join(
                [f"{choice['choiceDisplay']} ({choice['choiceCode']})" 
                 for choice in vs.get("valueSetChoices", [])]
            )
            writer.writerow([
                vs.get("valueSetName"), 
                vs.get("valueSetOrigin"), 
                vs.get("valueSetLink"), 
                vs.get("display"), 
                vs.get("valueSetCode"), 
                value_set_code_systems, 
                value_set_choices
            ])

    print(f"Individual CSV files created successfully in {output_dir}.")

def create_combined_csv(json_data, version, output_dir):
    """
    Generate a single CSV file from the entire RD CDM JSON data.

    Args:
        json_data (dict): The JSON data to be converted to CSV.
        version (str): The version of the RD CDM.
        output_dir (str): Directory where the CSV file will be saved.
    """
    csv_file_path = os.path.join(output_dir, f"rd_cdm_{version}.csv")
    
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow([
            "Type", "Name", "CodeSystem", "Version", "Code", "Description"
        ])
        
        # Write CodeSystems data
        for cs in json_data.get("codeSystems", []):
            writer.writerow([
                "CodeSystem",
                cs.get("codeSystemName"),
                cs.get("namespace_prefix"),
                cs.get("version"),
                cs.get("url"),
                "Synonyms: " + ",".join(cs.get("synonyms", []))
            ])
        
        # Write DataElements data
        for de in json_data.get("dataElements", []):
            writer.writerow([
                "DataElement",
                de.get("elementName"),
                de.get("elementCodeSystem"),
                "",  # Version is not directly available for DataElements
                de.get("elementCode"),
                "DataType: " + de.get("dataType", "")
            ])
        
        # Write ValueSets data
        for vs in json_data.get("valueSets", []):
            value_set_code_systems = ";".join(
                [f"{cs['codeSystem']} (v{cs['version']})"
                 for cs in vs.get("valueSetCodeSystem", [])]
            )
            value_set_choices = ";".join(
                [f"{choice['choiceDisplay']} ({choice['choiceCode']})"
                 for choice in vs.get("valueSetChoices", [])]
            )
            writer.writerow([
                "ValueSet",
                vs.get("valueSetName"),
                value_set_code_systems,
                "",  # Version is included in valueSetCodeSystem
                vs.get("valueSetCode"),
                "Choices: " + value_set_choices
            ])

    print(f"Single CSV file created successfully at {csv_file_path}.")

def create_final_rd_cdm_csv(version):
    """
    Load the final RD CDM JSON file and create both individual and combined CSVs.

    Args:
        version (str): The version of the RD CDM (e.g., "v2_0_0_dev0").
    """
    base_path = f"res/{version}/"
    json_file_path = os.path.join(base_path, f"rd_cdm_{version}.json")
    
    # Load the final RD CDM JSON file
    rd_cdm_json = load_json(json_file_path)
    
    if rd_cdm_json is None:
        print(f"Failed to load the RD CDM JSON file for version {version}.")
        return
    
    # Generate individual CSV files
    create_individual_csvs(rd_cdm_json, version, base_path)
    
    # Generate combined CSV file
    create_combined_csv(rd_cdm_json, version, base_path)

# Run the function for the desired version
if __name__ == "__main__":
    create_final_rd_cdm_csv("v2_0_0_dev0")
