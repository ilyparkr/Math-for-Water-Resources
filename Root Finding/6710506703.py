# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:25:24 2026

@author: LABCOM
"""
import numpy as np
import matplotlib.pyplot as plt


#Newton-Raphson method
#ก
x = np.arange(0,3,0.1)
fx = np.exp(x)
gx = 3*x
plt.plot(x,fx)
plt.plot(x,gx)
plt.grid()
plt.legend("f(x) vs g(x)")
plt.axhline(0)
plt.show()

#ข
def f(x):
    return np.exp(x) - (3*x)
def fp(x):
    return np.exp(x)-3
Epsilon = 10**(-6)
MaxIteration = 20
x0 = 1.5
xm = 0.4
for i in range(MaxIteration):
    xp = x0 - ((f(x0)*(xm-x0))/(f(xm)-f(x0)))
    if xp - x0 < Epsilon:
        break
    else:
        x0 = xp
        xm = x0
    print("Result",xp)
    print("Iteration",i+1)





