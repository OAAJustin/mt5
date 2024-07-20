# Import Dependencies
import MetaTrader5 as mt5
from client import TradeClient
from config import assets_to_use, digits
from order_open import open_buy, open_sell
from order_close import get_closed_trade, close_trade
import tools
import asyncio
import json
import time

# Get the prices of a symbol
async def get_prices(trade_client):
    symbols = await trade_client.get_symbols()
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

# Clean the account information
def clean_account(account):
    return {
        "account_number": account.login,
        "balance": account.balance,
        "profit": account.profit,
        "equity": account.equity,
        "margin": account.margin,
        "currency": account.currency,
        "leverage": account.leverage
    }

# Price check the symbol 
async def price_checker(client):
    prices = await get_prices(client)
    while True:
        new_prices = await get_prices(client)
        for price in new_prices:
            if prices[price] != new_prices[price]:
                print("{} price has changed ({} {})".format(price, new_prices[price]['bid'], new_prices[price]['ask']))
            prices[price] = new_prices[price]

# Get account information          
async def account(client):
    account = await client.get_account()
    # print(json.dumps(clean_account(account), indent = 2))
    return clean_account(account)

# Open trades
async def open_trade(client):
    for i in range(50):
        await open_buy(client, "EURUSD", 10, 10)
        await open_sell(client, "EURUSD", 10, 10)
        
# Close trades
async def close_all(client):
    trades = await client.get_positions()
    for trade in trades:
        t = tools.unpack_open_trade(trade)
        print(f"We are about to close trade{t.ticket}")
        await close_trade(client, t.ticket)
        print(f"We have closed trade {t.ticket}")
    
# Show open trades
async def show_open_trades(client):
    trades = await client.get_positions()
    print(trades)

## MAIN
# Get the price info of the symbol
async def main():
    mt5.initialize() # initialize MT5
    client = TradeClient() # Trade Client
    await open_trade(client)
    time.sleep(3)
    await close_all(client)
    
if __name__ == "__main__":
    asyncio.run(main()) # Display the prices of the symbol