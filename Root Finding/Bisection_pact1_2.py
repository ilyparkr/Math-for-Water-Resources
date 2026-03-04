import numpy as np
import matplotlib.pyplot as plt

def plot():
    x = np.arange(-10, 10, 0.1)
    # y = -0.8*(x**4) + 6.6*(x**3) - 16*(x**2) + 11.7*x + 5
    y = 8 - 4.5*(x-np.sin(x))
    plt.plot(x,y)
    plt.grid()
    plt.show()

a = 0
b = 5
tolerance = 0.001
iterations = 0
maxiterations = 100
f = lambda x : 8 - 4.5*(x-np.sin(x))

print('%9s %5s %12s %13s %13s %12s' % ('iteration', 'a', 'b', 'Sol', 'f(x)', 'Tole'))

while (b-a) / 2 > tolerance and iterations < maxiterations:
    iterations += 1
    m = a + (b-a)/2
    errT = (b-a) / 2 - tolerance
    if np.sign(f(a)) == np.sign(f(m)):
        a = m
    else:
        b = m
    print('%6.0f %12.6f %12.6f %12.6f %12.6f %12.6f' % (iterations, a, b, m, errT, f(m)))