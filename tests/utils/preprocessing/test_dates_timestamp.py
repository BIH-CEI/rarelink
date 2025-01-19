from rarelink.utils.processing.dates import (
    date_to_timestamp,
    year_month_to_timestamp,
    year_to_timestamp,
)
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

def test_date_to_timestamp():
    # Test with a valid date
    ts = date_to_timestamp("2018-03-01")
    expected_ts = Timestamp()
    expected_ts.FromDatetime(datetime(2018, 3, 1))
    assert ts.seconds == expected_ts.seconds
    assert ts.nanos == expected_ts.nanos

    # Test with another valid date
    ts = date_to_timestamp("2024-01-02")
    expected_ts = Timestamp()
    expected_ts.FromDatetime(datetime(2024, 1, 2))
    assert ts.seconds == expected_ts.seconds
    assert ts.nanos == expected_ts.nanos

    # Test with an empty string
    assert date_to_timestamp("") is None
def test_year_month_to_timestamp():
    assert year_month_to_timestamp(2018, 3) == "2018-03-01T00:00:00Z"
    assert year_month_to_timestamp(2024, 1) == "2024-01-01T00:00:00Z"
    assert year_month_to_timestamp(1900, 1) == "1900-01-01T00:00:00Z"
    assert year_month_to_timestamp(2024, 13) is None  # Invalid month


def test_year_to_timestamp():
    assert year_to_timestamp(2018) == "2018-01-01T00:00:00Z"
    assert year_to_timestamp(2024) == "2024-01-01T00:00:00Z"
    assert year_to_timestamp(1899) is None  # Invalid year

