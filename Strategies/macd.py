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
    macd, macdsignal, macdhist = talib.MACD(idata, fastperiod=12, slowperiod=26, signalperiod=9)
    real = talib.RSI(idata, timeperiod=14)
    plot(odata, macd, macdsignal, macdhist, real)
 

def plot(odata, macd, macdsignal, macdhist, real):
    pylab.plot(r, idata, 'b-', label="original")
    pylab.plot(r, odata, 'g-', label='MA')
    pylab.plot(r, macd, 'r-', label='MACD')
    pylab.plot(r, macdsignal, 'g-', label='macdsignal')
    pylab.plot(r, macdhist, 'b-', label ='macdhist')
    pylab.plot(r, real, 'g-', label='rsi')
    pylab.legend()
    pylab.show()

if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] == 'func':
        print('Using talib.func')
        func_example()
    else:
        print('Using talib.abstract')
        abstract_example()

#define strategy advice
        #set amcd thresholds
        #macd up = 0.025, if uptrend is above a certain threshold.
        #macd down = -0.025 if downtrend is below certain threshold
        #persistence = 1, how many data points indicate a slid trend.

        #if macd is above threshold then advice buy
        # if macd is below threshold then advice sell

        #if RSI is above 70 then advice overbought
        #if RSI is below 30 then advice oversold

        #if RSI is below 30 and MACD is above threshold up, then strong buy advice
        #if RSI is above 70 and MACD is below threshold downm then strong sell advice

        #if MACD is neither above or below thresholds and 30<RSI<70 , then sidewards trend
        #do nothing, hold position. 
        

