# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:47:04 2018

@author: joshua
"""

def model_control(fullData):
    '''
    This function calls the 'model' for every currency in the dataset
    and returns another dictionary with every currency and its prediction
    '''
    
    print('Processing the predictive model')
    processed_data={}
    
    for asset in fullData.keys():
        print('Processing model - {}'.format(asset))
        processed_data[asset]=model(fullData[asset])
        
    print('Predictive Model - Completed')
        
    return processed_data


def model(asset):
    '''
    This is an example of a basic predictive model.
    Strategy
    -Make a linear fit to all the data
    -Make another linear fit to the data from the last 3 hours
    -use the average of the two slopes to predict what the price will
     be over the next 6 hours
     
    
    TODO - replace the average by a weighting factor which can be optimised
    TODO - do the short term linear fit so it can be weighted with the longer
            term one
    TODO - Code in weighting factor
    '''
    

    
def decision(predictionData):
    '''
    Decision model - take a prediction from the regression model
    and produce a score, the more positive it is the more the asset should be
    bought
    '''

def decision_control(processed data):
    '''
    STEP 1: take the whole of processed_data and call the 'decision' method
    to get a buy/sell score.
    
    e.g.
    BNBBTC - 5
    ADABTC - 4.7
    ...
    
    STEP 2: determine a score, above which a 'BUY' rating will be issued. 
    Produce a list of buy-sell ratings
    '''
    