import numpy as np 

v0 = 1.0
Tole = 0.00001
Iteration = 0
MaxIteration = 3

def f(x):
    return (0.5*(x**1.75)) + (1.2*(x**2)) - 3

def fp(x):
    return (0.875*(x**0.75)) + (2.4*x)

while np.abs(f(v0)) > Tole and Iteration < MaxIteration:
    Iteration+=1
    v1 = v0 - (f(v0)/fp(v0))
    v0 = v1
    print("Iteration =",Iteration)
    print("f(x) =",f(v0))
    print("Result =",v0)