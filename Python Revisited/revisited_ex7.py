def Velocity(n,h,b,s):
    def Radius(h,b):
        return (h*b) / (2*h+b)
    return (1/n) * (Radius(h,b)**(2/3)) * (s**(1/2))

cal = Velocity(1,2,3,4)
print(cal)