import helper_functions
import pandas as pd
import numpy as np


def test_null_count():
    assert helper_functions.null_count(pd.DataFrame({'a': [0, 6, np.NaN],
                                                     'b': [np.NaN, np.NaN, -4]})) == 3


def test_split_dates():
    '''docstring'''
    df1 = helper_functions.split_dates(pd.Series(['09/12/2018', '11/23/2017']))
    assert df1.shape == (2, 3)
    assert df1['month'].to_list() == ['09', '11']
    assert df1['day'].to_list() == ['12', '23']
    assert df1['year'].to_list() == ['2018', '2017']


def test_list_2_series():
    '''docstring'''
    df2 = helper_functions.list_2_series([1, 2], pd.DataFrame())
    assert df2.shape == (2, 1)
    assert df2['list'].to_list() == [1, 2]
