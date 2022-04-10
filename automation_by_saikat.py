from datetime import datetime
from kiteconnect import KiteConnect


# key = 'msedx0q2eynocr2r'
# Kite = KiteConnect(api_key = 'msedx0q2eynocr2r')

# print("Login :", Kite.login_url())
api_key = input("Api Key :")
access_token = input("Access Token :")

kite = KiteConnect(api_key)
kite.set_access_token(access_token)

stock = input("Name of Stock :")
Qty = input("Quantity :")
transaction_type = input("Type BUY/SELL to buy or sell :")
price = input("Price :")
if (transaction_type == 'BUY') :
    trigger_price = float (price) * 0.99
else :
    trigger_price = float (price) * 1.01
# data = kite.generate_session(access_token,api_key)
# kite.set_access_token(data["access_token"])
# print(data)

kite.place_order(tradingsymbol=stock, variety='regular', exchange='NSE', transaction_type=transaction_type,
                     quantity=Qty, order_type='MARKET', product='CNC', price=price, trigger_price=trigger_price)