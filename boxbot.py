# -*- coding: utf-8 -*-
"""
BOXBOT V0.1

An automated method of trading cryptocurrencies on Binance

Author: Joshua Parkinson
"""
import numpy as np
import pandas as pd
from binance.client import Client
from pandas import DataFrame
from Modules import DataCollection, TradeObject, DataProcessing
from Modules import utils as u


#STEP 1 - Log In
client=u.log_on()

#STEP 2 - Import data from Binance (currencies that are tradable with BTC)
coinData = DataCollection.retrieve_data_binance(client,
                                                'BTC',
                                                Client.KLINE_INTERVAL_30MINUTE,
                                                '1 day ago UTC')
                                                
#STEP 3 - Sort and Characterise the data - adding other data if required to 
#         produce the 'fullData' dictionary which the model can operate on
                                                
fullData = DataProcessing.produce_summary(coinData)
                                                

#STEP 4 - The predictive model needs to give forcasts (and probability)
#           for each coin

#STEP 5 - The decision model needs to produce a list of coins, stakes and
#           prices based on the forecast

#STEP 6 - Buy the coins using the tradeobject class

#STEP 7 - Enter a loop to monitor and update the trade objects, ready to sell