# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:42:37 2022

@author: Parker
"""
import os
import pickle
import util

path=r'C:\Users\Parker\Documents\GitHub\Python-Toolbox'
#path=input("Enter the path of your raw files: ")
#os.chdir(path)

#########-------                    Load Data                  -------#########
try:
    with open(path+"\data\converted_ecg_data_pickle.txt", "rb") as fp:
        ecg_data=pickle.load(fp)
except:
    ecg_data = util.ecg_helpers.parse_ecg(path + '\data\ecg_data.csv')
try:
    with open(path+"\data\converted_ppg_data_pickle.txt", "rb") as fp:
        ppg_data=pickle.load(fp)
except:
    ppg_data = util.ppg_helpers.parse_ppg(path + '\data\ppg_data.csv')
try:
    with open(path+"\data\converted_cbt_data_pickle.txt", "rb") as fp:
        cbt_data=pickle.load(fp)
except:
    cbt_data = util.cbt_helpers.parse_cbt(path + '\data\cbt_data.csv')

a=1