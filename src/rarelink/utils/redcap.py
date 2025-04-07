import requests
from rarelink.cli.utils.file_utils import write_json

def fetch_redcap_data(api_url, api_token, project_name, output_dir, api_params=None):
    """
    Fetch records from the REDCap API and save them as {sanitized-project-name}-records.json.

    Args:
        api_url (str): REDCap API URL.
        api_token (str): API token for REDCap authentication.
        project_name (str): Name of the REDCap project.
        output_dir (Path): Directory to save the fetched data.
        api_params (dict, optional): Additional API parameters for the REDCap API.

    Returns:
        Path: Path to the saved JSON file.
    """
    # Sanitize project name: replace spaces with underscores
    sanitized_project_name = project_name.replace(" ", "_")

    # Define the output file using the sanitized project name
    output_file = output_dir / f"{sanitized_project_name}-records.json"

    # Base fields for the API request
    fields = {
        "token": api_token,
        "content": "record",
        "format": "json",
        "type": "flat",
    }

    # Add any additional API parameters
    if api_params:
        for key, value in api_params.items():
            # Special handling for lists (like records, forms, etc.)
            if isinstance(value, list) and value:
                fields[key] = ",".join(value)
            # Only add parameters with actual values
            elif value is not None:
                fields[key] = value

    # Make the request to fetch data
    response = requests.post(api_url, data=fields)
    response.raise_for_status()

    # Get the records from the response
    records = response.json()
    
    # Check if specific records were requested
    if "records" in fields and records:
        requested_record_ids = fields["records"].split(",") if isinstance(fields["records"], str) else fields["records"]
        received_record_ids = set()
        
        # Get the actual record IDs from the response
        # Different REDCap projects might use different field names for the record ID
        if records:
            # Try to determine the record ID field name from the first record
            record_id_field = next(iter(records[0].keys()))
            for record in records:
                received_record_ids.add(str(record[record_id_field]))
        
        # Check for missing records
        missing_records = []
        for req_id in requested_record_ids:
            req_id = req_id.strip()
            if req_id and req_id not in received_record_ids:
                missing_records.append(req_id)
        
        if missing_records:
            raise ValueError(f"The following requested record IDs were not found: {', '.join(missing_records)}")
    elif "records" in fields and not records:
        requested_records = fields["records"]
        raise ValueError(f"No records found matching the requested IDs: {requested_records}")
    
    # Write records to JSON
    write_json(records, output_file)

    return output_file