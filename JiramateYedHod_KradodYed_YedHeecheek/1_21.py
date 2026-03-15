# -*- coding: utf-8 -*-
"""
Spyder Editor

By Krittin Visessiri 6710506703

Created in 1/21/2026

List of exercise: type any_ex() on console
"""

#Any exercise
def any_ex():
    print("""
          >>Intro<<
              Exercise 1&2 : pay() 
              Exercise 3 : grade()
          >>Function<<
              Exercise 4 : computepay(hours,rates) & ex4()
              Exercise 5 : computegrade(score) & ex5()
              Exercise 6 : Manning(n,r,s) & ex6()
              Exercise 7 : velocity(b,h,n,s) , radius(b,h) and ex7()
          >>Loop<<
          """)
#Exercise 1 and 2
def pay():
    try:
        hours = int(input("Enter Hours: "))
        rates = int(input("Enter Rate: "))
    except:
        print("Error, please enter numeric input")
    if hours > 40: 
        return f"Pay: {(40*rates) + ((hours-40) * (rates*1.5))}"
    else:
        return f"Pay: {hours * rates}"

#Exercise 3
def grade():
    score = float(input("Input your grade here >> "))
    if score >= 0 and score < 1:
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        else:
            return "F"
    else:
        return "Error , please try again"
    
#Exercise 4
def computepay(hours,rates):
    if hours > 40: 
        return f"Pay: {(40*rates) + ((hours-40) * (rates*1.5))}"
    else:
        return f"Pay: {hours * rates}"
def ex4():
    hour = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))
    return computepay(hour,rate)

#Exercise 5
def computegrade(score):
    if score >= 0 and score < 1:
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        else:
            return "F"
    else:
        return "Error , please try again"
def ex5():
    score = float(input("Input your grade here >> "))
    return computegrade(score)

#Exercise 6
def Manning(n,r,s):
    return (1/n)*(r**(2/3))*(s**(1/2))
def ex6():
    n = float(input("Manning’s Coefficient: "))
    r = float(input("Hydraulic radius: "))
    s = float(input("Channel Slope: "))
    return f"Velocity: {Manning(n,r,s)} "
#Exercise 7 
def velocity(b,h,n,s):
    def radius(b,h):
        return (h*b)/((2*h)+b)
    return (1/n)*(radius(b,h)**(2/3))*(s**(1/2))
def ex7():
     n = float(input("Manning’s Coefficient: "))
     h = float(input("Channel height: "))
     b = float(input("Channel width:"))
     s = float(input("Channel Slope: "))
     return f"Velocity: {velocity(b,h,n,s)} "

#Exercise 8
def ex8():
    list1 = []
    while True:
        n = input(">> Enter a number: ")
        if n == "done":
            return f"{sum(list1)} {len(list1)} {(sum(list1)/len(list1))}"
            break
        else:
            list1.append(int(n))
            continue
        
        



















    