import numpy as np

#Midpoint method
h = 0.4
x = np.arange(0,1.2,0.2)
fx = np.array([0.48, 0.65, 0.87, 1.18, 1.60, 2.15, 2.73])
answer = []

for i in [1,3,5]:
    answer.append(fx[i])

print(h*sum(answer))