# -*- coding: utf-8 -*-
"""
Retrieve Training Data from various sources
"""


def import_data():
    import pandas as pd
    #Create a dictionary for importing all of the training data
    testData = {}

    #get the list of all csv files in the training directory
    dataList = glob.glob('*.csv')

    #pull in the training data for each coin into the testData Dictionary, ready
    #for streaming
    for data in dataList:
        testData[data[:-4]] =pd.DataFrame.from_csv(data)
    
    return testData

