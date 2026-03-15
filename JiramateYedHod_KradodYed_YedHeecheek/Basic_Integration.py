import numpy as np

x = np.arange(1,3.5,0.5)
fx = 1/x
h_rec = 0.5
h_mid = 1.0


answer_rec = []
answer_mid = []

for i in range(len(fx)-1):
    answer_rec.append(fx[i])
for i in [1,3]:
    answer_mid.append(fx[i])

print("answer from rectangular method =",h_rec*sum(answer_rec))
print("answer from MidPoint method =",h_mid*sum(answer_mid))

