# -*- coding: utf-8 -*-
"""
Data Processing and Sorting Module

Created as Part of BoxBot

Author: Joshua Parkinson

"""

def produce_summary(input_data):
    '''
    This function takes the raw market data for the coins of interest
    and returns:
    -Market Data
    -Summary Statistics
    
    This function calls coin_summary as a sub-function
    '''
    data_summary={}
    
    #Iterate through the input data, producing summary data and adding it
    #to the summary dictionary
    for coin in input_data.keys():
        data_summary[coin]={}
        data_summary[coin]['history']=input_data[coin]
        
    #use linear regression to take the slope of the whole dataset
    #feed in data from twitter etc?
    return data_summary



    