import numpy as np
from algorithms.dft_slow import dft_slow

def fft_recursive(sig):
    N = len(sig)
    
    if N % 2 > 0:
        raise ValueError("size of sig must be a power of 2")
    elif N <= 32:
        return dft_slow(sig)
    else:
        X_even = fft_recursive(sig[::2])
        X_odd = fft_recursive(sig[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N // 2] * X_odd,
                               X_even + factor[N // 2:] * X_odd])