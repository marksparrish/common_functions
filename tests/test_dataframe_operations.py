import pandas as pd
import pytest
from common_functions.dataframe_operations import concatenate_columns

def test_concatenate_columns_basic():
    df = pd.DataFrame({
        'col1': ['a', 'b', 'c'],
        'col2': ['1', '2', '3'],
        'col3': ['x', 'y', 'z']
    })
    expected = pd.Series(['a 1 x', 'b 2 y', 'c 3 z'])
    result = concatenate_columns(df, ['col1', 'col2', 'col3'])
    pd.testing.assert_series_equal(result, expected)

def test_concatenate_columns_with_missing_values():
    df = pd.DataFrame({
        'col1': ['a', None, 'c'],
        'col2': ['1', '2', None]
    })
    expected = pd.Series(['a 1', ' 2', 'c '])
    result = concatenate_columns(df, ['col1', 'col2'])
    pd.testing.assert_series_equal(result, expected)

def test_concatenate_columns_with_custom_separator():
    df = pd.DataFrame({
        'col1': ['a', 'b', 'c'],
        'col2': ['1', '2', '3']
    })
    expected = pd.Series(['a-1', 'b-2', 'c-3'])
    result = concatenate_columns(df, ['col1', 'col2'], sep='-')
    pd.testing.assert_series_equal(result, expected)

import pytest
# Run the tests
if __name__ == "__main__":
    pytest.main()
