import numpy as np 

def f(x):
    return x**7 - 1000

tol = 0.0001
x1 = 2
x2 = 3
maxiterations = 100

for i in range(maxiterations):
    xi = x2 - (f(x2) / ((f(x1)-f(x2)) / (x1-x2)))
    
    if np.abs((x2-x1) / x2) < tol:
        break

    x1 = x2
    x2 = xi

if i == maxiterations:
    print('Solution was not obtained in %i iterations. \n', maxiterations)
    xi=('No Answer')

print(xi,i)