l = [1]
fact = 1

for i in range(1,11):
    fact *= i
    l.append(fact)

e_est = 0
for j in l:
    e_est += 1/j
print(e_est)