# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 16:56:15 2017

@author: wkb16122
"""

import pandas as pd
import numpy as np
import os

column_name=['from','to','P','Q','rohm','xohm','maxi']

def get_ieee_data():
    column_name=['from','to','P','Q','rohm','xohm','maxi']
    path=r'C:\Users\wkb16122\Dropbox\python\padapower'
    data_33='ieee33bus.txt'
    data_69='ieee69bus.txt'
    file33=os.path.join(path,data_33)
    file69=os.path.join(path,data_69)
    fo=open(file33,'r')
    data33=[]
    for line in fo:
        data33.append(line.rstrip().split(' '))
        #print line.split(' ')
    df_33=pd.DataFrame(data33,columns=column_name)
    data69=[]
    fo=open(file69,'r')
    for line in fo:
        data69.append(line.rstrip().split(' '))
    df_69=pd.DataFrame(data69,columns=column_name)
    return df_33,df_69

if __name__=='__main__':
    path=r'C:\Users\wkb16122\Dropbox\python\padapower'
    data_33='ieee33bus.txt'
    data_69='ieee69bus.txt'
    file33=os.path.join(path,data_33)
    file69=os.path.join(path,data_69)
    fo=open(file33,'r')
    data33=[]
    for line in fo:
        data33.append(line.rstrip().split(' '))
        #print line.split(' ')
    df_33=pd.DataFrame(data33,columns=column_name)
    data69=[]
    fo=open(file69,'r')
    for line in fo:
        data69.append(line.rstrip().split(' '))
    df_69=pd.DataFrame(data69,columns=column_name)
    
    df_33.to_csv(os.path.join(path,'ieee33.csv'),index=False)
    df_69.to_csv(os.path.join(path,'ieee69.csv'),index=False)