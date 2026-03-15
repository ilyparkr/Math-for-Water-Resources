import numpy as np

x = np.linspace(np.pi/2,(3*np.pi)/2,1000003)
fx = np.cos(x)**3
h = np.diff(x)[0]

three = []
two = []

for i in range(1,len(fx)-1):
    if i%3 == 0:
        two.append(fx[i])
    else:
        three.append(fx[i])

answer = ( ( 3 * h ) / 8 ) * (fx[0] + fx[-1] + (2 * sum(two)) + (3* sum(three)))
print("answer = ", answer)