from typing import Optional, Union
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from google.protobuf.timestamp_pb2 import Timestamp
import logging

logger = logging.getLogger(__name__)


def parse_date(date_input: Union[str, datetime, Timestamp]) -> Optional[datetime]:
    """
    Parse a date input into a *UTC-aware* Python datetime object.
    Supports:
      - Google protobuf Timestamp
      - "seconds:1234567" (UTC epoch)
      - ISO8601 strings or "YYYY-MM-DD"
      - Python datetime (naive => treat as UTC; aware => convert to UTC)
    """

    if not date_input:
        return None
    
    # Case 1: Already a Python datetime
    if isinstance(date_input, datetime):
        return _ensure_utc_datetime(date_input)

    # Case 2: It's a Protobuf Timestamp
    if isinstance(date_input, Timestamp):
        # Convert to python datetime
        dt = date_input.ToDatetime()  # returns naive Python datetime in UTC
        return _ensure_utc_datetime(dt)

    # Case 3: Must be a string if we get here
    date_str = str(date_input).strip().lower()

    # 1) "seconds:..." => epoch in UTC
    if date_str.startswith("seconds:"):
        try:
            seconds = float(date_str.replace("seconds:", "").strip())
            return datetime.utcfromtimestamp(seconds).replace(tzinfo=timezone.utc)
        except ValueError:
            return None

    # 2) Try fromisoformat (handles "YYYY-MM-DD", "YYYY-MM-DDTHH:MM:SS", offsets, etc.)
    raw_str = str(date_input).strip()
    # If it ends with 'Z', convert to '+00:00'
    if raw_str.endswith("Z"):
        raw_str = raw_str[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(raw_str)
        return _ensure_utc_datetime(dt)
    except ValueError:
        pass

    # 3) Fallback: "YYYY-MM-DD"
    try:
        dt = datetime.strptime(raw_str, "%Y-%m-%d")
        return dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _ensure_utc_datetime(dt: datetime) -> datetime:
    """Ensure the given datetime is UTC-aware."""
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    else:
        return dt.astimezone(timezone.utc)


def date_to_timestamp(date_input: Union[str, datetime, Timestamp]) -> Optional[Timestamp]:
    """
    Convert a date to a Protobuf Timestamp in UTC.
    """
    dt = parse_date(date_input)
    if not dt:
        return None

    timestamp = Timestamp()
    # Protobuf’s FromDatetime can accept a naive datetime but interprets it as UTC.
    # We already have dt in UTC, so:
    timestamp.FromDatetime(dt.replace(tzinfo=None))
    return timestamp


def convert_date_to_iso_age(event_date: Union[str, datetime, Timestamp],
                            dob: Union[str, datetime, Timestamp]) -> Optional[str]:
    """
    Convert event_date - dob => ISO8601 duration, e.g. 'P3Y2M'.
    """
    logger.debug(f"[convert_date_to_iso_age] event_date={event_date}, dob={dob}")
    
    if not event_date or not dob:
        return None
    
    try:
        event_dt = parse_date(event_date)
        dob_dt = parse_date(dob)
        if not event_dt or not dob_dt:
            return None

        logger.debug(f"  -> parsed event_dt={event_dt}  dob_dt={dob_dt}")
        delta = relativedelta(event_dt, dob_dt)
        logger.debug(f"  -> relativedelta => years={delta.years}, months={delta.months}, days={delta.days}")

        return f"P{delta.years}Y{delta.months}M"
    except Exception as e:
        logger.error(f"Error calculating ISO age: {e}")
        return None
