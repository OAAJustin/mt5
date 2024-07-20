import decimal

# List of assets to use
assets_to_use = [
    "EURUSD",
    "GBPUSD",
    "USDCAD",
    "AUDUSD",
    "USDJPY",
    "EURJPY"
    ]

def pip_value(asset):
   if "JPY" in asset:
       return decimal.Decimal(0.01)
   return decimal.Decimal(0.0001)

def digits(asset):
    if "JPY" in asset:
        return 3
    return 5