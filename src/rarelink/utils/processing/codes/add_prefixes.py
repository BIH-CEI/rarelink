def add_prefix_to_code(code: str, prefix: str = "") -> str:
    """
    Adds a specific prefix to the REDCap code if not already present.

    Args:
        code (str): The original code (e.g., "G46.4", "62374-4").
        prefix (str): The prefix to add (e.g., "ICD10CM").

    Returns:
        str: The code with the appropriate prefix (e.g., "ICD10CM:G46.4").
    """
    if not code:
        return code 
    if prefix and not code.startswith(f"{prefix}:"):
        return f"{prefix}:{code}"
    return code