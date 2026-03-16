scores = float(input("Enter Score: "))

if scores < 0.0 or scores > 1.0:
    print("Out of range")
elif scores >= 0.9:
    print('A')
elif scores >= 0.8:
    print('B')
elif scores >= 0.7:
    print('B')
elif scores >= 0.6:
    print('B')
else:
    print('D')