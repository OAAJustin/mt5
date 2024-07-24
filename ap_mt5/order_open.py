#region Import Dependencies
from tools_pips import pip_value
import decimal
import MetaTrader5 as mt5
#endregion Import Dependencies

#region Open Buy Function
async def open_buy(client, symbol, tp_pips, sl_pips):
    symbol_info = await client.get_symbol(symbol)
    tick_value = symbol_info.trade_tick_value
    pip = decimal.Decimal(pip_value(symbol))
    
    price = decimal.Decimal(symbol_info.ask)
    sl = price - (sl_pips * pip)
    tp = price + (tp_pips * pip)
    
    request = {
        "type": mt5.ORDER_TYPE_BUY,
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": float(0.01),
        "price": float(price),
        "sl": float(sl),
        "tp": float(tp),
        "magic": 123,
        "comment": "Test Trade"
    }
    
    return await client.order_send(request)
#endregion Open Buy Function

#region Open Sell Function
async def open_sell(client, symbol, tp_pips, sl_pips):
    symbol_info = await client.get_symbol(symbol)
    tick_value = symbol_info.trade_tick_value
    pip = decimal.Decimal(pip_value(symbol))
    
    price = decimal.Decimal(symbol_info.bid)
    sl = price + (sl_pips * pip)
    tp = price - (tp_pips * pip)
    
    request = {
        "type": mt5.ORDER_TYPE_SELL,
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": float(0.01),
        "price": float(price),
        "sl": float(sl),
        "tp": float(tp),
        "magic": 123,
        "comment": "Test Trade"
    }
    
    return await client.order_send(request)
#endregion Open Sell Function 