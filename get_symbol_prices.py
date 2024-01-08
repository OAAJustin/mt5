# Import Dependencies
import MetaTrader5 as mt5
import json
import time

# List of assets to use
assets_to_use = ["EURUSD", "GBPUSD", "USDCAD", "AUDUSD", "USDJPY"]

# Get the prices of a symbol
def get_prices():
    symbols = mt5.symbols_get()
    return clean_prices(symbols)

# Get the symbol information of the name, ask price and bid price
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

# Price checker of the symbol 
def price_checker():
    prices = get_prices()
    while True:
        new_prices = get_prices()
        for price in new_prices:
            if prices[price] != new_prices[price]:
                print("{} price has changed ({} {})".format(price, new_prices[price]['bid'], new_prices[price]['ask']))
            time.sleep(1)

# Get the price info of the symbol
def price_info():
    # initialize MT5
    mt5.initialize()
    # Get prices from the database
    result = get_prices()
    # Run the price checker function to get the price values of the symbol
    price_checker()
    
if __name__ == "__main__":
    # Display the prices of the symbol
    price_info()