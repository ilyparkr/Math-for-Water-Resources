# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:54:58 2026

@author: LABCOM
"""

import scipy.integrate as scp
import numpy as np
import matplotlib.pyplot as plt

def Practice1():
    
    def f(y,t):
        return y * np.sin(t)
    
    t = np.arange(0,10,0.001)
    y0 = 5
    
    y = scp.odeint(f,y0,t)
    
    plt.plot(t,y)
    plt.title("Solution")
    plt.grid()
    plt.show()

def Practice2():
    
    def f(x,t):
        dxdt = 10 * ( x[1] - x[0] )
        dydt = (x[0] * ( 28 - x[2] )) - x[1]
        dzdt = (x[0] * x[1]) - (( 8 / 3 ) * x[2])
        dt = [dxdt,dydt,dzdt]
        return dt
    
    t = np.arange(0,100,0.01)
    ini = [0 , 1 , 2]
    y = scp.odeint(f, ini , t)
    
    plt.plot(t,y)
    plt.legend(["dx/dt","dy/dt","dz/dt"])
    plt.title("Lawrence equation")
    plt.grid()
    plt.show()
    
def Practice3():
    
    def f(x,t):
        dxdt = x[1]
        mdydt = (-0.5 * x[0]) - (0.1 * x[1])
        dt = [dxdt,mdydt]
        return dt
    
    t = np.arange(0,100,0.1)
    ini = [1,0]
    y = scp.odeint(f, ini, t)
    
    plt.plot(t,y)
    plt.legend(["dxdt","mdydt"])
    plt.title("Second order")
    plt.grid()
    plt.show()






    