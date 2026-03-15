import numpy as np

x = np.linspace(0,45,100000)
px = (1/(4*np.sqrt(2*np.pi))) * np.exp(-((x-50)**2)/(2*(4**2)))

answer = []
h = x[1] - x[0]

for i in range(1,len(px)):
    answer.append(px[i]+px[i-1])

print((h/2) * sum(answer))

