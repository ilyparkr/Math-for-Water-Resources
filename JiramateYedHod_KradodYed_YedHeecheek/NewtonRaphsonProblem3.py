import numpy as np

h0 = 1.5
Tole = 0.00000001
iteration = 0
MaxIteration = 3

def f(h):
    return (h**3) - (9*(h**2)) + 28.65
def fp(h):
    return (3*(h**2)) - (18*h)

while np.abs(f(h0)) > Tole and iteration < MaxIteration:
    iteration+=1
    h1 = h0 - (f(h0)/fp(h0))
    h0 = h1
    print("Iteration = ",iteration)
    print("f(x) = ",np.abs(f(h0)))
    print("Result = ",h1)
