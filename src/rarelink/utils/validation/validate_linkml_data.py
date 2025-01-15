import subprocess

def validate_linkml_data(schema_path, processed_file):
    """
    Validate the processed data against the LinkML schema.

    Args:
        schema_path (Path): Path to the LinkML schema YAML file.
        processed_file (Path): Path to the processed JSON file.

    Returns:
        bool: True if validation is successful, False otherwise.
    """
    try:
        result = subprocess.run(
            ["linkml-validate", "--schema", str(schema_path), str(processed_file)],
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except FileNotFoundError:
        raise RuntimeError("linkml-validate not found. Ensure it is installed.")
