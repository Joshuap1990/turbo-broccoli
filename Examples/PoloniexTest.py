# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:07:13 2018

@author: joshua
"""

from poloniex import Poloniex
polo = Poloniex()
ticker = polo.returnTicker()['BTC_ETH']
data = polo.returnTradeHistoryPublic()['BTC_ETH']
print(data)
