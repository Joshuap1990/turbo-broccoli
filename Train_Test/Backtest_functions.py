# -*- coding: utf-8 -*-
"""
Retrieve Training Data from various sources
"""


def import_data():
    import pandas as pd
    import glob
    #Create a dictionary for importing all of the training data
    testData = {}

    #get the list of all csv files in the training directory
    dataList = glob.glob('*.csv')

    #pull in the training data for each coin into the testData Dictionary, ready
    #for streaming
    for data in dataList:
        testData[data[:-4]] =pd.DataFrame.from_csv(data)
    
    return testData

def calculate_portfolio(wallet,activetrades):
    '''
    This function calculates the current value of the my portfolio,
    in bitcoin. As the wallet should be empty most of the time all of the
    bitcoin 'locked in' active trades needs to be accounted for
    '''
    activebitcoin=0
    
    for trade in activetrades:
        activebitcoin=activebitcoin+trade.bitcoin
        
    #add the active bitcoin to the bitcoin in the wallet
    total_bitcoin=activebitcoin+wallet.balance
    
    return total_bitcoin
    

