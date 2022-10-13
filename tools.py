import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def exponential(t, a, tau, c):
    return a * np.exp(-t / tau) + c
    
def fit_waveform(waveform, width=20, start_time=950, l = 1200):
    '''
    Fit raw waveforms to find values relevant for filtering
    
    Parameters
    ----------
    waveform: 1D np.array
        individual waveform
    width: 
        width of moving average, default 20
    
    Returns
    -------
    
    '''
    # Calculate the baseline value by averaging the first 20 data points
    # waveform = np.int64(waveform)
    # baseline_value = np.convolve(waveform[0:width], np.ones(width), 'valid') / width
    
    # Make a smooth version of the c
    waveform = np.convolve(waveform, np.ones(width), 'valid') / width
    max_location = np.argmax(waveform)
    
    # Determine Tau
    n = np.arange(0, len(waveform))
    decay_indices = n[max_location:-1]
    decay_indices_norm = (decay_indices - decay_indices[0])/(decay_indices[-1] - decay_indices[0])
    c_0 = waveform[-1]
    tau_0 = 1
    a_0 = (waveform[0] - waveform[-1])
    popt, pcov = curve_fit(exponential, decay_indices_norm, waveform[decay_indices], p0=(a_0, tau_0, c_0))
    a, tau, c = popt
    tau *= max(n)
    
    #print(max_location)
    k = max_location-start_time
    
    # time that waveform is flat at top
    # need to write code to find automatically
    
    return tau, k, l

def plot_fitted_waveform(waveform, decay_indices, decay_indices_norm, a, tau, n, c):
    '''
    Plot fitted waveform
    
    Parameters
    ----------
    waveform:
    decay_indices:
    decay_indices_norm:
    a:
    tau:
    n:
    c:
    
    Returns
    -------
    plt: matplolib.pyplot.figure
        plot of fitted waveform
    '''
    plt.figure()
    plt.plot(waveform, label="Raw waveform")
    #plt.plot(s, label="Trapezoid")
    plt.plot(decay_indices, exponential(decay_indices_norm, a, tau/max(n), c), label="tau: {0}".format(tau))
    #plt.xlim(800,1200)
    #plt.ylim(1,1000000)
    plt.legend()
    plt.show()
    return
    
    
def trapezoidal_filter(waveform, width, start_time, l):
    '''
    Trapezoidal filter for raw waveforms
    
    Parameters
    ----------
    raw_waveform: np.array
        1D array of individual raw waveform
    width: float
        width of moving average, default 20
    start_time: float
        start of 
    l: float
        time that waveform is flat at top

        
    start_time: float
    
    Returns
    -------
    filtered_waveform: np.array
        waveform after trapezoidal filter has been applied
    
    '''
    tau, k, l = fit_waveform(waveform, width=20)
    # start of rise - need to find code to find automatically
    
    
    #print(tau)
    s = np.zeros(len(waveform))
    for i in range(k+l, max(n)-(k+l)):
        j = i+k+l
        d_kl = waveform[j]-waveform[j-k]-waveform[j-l]+waveform[j-k-l]
        #print(d_kl)
        s[i] = s[i-1]*(1+1/tau) + d_kl
    
    return s
    
def find_activity(t12,A0,t):
    '''
    Find activity of source
    
    Parameters
    ----------
    t12: float
        half life of source
    A0: float
        activity of source (arb units)
    t: float
        time elapsed since source born date (A0)
    
    Returns
    -------
    A: float
        Activity at time t in same units as A0
    '''
    decay_constant = np.log(2) / t12
    return A0 * np.exp(-decay_constant*t)
    