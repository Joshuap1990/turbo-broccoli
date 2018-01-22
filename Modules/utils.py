# -*- coding: utf-8 -*-
"""
Utils module for BoxBot

Miscellaneous functions that do not sit in any particular tarding category
and are solely in support of the program

"""


def log_on(timeout):
    # ======== Select a file for opening:
    #file only needs to lines, the first line with API, second with secret
    import Tkinter,tkFileDialog
    from binance.client import Client


    #Choose License file containing API and secret data
    root = Tkinter.Tk()
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file != None:
        APIdata = file.readline().strip()
        secretdata=file.readline().strip()
        file.close()
    
    
    client = Client(APIdata,
                    secretdata,
                    {"timeout": timeout})
    print('Logged In Successfully')
    
    return client


def get_prices(client):
    '''
    This function is to take the default output of the get_ticker
    method in the defauly API and turn it into something more useful
    '''
    raw_price = client.get_all_tickers()
    
    processed_price = {}
    for asset in raw_price:
        
        processed_price[asset['symbol']]=asset['price']
        
    return processed_price