from dotenv import dotenv_values

def load_project_and_schema_info(env_path):
    """
    Load project and schema information dynamically from the environment or configuration.

    Args:
        env_path (Path): Path to the .env file.

    Returns:
        dict: Dictionary containing `project_name` and `schema_name`.
    """
    env_values = dotenv_values(env_path)
    project_name = env_values.get("REDCAP_PROJECT_NAME", "default_project")
    schema_name = env_values.get("LINKML_SCHEMA_NAME", "rarelink_cdm")
    return {"project_name": project_name, "schema_name": schema_name}
