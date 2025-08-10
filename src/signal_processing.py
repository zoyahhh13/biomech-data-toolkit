from scipy.signal import butter, filtfilt
import numpy as np

def butter_lowpass(cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff=6, fs=100):
    b, a = butter_lowpass(cutoff, fs)
    y = filtfilt(b, a, data)
    return y
