import os
import json
from dotenv import load_dotenv

# Load environment variables from the .env file in the root directory
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.env"))
load_dotenv(dotenv_path)

# Input and output file paths
input_file = "src/rarelink/tofhir/v2.0.0.dev0/mapping-jobs/rarelink-cdm.json"
output_file = "src/rarelink/tofhir/v2.0.0.dev0/mapping-jobs/rarelink-cdm-processed.json"

# Get environment variables
redcap_url = os.getenv("REDCAP_URL", "http://default-redcap-url")
fhir_repo_url = os.getenv("FHIR_REPO_URL", "http://default-fhir-url")
redcap_project_id = os.getenv("REDCAP_PROJECT_ID", "default_project_id")

# Read the input JSON file
with open(input_file, "r") as infile:
    data = json.load(infile)

# Replace placeholders with environment variable values
data["sourceSettings"]["redcap-kafka-source"]["sourceUri"] = redcap_url
data["sinkSettings"]["fhirRepoUrl"] = fhir_repo_url
data["mappings"][0]["sourceBinding"]["rarelinkpatient"]["topicName"] = f"{redcap_project_id}-rarelink_1_formal_criteria"
data["mappings"][0]["sourceBinding"]["rarelinkpersonalinformation"]["topicName"] = f"{redcap_project_id}-rarelink_2_personal_information"

# Write the processed JSON to the output file
with open(output_file, "w") as outfile:
    json.dump(data, outfile, indent=4)

print(f"Processed JSON saved to {output_file}")
