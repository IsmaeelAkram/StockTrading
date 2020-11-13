from dotenv import load_dotenv
load_dotenv()
import robin_stocks as robinhood
import os
import yahoo_finance
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chalk

def get_active_stocks(browser):
    browser.get("https://finance.yahoo.com/most-active")
    active_stocks_names = browser.find_elements_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[1]/a')
    active_stocks_prices = browser.find_elements_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[3]/span')
    return dict(zip(active_stocks_names, active_stocks_prices))

# Login to Robinhood
# account = robinhood.login(os.getenv('ROBINHOOD_USER'), os.getenv('ROBINHOOD_PASS'))

# Setup selenium browser
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)

# Get active stocks
active_stocks = get_active_stocks(browser)
for stock in active_stocks:
    print(f"{stock.text}: {active_stocks[stock].text}")