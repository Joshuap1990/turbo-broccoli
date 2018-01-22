# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:47:47 2018

@author: joshua
"""

import pandas as pd

for coin in coinData:
    coinData[coin].to_csv('{}.csv'.format(coin))