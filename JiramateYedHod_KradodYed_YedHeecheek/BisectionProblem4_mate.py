import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.1)
y = 8-(4.5*(x-np.sin(x)))

plt.plot(x,y)
plt.axhline(0)
plt.grid()
plt.show()

def f(x):
    return 8-(4.5*(x-np.sin(x)))

a = 2
b = 4
Tole = 0.0001
Iteration = 0
MaxIteration = 30
while (b-a)/2 > Tole and Iteration < MaxIteration:
    m = (b+a)/2
    if f(a)*f(m) > 0:
        a = m
    else:
        b = m
    print('%9s %5s %12s %13s %13s %12s' % ('iteration', 'a', 'b', 'Sol', 'f(x)', 'Tole'))
    print('%6.0f %12.6f %12.6f %12.6f %12.6f %12.6f' % (Iteration, a, b, m, f(m), Tole))