import numpy as np

x = np.linspace(-1.2,1.2,1000001)
fx = 1 / ( 1 + ( 9 *(x**2) ) )  
h = np.diff(x)[0]

sum_odd = np.sum(fx[1:-1:2])
sum_even = np.sum(fx[2:-1:2])

print("answer = ",( h / 3 ) * (fx[0] + fx[-1] + (4*sum_odd) + (2*sum_even)))