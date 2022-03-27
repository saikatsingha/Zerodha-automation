from kiteconnect import KiteTicker               
from kiteconnect import KiteConnect  
api_key='************************'                      
api_secret=' *************************'   
kite=KiteConnect(api_key,api_secret)
kite.login_url()

import logging
logging.basicConfig(level=logging.DEBUG)
kite = KiteConnect(api_key=api_key)
token="HTJQmxal5dsFRQ5WbibO1B4MYvclB8OF"
data = kite.generate_session(token,api_secret)
kite.set_access_token(data["access_token"])
print(data)

from pprint import pprint
import pandas as pd 
import numpy as np
from datetime import datetime 
from IPython.display import clear_output
import time
from kiteconnect import KiteTicker  
from kiteconnect import KiteConnect

def livedata():
    while (True):
        km=datetime.now().minute
        ks=datetime.now().second
        if km%1==0 and ks==1:
            clear_output(wait=True)
            z=kite.historical_data(2977281, "2021-01-01", "2021-03-01","minute",0)
            za=pd.DataFrame(z)
            rsi_period=14
            chg=za["close"].diff(1)
            gain=chg.mask(chg<0,0) 
            loss=chg.mask(chg>0,0)
            avg_gain=gain.ewm(com=rsi_period-1,min_periods=rsi_period).mean()
            avg_loss=loss.ewm(com=rsi_period-1,min_periods=rsi_period).mean()
            rs =abs(avg_gain / avg_loss)
            rsi =100 -(100/(1+rs))
            za['rsi']=rsi
            print(za.iloc[-1,6])
            
                # rsi value            #prev high        #current high 
                
            if za.iloc[-1,6] > 30 and  za.iloc[-2,2]  >  za.iloc[-1,2]:
                
                kite.place_order( variety="regular",tradingsymbol='NTPC',quantity=1,exchange='NSE',order_type='LIMIT',price= 99.00,transaction_type='BUY',product='CNC')
                print("one order placed")
                break
            else:
                pass
            time.sleep(60)
livedata()

