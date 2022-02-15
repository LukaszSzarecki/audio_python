import numpy as np

def dft_slow(sig):
  N = len(sig)
  Y = np.array([]) #transformata Fouriera
  n = np.arange(0,N)
  k = n.reshape((N,1))
  Y = np.exp(-2j * (np.pi/N) * k*n )
  Yf =  np.dot(Y, sig)
  
  return Yf