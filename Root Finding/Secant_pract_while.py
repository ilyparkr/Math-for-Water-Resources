import numpy as np 

def f(x):
    return x**7 - 1000

tol = 0.0001
x1 = 2
x2 = 3
maxiterations = 100
iterations = 0
err = tol * 100

while err > tol and iterations < maxiterations:
    iterations += 1
    xi = x2 - (f(x2) / ((f(x1)-f(x2)) / (x1-x2)))
    
    x1 = x2
    x2 = xi

    err = np.abs((x2-x1) / x2)
if iterations == maxiterations:
    print('Solution was not obtained in %i iterations. \n', maxiterations)
    xi=('No Answer')

print(xi,iterations)