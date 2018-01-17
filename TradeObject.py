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
    sellprice - what price was the stake sold at?
    '''
    def __init__(self,client,currency,stake,buyPrice,upperLim,lowerLim,sellPrice):
        '''
        These functions run on trade object initialization
        '''
        #assign the parameters to object attributes
        self.client=client
        self.currency=currency
        self.stake=stake
        self.buyprice = buyPrice
        self.upperLim=upperLim
        self.lowerLim=lowerLim
        self.sellPrice=sellPrice
        
        ###ERROR CHECKS NEEDED!!!!!!
        
        self.orderdetails = self.buy()
        

        
    def update(self):
        '''
        This method checks the market price of the asset and sells if the price 
        reaches the predefined High or Low sell price
        '''
        
        #need to test current price!
        curr_price = self.client.get_ticker(self.currency)
        
        #If price is above/below threshold then sell the asset
        if curr_price >=self.upperLim or curr_price<=self.lower_lim:
            self.sell()
       
       
    def buy(self):
        '''
        This method does error checks and performs the buy order
        '''
                
        #ERROR CHECKS NEEDED! MAYBE A TRY/EXCEPT STATEMENT
        #need to check account balance before buying anything!
        
        self.order = self.client.order_market_buy(
                        symbol=self.currency,
                        quantity=self.stake,
                        newOrderRespType='FULL')
                        
                        
    def sell(self):
        '''
        This method makes the sale then deactivates the object
        based on if it has hit the high or low sell price
        '''
        self.sellorder=self.client.order_market_sell(symbol=self.currrency,
                                                quantity=self.stake)
            
        #then record details of sale in the object
         #print out details to console?   
        

    def profitcalc(self):
        '''
        once the sale is complete calculate profit for this trade
        '''
        self.profit=put_stuff_here
        
