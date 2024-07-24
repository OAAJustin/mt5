#region Import dependencies
import decimal
#endregion Import dependencies

#region Pip value function
def pip_value(asset):
   if "JPY" in asset:
       return decimal.Decimal(0.01)
   return decimal.Decimal(0.0001)
#endregion Pip value function

#region Assets digit value
def digits(asset):
    if "JPY" in asset:
        return 3
    return 5
#endregion Assets digit value