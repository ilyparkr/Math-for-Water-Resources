# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 12:36:24 2026

@author: LABCOM
"""
import numpy as np
#Practice 1
def practice2():
    x = np.array([np.pi/2,(2/3)*np.pi,(3/4)*np.pi,(5/6)*np.pi,np.pi,(7/6)*np.pi,(5/4)*np.pi,(4/3)*np.pi,(3/2)*np.pi])
    fx = np.array(np.cos(x)**3)
    N = len(x) - 1
    h = (x[-1]-x[0])/N
    return (h/3) * (fx[0]+fx[-1]+(4*np.sum(fx[1:N:2]))+(2*np.sum(fx[2:N:2])))

def practice3():
    x = np.array([np.pi/2,(2/3)*np.pi,(3/4)*np.pi,(5/6)*np.pi,np.pi,(7/6)*np.pi,(5/4)*np.pi,(4/3)*np.pi,(3/2)*np.pi])
    fx = np.array(np.cos(x)**3)
    N = len(x) - 1
    h = (x[-1]-x[0])/N
    return ((3*h)/8) * (fx[0]+fx[-1]+(3*np.sum(fx[1:N-1:3] + fx[2:N:3]))+(2*np.sum(fx[3:N-2:3])))

def practice4():
    x = np.array([np.pi/2,(2/3)*np.pi,(3/4)*np.pi,(5/6)*np.pi,np.pi,(7/6)*np.pi,(5/4)*np.pi,(4/3)*np.pi,(3/2)*np.pi])
    fx = np.array(np.cos(x)**3)
    N = len(x) - 1
    h = (x[-1]-x[0])/N
    simpson38 = (h/3)*(fx[0]+(3*(fx[1] + fx[2]))) + (2*fx[3]+fx[-1])
    simpson13 = ((h*3)/8)*(fx[0]+(4*np.sum(fx[5:N:2]))+(2*np.sum(fx[4:N:2]))+fx[-1])
    return (simpson13 + simpson38)/










    