import numpy as np

Tole = 0.000000001
MaxIteration = 3
fm1 = 0.01
f0 = 0.05

def f(f):
    return (1/np.sqrt(f)) + (2.0*np.log10((0.002/3.7)+(2.51/(100000*np.sqrt(f)))))

for i in range(MaxIteration):
    fp1 = f0 - ((f(f0)*(fm1-f0))/(f(fm1)-f(f0)))
    if np.abs(f(fp1)) > Tole:
        fm1 = f0
        f0 = fp1
        print("Iteration = ",i+1)
        print("f(x) =",f(f0))
        print("Result =",f0)
    else:
        break