import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4,0.1)
y = (x**3)-(2.5*(x**2))+0.8155

plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.axhline(0)
plt.grid()
plt.show()

def y(x):
    return (x**3)-(2.5*(x**2))+0.8155

a = 1
b = 3
MaxIteration = 3
Tole = 0.00001
for i in range(MaxIteration):
    m = (b+a)/2

    if (b-a)/2 > Tole:
        if y(a)*y(m) > 0:
            a = m
        else:
            b = m
    else:
        break
print(m)