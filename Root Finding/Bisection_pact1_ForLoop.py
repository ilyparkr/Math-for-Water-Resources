import numpy as np
import matplotlib.pyplot as plt

def plot():
    x = np.arange(-10, 10, 0.1)
    y = 8 - 4.5*(x-np.sin(x))
    plt.plot(x,y)
    plt.grid()
    plt.show()

a = 0
b = 5
tolerance = 0.001 # เอาไว้ดูว่าค่าเข้าใกล้คำตอบหรือยัง
iterations = 0 # จำนวนรอบ
maxiterations = 100 # จำนวนรอบสูงสุด
f = lambda x : 8 - 4.5*(x-np.sin(x))

print('%9s %5s %12s %13s %13s %12s' % ('iteration', 'a', 'b', 'Sol', 'f(x)', 'Tole'))

for _ in range(maxiterations):
    iterations += 1
    m = a + (b-a)/2
    errT = (b-a) / 2 - tolerance
    
    print('%6.0f %12.6f %12.6f %12.6f %12.6f %12.6f' % (iterations, a, b, m, f(m), errT))
    
    if errT < tolerance or f(m) == 0:
        break

    if f(a)*f(m) > 0:
        a = m
    else:
        b = m

    

# while (b-a) / 2 > tolerance and iterations < maxiterations: # (b-a) / 2 คือ 
#     iterations += 1
#     m = a + (b-a)/2
#     errT = (b-a) / 2 - tolerance
#     if np.sign(f(a)) == np.sign(f(m)):
#         a = m
#     else:
#         b = m
    # print('%6.0f %12.6f %12.6f %12.6f %12.6f %12.6f' % (iterations, a, b, m, errT, f(m)))