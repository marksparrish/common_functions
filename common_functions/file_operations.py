import pandas as pd
import pyarrow.parquet as pq

def _extract(df) -> pd.DataFrame:
    print("Extracting Data...")
    # get file names
    df = pq.read_table(source=processed_data_path).to_pandas()
    return df.reset_index(drop=True)

def _load(df) -> pd.DataFrame:
    print('Loading data...')
    print("...saving processed data")
    df.to_parquet(processed_data_path, index=False, compression='gzip')

    return df.reset_index(drop=True)
