The modules that will be present in this folder will be trading strategies 

Trading strategies should be broken down into two functions

Predictive Model
Decision Model

The predictive model will have the following input
-A dictionary containing historical price data
	In time the dictionary can be expanded to accomodate other 		things that may be explanatory variables

The predictive model will output:
A copy of the input dictionary, with an addional key that will contain
its forecast

The decision model will have the following input
-output dictionary from the predictive model

The decision model will output:
a list of recommendations in the format
[curr,stake,highprice,sellprice]

This will be then fed into the object model so that trades can be executed
