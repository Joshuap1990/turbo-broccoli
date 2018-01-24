# -*- coding: utf-8 -*-
"""
Exampple Trading Class

This class creates objects that will be used to make practice trades


"""

class wallet(object):
    
    def __init__(self,open_balance):
        self.balance=open_balance
    
    def spend(self,amount):
        
        if amount>self.balance:
            raise ValueError ('Not enough bitcoin to conduct transaction')
        
        self.balance = self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance
        



class trade_practice(object):
    '''
    Practice Trade Class
    
    Interacts with the wallet
    '''
    
    import pandas as pd
    
    def __init__(self,asset,fullPrice,wallet,stake):
        '''
        These functions run on trade object initialization
        '''
        
        #assign the parameters to object attributes
        self.asset=asset                    # the name of the asset being bought
        self.wallet=wallet                  # embed the wallet in the object so
                                            #  it can deposit/withdraw from it
        self.bitcoin = stake                # keep track of how much bitcoin
                                            #  is 'locked up' in this trade 
        self.buy(fullPrice)                 # Go buy the asset using the amount of
                                            #   bitcoin in the object
        self.status='ACTIVE'

    def buy(self,fullPrice):
            
        currentprice = fullPrice[self.asset].tail(1)['4']
        
        # Pretend Sale - get the volume of asset that could be bought with
        # that amount of bitcoin
        self.volume=self.bitcoin/currentprice
        
        self.wallet.spend(self.bitcoin)
        
                        
    def sell(self,fullPrice):
        '''
        This method makes the sale then deactivates the object
        based on if it has hit the high or low sell price
        '''
        
        currentprice = fullPrice[self.asset].tail(1)['4']                     

        #calculate the amount of bitcoin that can be returned to the wallet
        self.bitcoin = self.volume/currentprice
        #deposit back in the wallet
        self.wallet.deposit(self.returned)
        self.status='INACTIVE'
        

        
        
    def update(self,buyholdsell,fullPrice):
        '''
        This method checks the market price of the asset and sells if the price 
        reaches the predefined High or Low sell price
        '''
        #1 - go to the decision model to get buy/sell recommendations
        # Depending on Buy-Sell recommendation then either do nothing, or sell
        
        if buyholdsell['recommendation'][self.asset]=='SELL':
            self.sell(fullPrice)
            

