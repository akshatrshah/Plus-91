from ast import parse
from datetime import datetime
import pandas as pd


def b():
    new_date_str = []
    df = pd.read_csv('./final_outputs/buyafterlow.csv', index_col=False)
    cols_to_keep = ['STOCK NAME', 'DATE']
    df1 = df.loc[:, cols_to_keep]
    df1.DATE = pd.to_datetime(df1.DATE)
    df1.DATE = df1.DATE.dt.date
    dates = pd.Series(df['DATE'].unique()).to_list()
    if len(dates) > 5:
        drop_for = dates[0]
        dates.pop(0)
        df = df.drop(df[df['DATE'] == drop_for].index)
    last_3_days = [x for x in dates if x == x][-3:]
    # last_3_days = last_3_days[-3:]
    stocks_on_date3 = df[df['DATE'] == last_3_days[2]]['STOCK NAME'].to_list()
    print(df)


b()
