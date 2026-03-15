import numpy as np
import matplotlib.pyplot as plt

h = np.arange(-10,10,0.01)
V = ((np.pi*(h**2))*((3*3)-h))/(3)
plt.plot(h,V)
plt.xlabel("h")
plt.ylabel("V")
plt.grid()
plt.show()


iteration = 0
MaxIteration = 3
a = 0
b = 3
def V(h):
    return (((np.pi*(h**2))*((3*3)-h))/(3)) - 30
Tole = 0.00001
while (b-a)/2 > Tole and iteration < MaxIteration:
    iteration+=1
    m = (b+a)/2
    if V(a)*V(m) > 0:
        a = m
    else:
        b = m
print(m)
