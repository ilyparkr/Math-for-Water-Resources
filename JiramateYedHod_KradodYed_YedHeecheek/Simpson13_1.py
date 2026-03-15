import numpy as np 

x = np.linspace(np.pi/2,(3*np.pi)/2,1000001)
fx = np.cos(x)**3
h = np.diff(x)[0]

odd = []
even = []

for i in range(1,len(fx)-1):
    if i % 2 != 0:
        odd.append(fx[i])
    else:
        even.append(fx[i])

print("answer =", (h/3)*(fx[0]+fx[-1]+(4*sum(odd)+(2*sum(even)))))

# fx[start:stop:step]
#sum_odd = np.sum(fx[1:-1:2])  # เริ่ม index 1 ถึงตัวรองสุดท้าย ขยับทีละ 2 (ได้คี่ทั้งหมด)
#sum_even = np.sum(fx[2:-1:2]) # เริ่ม index 2 ถึงตัวรองสุดท้าย ขยับทีละ 2 (ได้คู่ทั้งหมด)

#answer = (h/3) * (fx[0] + fx[-1] + 4*sum_odd + 2*sum_even)
#print("answer =", answer)