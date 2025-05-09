import os
import random

FHIR_BASE = input("Enter the FHIR server base URL (or just ENTER to use the default: http://localhost:8080/fhir): ") or 'http://localhost:8080/fhir'
HEADERS = {'Content-Type': 'application/fhir+json'}
OUTPUT_DIR = 'validation'

try:
    import requests
    import json
except ImportError as e:
    import subprocess
    import sys
    print(f"Missing module: {e.name}. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", e.name])
    import requests
    import json


os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_patient_resource_id():
    try:
        response = requests.get(f"{FHIR_BASE}/Patient", headers=HEADERS)
        response.raise_for_status()
        patients = response.json().get("entry", [])
        if patients:
            random_patient = random.choice(patients)
            return random_patient.get("resource", {}).get("id")
        response.raise_for_status()
        patients = response.json().get("entry", [])
        if patients:
            return patients[0].get("resource", {}).get("id")
        print("No patients found.")
        return None
    except Exception as e:
        print(f"Error fetching patient ID: {e}")
        return None


def get_patient_resources(patient_id):
    try:
        response = requests.get(f"{FHIR_BASE}/Patient/{patient_id}/$everything", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching resources for patient {patient_id}: {e}")
        return None


def convert_to_transaction_bundle(resources):
    transaction_bundle = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": []
    }

    for entry in resources:
        resource = entry.get("resource", {})
        resource_type = resource.get("resourceType")
        resource_id = resource.get("id")
        if not resource_type or not resource_id:
            print(f"Skipping invalid resource: {entry}")
            continue
        transaction_bundle["entry"].append({
            "resource": resource,
            "request": {
                "method": "PUT",
                "url": f"{resource_type}/{resource_id}"
            }
        })

    return transaction_bundle



def save_bundle_to_file(bundle, counter):
    file_path = os.path.join(OUTPUT_DIR, f"example_bundle_{counter}.json")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(bundle, f, indent=2)
        print(f"Bundle saved to {file_path}")
    except Exception as e:
        print(f"Error saving bundle: {e}")


# Main script execution
def main():
    patient_id = get_patient_resource_id()
    if not patient_id:
        print("No patient ID available.")
        return
    resources = get_patient_resources(patient_id)
    if resources:
        transaction_bundle = convert_to_transaction_bundle(resources.get("entry", []))
        save_bundle_to_file(transaction_bundle, len(os.listdir(OUTPUT_DIR)))
    else:
        print("No resources found for the given patient ID.")


if __name__ == "__main__":
    main()

