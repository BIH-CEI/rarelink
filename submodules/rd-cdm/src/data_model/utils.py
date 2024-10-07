from datetime import datetime

def json_serializer(obj):
    """
    Custom JSON serializer for objects not serializable by default.

    This function handles serialization of objects that the default `json` module
    cannot serialize, such as custom classes and datetime objects. It covers:

    - **Datetime objects**: Serializes `datetime` instances to ISO 8601 
        formatted strings.
    - **Class types (e.g., Date, Code)**: Serializes class references by 
        returning their class name as a string.
    - **Objects with a `__dict__` attribute**: Serializes objects by converting 
        their `__dict__` (attribute dictionary) to a serializable form.

    Args:
        obj (Any): The object to serialize.

    Returns:
        str or dict: A JSON-serializable representation of the input object.

    Raises:
        TypeError: If the object type is not supported for serialization.
    """
    if isinstance(obj, (datetime,)):
        return obj.isoformat()
    elif isinstance(obj, type):  # Handles class references like Date, Code, etc.
        return obj.__name__  # Return the name of the class
    elif hasattr(obj, "__dict__"):
        return obj.__dict__
    else:
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
