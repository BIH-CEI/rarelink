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


def process_prefix(code: str, prefix: str) -> str:
    """
    Processes a code by ensuring it has the correct prefix format.
    Specifically, replaces underscores with colons where applicable.

    Args:
        code (str): The code to process (e.g., "UO_1234").
        prefix (str): The expected prefix (e.g., "UO").

    Returns:
        str: The processed code with the correct prefix format (e.g., "UO:1234").
    """
    if not code or not prefix:
        return code 

    if code.startswith(f"{prefix}_"):
        return code.replace("_", ":", 1) 
    
    if code.startswith(f"{prefix}:"):
        return code

    return code
