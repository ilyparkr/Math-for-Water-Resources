import numpy as np

def f(x):
    return 8 - 4.5*(x-np.sin(x))

def SecantRoot(Fun,Xa, Xb, Err, imax):
    for i in range(imax):
        xi = Xb - (Fun(Xb) / ((Fun(Xa)-Fun(Xb))/(Xa-Xb)))
        if np.abs((xi-Xb) / Xb) <= Err:
            return xi
        Xa = Xb
        Xb = xi
    
    if i == imax:
        return ('Solution was not obtained in %i iterations. \n', imax)

Err = 0.0001
imax = 10
x = 2 # ไม่รู้ว่าโจทย์ผิดหรือเปล่าให้ x มาตัวเดียว
a = 2.1 # อันนี้สุ่มค่า a กับ b มาเองโจทย์ไม่บอก
b = 1.9
Xs=SecantRoot(f, a, b, Err, imax)
print(Xs)