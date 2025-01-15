

def convert_to_boolean(value: str, mapping: dict) -> bool:
    return mapping.get(value.lower(), None)