# date_handling.py
from typing import Optional, Union
from datetime import datetime
from dateutil.relativedelta import relativedelta
from google.protobuf.timestamp_pb2 import Timestamp
import logging

logger = logging.getLogger(__name__)

def parse_date(date_input: Union[str, datetime]) -> Optional[datetime]:
    """
    Parse a date input into a datetime object.
    
    Args:
        date_input: Date as string or datetime
        
    Returns:
        Parsed datetime or None if parsing fails
    """
    if not date_input:
        return None
    
    # Already a datetime
    if isinstance(date_input, datetime):
        return date_input
    
    if isinstance(date_input, str):
        # Handle "seconds:" format
        if "seconds:" in date_input.lower():
            try:
                seconds = float(date_input.lower().replace("seconds:", "").strip())
                return datetime.fromtimestamp(seconds)
            except ValueError:
                return None
        
        # Try ISO format
        try:
            return datetime.fromisoformat(date_input.rstrip('Z'))
        except ValueError:
            # Try YYYY-MM-DD format
            try:
                return datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                return None
    
    return None

def date_to_timestamp(date_input: Union[str, datetime]) -> Optional[Timestamp]:
    """
    Convert a date to a Protobuf Timestamp.
    
    Args:
        date_input: Date as string or datetime
        
    Returns:
        Protobuf Timestamp or None if conversion fails
    """
    dt = parse_date(date_input)
    if not dt:
        return None
    
    timestamp = Timestamp()
    timestamp.FromDatetime(dt)
    return timestamp



def convert_date_to_iso_age(event_date: Union[str, datetime], dob: Union[str, datetime]) -> Optional[str]:
    """
    Convert dates to ISO8601 duration string.
    
    Args:
        event_date: The event date
        dob: Date of birth
        
    Returns:
        ISO8601 duration string (e.g., "P38Y7M") or None
    """
    if not event_date or not dob:
        return None
    
    try:
        # Parse dates
        event_dt = parse_date(event_date)
        dob_dt = parse_date(dob)
        
        if not event_dt or not dob_dt:
            return None
        
        # Calculate difference
        delta = relativedelta(event_dt, dob_dt)
        return f"P{delta.years}Y{delta.months}M"
    except Exception as e:
        logger.error(f"Error calculating ISO age: {e}")
        return None