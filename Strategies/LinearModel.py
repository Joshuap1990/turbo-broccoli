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
    predictionData={}
    
    for asset in fullData.keys():
        print('Processing model - {}'.format(asset))
        predictionData[asset]={}
        predictionData[asset]['gradient']=model(fullData[asset])
        
    print('Predictive Model - Completed')
        
    return predictionData


def model(asset):
    '''
    make linear fit of data
    '''
    from scipy import stats
    slope, intercept, r_value, p_value, std_err =stats.linregress(asset['history'][4],asset['history'][6])
    
    return slope
    
def decision(predictionData):
    '''
    Decision model - take a prediction from the regression model
    and produce a score, the more positive it is the more the asset should be
    bought
    '''
    import pandas as pd    
    
    #if price is increasing, then buy, if decreasing then sell
    for asset in predictionData.keys():
        if predictionData[asset]['gradient']<0:
            predictionData[asset]['recommendation']='SELL'
        elif predictionData[asset]['gradient']>=0:
            predictionData[asset]['recommendation']='BUY'
    
    #turn compiled dictionary into a dataframe
    results=pd.DataFrame.from_dict(predictionData,orient='index') 

    decision=results.sort_values(by='gradient',ascending=False)     
    return decision
            

