import numpy as np

t = np.linspace(0,10,100000)
v = np.abs( ( np.exp( -0.5 * t ) ) * ( np.sin(( 60/np.pi ) * t) ) )
h = np.diff(t)[0]

answer = []

for i in range(1,len(v)):
    answer.append(v[i]+v[i-1])

print(5.2*((h/2) * sum(answer)))