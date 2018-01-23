# -*- coding: utf-8 -*-
"""
Retrieve Training Data from various sources
"""

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
    
'''
#example of streaming a subset of time history data
dataframe=pd.DataFrame.from_csv('ADABTC.csv')

windowWidth=60  # keep 60 minutes of data in memory
timeinterval=5  # data is in 5 minute intervals

numRows = windowWidth/timeinterval




#iterate down the dataframe in groups of 10
stream=[]

#use a generator to iterate down the rows of the dataframe, ensuring that 
#the last 1h worth of data is kept in the stream list
for index,row in dataframe.iterrows():
    stream.append(row)
    
    if len(stream)>numRows:
        del stream[0]'''
        
     #streamdata=pd.DataFrame