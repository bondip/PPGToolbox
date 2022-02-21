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
        print('ECG file already created')
except:
    ecg_data = util.ecg_helpers.parse_ecg(path + '\data\ecg_data.csv')
try:
    with open(path+"\data\converted_ppg_data_pickle.txt", "rb") as fp:
        ppg_data=pickle.load(fp)
        print('PPG file already created')
except:
    ppg_data = util.ppg_helpers.parse_ppg(path + '\data\ppg_data.csv')
try:
    with open(path+"\data\converted_cbt_data_pickle.txt", "rb") as fp:
        cbt_data=pickle.load(fp)
        print('CBT file already created')
except:
    cbt_data = util.cbt_helpers.parse_cbt(path + '\data\cbt_data.csv')

data_parameters = {'est_hf': 80,
                   'delta': 0.0003,
                   'ac_gain': 500000,
                   'dc_gain': 5000,
                   'ppg_highpass_cutoff':0.6,
                   'ppg_lowpass_cutoff':8,
                   'window_size':10,
                   'ecg_highpass_cutoff':0.1,
                   'ecg_lowpass_cutoff':35,
                   'decimation_factor':4,
                   'ppg_step_threshold':0.06
                   }

ecg_data['fs'] = 1/(ppg_data['ac_ts'][1] - ppg_data['ac_ts'][0])
ppg_data['fs'] = 1/(ecg_data['ts'][1] - ecg_data['ts'][0])
cbt_data['fs'] = 1/(cbt_data['ts'][1] - cbt_data['ts'][0])

ecg_data['decimated_ts'], ecg_data['decimated_ecg'] = util.helpers.decimator(ecg_data['ts'], ecg_data['ecg'], data_parameters['decimation_factor'])
ppg_data['decimated_ac_ts'], ppg_data['decimated_ac_ppg'] = util.helpers.decimator(ppg_data['ac_ts'], ppg_data['ac_ppg'], data_parameters['decimation_factor'])
ppg_data['decimated_dc_ts'], ppg_data['decimated_dc_ppg'] = util.helpers.decimator(ppg_data['dc_ts'], ppg_data['dc_ppg'], data_parameters['decimation_factor'])
cbt_data['decimated_ts'], cbt_data['decimated_cbt'] = util.helpers.decimator(cbt_data['ts'], cbt_data['cbt'], data_parameters['decimation_factor'])

#########-------            PPG AACM Loop Corrector            -------#########
"""
PPG sensing IC's commonly use a digitally measured DC cancellation loop that
steps the AC signal in the opposite direction of the DC trend. This allows us
to use a higher gain on the PPG AC signal but remain in the ADC range
"""
ppg_data['loop_corrected_ac_ppg'] = util.ppg_helpers.aacm_loop_corrector_v2(ppg_data['ac_ppg'], data_parameters['ppg_step_threshold'])


#########-------                    Save Data                  -------#########
with open(path + "\data\converted_ecg_data_pickle.txt", "wb") as fp:
    pickle.dump(ecg_data, fp)
with open(path + "\data\converted_ppg_data_pickle.txt", "wb") as fp:
    pickle.dump(ppg_data, fp)
with open(path + "\data\converted_cbt_data_pickle.txt", "wb") as fp:
    pickle.dump(cbt_data, fp)