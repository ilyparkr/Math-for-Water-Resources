import numpy as np

t = np.linspace(0,24,1000003)
v = 50 + (3*np.sin((np.pi*t)/12)) + np.exp(0.2*t)
h = np.diff(t)[0]

#Composite Rectangular method
Composite_answer = h * np.sum(v[:-2])

#Composite Midpoint method
Midpoint_answer = h * np.sum(v[:-1])

#Composite Trapezoidal method
Trapezoidal_answer = (h/2) * (np.sum(v[1:])+np.sum(v[:-1]))

#Simpson1/3 method
Simpson13 = (h/3) * ( v[0] + v[-1] + ( 4 * np.sum(v[1:-1:2]) ) + ( 2 * np.sum(v[2:-1:2]) ))

#Simpson3/8 method
Simpson38 = ((3*h)/8) * ( v[0] + v[-1] + ( 3 * (np.sum(v[1:-1:3]) + np.sum(v[2:-1:3])) ) + ( 2 * np.sum(v[3:-1:3]) ))

print(Composite_answer)
print(Midpoint_answer)
print(Trapezoidal_answer)
print(Simpson13)
print(Simpson38)