from datetime import datetime, timezone
import hashlib
import hmac
import time
import traceback

import pandas as pd
import numpy as np
from typing import Tuple, List, Optional


def get_timing(start_time):
    execution_time = (time.time() - start_time) / 60
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')
    print(f"Date/Time: {current_time}")
    print('Total Execution time in minutes: ' + str(execution_time))

def get_traceback(e):
    lines = traceback.format_exception(type(e), e, e.__traceback__)
    return ''.join(lines)

def create_hash(value):
    salt = 'votetracker'
    hash_value = hmac.new(bytes(salt , 'utf-8'), msg = bytes(value , 'utf-8'), digestmod = hashlib.sha256).hexdigest()
    return hash_value


def cast_date(date_string: str, from_formats: Optional[List[str]] = None) -> Tuple[Optional[str]]:
    """
    Converts a date string from various formats to the standard format '%Y-%m-%d'.

    Args:
    date_string (str): The date string to be converted.
    from_formats (List[str], optional): List of formats to try for parsing the date string. Defaults to ['%m-%d-%Y', '%Y'].

    Returns:
    Tuple[Optional[str]]: A tuple containing the formatted date string or np.nan if conversion fails.
    """

    if date_string is None:
        return (np.nan,)

    if from_formats is None:
        from_formats = ['%m-%d-%Y', '%Y']

    for from_format in from_formats:
        try:
            return datetime.strptime(date_string, from_format).strftime('%Y-%m-%d'),
        except ValueError:
            continue

    return (np.nan,)
