import numpy as np

l = np.linspace(0,6,1000003)
w = (15*np.sin((np.pi*l)/6)) + (2*np.exp(0.5*l))
h = np.diff(l)[0]

# Composite rectangular method
Rec = []
for i in range(len(w)-1):
    Rec.append(w[i])

# Composite Midpoint method
Mid = []
for i in range(len(w)):
    Mid.append(w[i])

# Composite Trapezoidal method
Trapez = []
for i in range(1,len(w)):
    Trapez.append(w[i] + w[i-1])
Trape = (h/2) * sum(Trapez)
# Simpson 1/3 Method
Odd = []
Even = []
for i in range(1,len(w)-1):
    if i%2 != 0:
        Odd.append(w[i])
    else:
        Even.append(w[i])
Simpson13 = ( h/3 ) * (w[0] + w[-1] + (4*sum(Odd)) + (2*sum(Even)))

# Simpson 3/8 Method
Three = []
Two = []
for i in range(1,len(w)-1):
    if i%3 == 0:
        Two.append(w[i])
    else:
        Three.append(w[i])
Simpson38 = ( (3*h) / 8) * (w[0] + w[-1] + (3*sum(Three)) + (2*sum(Two)))

print("Rectangular method =", h * sum(Rec))
print("Midpoint method =", h * sum(Mid))
print("Trapezoidal method =",Trape)
print("Simpson1/3 method =", Simpson13)
print("Simpson3/8 method =", Simpson38)