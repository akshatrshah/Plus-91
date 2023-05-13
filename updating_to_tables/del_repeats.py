import pandas as pd


def c():
    dfmain = pd.read_excel('./final_outputs/Result.xlsx', sheet_name=None)
    high_page = dfmain['High']
    low_page = dfmain['Low']
    trend_buy_page = dfmain['Trend Buy']
    trend_sell_page = dfmain['Trend Sell']
    buy_after_low_page = dfmain['Buy After Low']

    cols_to_keep = ['STOCK NAME', 'DATE']
    high_page = high_page.loc[:, cols_to_keep]
    high_page.DATE = pd.to_datetime(high_page.DATE)
    high_page.DATE = high_page.DATE.dt.date

    cols_to_keep = ['STOCK NAME', 'DATE']
    low_page = low_page.loc[:, cols_to_keep]
    low_page.DATE = pd.to_datetime(low_page.DATE)
    low_page.DATE = low_page.DATE.dt.date

    cols_to_keep = ['STOCK NAME', 'DATE']
    buy_after_low_page = buy_after_low_page.loc[:, cols_to_keep]
    buy_after_low_page.DATE = pd.to_datetime(buy_after_low_page.DATE)
    buy_after_low_page.DATE = buy_after_low_page.DATE.dt.date

    cols_to_keep = ['STOCK NAME', 'DATE']
    trend_buy_page = trend_buy_page.loc[:, cols_to_keep]
    trend_buy_page.DATE = pd.to_datetime(trend_buy_page.DATE)
    trend_buy_page.DATE = trend_buy_page.DATE.dt.date

    cols_to_keep = ['STOCK NAME', 'DATE']
    trend_sell_page = trend_sell_page.loc[:, cols_to_keep]
    trend_sell_page.DATE = pd.to_datetime(trend_sell_page.DATE)
    trend_sell_page.DATE = trend_sell_page.DATE.dt.date

    high_page = high_page.drop_duplicates(
        subset=['STOCK NAME', 'DATE'], keep='first')
    low_page = low_page.drop_duplicates(
        subset=['STOCK NAME', 'DATE'], keep='first')
    trend_buy_page = trend_buy_page.drop_duplicates(
        subset=['STOCK NAME', 'DATE'], keep='first')
    trend_sell_page = trend_sell_page.drop_duplicates(
        subset=['STOCK NAME', 'DATE'], keep='first')
    buy_after_low_page = high_page.drop_duplicates(
        subset=['STOCK NAME', 'DATE'], keep='first')

    with pd.ExcelWriter("./final_outputs/Result.xlsx", mode="a", engine="openpyxl", if_sheet_exists='replace') as writer:

        high_page.to_excel(writer, sheet_name="High", index=False)
        low_page.to_excel(writer, sheet_name="Low", index=False)
        trend_buy_page.to_excel(
            writer, sheet_name="Trend Buy", index=False)
        trend_sell_page.to_excel(
            writer, sheet_name="Trend Sell", index=False)


# c()
