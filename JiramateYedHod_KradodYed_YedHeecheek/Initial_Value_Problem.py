import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scp

def f(y,t):
    return -(1.2*y) + (7*np.exp(-0.5*t))

y0 = 3
t = np.arange(0,2.5,0.5)
integrate = scp.odeint(f,y0,t)

plt.plot(t,integrate)
plt.grid()
plt.show()