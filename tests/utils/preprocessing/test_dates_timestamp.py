from rarelink.utils.processing.dates import (
    date_to_timestamp,
    year_month_to_timestamp,
    year_to_timestamp,
)

def test_date_to_timestamp():
    assert date_to_timestamp("2018-03-01") == "2018-03-01T00:00:00Z"
    assert date_to_timestamp("2024-01-02") == "2024-01-02T00:00:00Z"
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

