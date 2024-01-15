from enum import Enum
import pandas as pd
import gender_guesser.detector as gender_detector
from gender_guesser.detector import Detector

class Gender(Enum):
    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'

def assume_gender(*names):
    """
    Guesses a person's gender based on their first and/or middle names.

    Parameters:
    names (str): Names to use for guessing gender.

    Returns:
    str: Guessed gender ('M', 'F', or 'U' for unknown).
    """
    detector = gender_detector.Detector(case_sensitive=False)
    try_again = {'mostly_female', 'mostly_male', 'unknown', 'andy'}
    guesses = []

    for name in names:
        if pd.notna(name) and len(name) > 1:
            guess = detector.get_gender(name, 'usa')
            if guess not in try_again:
                guesses.append(guess)

    # Decide gender based on collected guesses
    if 'male' in guesses:
        return Gender.MALE.value
    elif 'female' in guesses:
        return Gender.FEMALE.value
    else:
        return Gender.UNKNOWN.value
