import numpy as np

x0 = 4
# x = float(input("Guess the number : "))

def f(x):
    return 8 - 4.5 * (x-np.sin(x))

def fprime(x):
    return -4.5 * (1 - np.cos(x))

tolerance = 10**(-7)
epsilon = 10**(-14)
maxinterations = 20
iterations = 0

while iterations < maxinterations and np.abs(f(x0)) > tolerance:
    iterations += 1
    x_next = x0 - f(x0) / fprime(x0)
    x0 = x_next
    # x = x - f(x) / fprime(x)

if iterations == maxinterations:
    print("Error: can't find solution")
else:
    print(f"Root = {x_next:.10f} found in {iterations} iterations.")