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
client=u.log_on()

#STEP 1b - Choose the base currency that will be used for the exchange
baseCurrency = 'BTC'

#STEP 2 - Import data from Binance (currencies that are tradable with BTC)
coinData = DataCollection.retrieve_data_binance(client,
                                                baseCurrency,
                                                Client.KLINE_INTERVAL_5MINUTE,
                                                '1 days ago UTC')
                                                
#STEP 3 - Sort and Characterise the data - adding other data if required to 
#         produce the 'fullData' dictionary which the model can operate on
                                                
fullData = DataProcessing.produce_summary(coinData)
                                                

#STEP 4 - The predictive model needs to give forcasts (and probability)
#           for each coin

predictionData = model.model_control(fullData)

#STEP 5 - The decision model needs to produce a list of coins, stakes and
#           prices based on the forecast

assetlist=model.decision(predictionData)

#STEP 6 - Buy the coins using the tradeobject class
activetrades=[]

for asset in assetlist:
    activetrades.append(TradeObject(asset,stake,hiprice,lowprice))


#STEP 7 - Enter a loop to monitor and update the trade objects, ready to sell
While True:
    a=0
while True:
    time.sleep(5)
    a=a+1
    print('About the check the price...')
    print('Check Number {}'.format(a))
    
    
    #Try and get the latest price from the server
    try:
        latest_price = float(client.get_ticker(symbol='BNBBTC')['lastPrice'])
        print('Latest Price: {}'.format(latest_price))
    except:
        print('WARNING- Check Number {} may have timed out...trying again')
        latest_price = float(client.get_ticker(symbol='BNBBTC')['lastPrice'])
        print('Latest Price: {}'.format(latest_price))
        
    # Update the trade objects    
    trade1.update(latest_price)
    
    #if asset has been sold then  need to quit the program!
    if len(trade1.sellorder.keys())>1:
        break