from common_functions.physical_address import standardize_address
import pytest

def test_standardize_valid_address():
    input_address = "123 Main St, Anytown, CA 12345"
    {'address_line_1': '123 MAIN STY', 'address_line_2': '', 'city': 'ANYTOWN', 'state': 'CA', 'postal_code': '12345', 'address_type': 'Street Address'}
    expected_output = ('123 MAIN ST', '', 'ANYTOWN', 'CA', '12345', 'Street Address')
    assert standardize_address(input_address) == expected_output

def test_standardize_address_with_secondary_unit():
    input_address = "456 Elm St Apt 2, Smallville, KS 67890"
    expected_output = ('456 ELM ST', 'APT 2', 'SMALLVILLE', 'KS', '67890', 'Street Address')
    assert standardize_address(input_address) == expected_output

def test_standardize_incorrect_address():
    input_address = "This is not a real address"
    expected_output = ('', '', '', '', '', 'Ambiguous')
    assert standardize_address(input_address) == expected_output

import pytest
# Run the tests
if __name__ == "__main__":
    pytest.main()
