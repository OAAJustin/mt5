import MetaTrader5 as mt5
import json
import time

assets_to_use = ["EURUSD", "GBPUSD", "USDCAD", "AUDUSD", "USDJPY"]

def get_prices():
    symbols = mt5.symbols_get()
    return clean_prices(symbols)

def clean_prices(prices):
    return_value = {}
    for symbol in prices:
        if symbol.name in assets_to_use:
            return_value[symbol.name]={
                'asset':symbol.name,
                'ask':symbol.ask,
                'bid':symbol.bid
            }
    return return_value

def price_checker():
    prices = get_prices()
    while True:
        new_prices = get_prices()
        for price in new_prices:
            if prices[price] != new_prices[price]:
                print("{} price has changed ({} {})".format(price, new_prices[price]['bid'], new_prices[price]['ask']))
            time.sleep(1)

def run():
    mt5.initialize()
    result = get_prices()
    price_checker()
    
if __name__ == "__main__":
    run()