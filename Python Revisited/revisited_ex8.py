total = 0
lap = 0
while True:
    num = input("Enter a number : ")

    if num == 'done':
        break
    
    try:
        total += int(num)
        lap += 1
    except ValueError:
        print("bad data")

print(total,lap,total/lap)