# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:47:04 2018

@author: joshua
"""

def linear_model(asset):
    '''
    This is an example of the most basic predictive model.
    It will fit a line to the data from the sample period,
    and produce a prediction of the price at t+(t/10)
    '''
    from scipy import stats
    
    #make a new dictionary, as this will contain the original data,
    #plus any forecasts and statistics 
    modeldata={}
    modeldata['history']=asset['history']
    
    #Perform the linear regression and file away the statistics
    slope, intercept, r_value, p_value, std_err =stats.linregress(pricedata[0],
                                                                  pricedata[1])
    modeldata['stats']={'slope': slope,
                        'intercept': intercept,
                        'r_value': r_value,
                        'p_value':p_value
                        'std_err':std_err}
                        
    #Based on this basic linear fit produce a forecast for the next 24 hours
                        
    #TODO - figure out what the timestamp of the input data is doing and
    #convert it to datetime format (if thats easier) there appears to be
    #too many numbers for a unix timestamp                        
                        
                                                                  
                                                                  
    return linear_model_data
    

def decision_model