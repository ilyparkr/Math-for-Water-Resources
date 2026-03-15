import numpy as np

x = np.linspace(0,3,100000)
Fx = 15 * np.exp(-0.2*x) * np.sin(x)
h = np.diff(x)[0]

answer = []

for i in range(1,len(Fx)):
    answer.append(Fx[i]+Fx[i-1])

print( "Answer = " , (h/2) * sum(answer) )