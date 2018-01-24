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
numrows =50                            #for a 5 minute frequency, what is
                                        #the number of rows that are 
                                        #required to capture 1h data

activetrades=[]                         # Start an empty list to capture active
                                        #trades

portfolio=[]                            #create a list to store the full value
                                        # of the portfolio

myWallet=PracticeTrade.wallet(0.5)      #start life with half a bitcoin
tradestake = 0.1                       #how much bitcoin to spend each transaction


#iterate through the whole dataset, frame by frame
for number in range(1,(maxlen-numrows)):
    
    print(number)
    
    #produce the market data for this freze frame
    current_data={}
    
    for asset in testData.keys():
            
        current_data[asset]=testData[asset].iloc[range(number,(number+numrows))]
        current_data[asset].columns=['starttime','open','high','low','close','volume','endtime','data1','data2','data3','data4','data5']
        
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
        balance = float(myWallet.balance)
                    
        if balance > tradestake:
                    
        
            if row['recommendation']=='BUY':
                 
                #create a new trade object and add it to the active 
                # trade list
                activetrades.append(PracticeTrade.trade_practice(index,
                                                                 fullData,
                                                                 myWallet,
                                                                 tradestake))
            elif row['recommendation']=='SELL':
                #we have reached the sell portion so there is no need to keep
                #on looping through
                break
            
    #------------------------------------------------------
    # Report current bitcoin balance
    #------------------------------------------------------
    
    portfolio.append(backtest.calculate_portfolio(myWallet,activetrades))
    print('current balance    ',portfolio[-1])
#deposit everything back in the wallet           
for trade in activetrades:
    trade.sell(fullData)