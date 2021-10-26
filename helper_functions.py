import pandas as pd

def split_dates(date_series):
    months = date_series.apply(lambda x: x[:2])
    days = date_series.apply(lambda x: x[3:5])
    years = date_series.apply(lambda x: x[6:])
    print(pd.DataFrame({'month': months, 'day': days, 'year': years}))

def list_2_series(list_2_series, df):
    df['list'] = list_2_series
    print(df)



print(list_2_series([1,2], pd.DataFrame()))
split_dates(pd.Series(['09/12/2018', '11/23/2017']))