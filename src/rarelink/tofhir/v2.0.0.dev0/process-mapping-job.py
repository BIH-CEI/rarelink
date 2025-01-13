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
# Update source URI
data["sourceSettings"]["redcap-kafka-source"]["sourceUri"] = redcap_url

# Update FHIR repository URL
data["sinkSettings"]["fhirRepoUrl"] = fhir_repo_url

# Process all mappings and update topicName placeholders
for mapping in data.get("mappings", []):
    source_bindings = mapping.get("sourceBinding", {})
    for binding_name, binding_details in source_bindings.items():
        topic_name = binding_details.get("topicName", "")
        # Replace the placeholder in topicName
        if "${REDCAP_PROJECT_ID}" in topic_name:
            binding_details["topicName"] = topic_name.replace("${REDCAP_PROJECT_ID}", redcap_project_id)

# Write the processed JSON to the output file
with open(output_file, "w") as outfile:
    json.dump(data, outfile, indent=4)

print(f"Processed JSON saved to {output_file}")
