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
        

        
    def update(self):
        '''
        This method checks the market price of the asset and sells if the price 
        reaches the predefined High or Low sell price
        '''
        
        #need to test current price!
        curr_price = float(self.client.get_ticker(symbol=self.currency)['lastPrice'])
        
        #If price is above/below threshold then sell the asset
        if curr_price >=self.upperLim or curr_price<=self.lower_lim:
            self.sell()
       
       
    def buy(self):
        '''
        This method does error checks and performs the buy order
        '''
                
        #ERROR CHECKS NEEDED! MAYBE A TRY/EXCEPT STATEMENT
        #need to check account balance before buying anything!
        
        self.buyorder = self.client.order_market_buy(
                        symbol=self.currency,
                        quantity=self.stake,
                        newOrderRespType='FULL')
                        
                        
    def sell(self):
        '''
        This method makes the sale then deactivates the object
        based on if it has hit the high or low sell price
        '''
        
        #how much is being sold? given that some will be taken off for
        #commission
        self.sellorder=self.client.order_market_sell(symbol=self.currency,
                                                quantity=self.stake)
        print('-------SELL COMPLETED-------')                                       
            
        #then record details of sale in the object
         #print out details to console?   
        

    def profitcalc(self):
        '''
        once the sale is complete calculate profit for this trade
        '''
        self.profit=put_stuff_here
        
