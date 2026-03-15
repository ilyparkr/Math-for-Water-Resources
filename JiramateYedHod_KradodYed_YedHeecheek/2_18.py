# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 12:36:24 2026

@author: LABCOM
"""
import numpy as np
#Practice 1
def practice2():
    x = np.linspace(np.pi/2,(3*np.pi)/2,1000)
    fx = np.array(np.cos(x)**3)
    N = len(x) - 1
    h = (x[-1]-x[0])/N
    return (h/3) * (fx[0]+fx[-1]+(4*np.sum(fx[1:N:2]))+(2*np.sum(fx[2:N:2])))

def practice3():
    x = np.linspace(np.pi/2,(3*np.pi)/2,1000)
    fx = np.array(np.cos(x)**3)
    N = len(x) - 1
    h = (x[-1]-x[0])/N
    return ((3*h)/8) * (fx[0]+fx[-1]+(3*np.sum(fx[1:N-1:3] + fx[2:N:3]))+(2*np.sum(fx[3:N-2:3])))


def practice4():
    x = np.linspace(np.pi/2,(3*np.pi)/2,100000)
    fx = np.array(np.cos(x)**3)
    N = len(x) - 1
    h = (x[-1]-x[0])/N
    simpson38 = (h/3)*((3*(fx[1] + fx[2]))) + (fx[3]+fx[-1])
    simpson13 = ((h*3)/8)*((4*np.sum(fx[5:N:2]))+(np.sum(fx[4:N:2])))
    return (simpson13 + simpson38)










    