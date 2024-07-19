import MetaTrader5 as mt5
import json

mt5.initialize()
account_info = mt5.account_info()

def clean_account(account_info):
    return {
        "account": account_info.login,
        "leverage": account_info.leverage,
        "profit": account_info.profit,
        "equity": account_info.equity,
        "name": account_info.name,
        "server": account_info.server,
        "currency": account_info.currency
    }
