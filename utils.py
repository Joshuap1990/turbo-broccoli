# -*- coding: utf-8 -*-
"""
Utils module for BoxBot

Miscellaneous functions that do not sit in any particular tarding category
and are solely in support of the program

"""


def log_on():
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
                    {"timeout": 150})
    
    print APIdata
    print secretdata
    return client