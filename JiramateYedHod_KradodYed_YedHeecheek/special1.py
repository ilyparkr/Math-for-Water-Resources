import numpy as np

t = np.linspace(0,10,100002)
v = np.abs( ( np.exp( -0.5 * t ) ) * ( np.sin(( 60/np.pi ) * t) ) )
h = np.diff(t)[0]

ans = (h/2) * np.sum((v[1:]+v[:-1]))
print(ans*5.2)