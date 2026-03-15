import numpy as np

x = np.linspace(-1.2,1.2,1000003)
fx = 1 / ( 1 + ( 9 *(x**2) ) )  
h = np.diff(x)[0]

sum_three = sum(fx[1:-1:3]) + sum(fx[2:-1:3])
sum_two = sum(fx[3:-1:3])

answer = ((3*h)/8) * (fx[0] + fx[-1] + (3*sum_three) + (2*sum_two))
print("answer =", answer)