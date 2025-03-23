import requests
from rarelink.cli.utils.file_utils import write_json

def fetch_redcap_data(api_url, api_token, project_name, output_dir):
    """
    Fetch records from the REDCap API and save them as {sanitized-project-name}-records.json.

    Args:
        api_url (str): REDCap API URL.
        api_token (str): API token for REDCap authentication.
        project_name (str): Name of the REDCap project.
        output_dir (Path): Directory to save the fetched data.

    Returns:
        Path: Path to the saved JSON file.
    """
    # Sanitize project name: replace spaces with underscores
    sanitized_project_name = project_name.replace(" ", "_")

    # Define the output file using the sanitized project name
    output_file = output_dir / f"{sanitized_project_name}-records.json"

    fields = {
        "token": api_token,
        "content": "record",
        "format": "json",
        "type": "flat",
    }

    # Make the request to fetch data
    response = requests.post(api_url, data=fields)
    response.raise_for_status()

    # Get the records from the response and write to JSON
    records = response.json()
    write_json(records, output_file)

    return output_file
