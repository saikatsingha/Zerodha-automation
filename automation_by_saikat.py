from datetime import datetime
from kiteconnect import KiteConnect


# key = 'msedx0q2eynocr2r'
# Kite = KiteConnect(api_key = 'msedx0q2eynocr2r')

# print("Login :", Kite.login_url())
api_key = input("Api Key :")
access_token = input("Access Token :")

kite = KiteConnect(api_key)
kite.set_access_token(access_token)
print(kite)
