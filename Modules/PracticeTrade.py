# -*- coding: utf-8 -*-
"""
Exampple Trading Class

This class creates objects that will be used to make practice trades


"""

class trade_practice(object):
    '''
    Trade Class
    
    client      - the log on details for you account
    baseCurr    - the currency that will be used as the trading currency
                instead of GBP/USD
    asset       - what trading pair being bought/sold?
    volume      - how much of the currency is going to be bought?
    '''
    
    import pandas as pd
    from binance.client import Client
    
    def __init__(self,asset,volume,currPrice):
        '''
        These functions run on trade object initialization
        '''
        
        #assign the parameters to object attributes
        self.asset=asset            #the asset being traded e.g 'BNBBTC'
        self.volume=volume               #how much of the thing to buy?
        
        
        #--------------------------------------------------------------------
        #                        Pre-Buy Checks
        #--------------------------------------------------------------------

        
        if balance >= minstake: 
            #buy the stock!
            self.buy()
            print('-------BUY COMPLETED-------')
            print(self.buyorder)
            self.status='ACTIVE'
        

        
    def update(self,buyholdsell):
        '''
        This method checks the market price of the asset and sells if the price 
        reaches the predefined High or Low sell price
        '''
        #1 - go to the decision model to get buy/sell recommendations
        # Depending on Buy-Sell recommendation then either do nothing, or sell
        
        if buyholdsell['recommendation'][self.asset]=='SELL':
            self.sell()
            
            
       
       
    def buy(self):
        '''
        This method performs the buy order
        '''
                
                            
         # Initialise an empty sell order dictionary - this will be overwritten
         # when the product is actually sold
        self.sellorder={}
                        
    def sell(self):
        '''
        This method makes the sale then deactivates the object
        based on if it has hit the high or low sell price
        '''
                              
        
        self.status='INACTIVE'
        #then record details of sale in the object
         #print out details to console?   
     

    def profitcalc(self):
        '''
        once the sale is complete calculate profit for this trade
        '''
        self.profit=put_stuff_here
        
