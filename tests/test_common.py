import hashlib
import hmac
from common_functions.common import create_hash

def test_create_hash():
    test_value = "test_input"
    salt = 'votetracker'
    expected_hash = hmac.new(bytes(salt , 'utf-8'), msg = bytes(test_value , 'utf-8'), digestmod = hashlib.sha256).hexdigest()

    assert create_hash(test_value) == expected_hash

import pytest
from common_functions.common import cast_date
import numpy as np

def test_valid_date_conversion():
    # Test with valid dates and expected conversions
    test_cases = [
        ('01-15-2024', '%m-%d-%Y', '2024-01-15'),
        ('2024', '%Y', '2024-01-01'),
        # Add more test cases as needed
    ]
    for date_string, from_format, expected in test_cases:
        assert cast_date(date_string, [from_format]) == (expected,)

def test_invalid_date_input():
    # Test with invalid date inputs
    invalid_dates = ['invalid-date', '2024-13-01', '02-30-2024']
    for date_string in invalid_dates:
        assert cast_date(date_string) == (np.nan,)

def test_empty_date_input():
    # Test with empty string
    assert cast_date('') == (np.nan,)

def test_none_date_input():
    # Test with None as input
    assert cast_date(None) == (np.nan,)

def test_custom_date_formats():
    # Test with custom date formats
    custom_formats = ['%Y-%m-%d', '%d-%m-%Y']
    test_cases = [
        ('2024-01-15', custom_formats, '2024-01-15'),
        ('15-01-2024', custom_formats, '2024-01-15'),
        # Add more test cases as needed
    ]
    for date_string, formats, expected in test_cases:
        assert cast_date(date_string, formats) == (expected,)

import pytest
# Run the tests
if __name__ == "__main__":
    pytest.main()
