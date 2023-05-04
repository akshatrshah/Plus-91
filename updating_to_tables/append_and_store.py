from buy_after_low import buyafterlow
import pandas as pd
from high_extractor import runner
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def update_table():
    buy_after_low_list = []
    # reading all sheets
    dfmain = pd.read_excel('./final_outputs/Result.xlsx', sheet_name=None)
    high_page = dfmain['High']
    low_page = dfmain['Low']
    buy_after_low_page = dfmain['Buy After Low']
    trend_buy_page = dfmain['Trend Buy']
    trend_sell_page = dfmain['Trend Sell']

    # cols_to_keep = ['STOCK NAME', 'DATE']
    # buyafterlowcsv = buyafterlowcsv.loc[:, cols_to_keep]
    # buyafterlowcsv.DATE = pd.to_datetime(buyafterlowcsv.DATE)
    # buyafterlowcsv.DATE = buyafterlowcsv.DATE.dt.date

    # column filtering
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
    # extractor
    x, y, z, a, b, c, d = runner.daily_high_low_scrapper()
    # x, y, z, a, b, c, d = [[], '26-04-2023', [], [], '', ['X', 'Y']]
    with open('dates_covered.txt', 'r') as file:
        date_covered = file.readlines()
        if (y == date_covered[2]):
            print()
        else:
            for i in x:
                row_data = {'STOCK NAME': i, 'DATE': y}
                new_df = pd.DataFrame(row_data, index=[0])
                high_page = pd.concat([high_page, new_df], ignore_index=True)

        high_page = high_page.sort_values(
            by=['STOCK NAME', 'DATE'], ascending=[True, True])

    with open('dates_covered.txt', 'r') as file:
        date_covered = file.readlines()

        if (y == date_covered[2]):
            print()
        else:

            for i in a:
                row_data = {'STOCK NAME': i, 'DATE': y}
                new_df = pd.DataFrame(row_data, index=[0])
                low_page = pd.concat([low_page, new_df], ignore_index=True)
        low_page = low_page.sort_values(
            by=['STOCK NAME', 'DATE'], ascending=[True, True])

        # trend buy
        for i in z:
            row_data = {'STOCK NAME': i, 'DATE': y}
            new_df = pd.DataFrame(row_data, index=[0])
            trend_buy_page = pd.concat(
                [trend_buy_page, new_df], ignore_index=True)
            # trend_buy_page = trend_buy_page.sort_values(
            #     by=['DATE'], ascending=[True])

        # trend sell
        for i in c:
            row_data = {'STOCK NAME': i, 'DATE': y}
            new_df = pd.DataFrame(row_data, index=[0])
            trend_sell_page = pd.concat(
                [trend_sell_page, new_df], ignore_index=True)
            # trend_sell_page = trend_sell_page.sort_values(
            #     by=['STOCK NAME', 'DATE'], ascending=[True, True])

        # buy after low
        buy_after_low_list = buyafterlow(y, d)
        print("Buy After Low: ", buy_after_low_list)
        # sending back to excel sheets
        with pd.ExcelWriter("./final_outputs/Result.xlsx", mode="a", engine="openpyxl", if_sheet_exists='replace') as writer:

        high_page.to_excel(writer, sheet_name="High", index=False)
        low_page.to_excel(writer, sheet_name="Low", index=False)
        # # buy_after_low_page.to_excel(
        # #     writer, sheet_name="Buy After Low", index=False)
        trend_buy_page.to_excel(
            writer, sheet_name="Trend Buy", index=False)
        trend_sell_page.to_excel(
            writer, sheet_name="Trend Sell", index=False)


# update_table()
