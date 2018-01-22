# -*- coding: utf-8 -*-
"""
Retrieve Training Data from various sources
"""


from binance.client import Client
from Modules import DataCollection, TradeObject, DataProcessing
from Modules import utils as u

#STEP 1 - Log In to Binance
client = u.log_on(9999)

#STEP 1b - Choose the base currency that will be used for the exchange
baseCurrency = 'BTC'

#STEP 2 - Import data from Binance (currencies that are tradable with BTC)
coinData = DataCollection.retrieve_data_binance(client,
                                                baseCurrency,
                                                Client.KLINE_INTERVAL_5MINUTE,
                                                '1 month ago UTC')