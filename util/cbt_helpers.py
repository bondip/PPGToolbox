# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:41:37 2022

@author: Parker
"""

import csv


def parse_cbt(file_path):
    
    cbt_ts = []
    cbt = []
    
    with open(file_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        j = 0
        for row in readCSV:
            if j == 0:
                j = 1
                continue
            if j == 1:
                recording = row
                j = 2
                continue
            if len(row) > 1:
                data = [recording[i] for i in range(len(row)) if row[i] != '']
                row = [x for x in row if x != '']
                if 'Timestamp' in data:
                    cbt_ts.append(float(row[data.index('Timestamp')]))
                if 'cbt [mC]' in data:
                    cbt.append(float(row[data.index('cbt [mC]')]))

    data_dict = dict(ts=cbt_ts, sig=cbt)
    
    
    return data_dict