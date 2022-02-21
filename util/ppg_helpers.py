# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:41:27 2022

@author: Parker
"""

import csv


def parse_ppg(file_path):
    
    ppg_dc_ts = []
    ppg_dc = []
    ppg_ac_ts = []
    ppg_ac = []
    
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
                if 'GRE-DC_Time' in data:
                    ppg_dc_ts.append(float(row[data.index('GRE-DC_Time')]))
                if 'GRE-DC_Value' in data:
                    ppg_dc.append(float(row[data.index('GRE-DC_Value')]))
                if 'GRE-AMB_Time' in data:
                    ppg_ac_ts.append(float(row[data.index('GRE-AMB_Time')]))
                if 'GRE-AMB_Value' in data:
                    ppg_ac.append(float(row[data.index('GRE-AMB_Value')]))

    data_dict = dict(dc_ts=ppg_dc_ts, dc_sig=ppg_dc, ac_ts=ppg_ac_ts, ac_sig=ppg_ac)
    
    
    return data_dict