# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:41:27 2022

@author: Parker
"""

import csv
import numpy as np

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

    data_dict = dict(dc_ts=ppg_dc_ts, dc_ppg=ppg_dc, ac_ts=ppg_ac_ts, ac_ppg=ppg_ac)
    
    
    return data_dict

def aacm_loop_corrector_v2(sig, step_threshold):
    
    corrected_sig = list(np.zeros(len(sig)))
    corrected_sig[0] = sig[0]
    stepper=0
    prev_step=0
    iir=0
    
    # plt.figure()
    # plt.plot(sig)
    
    prev_steps=[]
    
    for i in range(1, len(sig)):
        if i<=5:
            iir+=1
        alpha = 1/iir
        step = sig[i] - sig[i - 1]
        if abs(step) > step_threshold:
            prev_steps.append(prev_step)
            if step > 0:
                stepper += step - prev_step
            if step < 0:
                stepper += step - prev_step
        else:
            prev_step = (1 - alpha) * prev_step + alpha * step
            prev_steps.append(prev_step)
        corrected_sig[i] += sig[i] - stepper
        
    # plt.figure()
    # plt.plot(avg_steps)
    # plt.plot(prev_steps)
    # plt.show()
    
    # plt.plot(corrected_sig)
    # plt.plot(prev_steps)
    # plt.show()
    

    return corrected_sig







