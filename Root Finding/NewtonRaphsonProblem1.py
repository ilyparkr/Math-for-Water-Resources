import numpy as np
import matplotlib.pyplot as plt

y0 = 1
tole = 0.00000001
iteration = 0
MaxIteration = 40
def f(y):
    return (9.81*(((3*y)+(2*(y**2)))**3)) - (400*(3+(4*y)))
def fp(y):
    return (29.43*(((3*y)+(2*(y**2)))**2)*(3+(4*y))) - 1600

while np.abs(f(y0)) > tole and iteration < MaxIteration:
    iteration+=1
    y1 = y0 - (f(y0)/fp(y0))
    y0 = y1
print(y0)