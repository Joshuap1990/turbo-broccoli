# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:58:17 2018

@author: joshua
"""

from binance.enums import *
from binance.client import Client
from pandas import DataFrame
from Modules import DataCollection, TradeObject, DataProcessing
from Modules import utils as u
import time


#STEP 1 - Log In
client = u.log_on()


'''order = client.create_test_order(
    symbol='LTCBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_MARKET,
    quantity=1)'''
    
    
tickers = float(client.get_ticker(symbol='BNBBTC')['lastPrice'])
balance = client.get_asset_balance(asset='BTC')

trade1=TradeObject.trade_binance(client,'BNBBTC',0.04,0.001282,0.001271)

#Enter a loop updating the price of the ticker - the object should sell itself
#at the predefined price
a=0
while True:
    time.sleep(5)
    a=a+1
    print('About the check the price...')
    print('Check Number {}'.format(a))
    latest_price = float(client.get_ticker(symbol='BNBBTC')['lastPrice'])
    print('Latest Price: {}'.format(latest_price))
    trade1.update(latest_price)
    
    #if asset has been sold then  need to quit the program!
    '''
    
'''#sellsell = trade1.sell()
order = client.order_market_sell(
                        symbol='BNBBTC',
                        quantity=0.04,
                        newOrderRespType='FULL')