import os
import pandas as pd
import pyarrow.parquet as pq


def read_extract_multiple(df, file_path) -> pd.DataFrame:
    print("Extracting Data...")
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            print(os.path.join(file_path, file))
            temp_df = pd.read_csv(os.path.join(file_path, file), sep='\t', dtype=str, low_memory=False, encoding_errors='ignore', on_bad_lines='skip')
            df = pd.concat([df, temp_df], ignore_index=True)

    return df.reset_index(drop=True)

def read_extract(df, file_path) -> pd.DataFrame:
    print("Extracting Data...")
    # get file names
    df = pq.read_table(source=file_path).to_pandas()

    return df.reset_index(drop=True)

def write_load(df, file_path) -> pd.DataFrame:
    print('Loading data...')
    print("...saving processed data")
    df.to_parquet(file_path, index=False, compression='gzip')

    return df.reset_index(drop=True)

def validate_data_contract(df, data_contract):
    print("Validating...", end=" ")

    vdf = pd.DataFrame()

    for key, possible_headers in data_contract.items():
        matching_columns = df.columns[df.columns.isin(possible_headers)]

        if len(matching_columns) > 0:
            vdf[key] = df[matching_columns[0]].str.strip()
        else:
            raise ValueError(f"Broken Contract! Missing columns for {key}: {possible_headers}")

    print("Done")
    return vdf.reset_index(drop=True)
