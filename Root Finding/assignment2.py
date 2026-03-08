import numpy as np

def f(x):
    return 8 - 4.5*(x-np.sin(x))

def fprime(x):
    return -4.5*(1-np.cos(x))

def NewtonRoot(Fun,FunDer, Xest, Err, imax):
    for _ in range(1,imax+1):
        xi = Xest - (Fun(Xest)/FunDer(Xest))

        if np.abs((xi - Xest) / xi) < Err:
            break
        Xest = xi

    return xi

xs = NewtonRoot(f, fprime, 2, 0.0001, 10)
print(xs)