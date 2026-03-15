import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,100000)
ft = (15*np.exp(-0.2*t)) * np.cos( 0.5 * t ) - 3

plt.plot(t,ft)
plt.axhline(0)
plt.grid()
plt.show()

def f(t):
    return (15*np.exp(-0.2*t)) * np.cos( 0.5 * t ) - 3

def fp(t):
    return 
#Bisection method
tL = 2.0
tR = 4.0