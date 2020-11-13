from stock import Stock
import chalk

def get_active_stocks(browser):
    print(chalk.green("Getting active stocks..."))
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