from rarelink.utils.loading.project_and_schema import load_project_and_schema_info
from rarelink.utils.loading.fetch import fetch_redcap_data
from rarelink.utils.processing.schemas import process_redcap_data
from rarelink.utils.validation import validate_linkml_data

def load_redcap_to_linkml(env_path, output_dir, mapping_functions, schema_path):
    """
    End-to-end loader for fetching REDCap data, processing it into LinkML, 
    and validating the output.

    Args:
        env_path (Path): Path to the .env file.
        output_dir (Path): Directory to save intermediate and final outputs.
        mapping_functions (dict): Mapping functions for processing REDCap data.
        schema_path (Path): Path to the LinkML schema for validation.

    Returns:
        None
    """
    # Load project and schema information
    project_info = load_project_and_schema_info(env_path)
    project_name = project_info["project_name"]
    schema_name = project_info["schema_name"]

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Fetch REDCap data
    records_file = fetch_redcap_data(
        api_url="https://example.redcap.api",  # Replace with actual API URL
        api_token="your_api_token_here",     # Replace with actual API token
        project_name=project_name,
        output_dir=output_dir,
    )

    # Step 2: Process REDCap data into LinkML schema
    processed_file = process_redcap_data(
        input_file=records_file,
        mapping_functions=mapping_functions,
        schema_name=schema_name,
        output_dir=output_dir,
    )

    # Step 3: Validate processed data
    if validate_linkml_data(schema_path, processed_file):
        print(f"✅ Validation successful for {processed_file}")
    else:
        print(f"❌ Validation failed for {processed_file}")
