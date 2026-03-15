import numpy as np

t = np.arange(0,3.5,0.5)
P = [12.0,18.5,25.0,21.5,15.0,10.5,8.0]
h = t[1] - t[0]

answer = []

for i in range(1,len(P)):
    answer.append(P[i]+P[i-1])

print("answer = ",(h/2)*sum(answer))