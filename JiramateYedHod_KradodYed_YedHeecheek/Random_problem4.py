import numpy as np

Theta0 = 2.5
Tole = 0.000001
Iteration = 0
MaxIteration = 20

def f(x):
    return ((x-np.sin(x))**5) - (14.722*(x**2))

def fp(x):
    return ((5*((x-np.sin(x))**4))*(1-np.cos(x))) - (29.444*x)

while np.abs(f(Theta0)) > Tole and Iteration < MaxIteration:
    Iteration += 1
    Theta1 = Theta0 - (f(Theta0)/fp(Theta0))
    Theta0 = Theta1
    print("Iteration =",Iteration)
    print("f(x) =",f(Theta0))
    print("Result =",1.5*(1-np.cos(Theta0/2)))