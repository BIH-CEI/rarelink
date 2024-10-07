import data_model
import json
import os

def validate_schemas(version):
    base_path = f'../res/v{version}/'  # Adjusted for subfolder

    schema_file = f'{base_path}schema_v{version}.json'
    data_elements_file = f'{base_path}data_elements_v{version}.json'
    codesystems_file = f'{base_path}codesystems_v{version}.json'
    value_sets_file = f'{base_path}value_sets_v{version}.json'

    with open(schema_file) as schema_file:
        schema = json.load(schema_file)
        
    for file in [data_elements_file, codesystems_file, value_sets_file]:
        with open(file) as json_file:
            data = json.load(json_file)
            try:
                data_model.validate(instance=data, schema=schema)
            except data_model.ValidationError as e:
                print(f"Validation error in {file}: {e.message}")
                return False

    print(f"All schemas for version {version} are valid.")
    return True

__all__ = ['validate_schemas']