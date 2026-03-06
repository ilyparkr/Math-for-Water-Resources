"""Practice 1"""

def compute_rectangle_method():
    h = 0.2
    fx = [0.48, 0.65, 0.87, 1.18, 1.60, 2.15, 2.73]
    result = sum(fx)*h
    print(result)

def mid_point_method():
    h = 0.4
    fx = [0.48, 0.65, 0.87, 1.18, 1.60, 2.15, 2.73]
    result = (fx[0]+fx[-1] / 2)*(fx[-1]-fx[0])
    print(result*h)

compute_rectangle_method()
mid_point_method()