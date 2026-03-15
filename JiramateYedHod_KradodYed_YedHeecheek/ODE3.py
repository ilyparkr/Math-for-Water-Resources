import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scp

def f(z,t):
    dz0dt = z[1]
    dz1dt = -0.5*z[1] - ((9.81/1.0)*np.sin(z[0]))
    dt = [dz0dt,dz1dt]
    return dt

ini = [np.pi/2,0]
t = np.arange(0,15,0.05)
y = scp.odeint(f,ini,t)

plt.plot(t, y[:,0], label='Angle (rad)', color='blue')
plt.plot(t, y[:,1], label='Angular Velocity (rad/s)', color='red', linestyle='--')
plt.legend()
plt.grid()
plt.show()