"""Assignment 1"""

import numpy as np

def rectangle(y,r):
    return np.diff(y)[0] * np.sum(r)

def trapzoid(y,r):
    return np.sum(np.diff(y)[0] * (r[:-1] + r[1:]) / 2)

y = np.arange(0,31,2)
r = np.array([15, 13.5, 11.9, 10.8, 9.7, 9.0, 8.4, 8, 7.8, 7.8, 7.9, 8.0, 8.3, 8.9, 9.6, 10.6])

s_rect = 2*np.pi*rectangle(y,r)
v_rect = np.pi*rectangle(y,r)

s_trapz = 2*np.pi*trapzoid(y,r)
v_trapz = np.pi*trapzoid(y,r)

print(f"Rectangle method : s = {s_rect} v = {v_rect}")
print(f"Trapzoid method : s = {s_trapz} v = {v_trapz}")