#region Import dependencies
import asyncio
import concurrent.futures
import MetaTrader5 as mt5
#endregion Import dependencies

#region TradeClient class
class TradeClient:
    def __init__(self, loop = None):
        self.loop = loop or asyncio.get_running_loop()
        self.pool = concurrent.futures.ThreadPoolExecutor()
        
    async def get_symbols(self):
        return await self.loop.run_in_executor(self.pool, lambda:mt5.symbols_get())
    
    async def get_account(self):
        return await self.loop.run_in_executor(self.pool, lambda:mt5.account_info())
    
    async def get_symbol(self, symbol_name):
        return await self.loop.run_in_executor(self.pool, lambda:mt5.symbol_info(symbol_name))
    
    async def order_send(self, request):
        return await self.loop.run_in_executor(self.pool, lambda:mt5.order_send(request))
    
    async def get_position_by_ticket(self, ticket):
        return await self.loop.run_in_executor(self.pool, lambda:mt5.positions_get(ticket=ticket))
    
    async def close_by_ticket(self, symbol, ticket):
        return await self.loop.run_in_executor(self.pool, lambda:mt5.Close(symbol = symbol, ticket = ticket))
    
    async def get_positions(self):
        return await self.loop.run_in_executor(self.pool, lambda:mt5.positions_get())
    
    async def get_history_deals(self, ticket):
        return await self.loop.run_in_executor(self.pool, lambda:mt5.history_deals_get(position = ticket))
    
    async def get_history_orders(self, ticket):
        return await self.loop.run_in_executor(self.pool, lambda:mt5.history_orders_get(position = ticket))
#endregion TradeClient class