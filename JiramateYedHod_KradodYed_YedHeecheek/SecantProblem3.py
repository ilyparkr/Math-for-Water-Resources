import numpy as np

Qm1 = 1.0
Q0 = 2.0 
MaxIteration = 3
Tole = 0.00000000001
def f(Q):
    return (Q**3) + (5*(Q**2)) + (10*Q) - 20
for i in range(MaxIteration):
    Qp1 = Q0 - ((f(Q0)*(Qm1 - Q0))/(f(Qm1)-f(Q0)))
    if np.abs(f(Q0)) < Tole:
        break
    Qm1 = Q0
    Q0 = Qp1
    print("Iteration = ",i)
    print("Result = ",Q0)