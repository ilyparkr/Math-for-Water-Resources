import numpy as np

y0 = 1.5 
MaxIteration = 3
Tole = 0.0000001

def f(x):
    return (4*(x**2.5)) - (3.674*x) - 7.348
def fp(x):
    return (10*(x**1.5)) - 3.674

for i in range(MaxIteration):
    y1 = y0 - (f(y0)/fp(y0))
    if np.abs(f(y1)) < Tole:
        break
    else:
        y0 = y1
        print("Iteration =",i+1)
        print("result =",y0)
        print("Checking(f(x)) = ",f(y0))
