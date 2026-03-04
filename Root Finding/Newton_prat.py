import numpy as np

x0 = 4

def f(x):
    return 8 - 4.5 * (x-np.sin(x))

def fprime(x):
    return -4.5 * (1 - np.cos(x))

tolerance = 10**(-7)
epsilon = 10**(-14)
maxinterations = 20

for i in range(1, maxinterations+1):
    fx = f(x0)
    dfx = fprime(x0)
    
    if abs(dfx) < epsilon:
        print("Error: slope is too close to 0 can't calculate")
        break

    x_next = x0 - (fx/dfx)

    if abs(x_next - x0) < tolerance:
        print(f"Solution : x = {x_next}")
        print(f"interations : {i+1}")
        break

    x0 = x_next

else:
    print(f"Can't find the right root in {maxinterations}")