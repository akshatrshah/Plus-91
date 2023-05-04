from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from date_format_extract import date_formatter
import time
from dateutil import parser
from datetime import date


class runner():

    def daily_high_low_scrapper():
        universal_derivatives = open('.\\derivatives.csv', 'r')
        data = list(csv.reader(universal_derivatives, delimiter=","))
        all_derivatives = [row[0] for row in data]
        stocks_for_today_high = []
        stocks_for_today_date_high = []
        result_for_today_high = []
        result_for_today2_high = {}
        trend_buy = []
        stocks_for_today_low = []
        stocks_for_today_date_low = []
        result_for_today_low = []
        result_for_today2_low = {}
        trend_sell = []
        low_for_buy_after_low = []

        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver = webdriver.Firefox()
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "C:\chromedriver.exe"
        driver = webdriver.Chrome("C:\chromedriver.exe")
        driver.get(
            "https://www.nseindia.com/market-data/new-52-week-high-low-equity-market")
        driver.implicitly_wait(1000)
        x = driver.find_element(
            By.XPATH, '//*[@id="nseMarketStatus"]/div/div[1]/div[2]/div/div[2]/p/span')
        date_string = x.text
        date_string = date_formatter(date_string)
        max_high_stocks = len(driver.find_elements(
            By.XPATH, '//*[@id="weekHighTable"]/tbody/tr'))
        time.sleep(5)
        for i in range(1, max_high_stocks+1):
            for element in driver.find_elements(By.XPATH, '//*[@id="weekHighTable"]/tbody/tr['+str(i)+']/td[1]'):
                stocks_for_today_high.append(element.text)
        for i in range(1, max_high_stocks+1):
            for element in driver.find_elements(By.XPATH, '//*[@id="weekHighTable"]/tbody/tr['+str(i)+']/td[5]'):
                stocks_for_today_date_high.append(element.text)

        max_low_stocks = len(driver.find_elements(
            By.XPATH, '//*[@id="weekLowTable"]/tbody/tr'))
        driver.implicitly_wait(100)
        next_page = driver.find_element(
            By.XPATH, '/html/body/div[10]/div/section/div/div/div[2]/div/div/nav/ul/li[2]/a').click()
        time.sleep(8)
        for i in range(1, max_low_stocks+1):

            for element in driver.find_elements(By.XPATH, '//*[@id="weekLowTable"]/tbody/tr['+str(i)+']/td[1]'):
                stocks_for_today_low.append(element.text)
                low_for_buy_after_low.append(element.text)

        for i in range(1, max_low_stocks+1):
            # next_page = driver.find_element(
            #     By.XPATH, '/html/body/div[10]/div/section/div/div/div[2]/div/div/nav/ul/li[2]/a').click()
            # time.sleep(2)
            for element in driver.find_elements(By.XPATH, '//*[@id="weekLowTable"]/tbody/tr['+str(i)+']/td[5]'):
                stocks_for_today_date_low.append(element.text)

        driver.quit()
        res_high = {}
        for key in stocks_for_today_high:
            for value in stocks_for_today_date_high:
                res_high[key] = value
                stocks_for_today_date_high.remove(value)
                break
        for i in res_high:
            if i in all_derivatives:
                result_for_today2_high[i] = res_high[i]
                result_for_today_high.append(i)
        res_low = {}

        for key in stocks_for_today_low:
            for value in stocks_for_today_date_low:
                res_low[key] = value
                stocks_for_today_date_low.remove(value)
                break
        for i in res_low:
            if i in all_derivatives:
                result_for_today2_low[i] = res_low[i]
                result_for_today_low.append(i)
        print('High: ', result_for_today_high)
        print('Low: ', result_for_today_low)

        # # trend working
        # print(result_for_today2_high)
        # print(result_for_today2_low)
        for i in result_for_today2_high:
            if (((parser.parse(date_string))-(parser.parse(result_for_today2_high[i]))).days > 30):
                trend_buy.append(i)
        for i in result_for_today2_low:
            if (((parser.parse(date_string))-(parser.parse(result_for_today2_low[i]))).days > 30):
                trend_sell.append(i)
        print('trend_buy: ', trend_buy)
        print('trend_sell: ', trend_sell)
        return (result_for_today_high, date_string, trend_buy, result_for_today_low, date_string, trend_sell, low_for_buy_after_low)


# runner.daily_high_low_scrapper()
