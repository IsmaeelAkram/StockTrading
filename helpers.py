from stock import Stock
import chalk
import sys
import sqlite3

db = sqlite3.connect("stocks.db")
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stocks (
        symbol TEXT PRIMARY KEY,
        name TEXT,
        shares REAL,
        initial_price REAL
    )
""")
db.commit()

def get_active_stocks(browser):
    print(chalk.blue("Getting active stocks from Yahoo..."))
    browser.get("https://finance.yahoo.com/most-active")
    active_stocks_symbols = browser.find_elements_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[1]/a')
    active_stocks_names = browser.find_elements_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/div/div[2]/div[1]/table/tbody/tr/td[2]')
    active_stocks_prices = browser.find_elements_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[3]/span')
    active_stocks_dict = dict(zip(active_stocks_symbols, zip(active_stocks_names, active_stocks_prices)))
    active_stocks = []
    for stock in active_stocks_dict:
        symbol = stock.text
        name = active_stocks_dict[stock][0].text
        price = float(active_stocks_dict[stock][1].text)
        active_stocks.append(Stock(symbol, name, price))
    return active_stocks

def get_cheapest_stock(stocks):
    print(chalk.blue("Getting cheapest of active stocks..."))
    stock_prices = []
    for stock in stocks:
        stock_prices.append(stock.price)
    min_stock_price = min(stock_prices)

    cheapest_stock = None
    for stock in stocks:
        if(min_stock_price is stock.price):
            cheapest_stock = stock
    if(cheapest_stock is None):
        print(chalk.red("Could not find cheapest of active stocks!"))
        sys.exit(1)
    else:
        return cheapest_stock

# Trading stocks
def get_stocks():
    cursor.execute("SELECT * from stocks")
    return cursor.fetchall()

def buy_stock(stock: Stock, shares: float):
    print(chalk.blue(f"Buying {shares} shares of stock {stock.symbol} for ${shares*stock.price}"))
    cursor.execute(f'INSERT INTO stocks VALUES ("{stock.symbol}", "{stock.name}", {shares}, {stock.price})')
    db.commit()
    print(chalk.green("Success!"))

def sell_stock(stock_symbol: str, current_shares: float, selling_shares: float):
    print(chalk.blue(f"Selling {selling_shares} shares of stock {stock_symbol}..."))
    cursor.execute(f'UPDATE stocks SET shares = {current_shares - selling_shares} WHERE symbol = "{stock_symbol}"')
    db.commit()
    print(chalk.green("Success!"))