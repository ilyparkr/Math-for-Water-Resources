import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(0.1,10,100000)
fy = ( ((10*y)/0.018) * (((10*y)/(10 + (2*y)))**(2/3)) * (np.sqrt(0.001)) ) - 25

# Function
def f(y):
    return ( ((10*y)/0.018) * (((10*y)/(10 + (2*y)))**(2/3)) * (np.sqrt(0.001)) ) - 25

def fp(y):
    return 17.568 * ((((10*y)/(10 + (2*y)))*(2/3)) + ((y*(((10*y)/(10 + (2*y)))**(-1/3)))*((100/((10 + (2*y))**2)))))
# Graph
plt.plot(y,fy)
plt.axhline(0)
plt.grid()
plt.show()

# Bisection method
yL = 0.1 #Minus
yR = 5.0 #Plus
Iteration = 0
Maxiteration = 100
Tole = 10**(-6)
while np.abs(yR-yL)/2 > Tole and Iteration < Maxiteration:
    Iteration += 1
    yM = (yR+yL)/2
    if f(yR) * f(yM) > 0:
        yR = yM
    else:
        yL = yM

Bisection_answer = yM
Bisection_fx = f(yM)

# Newton-Raphson method
y0 = 2.0
Iteration = 0
Maxiteration = 100
while np.abs(f(y0)) > Tole and Iteration < Maxiteration:
    Iteration += 1
    y1 = y0 - (f(y0)/fp(y0))
    y0 = y1

Newton_Raphson_answer = y0
Newton_Raphson_fx = f(y0)

# Secant method
y0 = 1.0
y1 = 2.0
Iteration = 0
Maxiteration = 100
while np.abs(f(y1)) > Tole and Iteration < Maxiteration:
    Iteration += 1
    y2 = y1 - ((f(y1)*(y0-y1))/(f(y0)-f(y1)))
    y0 = y1
    y1 = y2

Secant_answer = y1 
Secant_fx = f(y1)

print(f"Bisection: answer = {Bisection_answer} fx = {Bisection_fx}")
print(f"Newton-Raphson: answer = {Newton_Raphson_answer} fx = {Newton_Raphson_fx}")
print(f"Secant: answer = {Secant_answer} fx = {Secant_fx}")