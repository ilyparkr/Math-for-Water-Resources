import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5,20,0.1)
y = ((668.061/x)*(1-np.exp(-0.147*x))) - 40
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.axhline(0)
plt.grid()
plt.show()

def f(x):
    return ((668.061/x)*(1-np.exp(-0.147*x))) - 40

a = 10
b = 20
MaxIteration = 3
Tole = 0.0001
for i in range(MaxIteration):
    m = (b+a)/2
    if (b-a)/2 > Tole:
        if f(a)*f(m) > 0:
            a = m
        else:
            b = m
    else:
        break
print(m)