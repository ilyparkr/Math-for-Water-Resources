import numpy as np
import matplotlib.pyplot as plt

def plot(): # plot กราฟ
    x = np.arange(0, 5, 0.1)
    y = 8 - 4.5*(x-np.sin(x))
    plt.plot(x,y)
    plt.grid()
    plt.show()

a = 0 # ขอบบน
b = 5 # ขอบล่าง
maxits = 100
tol = 0.001
inerations = 0 # จำนวนรอบ

def f(x):
    return 8 - 4.5 * (x-np.sin(x))

while (b - a) / 2 > tol and inerations < maxits:
    inerations += 1
    m = a + (b-a) / 2
    err = (b - a) / 2 - tol # ค่า mean - ค่า tolerance
    if np.sign(f(a)) == np.sign(f(m)):
        a = m
    else:
        b = m
print(inerations, m)
plot()