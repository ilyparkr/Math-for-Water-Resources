try:
    hours = int(input("Enter Hours : "))
    rate = int(input("Enter Rate : "))
    if hours > 40:
        extra = (hours - 40) * (rate*1.5)
        pay = 400
        print(pay+extra)
    else:
        print(hours*rate)
except ValueError:
    print("Error, please enter numeric input")