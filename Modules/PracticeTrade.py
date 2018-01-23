# -*- coding: utf-8 -*-
"""
Exampple Trading Class

This class creates objects that will be used to make practice trades


"""

class wallet(object):
    
    def __init__(self,open_balance):
        self.balance=open_balance
    
    def spend(amount):
        
        if amount>self.balance:
            raise ValueError ('Not enough bitcoin to conduct transaction')
        
        self.balance = self.balance-amount

    def deposit(amount):
        self.balance=self.balance
        
    def balance():
        return self.balance


class trade_practice(object):
    '''
    Practice Trade Class
    
    Interacts with the wallet
    '''
    
    import pandas as pd
    
    def __init__(self,asset,fullPrice,wallet):
        '''
        These functions run on trade object initialization
        '''
        
        #assign the parameters to object attributes
        self.asset=asset                    # the name of the asset being bought
        self.wallet=wallet
        self.buy(fullprice)
        self.status='ACTIVE'

    def buy(self,fullPrice,bitcoinbalance):
            
        currentprice = fullPrice[self.asset].tail(1)['4']
        
        #calculate how much of the asset is being bough
        self.volume=bitcoinbalance/currentprice
        
        self.wallet.spend(bitcoinbalance)
        
                        
    def sell(self,fullPrice):
        '''
        This method makes the sale then deactivates the object
        based on if it has hit the high or low sell price
        '''
        
        currentprice = fullPrice[self.asset].tail(1)['4']                     
        self.sellprice=currentprice
        self.status='INACTIVE'
        
        #deposit back in the wallet
        self.returned=self.volume*currentprice
        self.wallet.deposit(self.returned)
        
    def update(self,buyholdsell,fullPrice):
        '''
        This method checks the market price of the asset and sells if the price 
        reaches the predefined High or Low sell price
        '''
        #1 - go to the decision model to get buy/sell recommendations
        # Depending on Buy-Sell recommendation then either do nothing, or sell
        
        if buyholdsell['recommendation'][self.asset]=='SELL':
            self.sell(fullPrice)
            

