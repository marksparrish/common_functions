from common_functions.gender_guessing import assume_gender, Gender

def test_assume_gender_male():
    assert assume_gender('John') == Gender.MALE.value

def test_assume_gender_female():
    assert assume_gender('Julie') == Gender.FEMALE.value

def test_assume_gender_unknown():
    assert assume_gender('Xyz') == Gender.UNKNOWN.value

def test_assume_gender_with_multiple_names_male():
    assert assume_gender('John', 'Michael') == Gender.MALE.value

def test_assume_gender_with_multiple_names_female():
    assert assume_gender('Mary', 'Elizabeth') == Gender.FEMALE.value

def test_assume_gender_with_mixed_names():
    assert assume_gender('John', 'Mary') in {Gender.MALE.value, Gender.FEMALE.value}

def test_assume_gender_with_empty_names():
    assert assume_gender('', '') == Gender.UNKNOWN.value

import pytest
# Run the tests
if __name__ == "__main__":
    pytest.main()
