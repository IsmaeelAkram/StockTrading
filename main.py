from dotenv import load_dotenv
load_dotenv()
import robin_stocks as robinhood
import os
import sys
import yahoo_finance
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chalk

from stock import Stock
from helpers import get_active_stocks, get_cheapest_stock

# Login to Robinhood
# print(chalk.green("Logging into Robinhood..."))
# account = robinhood.login(os.getenv('ROBINHOOD_USER'), os.getenv('ROBINHOOD_PASS'))

# Setup selenium browser
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)


# Get active stocks
stocks = get_active_stocks(browser)

# Get cheapest stock
cheapest_stock = get_cheapest_stock(stocks)
print(chalk.green("Cheapest stock is: ") + f"{cheapest_stock.symbol} ({cheapest_stock.name}) (${cheapest_stock.price})")