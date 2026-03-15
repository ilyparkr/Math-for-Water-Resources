import numpy as np

ym1 = 1.0
y0 = 2.0
iteration = 0
MaxIteration = 3
Tole = 0.000000001
def f(y):
    return (243*(y**5)) - (500*(y**2)) - (1500*y) - 1125 

while np.abs(f(y0)) > Tole and iteration < MaxIteration:
    iteration+=1
    yp1 = y0 -((f(y0)*(ym1-y0))/(f(ym1)-(f(y0))))
    ym1 = y0
    y0 = yp1
    print("Iteration = ",iteration)
    print("Result = ",y0)