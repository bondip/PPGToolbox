# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 13:21:09 2022

@author: Parker
"""
import numpy as np
from scipy import signal

def decimator(ts, sig, dec_factor):
    
    dec_ts_ = signal.decimate(ts, dec_factor)
    dec_sig_ = signal.decimate(sig, dec_factor)
    dec_sig = []
    dec_ts = []
    arr_sig = []
    arr_ts = []
    for i in range(len(sig)):
        arr_sig.append(sig[i])
        if (i+1) % dec_factor == 0:
            arr_sig_mean = np.mean(arr_sig)
            dec_sig.append(arr_sig_mean)
            dec_ts.append(ts[i])
            arr_sig = []
            arr_ts = []
    
    return dec_ts, dec_sig