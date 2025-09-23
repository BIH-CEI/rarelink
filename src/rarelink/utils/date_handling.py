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

    # Case 2: Protobuf Timestamp
    if isinstance(date_input, Timestamp):
        # protobuf >= 4 supports tzinfo param; fall back gracefully if not
        try:
            dt = date_input.ToDatetime(tzinfo=timezone.utc)  # aware UTC
        except TypeError:
            dt = date_input.ToDatetime()  # often naive UTC
        return _ensure_utc_datetime(dt)

    # Case 3: String
    date_str = str(date_input).strip()
    low = date_str.lower()

    # 1) "seconds:..." => epoch in UTC  (use fromtimestamp with tz to avoid deprecation)
    if low.startswith("seconds:"):
        try:
            seconds = float(date_str.split(":", 1)[1].strip())
            return datetime.fromtimestamp(seconds, tz=timezone.utc)
        except ValueError:
            return None

    # 2) Try fromisoformat (handles YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, offsets)
    raw = date_str
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(raw)
        return _ensure_utc_datetime(dt)
    except ValueError:
        pass

    # 3) Fallback: "YYYY-MM-DD"
    try:
        dt = datetime.strptime(raw, "%Y-%m-%d")
        return dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _ensure_utc_datetime(dt: datetime) -> datetime:
    """Ensure the given datetime is timezone-aware in UTC."""
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def date_to_timestamp(date_input: Union[str, datetime, Timestamp]) -> Optional[Timestamp]:
    """
    Convert a date-like input to a Protobuf Timestamp in UTC.
    - Accepts ISO strings, datetime, or Timestamp.
    - Always passes a timezone-aware UTC datetime to FromDatetime.
    """
    dt = parse_date(date_input)
    if not dt:
        return None
    dt = _ensure_utc_datetime(dt)

    ts = Timestamp()
    ts.FromDatetime(dt)  # aware UTC datetime
    return ts


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
