import pandas as pd
from dateutil import parser
from datetime import datetime, timedelta
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def buyafterlow(y, stocks_for_today_date_low):
    res = []
    last_3_days = []
    df = pd.read_csv('./final_outputs/buyafterlow.csv', index_col=False)
    dfmain = pd.read_excel('./final_outputs/Result.xlsx', sheet_name=None)
    df1 = dfmain['Buy After Low']
    cols_to_keep = ['STOCK NAME', 'DATE']
    df1 = df.loc[:, cols_to_keep]
    df1.DATE = pd.to_datetime(df1.DATE)
    df1.DATE = df1.DATE.dt.date
    last_3_days = pd.Series(df['DATE'].unique()).to_list()[-3:]
    stocks_on_date3 = df[df['DATE'] == last_3_days[0]]['STOCK NAME'].to_list()
    # df = df.set_index("STOCK NAME")
    # with open('dates_covered.txt', 'r') as file:
    #     lines = file.readlines()
    #     lines = [line.rstrip() for line in lines]

    # for i in lines:
    #     date_obj = datetime.strptime(i, '%Y-%m-%d')
    #     new_date_str.append(date_obj.strftime('%d-%m-%Y'))
    # stocks_on_date1 = df[df['DATE'] == last_3_days[0]]['STOCK NAME'].to_list()
    # stocks_on_date2 = df[df['DATE'] == last_3_days[1]]['STOCK NAME'].to_list()
    # stocks_on_date3 = df[df['DATE'] == last_3_days[2]]['STOCK NAME'].to_list()
    dates = pd.Series(df['DATE'].unique()).to_list()
    last_3_days = [x for x in dates if x == x]
    last_3_days = last_3_days[-3:]
    stocks_on_date1 = df[df['DATE'] == last_3_days[0]]['STOCK NAME'].to_list()
    stocks_on_date2 = df[df['DATE'] == last_3_days[1]]['STOCK NAME'].to_list()
    stocks_on_date3 = df[df['DATE'] == last_3_days[2]]['STOCK NAME'].to_list()
    # print('1', stocks_on_date1)
    # print('2', stocks_on_date2)
    # print('3', stocks_on_date3)
    for i in stocks_on_date1:
        if i not in stocks_on_date2:
            if i not in stocks_on_date3:
                if i not in stocks_for_today_date_low:
                    res.append(i)

    if len(dates) > 5:
        drop_for = dates[0]
        dates.pop(0)
        df = df.drop(df[df['DATE'] == drop_for].index)
    # print(res)
    # lines.append(y)
    # lines.pop(0)
    # with open('dates_covered.txt', 'w') as fp:
    #     for item in lines:
    #         fp.write(item+'\n')
    for i in res:
        row_data = {'STOCK NAME': i, 'DATE': y}
        new_df = pd.DataFrame(row_data, index=[0])
        df1 = pd.concat(
            [df1, new_df], ignore_index=True)
    with pd.ExcelWriter("./final_outputs/Result.xlsx", mode="a", engine="openpyxl", if_sheet_exists='replace') as writer:
        df1.to_excel(
            writer, sheet_name="Buy After Low", index=False)

    for i in stocks_for_today_date_low:
        row_data = {'STOCK NAME': i, 'DATE': y}
        new_df = pd.DataFrame(row_data, index=[0])
        df = pd.concat(
            [df, new_df], ignore_index=True)
    df.to_csv('./final_outputs/buyafterlow.csv', index=False)
    return res


# buyafterlow('2023-05-12', [])
