# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import csv
# from date_format_extract import date_formatter
# import time
# from selenium.webdriver.support.select import Select
# from dateutil import parser
# from datetime import date


# class runner():

#     def daily_high_low_scrapper():
#         universal_derivatives = open('derivatives.csv', 'r')
#         data = list(csv.reader(universal_derivatives, delimiter=","))
#         all_derivatives = [row[0] for row in data]
#         # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         # driver = webdriver.Firefox()
#         options = webdriver.ChromeOptions()
#         options.add_argument('--ignore-certificate-errors')
#         options.add_argument("--test-type")
#         options.binary_location = "C:\chromedriver.exe"
#         driver = webdriver.Chrome("C:\chromedriver.exe")
#         driver.get(
#             "https://www.nseindia.com/market-data/new-52-week-high-low-equity-market")
#         driver.implicitly_wait(1000)
#         next_page = driver.find_element(
#             By.XPATH, '/html/body/div[10]/div/section/div/div/div[2]/div/div/nav/ul/li[2]/a').click()
#         time.sleep(2)
#         next_page2 = driver.find_element(
#             By.XPATH, '//*[@id="secutities_less20"]').click()

#         sel = Select(driver.find_element(
#             By.XPATH, '//select[@id="secutities_less20"]'))
#         sel.select_by_value('dataLtpLess20')
#         time.sleep(10)
#         max_low_stocks = len(driver.find_elements(
#             By.XPATH, '//*[@id="weekLowTable"]/tbody/tr'))
#         print(max_low_stocks)


# runner.daily_high_low_scrapper()
import pandas as pd
buyafterlowcsv = pd.read_csv(
    './final_outputs/buyafterlow.csv', index_col=False)
cols_to_keep = ['STOCK NAME', 'DATE']
buyafterlowcsv = buyafterlowcsv.loc[:, cols_to_keep]
buyafterlowcsv.DATE = pd.to_datetime(buyafterlowcsv.DATE)
buyafterlowcsv.DATE = buyafterlowcsv.DATE.dt.date
row_data = {'STOCK NAME': 'X', 'DATE': '25-04-2023'}
new_df = pd.DataFrame(row_data, index=[0])
buyafterlowpage = pd.concat(
    [buyafterlowcsv, new_df], ignore_index=True)
print(buyafterlowpage.tail())
buyafterlowpage.to_csv('./final_outputs/buyafterlow.csv', index=False)
buyafterlowcsv = pd.read_csv('./final_outputs/buyafterlow.csv')
print(buyafterlowcsv.tail())
