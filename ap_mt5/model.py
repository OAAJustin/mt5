#region Import Dependencies
from pydantic.dataclasses import dataclass
import decimal
import datetime
#endregion Import Dependencies

#region Price dataclass
@dataclass
class Price:
    asset:str
    bid: decimal.Decimal
    ask: decimal.Decimal
    tick_value: decimal.Decimal
#endregion Price dataclass

#region Account dataclass
@dataclass
class Account:
    account_number: int
    balance: decimal.Decimal
    profit: decimal.Decimal
    equity: decimal.Decimal
    leverage: int
    margin: decimal.Decimal
    currency: str
#endregion Account dataclass

#region Trade dataclass
@dataclass
class Trade:
    ticket: int
    asset: str
    order_type: int
    tp_pips: decimal.Decimal
    tp_price: decimal.Decimal
    sl_pips: decimal.Decimal
    sl_price: decimal.Decimal
    open_time: datetime.datetime
    close_time: datetime.datetime
    status: str
    pnl_pips: decimal.Decimal
    pnl_cash: decimal.Decimal
    swap: decimal.Decimal
    volume: decimal.Decimal
    comment: str
    magic: int
#endregion Trade dataclass

