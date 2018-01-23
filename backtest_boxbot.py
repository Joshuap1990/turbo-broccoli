# -*- coding: utf-8 -*-
"""
Backtesting functions

"""
from Modules import DataCollection, TradeObject, DataProcessing
import pandas as pd
from Strategies import LinearModel as model
from Train_Test import Backtest_functions as backtest

#Create a dictionary for importing all of the training data
testData = backtest.import_data()


maxlen=8904
numrows =13


#iterate through the whole dataset, frame by frame
for number in range(1,(maxlen-numrows)):
    
    print(number)
    
    #produce the market data for this freze frame
    current_data={}
    
    for asset in testData.keys():
            
        current_data[asset]=testData[asset].iloc[range(number,(number+numrows))]
        
    #---------------------------------------------------------
    #      Backtest the data held in current_data
    #--------------------------------------------------------        
    
    fullData = DataProcessing.produce_summary(current_data)
    

    predictionData = model.model_control(fullData)

    #STEP 5 - The decision model needs to produce a list of coins, stakes and
    #           prices based on the forecast

    buyholdsell=model.decision(predictionData)