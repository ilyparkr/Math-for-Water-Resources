import numpy as np
import matplotlib.pyplot as plt

# def plot(a,b):
#     x = np.arange(a, b, 0.1)
#     y = 


def BisectionRoot(Fun,a,b,TolMax):
    if Fun(a) * Fun(b) > 0:
        print("Error")
        return
    
    n = np.ceil(np.log(b-a) - np.log(TolMax) / np.log(2))

    for _ in range(int(n)):
        m = a + (b-a)/2
        # if np.sign(Fun(a)) == np.sign(Fun(m)):
        if Fun(a)*Fun(m) > 0:
            a = m
        else:
            b = m
    return m

a = -10
b = 10

f1 = lambda x: 8 - 4.5*(x-np.sin(x))
f2 = lambda x: x**3 - np.exp(-0.5*x)

ans1 = BisectionRoot(f1, a, b, 0.00001)
ans2 = BisectionRoot(f2, a, b, 0.00001)
print(ans1)
print(ans2)