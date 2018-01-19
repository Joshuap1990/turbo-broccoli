# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:26:01 2018

@author: joshua
"""

class trade_binance(object):
    '''
    Trade Class
    written for the binance exchange
    
    Currency - what coin is being bought?
    stake - how much of the currency is going to be bought?
    buyPrice - What price should it be bought at?
    upperLim - if the price reaches this upper value, then it should be sold
    lowerLim - if the price reaches this low value, then it should be sold
    '''
    
    import pandas as pd
    from binance.client import Client
    
    def __init__(self,client,currency,stake,upperLim,lowerLim):
        '''
        These functions run on trade object initialization
        '''
        
        #assign the parameters to object attributes
        self.client=client             #log on details
        self.currency=currency         #the asset being traded e.g 'BNBBTC'
        self.stake=stake               #how much of the thing to buy?
        # self.buyprice = buyPrice     #currently dont need this as it is
                                       #a market order
        self.upperLim=upperLim         # what is the upper price?
        self.lowerLim=lowerLim         #what is the lower price?
        
        ###ERROR CHECKS NEEDED!!!!!!
        #buy the stock!
        self.buy()
        print('-------BUY COMPLETED-------')
        print(self.buyorder)
        

        
    def update(self,price):
        '''
        This method checks the market price of the asset and sells if the price 
        reaches the predefined High or Low sell price
        '''
        
        #If price is above/below threshold then sell the asset
        if price >=self.upperLim or price<=self.lowerLim:
            self.sell()
            print(self.sellorder)
            
       
       
    def buy(self):
        '''
        This method does error checks and performs the buy order
        '''
                
        #need to check account balance before buying anything!
        try:
            self.buyorder = self.client.order_market_buy(
                            symbol=self.currency,
                            quantity=self.stake,
                            newOrderRespType='FULL')
        except:
            #server may have timed out, give it one more try
            print('WARNING - Server is not responsive...about to try again')
            self.buyorder = self.client.order_market_buy(
                            symbol=self.currency,
                            quantity=self.stake,
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
            self.sellorder=self.client.order_market_sell(symbol=self.currency,
                                                         quantity=self.stake,
                                                         newOrderRespType='FULL')
            print('-------SELL COMPLETED-------')
        except:
            #need to change this except statement only for a timeout error
            #replace this warning message with a warning from the warning module
            print('WARNING - Server is not responsive...about to try again')
            self.sellorder=self.client.order_market_sell(symbol=self.currency,
                                                         quantity=self.stake,
                                                         newOrderRespType='FULL')
            print('-------SELL COMPLETED-------')                                       
        
        #then record details of sale in the object
         #print out details to console?   
     
    def check_balance(self,client):
        #need to check the balance of the base currency before
        #trying to buy anything. if balance is not enough exit the code and
        #deactivate the object
        a=stuff

    def profitcalc(self):
        '''
        once the sale is complete calculate profit for this trade
        '''
        self.profit=put_stuff_here
        
