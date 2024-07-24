from tools_pips import pip_value, digits
import MetaTrader5 as mt5
from decimal import Decimal
from model import Trade
import datetime

def unpack_open_trade(trade):
    tp_pips, sl_pips, pnl_pips = 0, 0, 0
    pip = pip_value(trade.symbol)
    open_price = Decimal(trade.price_open)
    current_price = Decimal(trade.price_current)
    swap = Decimal(trade.swap)
    ticket = trade.identifier
    time = trade.time
    profit = Decimal(trade.profit) 
    volume = Decimal(trade.volume)
    sl = Decimal(trade.sl)
    tp = Decimal(trade.tp)
    
    if trade.type == mt5.ORDER_TYPE_BUY:
        tp_pips = 0 if tp == 0 else (tp - open_price) / pip
        sl_pips = 0 if sl == 0 else (open_price - sl) / pip
        pnl_pips = (current_price - open_price) / pip
        
    if trade.type == mt5.ORDER_TYPE_SELL:
        tp_pips = 0 if tp == 0 else (open_price - tp) / pip
        sl_pips = 0 if sl == 0 else (sl - open_price) / pip
        pnl_pips = (open_price - current_price) / pip 
        
    open_trade = Trade(
        ticket = ticket,
        asset = trade.symbol,
        order_type = trade.type,
        tp_pips = round(tp_pips, 1),
        sl_pips = round(sl_pips, 1),
        tp_price = round(tp, digits(trade.symbol)),
        sl_price = round(sl,digits(trade.symbol)),
        open_time = datetime.datetime.fromtimestamp(time),
        close_time = datetime.datetime(1970, 1, 1),
        open_price = round(open_price, digits(trade.symbol)),
        close_price = round(current_price, digits(trade.symbol)),
        status = "OPEN",
        pnl_pips = round(pnl_pips, 1),
        pnl_cash = round(profit, 2),
        swap = swap,
        volume = volume,
        comment = trade.comment,
        magic = trade.magic
    )
    
    return open_trade

def unpack_closed_trade(deals, history):
    entry = history[0]
    exit = history[1]
    trade = deals[1]
    tp_pips, sl_pips, pnl_pips = 0, 0, 0
    ticket = entry.ticket
    order_type = entry.type
    symbol = entry.symbol
    open_price = Decimal(deals[0].price)
    close_price = Decimal(trade.price)
    pnl_cash = Decimal(trade.price)
    open_time = entry.time_setup
    close_time = exit.time_setup
    swap = Decimal(trade.swap)
    volume = Decimal(trade.volume)
    comment = deals[0].comment
    magic = entry.magic
    
    if exit.tp == 0:
        tp = Decimal(entry.tp)
    else:
        tp = Decimal(exit.tp)
    
    if exit.sl == 0:
        sl = Decimal(entry.sl)
    else:
        sl = Decimal(entry.sl)
        
    pip = pip_value(symbol)
    
    if order_type == mt5.ORDER_TYPE_BUY:
        tp_pips = (tp - open_price) / pip if tp > 0 else 0
        sl_pips = (open_price - sl) / pip if sl > 0 else 0
        pnl_pips = (close_price - open_price) / pip
        
    if order_type == mt5.ORDER_TYPE_SELL:
        tp_pips = (open_price - tp) / pip if tp > 0 else 0
        sl_pips = (sl - open_price) / pip if sl > 0 else 0
        pnl_pips = (open_price - close_price) / pip
        
    closed_trade = Trade(
        ticket = ticket, 
        asset = symbol,
        order_type = order_type,
        tp_pips = round(tp_pips, 1),
        sl_pips = round(sl_pips, 1),
        tp_price = round(tp, digits(symbol)),
        sl_price = round(sl, digits(symbol)),
        open_time = datetime.datetime.fromtimestamp(open_time),
        close_time = datetime.datetime.fromtimestamp(close_time),
        open_price = round(open_price, digits(symbol)),
        close_price = round(close_price, digits(symbol)),
        status = "CLOSED",
        pnl_pips = round(pnl_pips, 1),
        pnl_cash = round(pnl_cash, 2),
        swap = swap,
        volume = round(volume, 2),
        comment = comment,
        magic = magic
    )
    
    return closed_trade