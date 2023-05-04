from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

all_derivatives = []


def derivatives_scrapper():
    driver = webdriver.Firefox()
    driver.get(
        "https://www.nseindia.com/products-services/equity-derivatives-list-underlyings-information")
    # driver.implicitly_wait(500)
    max_high_stocks = len(driver.find_elements(
        By.XPATH, '/html/body/div[9]/div/section/div/div/div/div/div/div/div[1]/div[4]/div/div/table/tbody/tr'))
    for i in range(7, max_high_stocks+1):
        for element in driver.find_elements(By.XPATH, '/html/body/div[9]/div/section/div/div/div/div/div/div/div[1]/div[4]/div/div/table/tbody/tr['+str(i)+']/td[3]'):
            all_derivatives.append(element.text)
    driver.quit()

    data = {'Derivative Stocks Name': all_derivatives}
    df = pd.DataFrame(data)
    df.to_csv('derivatives.csv', header=False, index=False)


derivatives_scrapper()
