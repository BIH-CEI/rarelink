from dotenv import dotenv_values

def load_project_and_schema_info(env_path):
    """
    Load project and schema information dynamically from the environment or 
    configuration.

    Args:
        env_path (Path): Path to the .env file.

    Returns:
        dict: Dictionary containing `project_name` and `schema_name`.
    """
    env_values = dotenv_values(env_path)

    if "REDCAP_PROJECT_NAME" not in env_values or "LINKML_SCHEMA_NAME" \
        not in env_values:
        raise KeyError("Missing REDCAP_PROJECT_NAME or LINKML_SCHEMA_NAME "
                       "in the .env file.")

    return {
        "project_name": env_values["REDCAP_PROJECT_NAME"],
        "schema_name": env_values["LINKML_SCHEMA_NAME"],
    }
