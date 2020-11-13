from dotenv import load_dotenv
load_dotenv()
import robin_stocks as robinhood
import os
import yahoo_finance

account = robinhood.login(os.getenv('ROBINHOOD_USER'), os.getenv('ROBINHOOD_PASS'))

