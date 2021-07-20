import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

amp = 1
f = 2
initPhase = np.pi/2
sampleRate = 44100
time = np.linspace(0,1,sampleRate)

sinusWave = amp * np.cos((2*np.pi*f) * time + initPhase)

def lowpass (x):
    n = len(x)
    y = np.zeros(n)
    for i in range(n):
        y[i] = x[i] + x[n-1]
    return y

plt.plot(time,lowpass(sinusWave))
plt.show()
