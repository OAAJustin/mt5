# Import Dependencies
import MetaTrader5 as mt5

# Get the terminal information
def terminal_info():

    # Initialize MetaTrader5
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()
        
    # Terminal Info as Dictionary
    terminal_info_dict = mt5.terminal_info()._asdict()
    
    # Display the terminal info 
    for property in terminal_info_dict:
        print(f"{property} : {terminal_info_dict[property]}")

if __name__ == '__main__':
    # Display header
    print("This Terminal's Info\n")
    
    # Display terminal info
    terminal_info()


""" What information do I want from the account info? 
    - connected
    - dlls_allowed
    - trade_allowed
    - build
    - path
    - data_path
"""
