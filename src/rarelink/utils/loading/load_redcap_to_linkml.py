from rarelink.utils.loading.fetch import fetch_redcap_data
from rarelink.utils.processing.schemas import redcap_to_linkml
from rarelink.utils.validation import validate_linkml_data
from dotenv import dotenv_values

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
    # Load environment variables
    env_values = dotenv_values(env_path)
    project_name = env_values.get("REDCAP_PROJECT_NAME", "default_project")
    api_url = env_values["REDCAP_URL"]
    api_token = env_values["REDCAP_API_TOKEN"]

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Define file paths
    records_file = output_dir / f"{project_name}-records.json"
    processed_file = output_dir / f"{project_name}-linkml-records.json"

    # Step 1: Fetch REDCap data
    fetch_redcap_data(
        api_url=api_url,
        api_token=api_token,
        project_name=project_name,
        output_dir=output_dir,
    )
    print(f"✅ Records fetched and saved to {records_file}")

    # Step 2: Process REDCap data into LinkML schema
    redcap_to_linkml(
        flat_data_file=records_file,
        output_file=processed_file,
        mapping_functions=mapping_functions,
    )
    print(f"✅ Processed data saved to {processed_file}")

    # Step 3: Validate processed data
    if validate_linkml_data(schema_path, processed_file):
        print(f"✅ Validation successful for {processed_file}")
    else:
        raise RuntimeError(f"❌ Validation failed for {processed_file}")
