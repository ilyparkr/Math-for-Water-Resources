import numpy as np
n = 0
p_est = 0
while np.abs(p_est - np.pi) > 0.0001:
    p_est += 4 * (((-1)**n) / (2*n+1))
    n += 1
print(p_est)