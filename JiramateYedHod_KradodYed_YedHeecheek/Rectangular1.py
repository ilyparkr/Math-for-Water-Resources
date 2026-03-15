import numpy as np

#Rectangular method
h = 0.2
x = np.arange(0,1.2,0.2)
fx = np.array([0.48, 0.65, 0.87, 1.18, 1.60, 2.15, 2.73])
answer = []

for i in range(len(fx)-1):
    answer.append(fx[i])

print(h*sum(answer))