import pytest
from common_functions.voter_functions import confidential_voter, confidential_address  # Replace 'your_module' with the name of your module

def test_confidential_voter():
    # Test with valid inputs
    assert confidential_voter(['XX']) == ('YES',)
    assert confidential_voter(['']) == ('NO',)
    assert confidential_voter(['Some Other Value']) == ('NO',)

    # Test with edge cases
    assert confidential_voter([]) == ('NO',)
    assert confidential_voter(['XX', 'Extra Value']) == ('YES',)

def test_confidential_address():
    # Test with valid inputs
    assert confidential_address(['XX']) == 'YES'
    assert confidential_address(['']) == 'NO'
    assert confidential_address(['Some Other Value']) == 'NO'

    # Test with edge cases
    assert confidential_address([]) == 'NO'
    assert confidential_address(['XX', 'Extra Value']) == 'YES'

# Run the tests
if __name__ == "__main__":
    pytest.main()
