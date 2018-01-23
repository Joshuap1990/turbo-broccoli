# -*- coding: utf-8 -*-
"""
Retrieve Training Data from various sources
"""

import pandas as pd
import glob



#----------------Input Data---------------------------
windowWidth=60  # keep 60 minutes of data in memory
timeinterval=5  # data is in 5 minute intervals
#----------------------------------------------------




#Create a dictionary for importing all of the training data
testData = {}

#get the list of all csv files in the training directory
dataList = glob.glob('*.csv')

#pull in the training data for each coin into the testData Dictionary, ready
#for streaming
for data in dataList:
    testData[data[:-4]] =pd.DataFrame.from_csv(data)

#calculate the number of rows that need to be held in stream
numRows = windowWidth/timeinterval

#create the empty stream list
stream=[]

#use a generator to iterate down the rows of the dataframe, ensuring that 
#the last 1h worth of data is kept in the stream list
for index,row in dataframe.iterrows():
    stream.append(row)
    
    if len(stream)>numRows:
        del stream[0]
        
     #streamdata=pd.DataFrame