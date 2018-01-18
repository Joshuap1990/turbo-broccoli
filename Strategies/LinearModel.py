# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:47:04 2018

@author: joshua
"""

def linear_model(fulldata):
    '''
    This is an example of the most basic predictive model.
    It will fit a line to the data from the sample period,
    and produce a prediction of the price at t+(t/10)
    '''
    from scipy import stats
    
    pricedata = fulldata['history']
    
    slope, intercept, r_value, p_value, std_err =stats.linregress(pricedata[0],
                                                                  pricedata[1])
                                                                  
    #Then go on to add another key to this dictionary with the prediction
                                                                  
                                                                  
    return processed_data
    

def decision_model