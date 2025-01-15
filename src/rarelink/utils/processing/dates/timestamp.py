from datetime import datetime, timezone
from google.protobuf.timestamp_pb2 import Timestamp
import logging

logger = logging.getLogger(__name__)

def date_to_timestamp(date_input):
    """
    Converts a full date (YYYY-MM-DD) into an ISO8601 UTC timestamp.

    :param date_input: Date input as a string in "YYYY-MM-DD" format.
    :type date_input: str
    :return: ISO8601 UTC timestamp string or None for invalid dates.
    :rtype: str | None
    """
    if not date_input:
        logger.warning("Empty or invalid date input; returning None")
        return None

    try:
        parsed_date = datetime.strptime(date_input, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        timestamp = Timestamp()
        timestamp.FromDatetime(parsed_date)
        return timestamp.ToJsonString()
    except ValueError:
        logger.error(f"Invalid date format: {date_input}. Expected format: YYYY-MM-DD.")
        return None


def year_month_to_timestamp(year, month):
    """
    Converts a year and month (YYYY, MM) into an ISO8601 UTC timestamp.

    :param year: Year input as an integer.
    :type year: int
    :param month: Month input as an integer (1-12).
    :type month: int
    :return: ISO8601 UTC timestamp string or None for invalid dates.
    :rtype: str | None
    """
    if not year or not month:
        logger.warning("Empty or invalid year/month input; returning None")
        return None

    try:
        if not (1900 <= year <= datetime.now(timezone.utc).year):
            raise ValueError(f"Year must be between 1900 and {datetime.now(timezone.utc).year}")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")

        parsed_date = datetime(year, month, 1, tzinfo=timezone.utc)
        timestamp = Timestamp()
        timestamp.FromDatetime(parsed_date)
        return timestamp.ToJsonString()
    except ValueError as e:
        logger.error(f"Invalid year/month input: {year}-{month}. {e}")
        return None


def year_to_timestamp(year):
    """
    Converts a year (YYYY) into an ISO8601 UTC timestamp.

    :param year: Year input as an integer.
    :type year: int
    :return: ISO8601 UTC timestamp string or None for invalid dates.
    :rtype: str | None
    """
    if not year:
        logger.warning("Empty or invalid year input; returning None")
        return None

    try:
        if not (1900 <= year <= datetime.now(timezone.utc).year):
            raise ValueError(f"Year must be between 1900 and {datetime.now(timezone.utc).year}")

        parsed_date = datetime(year, 1, 1, tzinfo=timezone.utc)
        timestamp = Timestamp()
        timestamp.FromDatetime(parsed_date)
        return timestamp.ToJsonString()
    except ValueError as e:
        logger.error(f"Invalid year input: {year}. {e}")
        return None
