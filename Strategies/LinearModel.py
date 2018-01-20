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
    '''
    from scipy import stats
    import numpy as np
    
    #make a new dictionary, as this will contain the original data,
    #plus any forecasts and statistics 
    modelData={}
    modelData['history']=asset['history']
    
    #have a look at the data and get the latest timestamp
    latestTime = max(modelData['history'][6])
    #Produce a time array (in ms) for the next 6 hours
    timeRange= np.linspace(latestTime,latestTime+(6*3600*1000),num=50) 
    #What is the latest price at the end of the reporting period?
    latestPrice=modelData['history'].loc[modelData['history'][6]==latestTime]
    latestPrice=float(latestPrice[4])
    
    
    #-------------------------------------------------------------------------
    #               STEP 1 - Perform fit and prediction
    #------------------------------------------------------------------------
    #Perform the linear regression and file away the statistics
    slope, intercept, r_value, p_value, std_err =stats.linregress(modelData['history'][6],
                                                                  modelData['history'][4])
    modelData['stats']={}                                                              
    modelData['stats']['slope']=slope
    modelData['stats']['intercept']=intercept
    modelData['stats']['r_value']=r_value
    modelData['stats']['std_err']=std_err
    modelData['stats']['latestPrice']=latestPrice
                        
    #Based on this basic linear fit produce a forecast for the next 6 hours
    pricePrediction=slope*timeRange + intercept
    
    modelData['prediction'] = np.array(zip(timeRange,pricePrediction))
                                       
    return modelData
    
def decision(predictionData):
    '''
    The role of the decision model is to take the forecast produced by
    the prediction model and rank the different assets to buy.
        
    it will also set the volume of asset to be bought, plus the upper
    and lower sale price
        
    Produces a nested list of recommendations
        
    [[asset1,stake1,highsell1,lowsell1],
     [asset2,stake2,highsell2,lowsell2]]
        
        
    Logic in this decision model
    1)rank by gradient
    2.)re-rank by which current values are lower than the mean
    3.)this model will work by fixed stake for now, so need to figure out
    how many assets can be bought 
    4.) if we have enough money for 5 assets the top five ranked assets
    will be output as a recommendation
            
    '''
    import pandas as pd
        
    #start a new dictionary which can be used to collect summary data
    ranklist={}
        
    for asset in predictionData.keys():
         
        #if slope is greater than zero, add it to the list of potential
         #candidates
         if predictionData[asset]['stats']['slope'] > 0:
             
             #also calculate by how much the current price is below the mean
             current_price=predictionData[asset][]
             rankasset[asset][]
      
        #summarise these parameters to some growth potential
        ranklist[asset]=(meandelta+growth).values
            
            
        #growthpotential=pd.DataFrame(ranklist)
        #growthpotential=growthpotential.rank()
        
    return ranklist