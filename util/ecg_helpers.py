# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:40:17 2022

@author: Parker
"""
import csv


def parse_ecg(file_path):
    
    ecg_ts = []
    ecg = []
    
    with open(file_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        j = 0
        for row in readCSV:
            if j == 0:
                recording = row
                j = 1
                continue
            if len(row) > 1:
                data = [recording[i] for i in range(len(row)) if row[i] != '']
                row = [x for x in row if x != '']
                if 'Time [s]' in data:
                    ecg_ts.append(float(row[data.index('Time [s]')]))
                if 'Lead 1 ECG [uV]' in data:
                    ecg.append(float(row[data.index('Lead 1 ECG [uV]')]))

    data_dict = dict(ts=ecg_ts, ecg=ecg)
    
    return data_dict