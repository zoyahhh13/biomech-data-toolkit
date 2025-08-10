import numpy as np

def range_of_motion(signal):
    """
    Calculate the range of motion (max-min) for a signal.
    """
    return np.max(signal) - np.min(signal)
