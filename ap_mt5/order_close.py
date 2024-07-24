#region Import Dependencies
import asyncio
from tools import unpack_closed_trade
#endregion Import Dependencies

#region Close trade function
async def close_trade(client, ticket):
    trade = await client.get_position_by_ticket(ticket)
    if len(trade) > 0:
        trade = trade[0]
        response = await client.close_by_ticket(trade.symbol, ticket)
        if response:
            closed_trade = await get_closed_trade(client, ticket)
            print(f"Trade closed at {closed_trade.close_time}")
            return closed_trade
    print("Trade not found!")
    # await client.close_by_ticket(trade.symbol, ticket)
#endregion Close trade function

#region Get closed trade
async def get_closed_trade(client, ticket):
    deals = await client.get_history_deals(ticket = ticket)
    history = await client.get_history_orders(ticket = ticket)
    
    return unpack_closed_trade(deals, history)
#endregion Get closed trade

