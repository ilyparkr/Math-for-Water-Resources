import numpy as np

y = np.arange(0,32,2)
r = np.array([15,13.5,11.9,10.8,9.7,9.0,8.4,8,7.8,7.8,7.9,8.0,8.3,8.9,9.6,10.6])
r_square = r**2
h = y[1] - y[0]

integration_S = []
integration_V = []

for i in range(1,len(r)):
    integration_S.append(r[i]+r[i-1])
    integration_V.append(r_square[i]+r_square[i-1])

print("Surface area :", 2*np.pi*((h/2)*sum(integration_S)))
print("Volume :", np.pi*((h/2)*sum(integration_V)))