import numpy as np
import scipy.integrate as scp
import matplotlib.pyplot as plt

def f(T,t):
    return -0.05 * (T - 25)

T0 = 180 
t = np.arange(0,100,0.5)
y = scp.odeint(f,T0,t)

plt.plot(t,y)
plt.grid()
plt.show()