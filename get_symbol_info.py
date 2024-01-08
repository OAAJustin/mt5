# Import Dependencies
import MetaTrader5 as mt5

def get_symbol_info(symbol):
    # Initialize MetaTrader5
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()
    
    # Trading Account Info as Dictionary
    symbol_info_dict = mt5.symbol_info(symbol)._asdict()

    # List the values within the dictionary 
    for property in symbol_info_dict:
        print(f"{property} = {symbol_info_dict[property]}")
    
if __name__ == '__main__':
    # Input the symbol info to get
    symbol = input("Choose a symbol: ").upper()
    
    # Display Header
    print(f'Symbol info for {symbol}.\n')
    
    # Display the symbol info 
    get_symbol_info(symbol)