# -*- coding: utf-8 -*-
"""
Binance Trade Class

This class creates objects that will be used to make trades on the binance
exchange.

In time move this plus all other binance related functions and classes to a 
seperate module as part of work to support other exchanges

"""

class trade_binance(object):
    '''
    Trade Class
    written for the binance exchange
    
    client      - the log on details for you account
    baseCurr    - the currency that will be used as the trading currency
                instead of GBP/USD
    asset       - what trading pair being bought/sold?
    volume      - how much of the currency is going to be bought?
    '''
    
    import pandas as pd
    from binance.client import Client
    
    def __init__(self,client,baseCurr,asset,volume,currPrice):
        '''
        These functions run on trade object initialization
        '''
        
        #assign the parameters to object attributes
        self.client=client             #log on details
        self.asset=asset            #the asset being traded e.g 'BNBBTC'
        self.volume=volume               #how much of the thing to buy?
        
        
        #--------------------------------------------------------------------
        #                        Pre-Buy Checks
        #--------------------------------------------------------------------

        #Check the amount of base currencty in your account to ensure that
         #there is enough to make the trade
        balance = client.get_asset_balance(asset=baseCurr)
        
        #Estimate how much is needed to make the trade, at the current
        #market price 
        reqBalance = currPrice/volume
        
        #TODO-finish checking this - is the calculation correct?
        #go on binance website to sense check
        if balance >= 1.05*reqBalance: 
            #buy the stock!
            self.buy()
            print('-------BUY COMPLETED-------')
            print(self.buyorder)
        

        
    def update(self,price):
        '''
        This method checks the market price of the asset and sells if the price 
        reaches the predefined High or Low sell price
        '''
        #1 - go to the decision model to get buy/sell recommendations
        # Depending on Buy-Sell recommendation then either do nothing, or sell
        
        if buyholdsell[self.asset]['recommendation']=='SELL':
            self.sell()
            
            
       
       
    def buy(self):
        '''
        This method performs the buy order
        '''
                
        try:
            self.buyorder = self.client.order_market_buy(
                            symbol=self.asset,
                            quantity=self.volume,
                            newOrderRespType='FULL')
        except:
            #server may have timed out, give it one more try
            print('WARNING - Server is not responsive...about to try again')
            self.buyorder = self.client.order_market_buy(
                            symbol=self.asset,
                            quantity=self.volume,
                            newOrderRespType='FULL')
                            
         # Initialise an empty sell order dictionary - this will be overwritten
         # when the product is actually sold
        self.sellorder={}
                        
    def sell(self):
        '''
        This method makes the sale then deactivates the object
        based on if it has hit the high or low sell price
        '''
        
        #how much is being sold? given that some will be taken off for
        #commission
        try:
            self.sellorder=self.client.order_market_sell(symbol=self.asset,
                                                         quantity=self.volume,
                                                         newOrderRespType='FULL')
            print('-------SELL COMPLETED-------')
        except:
            #need to change this except statement only for a timeout error
            #replace this warning message with a warning from the warning module
            print('WARNING - Server is not responsive...about to try again')
            self.sellorder=self.client.order_market_sell(symbol=self.asset,
                                                         quantity=self.volume,
                                                         newOrderRespType='FULL')
            print('-------SELL COMPLETED-------')                                       
        
        #then record details of sale in the object
         #print out details to console?   
     

    def profitcalc(self):
        '''
        once the sale is complete calculate profit for this trade
        '''
        self.profit=put_stuff_here
        
