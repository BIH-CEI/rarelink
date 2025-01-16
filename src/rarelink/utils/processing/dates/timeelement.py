from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from phenopackets import TimeElement
import logging

logger = logging.getLogger(__name__)

def create_time_element_from_date(date_input: str) -> TimeElement:
    """
    Creates a Phenopacket `TimeElement` from a date string.

    Args:
        date_input (str): Date input as a string in "YYYY-MM-DD" or ISO8601 format.

    Returns:
        TimeElement: A Phenopacket TimeElement containing the parsed Timestamp, or None if invalid.
    """
    if not date_input:
        logger.warning("Empty or invalid date input; returning None")
        return None

    try:
        # Attempt to parse ISO8601 format
        parsed_date = datetime.fromisoformat(date_input.rstrip("Z"))
    except ValueError:
        # Fallback to "YYYY-MM-DD" format
        try:
            parsed_date = datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            logger.error(f"Invalid date format: {date_input}. Expected ISO8601 or YYYY-MM-DD.")
            return None

    # Convert to Protobuf Timestamp
    timestamp = Timestamp()
    timestamp.FromDatetime(parsed_date)

    # Wrap in TimeElement
    time_element = TimeElement(timestamp=timestamp)
    logger.info(f"Created TimeElement: {time_element}")
    return time_element
