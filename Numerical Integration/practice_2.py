"""Practice 2"""

import numpy as np
mean = 50
sd = 4
h = np.linspace(45,50,1000)
x = np.diff(h)
y = (1 / (sd*np.sqrt(2*np.pi))) * (np.exp(-((h-mean)**2) / (2*sd**2)))
p = np.sum(x * (y[:-1]+y[1:])/2)

print(0.5-p)