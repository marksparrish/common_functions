import sys
import hashlib
import hmac
from datetime import datetime
sys.path.append('/app')

import gender_guesser.detector as gender_detector
import numpy as np
import pandas as pd
import usaddress
from config import GOOGLE_API_KEY
from geopy import GoogleV3
# from geopy import Nominatim
from pandarallel import pandarallel

from scourgify import normalize_address_record

guesser = gender_detector.Detector(case_sensitive=False)

geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
# geolocator = Nominatim(user_agent="votetracker")

pandarallel.initialize(progress_bar=True, verbose=0)

def transformations(df, transforms = []) -> pd.DataFrame:
    for transformation in transforms:
        final = transformation['column']
        action = transformation['action']['type']
        raw = transformation['action']['column']
        kwargs = transformation['action']['kwargs']
        series = transformation['action']['series']

        print(f"...{final} using {action} from {raw} with {kwargs}")
        action = globals()[action]
        if series == 1:
            df[final] = df[raw].parallel_apply(lambda row: action(row, additional=kwargs), axis=1, result_type='expand')
            # df[final] = df[raw].apply(lambda row: action(row, additional=kwargs), axis=1, result_type='expand')
        else:
            df[final] = [ action(fields=row, additional=kwargs) for row in df[raw].to_numpy(na_value='')]

    return df.reset_index(drop=True)
