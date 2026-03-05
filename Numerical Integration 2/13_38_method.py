import numpy as np
def a():
    x = np.linspace(np.pi/2, 3*np.pi/2, 1000)
    y = np.cos(x)**3
    # y = 1 / (1+(9*x**2))
    n = len(x)-1
    h = (x[-1] - x[0]) / n
    intergral3_8 = h/3 * (y[0] + 3 * np.sum(y[1] + y[2]) + 2 * np.sum(y[3]))
    intergral1_3 = h/3 * (4 * np.sum(y[4:n:2]) + 2 * np.sum(y[5:n-1:2]) + y[-1])
    return intergral1_3 + intergral3_8
print(a())
