def write_env_file(env_path, key, value):
    """
    Write or update a key-value pair in a .env file without adding quotes 
    around the value. If the key already exists, its value will be replaced.

    Args:
        env_path (Path): The path to the .env file where the key-value pair should be written.
        key (str): The key to be written or updated in the .env file.
        value (str): The value to be associated with the key in the .env file.

    Behavior:
        - Reads the existing contents of the .env file, if it exists.
        - Removes any existing entry with the same key.
        - Appends the new key-value pair in the format `KEY=VALUE` without quotes.
        - Writes back the updated content to the .env file, ensuring it ends with a newline.

    Example:
        >>> from pathlib import Path
        >>> write_env_file(Path('.env'), 'API_KEY', '12345')
        # Updates or creates a .env file with the content:
        # API_KEY=12345

    Raises:
        IOError: If the function fails to write to the .env file.
    """
    # Read existing lines or create an empty list if the file doesn't exist
    lines = []
    if env_path.exists():
        lines = env_path.read_text().splitlines()

    # Remove any existing entry for the key
    lines = [line for line in lines if not line.startswith(f"{key}=")]

    # Add the new key-value pair without quotes
    lines.append(f"{key}={value}")

    # Write back all lines
    env_path.write_text("\n".join(lines) + "\n")
