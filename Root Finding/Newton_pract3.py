import numpy as np

def NewtonRoot(FunExample, FunDerExample,x0,tolerance,maxiterations):
    x_current = x0
    iterations = 0
    
    while iterations < maxiterations and np.abs(FunExample(x_current)) > tolerance:
        iterations += 1
        x_next = x_current - (FunExample(x_current) / FunDerExample(x_current))
        x_current = x_next

    if iterations == maxiterations:
        return "Error"
    else:
        return x_current,iterations


f = lambda x: 8 - 4.5 * (x-np.sin(x))
fprime = lambda x: -4.5 * (1 - np.cos(x))

xSolution = NewtonRoot(f, fprime,2,0.0001,10)
print(f"Root : x = {xSolution[0]}")
print(f"{xSolution[-1]} iterations.")
