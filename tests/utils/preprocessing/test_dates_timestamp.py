from rarelink.utils.date_handling import (
    date_to_timestamp
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