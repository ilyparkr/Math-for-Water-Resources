"""Practice 3"""

import numpy as np
t = np.linspace(0,10,100)
v = 5.2*abs(np.exp(-0.5*t) * np.sin(60/np.pi*t))
I = sum(np.diff(t)*((v[:-1])+(v[1:]))/2)
print(I)