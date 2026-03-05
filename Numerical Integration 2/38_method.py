"""Simson's 3/8"""

import numpy as np
def method1():
    x = np.arange(13)
    y = np.cos(x)**3
    n = len(x)-1
    h = (x[-1] - x[0]) / n
    m  = n // 3
    rdiff = 3 * np.arange(1,m)
    w = 3 * np.ones(len(x))
    w[0] = 1
    w[-1] = 1
    w[rdiff] = 2
    integral = 3 * h/8 * np.sum(w*y)
    return integral

def method2():
    x = np.linspace(np.pi/2, 3*np.pi/2, 1000)
    y = np.cos(x)**3
    n = len(x)-1
    h = (x[-1] - x[0]) / n
    integral = 3*h / 8 * (y[0] + 3*np.sum(y[1:12:3] + y[2:n:3]) + 2*np.sum(y[3:n-2:3]) + y[-1])
    return integral

print("method1 : ", method1())
print("method2 : ", method2())