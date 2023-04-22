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

def run():
    mt5.initialize()
    result = get_prices()
    print(json.dumps(result, indent =2))
    
if __name__ == "__main__":
    run()