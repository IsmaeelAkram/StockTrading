from dotenv import load_dotenv
load_dotenv()
import robin_stocks as robinhood
import os
import yahoo_finance
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Login to Robinhood
# account = robinhood.login(os.getenv('ROBINHOOD_USER'), os.getenv('ROBINHOOD_PASS'))

# Setup selenium browser
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)

# Get most active stocks
browser.get("https://finance.yahoo.com/most-active")