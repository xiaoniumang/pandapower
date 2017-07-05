# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 12:57:38 2017

@author: wkb16122
"""


import pandas as pd
import numpy as np
import os
import sys
import pandapower as pp
sys.path.append(r'C:\Users\wkb16122\Dropbox\python\padapower\processing_33_and_69_bus-data')
from process_ieee_txt_data import *

def build_case33(df):
    net=pp.create_empty_network()
    #build 33+1 buses
    for i in range(34):
        if i==0:
            pp.create_bus(net,vn_kv=33)
        else:
            pp.create_bus(net,vn_kv=11)
    pp.create_ext_grid(net,bus=0,vm_pu=1.02)
    #create lines based on the df, and add loads to the buses 
    for index,row in df.iterrows():
        pp.create_line_from_parameters(net,from_bus=int(row['from']),to_bus=int(row['to']),length_km=1,r_ohm_per_km=float(row['rohm']),x_ohm_per_km=float(row['xohm']),c_nf_per_km=0,max_i_ka=float(row['maxi'])/100.0)
        pp.create_load(net,bus=int(row['to']),p_kw=float(row['P']),q_kvar=float(row['Q']))
    #add the transformer
    pp.create_transformer_from_parameters(net,hv_bus=0,lv_bus=1,sn_kva=6000.0,vn_hv_kv=33.0,vn_lv_kv=11.0,vscr_percent=0.25,vsc_percent=12.0,pfe_kw=30,i0_percent=0.06)
    return net

def build_case69(df):
    net=pp.create_empty_network()
    #build 69+1 buses
    for i in range(70):
        if i==0:
            pp.create_bus(net,vn_kv=33)
        else:
            pp.create_bus(net,vn_kv=11)
    pp.create_ext_grid(net,bus=0,vm_pu=1.02)
    #create lines based on the df, and add loads to the buses 
    for index,row in df.iterrows():
        pp.create_line_from_parameters(net,from_bus=int(row['from']),to_bus=int(row['to']),length_km=1,r_ohm_per_km=float(row['rohm']),x_ohm_per_km=float(row['xohm']),c_nf_per_km=0,max_i_ka=float(row['maxi'])/100.0)
        pp.create_load(net,bus=int(row['to']),p_kw=float(row['P']),q_kvar=float(row['Q']))
    #add the transformer
    pp.create_transformer_from_parameters(net,hv_bus=0,lv_bus=1,sn_kva=6000.0,vn_hv_kv=33.0,vn_lv_kv=11.0,vscr_percent=0.25,vsc_percent=12.0,pfe_kw=30,i0_percent=0.06)
    return net

if __name__=='__main__':
    df33,df69=get_ieee_data()
    net1=build_case33(df33)
    pp.runpp(net1)
    net2=build_case69(df69)
    pp.runpp(net2)