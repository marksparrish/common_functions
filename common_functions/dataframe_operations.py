import pandas as pd
from functools import reduce

def concatenate_columns(df, columns, sep=' '):
    """
    Concatenates multiple columns in a DataFrame into a single column.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the columns to concatenate.
    columns (list of str): The list of column names to concatenate.
    sep (str, optional): The separator to use between column values.

    Returns:
    pandas.Series: A Series representing the concatenated column.
    """
    if len(columns) <= 1:
        raise ValueError("At least two columns are required for concatenate_columns.")

    if df.empty:
        return pd.Series([], dtype='str')

    slist = [df[x].fillna('').astype('str') for x in columns]
    return reduce(lambda x, y: x.str.strip() + sep + y.str.strip(), slist[1:], slist[0])

def copy_column(*row, **kwargs):
    column = kwargs['fields']
    return column[0]
