"""Simson's 1/3"""

import numpy as np
def a():
    n = 9
    rodd = np.arange(0, n, 2) # [0,2,4,6,8]
    reven = np.arange(1, n-1, 2) # [1,3,5,7]
    weight_n9 = np.zeros(n) # [0,0,0,0,0,0,0,0,0]
    weight_n9[rodd] = 2 # [2,0,2,0,2,0,2,0,2]
    weight_n9[0] = 1 # [1,0,2,0,2,0,2,0,2]
    weight_n9[-1] = 1 # [1,0,2,0,2,0,2,0,1]
    weight_n9[reven] = 4 # [1,4,2,4,2,4,2,4,1]
    print(weight_n9)
    
def method1():
    weight_n9 = np.array([1, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4 ,1])
    x = np.linspace(np.pi/2, 3*np.pi/2, 13) 
    f = np.cos(x)**3
    n = len(x)-1
    h = (x[-1] - x[0]) / n
    intergral = h/3 * np.sum(weight_n9*f)
    return intergral

def method2():
    x = np.linspace(np.pi/2, 3*np.pi/2, 1000)
    y = np.cos(x)**3
    n = len(x)-1
    h = (x[-1] - x[0]) / n
    intergral = h/3 * (y[0] + 4*np.sum(y[1:n:2]) + 2*np.sum(y[2:n-1:2]) + y[-1])
    return intergral

def method3():
    x = np.linspace(np.pi/2, 3*np.pi/2, 1001)
    y = np.cos(x)**3
    n = len(x)-1
    h = (x[-1] - x[0]) / n
    intergral = 0
    for j in range(0, n, 2):
        intergral += h/3 * (y[j] + 4*y[j+1] + y[j+2])
    return intergral
    
print("Method 1 :", method1())
print("Method 2 :", method2())
print("Method 3 :", method3())