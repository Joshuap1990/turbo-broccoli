#written by Dan Machen
#Date: 21/01/2018
#code to execute MACD trading strategy

#Step 1 - initiate strategy
#initiate the strategy with a neutral trading advice.
#python version 3.6.4

from __future__ import print_function

import sys
import talib
import numpy as np
from talib.abstract import Function
import pylab

#print('Python Version: ', sys.version)

#generate random data to simulate code against
TEST_LEN = int(sys.argv[1]) if len(sys.argv) > 1 else 100
r = np.arange(TEST_LEN)
idata = np.random.random(TEST_LEN)
#end of data generation

#def initialize(context):  
#    context.stock = symbol('SPY')

#def handle_data(context, data):  
#    close = history(36, '1d', 'close_price')[context.stock]  
#    macd, macdsignal, macdhist = talib.MACD(close, 12, 26, 9)  
#    macd = macd[-1]  
#    macdsignal = macdsignal[-1]  
#    record(macd = macd, macdsignal = macdsignal) 

def func_example():
    odata = talib.MA(idata)
    macd, macdsignal, macdhist = talib.MACD(idata)
    plot(odata, macd, macdsignal, macdhist)

#def abstract_example():
#    sma = Function('sma')
#    input_arrays = sma.get_input_arrays()
#    for key in input_arrays.keys():
#        input_arrays[key] = idata
#    sma.set_input_arrays(input_arrays)
#    odata = sma(30) # timePeriod=30, specified as an arg
#
#    macd = Function('macd', input_arrays)
#    macd.parameters = {
#        'slowperiod': 26,
#        'fastperiod': 12,
#        'signal': 9
#    }
#    macd, macdsignal, macdhist = macd() # multiple output values unpacked (these will always have the correct order)
#    plot(odata, macd, macdsignal, macdhist)

def plot(odata, macd, macdsignal, macdhist):
    pylab.plot(r, idata, 'b-', label="original")
    pylab.plot(r, odata, 'g-', label='MA')
    pylab.plot(r, macd, 'r-', label='MACD')
    pylab.plot(r, macdsignal, 'r-', label='macdsignal')
    pylab.plot(r, macdhist, 'r-', label ='macdhist')
    pylab.legend()
    pylab.show()

if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] == 'func':
        print('Using talib.func')
        func_example()
    else:
        print('Using talib.abstract')
        abstract_example()

