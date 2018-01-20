# -*- coding: utf-8 -*-
"""
Cryptocurrency Trading Bot

Data Collection and Sorting Routines
These routines belong in Step 1 of the trading process

Author: Joshua Parkinson
Date: 15th Jan 2018
"""

def retrieve_data_binance(client,base_coin,interval,timespan):
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
    from binance.client import Client
    from pandas import DataFrame
    import pandas as pd
    import numpy as np
    import datetime as dt

    tickers=[]
    prices = client.get_all_tickers()

    for commodity in prices:
        if base_coin in commodity['symbol']:
            tickers.append(commodity['symbol'])
        
    #Create new dictionary containing all historical data traded in bitcoin
    allData = {}

    for ticker in tickers:
        data=pd.DataFrame(client.get_historical_klines(ticker,
                                                       interval,
                                                       timespan))
        #a lot of the data is a str - convert to float for 
        # further processing                                               
        allData[ticker]=data.astype(float)
        
                                                                    
    return allData