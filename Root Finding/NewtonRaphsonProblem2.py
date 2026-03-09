import numpy as np

y0 = 0.5
Tole = 0.000001
MaxIteration = 3

def f(x):
    return (x**3) - (2.5*(x**2)) + 0.8155
def fp(x):
    return (3*(x**2)) - (5*x)

for i in range(MaxIteration):
    y1 = y0 - (f(y0)/fp(y0))
    if np.abs(f(y0)) > Tole:
        y0 = y1
        print(y0)
    else:
        break