import yaml
import os

def load_schema(schema_name, base_dir="schema_definitions"):
    """
    Load a LinkML schema YAML definition.
    """
    schema_path = os.path.join(base_dir, f"{schema_name}.yaml")
    with open(schema_path, "r") as f:
        schema = yaml.safe_load(f)
    return schema
