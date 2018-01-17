# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 17:25:09 2018

@author: joshua
"""

from scipy import stats
import matplotlib.pyplot as plt

data=coinData['ADABTC']

x=data[0]
y=data[1]

plt.scatter(x,y)

slope, intercept, r_value, p_value, std_err =stats.linregress(data[0],data[1])

plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()