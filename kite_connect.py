import logging
from datetime import datetime

from dateutil.relativedelta import relativedelta, TH
from kiteconnect import KiteConnect
# import pickle


# key = 'msedx0q2eynocr2r'
# Kite = KiteConnect(api_key = 'msedx0q2eynocr2r')

# print("Login :", Kite.login_url())
# req_token = input("Enter :")

# print(req_token)

# Kite.set_access_token('ACCESS_TOKEN')
# print(Kite)
Qty         = 50
S1          = "NIFTY22APRFUT"
S2          = "NIFTY22APRFUT"
entryPrice  = 190
stopLoss    = 200
targetPrice = 170

# https://kite.zerodha.com/connect/login?v=3&api_key=
kite = KiteConnect(api_key="msedx0q2eynocr2r")
kite.set_access_token("GjjZbY6ddvJGYSPnL5g2TRlqwAHsetBZ")

# def getCMP(tradingSymbol):
#     quote = kite.quote(tradingSymbol)
#     if quote:
#         return quote[tradingSymbol]['last_price']
#     else:
#         return 0


# def get_symbols(expiry, name, strike, ins_type):
#     global instrumentsList

#     if instrumentsList is None:
#         instrumentsList = kite.instruments('NFO')

#     lst_b = [num for num in instrumentsList if num['expiry'] == expiry and num['strike'] == strike
#              and num['instrument_type'] == ins_type and num['name'] == name]
#     return lst_b[0]['tradingsymbol']

try:
    kite.place_order(tradingsymbol=S1, variety='regular', exchange='NFO', transaction_type='SELL',
                     quantity=Qty, order_type='MARKET', product='MIS')
except: print("Order placement failed")

# def place_order(tradingSymbol, price, qty, direction, exchangeType, product, orderType):
#     try:
#         orderId = kite.place_order(
#             variety=kite.VARIETY_REGULAR,
#             exchange=exchangeType,
#             tradingsymbol=tradingSymbol,
#             transaction_type=direction,
#             quantity=qty,
#             price=price,
#             product=product,
#             order_type=orderType)

#         logging.info('Order placed successfully, orderId = %s', orderId)
#         return orderId
#     except Exception as e:
#         logging.info('Order placement failed: %s', e.message)


# if __name__ == '__main__':
#     # Find ATM Strike of Nifty
#     atm_strike = round(getCMP('NSE:NIFTY 50'), -2)

#     next_thursday_expiry = datetime.today() + relativedelta(weekday=TH(1))

#     symbol_ce = get_symbols(next_thursday_expiry.date(), 'NIFTY', atm_strike, 'CE')
#     print(symbol_ce)
#     symbol_pe = get_symbols(next_thursday_expiry.date(), 'NIFTY', atm_strike, 'PE')
#     print(symbol_ce)

