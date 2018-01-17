# -*- coding: utf-8 -*-
"""
Binance Automated Trading Bot

Data Collection Routine

Author: J.Parkinson 
Date: 15th Jan 2018

"""

from binance.client import Client
from pandas import DataFrame
import pandas as pd
import numpy as np



# Define API data to allow access to Binance Account
client = Client('3XeGLhojcbAdd24B7Rmo66aF7YzRJDXyteOUMKhA7KlY6yvcIIw3VwUXt5qlZRrT',
                'LNNxRrsfV0yzbJY7rk6OU6viUXYlWVwUNQzjFoYT79Y4E4EwEFDuB0Wu2sH6yaGN',
                {"timeout": 40})



def retrieve_data(base_coin,interval,timespan):
    '''
    a function which returns a dataframe containing OHLCV volume over the specified period
    
    Inputs:
        base_coin - a coin that will be used to trade all other altcoins (e.g.'BTC')
        interval - The fidelity of the time series data
                Client.KLINE_INTERVAL_1MINUTE
                Client.KLINE_INTERVAL_30MINUTE
                Client.KLINE_INTERVAL_1WEEK
        timespan - the time over which the data can be collected. Can be relative
                or between two specific times
                e.g. "1 week ago UTC"
     '''           

    tickers=[]
    prices = client.get_all_tickers()

    for commodity in prices:
        if 'BNB' in commodity['symbol']:
            tickers.append(commodity['symbol'])
        
    #Create new dictionary containing all historical data traded in bitcoin
    allData = {}

    for ticker in tickers:
        allData[ticker]=pd.DataFrame(client.get_historical_klines(ticker,
                                                                    Client.KLINE_INTERVAL_30MINUTE,
                                                                    "1 week ago UTC"))
                                                                    
    return allData

alldata=retrieve_data('BNB',Client.KLINE_INTERVAL_30MINUTE,"1 week ago UTC")