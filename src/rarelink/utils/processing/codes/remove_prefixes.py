
def remove_prefix_from_code(value, prefix):
    """
    Removes a specific prefix from the value if it exists.

    Args:
        value (str): The original value.
        prefix (str): The prefix to remove.

    Returns:
        str: The value without the prefix, or the original value if the prefix is not present.
    """
    if value and value.startswith(f"{prefix}:"):
        return value[len(prefix) + 1:]
    return value