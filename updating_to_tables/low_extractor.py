from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from date_format_extract import date_formatter


def daily_low_scrapper():

    stocks_for_today_low = []
    stocks_for_today_date_low = []
    result_for_today_low = []
    result_for_today2_low = {}
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "C:\chromedriver.exe"
    driver = webdriver.Chrome("C:\chromedriver.exe")
    driver.get(
        "https://www.nseindia.com/market-data/new-52-week-high-low-equity-market")
    x = driver.find_element(
        By.XPATH, '//*[@id="nseMarketStatus"]/div/div[1]/div[2]/div/div[2]/p/span')
    date_string = x.text
    date_string = date_formatter(date_string)
    max_low_stocks = len(driver.find_elements(
        By.XPATH, '//*[@id="weekLowTable"]/tbody/tr'))
    for i in range(1, max_low_stocks):
        next_page = driver.find_element(
            By.XPATH, '/html/body/div[10]/div/section/div/div/div[2]/div/div/nav/ul/li[2]/a').click()
        for element in driver.find_elements(By.XPATH, '//*[@id="weekLowTable"]/tbody/tr['+str(i)+']/td[1]'):
            stocks_for_today_low.append(element.text)
    for i in range(1, max_low_stocks):
        next_page = driver.find_element(
            By.XPATH, '/html/body/div[10]/div/section/div/div/div[2]/div/div/nav/ul/li[2]/a').click()
        for element in driver.find_elements(By.XPATH, '//*[@id="weekLowTable"]/tbody/tr['+str(i)+']/td[5]'):
            stocks_for_today_date_low.append(element.text)
    print(result_for_today_low)
    return (result_for_today_low, date_string, result_for_today2_low)


# REF for multipaging=https://levelup.gitconnected.com/efficiently-scraping-multiple-pages-of-data-a-guide-to-handling-pagination-with-selenium-and-3ed93857f596
daily_low_scrapper()
