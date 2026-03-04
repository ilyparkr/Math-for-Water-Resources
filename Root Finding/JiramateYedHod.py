# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 12:48:51 2026

@author: LABCOM

"""

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-2.0, 7, 0.1)
y = 8-(4.5*(x-np.sin(x)))
plt.plot(x,y)
plt.grid()
plt.show()

def bisectionWhile():
    iteration = 0
    maxiteration = 100
    a = 2
    b = 4
    Tole = 0.00001
    def f(x):
        return 8-(4.5*(x-np.sin(x)))
    while (b-a)/2 > Tole and iteration < maxiteration:
        iteration +=1 
        m = (b+a)/2
        errT = (b-a)/2 - Tole
        if f(a)*f(m) > 0:
            a = m
        else:
            b = m
        print('%6.0f %12.6f %12.6f %12.6f %12.6f %12.6f' % (iteration, a, b, m, errT,f(m)))
        
def bisectionFor():
    return 0

def Newton_Raphson_While():
    iteration = 0
    tolerance = 10 ** (-7)
    epsilon = 10 ** (-14) #error ฟังก์ชั่นเข้าใกล้ศูนย์
    maxIterations = 20
    x0 = 4
    def f(x):
            return 8 - 4.5 * (x - np.sin(x))
    def fprime(x):
            return -4.5 * (1 - np.cos(x))
    while iteration < maxIterations:
        iteration +=1 
        x1 = x0 - (f(x0)/fprime(x0))
        if abs(f(x0)) > tolerance:
            x0 = x1
        else:
            break
    print(x0)
    
def Newton_Raphson_For():
    iteration = 0
    tolerance = 10 ** (-7) #Y ที่หาเข้าใกล์ศูนย์รึยัง
    epsilon = 10 ** (-14) #error ฟังก์ชั่นเข้าใกล้ศูนย์
    maxIterations = 20
    x0 = 4
    def f(x):
            return 8 - 4.5 * (x - np.sin(x))
    def fprime(x):
            return -4.5 * (1 - np.cos(x))
    for i in range(iteration,maxIterations):
        x1 = x0 - (f(x0)/fprime(x0))
        if abs((x1-x0)/x1) > epsilon:
            x0 = x1
        else:
            break
    print(x0)

def NewtonRoot(func,pfunc,ini,tols,maxitr):
    iteration = 0
    while iteration < maxitr:
        iteration +=1 
        x1 = ini - (func(ini)/pfunc(ini))
        if abs((func(x1)-func(ini))/func(x1)) > tols:
            ini = x1
        else:
            break
    return ini
def f(x):
        return 8 - 4.5 * (x - np.sin(x))
def fprime(x):
        return -4.5 * (1 - np.cos(x))

def secant(): #ใช้กับfunctionที่diffไม่ได้
    Err = 10 ** (-7) #Y ที่หาเข้าใกล์ศูนย์รึยัง
    imax = 20
    x1 = 2
    x2 = 3
    def f(x):
        return (x**7) - 1000
    for i in range(imax):
        x3 = x2 - (f(x2)/((f(x1)-f(x2))/(x1-x2)))
        if abs((x3-x2)/x2) <= Err:
            Xs=x3
            break
        x1=x2
        x2=x3
    return Xs
