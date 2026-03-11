import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scp

def f(x,t):
    dxdt = -0.05*x[0]
    dydt = (0.05*x[0]) - (0.1*x[1])
    diff = [dxdt,dydt]
    return diff

ini = [20,0] 
t = np.arange(0,100,0.1)
y = scp.odeint(f,ini,t)

plt.plot(t,y)
plt.grid()
plt.legend(["Tank1","Tank2"])
plt.title("System of two tank")
plt.xlabel("Time")
plt.show()