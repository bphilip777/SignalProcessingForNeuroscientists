import numpy as np 
import matplotlib.pyplot as plt 

sz = 256
noise_trials = np.random.randn(sz, sz)
SZ = np.linspace(sz)
SZ = SZ / (sz//2)
S = np.sin(2 * np.pi * SZ)

for i in range(sz):
    noise_trials[i, :] += S

avg = np.mean(noise_trials, 1)

