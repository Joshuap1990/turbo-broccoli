# -*- coding: utf-8 -*-
"""
BOXBOT V0.1

An automated method of trading cryptocurrencies on Binance

Author: Joshua Parkinson
"""
from binance.client import Client
from Modules import DataCollection, TradeObject, DataProcessing
from Modules import utils as u
from Strategies import LinearModel as model


#STEP 1 - Log In
client=u.log_on(150)

#STEP 1b - Choose the base currency that will be used for the exchange
baseCurrency = 'BTC'
minimumStake = 15       #minimum Stake in USD to put in each crypto


'''
activetrades=[]
#Enter the loop
while True:


    #STEP 2 - Import data from Binance (currencies that are tradable with BTC)
    coinData = DataCollection.retrieve_data_binance(client,
                                                baseCurrency,
                                                Client.KLINE_INTERVAL_5MINUTE,
                                                '1 hour ago UTC')
                                                
    #STEP 3 - Sort and Characterise the data - adding other data if required to 
    #         produce the 'fullData' dictionary which the model can operate on
                                                
    fullData = DataProcessing.produce_summary(coinData)
                                                

    #STEP 4 - The predictive model needs to give forcasts (and probability)
    #           for each coin

    predictionData = model.model_control(fullData)

    #STEP 5 - The decision model needs to produce a list of coins, stakes and
    #           prices based on the forecast

    buyholdsell=model.decision(predictionData)
    
    #get current market price for all assets
    prices=u.get_prices(client)
    
    #update the active trade objects to see if any need to be sold
    
    if len(activetrades)>0:
        for trade in activetrades:
            trade.update(buyholdsell)
        
            #need to remove item from list if it has been sold
            if trade.status=='INACTIVE':
                activetrades.remove(trade)
            
            
        
    #Loop through current trade recommendations to see if any money can be
    # re-invested
        
    for index,row in buyholdsell.iterrows():
        
        #Get current price of that asset to figure out approximate price
        #of bitcoin to spend
        bitcoinStake = minimumStake/prices['BTCUSDT']
        
        #check current bitcoin balance to see if we have enough with margin
        balance = client.get_asset_balance(asset=baseCurrency)
        
        #Estimate what volume of asset to buy with the bitcoin
        estVolume = bitcoinStake/prices[index]
            
        if balance > 1.05*bitcoinStake:
                    
        
            if row['recommendation']=='BUY':
                #Get current price of that asset to figure out approximate price
                #of bitcoin to spend
                bitcoinStake = minimumStake/prices['BTCUSDT']
        
                #check current bitcoin balance to see if we have enough with margin
                balance = client.get_asset_balance(asset=baseCurrency)
            
            
            elif row['recommendation']=='SELL':
                #we have reached the sell portion so there is no need to keep
                #on looping through
                break
            
        


'''