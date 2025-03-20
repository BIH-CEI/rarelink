


def _get_field_value(data, field_path):
    """Get a field value from data, handling direct and nested access."""
    if not field_path or not data:
        return None
        
    # Direct field access
    if "." not in field_path:
        return data.get(field_path)
        
    # Nested field access
    parts = field_path.split(".", 1)
    if len(parts) == 2:
        # If parts[0] is missing, use parts[1] directly (this happens when instrument name is same as data key)
        if parts[0] not in data and parts[1] in data:
            return data.get(parts[1])
            
        # Normal case - nested dictionary
        if parts[0] in data:
            nested_data = data.get(parts[0])
            if isinstance(nested_data, dict):
                return nested_data.get(parts[1])
    
    # Try matching the exact path as a fallback
    if field_path in data:
        return data[field_path]
    
    return None