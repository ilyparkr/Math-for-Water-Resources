def computegrade(scores):
    if scores >= 0.9:
        grade = 'A'
    elif scores >= 0.8:
        grade = 'B'
    elif scores >= 0.7:
        grade = 'C'
    elif scores >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    
    return grade

try :
    score = float(input("Enter scores : "))
    if score > 1.0 or score < 0.0:
        print("Out of range")
    else:
        print(computegrade(score))
except ValueError:
    print("Error, please input numeric")