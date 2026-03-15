# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:49:45 2026

@author: LABCOM
"""
import numpy as np
def Practise2():
    x = np.linspace(45,50,100000)
    fx = (1/(4*(2*np.sqrt(2*np.pi))))*np.exp(-((x-50)**2)/(2*(4**2)))
    I=sum(np.diff(x)*((fx[:-1])+(fx[1:]))/2)
    return I
        

def Practise4():
    t = np.arange(0,270,15) #X
    y = [0.10,0.10,0.13,0.29,0.60,1.90,3.97,5.55,6.23,5.18,3.76,2.00,1.17,0.64,0.25,0.13,0.10,0.10,0.10] #Y
    c = np.array(y)
    Q = [] 
    for i in range(len(t)-1): #Summation c-c0
        Q.append(c[i]-0.10)
    q = np.array(Q)  #F(X)
    I=sum(15*(np.array(q[:-1])+np.array(q[1:]))/2) #Vectorisation trapezoidal
    return 500000/I #Q = M/sum(c-c0)


def assignS():
    y = np.arange(0,30,2) #X
    r = np.array([15,13.5,11.9,10.8,9.7,9.0,8.4,8.0,7.8,7.8,7.9,8.0,8.3,8.9,9.6,10.6]) #Y
    I = sum(2*(r[:-1]+r[1:])/2) #Vectorisation trapezoidal #r
    return (2*np.pi)*I #2*pi*sum(r)

def assignV():
    y = np.arange(0,30,2) #X
    r = np.array([15,13.5,11.9,10.8,9.7,9.0,8.4,8,7.8,7.8,7.9,8.0,8.3,8.9,9.6,10.6]) #Y
    I = sum(2*((r[:-1]**2)+(r[1:]**2))/2)  #r^2
    print(np.pi*I) #2*pi*sum(r^2)

def practise3():
    t = np.linspace(0, 10, 10000000) #X
    v = 5.2 * np.exp(-0.5 * t) * np.sin((60 / np.pi) * t) #F(X)
    I=sum(np.diff(t)*(np.array(np.abs(v[:-1]))+np.array(np.abs(v[1:])))/2) #Vectorisation trapezoidal
    return I
    
    
    
    
    
    
    
    
    
    
    
    
    