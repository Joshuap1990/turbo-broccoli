# -*- coding: utf-8 -*-
"""
Backtesting functions

"""
from Modules import DataProcessing, PracticeTrade
import pandas as pd
from Strategies import LinearModel as model
from Train_Test import Backtest_functions as backtest

#Create a dictionary for importing all of the training data
testData = backtest.import_data()


maxlen=8904
numrows =13

activetrades=[]

myWallet=PracticeTrade.wallet(0.5)      #start life with half a bitcoin
tradestake = 0.05                       #how much bitcoin to spend each transaction


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
     
    #--------------------------------------------------------------------------
    #update the active trade objects to see if any need to be sold
    #--------------------------------------------------------------------------
    
    if len(activetrades)>0:
        for trade in activetrades:
            trade.update(buyholdsell,fullData)
        
            #need to remove item from list if it has been sold
            if trade.status=='INACTIVE':
                activetrades.remove(trade)
                
    
    #------------------------------------------------------------------------
    #Loop through current trade recommendations to see if any money can be
    # re-invested
    #=----------------------------------------------------------------------
        
    for index,row in buyholdsell.iterrows():
        
        
        #check current bitcoin balance to see if we have enough with margin
        balance = myWallet.balance()
                    
        if balance >= tradestake:
                    
        
            if row['recommendation']=='BUY':
                                
                activetrades.append(PracticeTrade.trade_practice(index,fullData,myWallet)
                
            
            
            elif row['recommendation']=='SELL':
                #we have reached the sell portion so there is no need to keep
                #on looping through
                break
 
#deposit everything back in the wallet           
for trade in activetrades:
    trade.sell(fullData)