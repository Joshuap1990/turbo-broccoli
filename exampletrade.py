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


#STEP 1 - Log In
client = u.log_on()


'''order = client.create_test_order(
    symbol='LTCBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_MARKET,
    quantity=1)'''
    
    
tickers = float(client.get_ticker(symbol='BNBBTC')['lastPrice'])
balance = client.get_asset_balance(asset='BTC')

trade1=TradeObject.trade_binance(client,'BNBBTC',0.04,0.0014,0.0010)
sellsell = trade1.sell()
'''order = client.order_market_sell(
                        symbol='BNBBTC',
                        quantity=0.04,
                        newOrderRespType='FULL')'''