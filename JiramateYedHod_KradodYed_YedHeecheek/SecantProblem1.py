import numpy as np

Cminus1 = 10
C0 = 20
MaxIteration = 3
Tole = 0.000000001
def f(c):
    return ((668.061/c) * (1-np.exp(-0.14684*c))) - 40

for i in range(MaxIteration):
    Cplus1 = C0 -((f(C0)*(C0-Cminus1))/(f(Cminus1) - f(C0)))
    if np.abs(f(C0)) > Tole:
        Cminus1 = C0
        C0 = Cplus1
        print("Iteration = ",i)
        print("f(c) = ",f(C0))
        print("Result = ",Cplus1)
    else:
        break