# Defining functions
def farewell_world():
    print("farewell_world")


farewell_world()


def square_it(number):
    return number**2


print(square_it(3))


def bil_plus_tip_calc(bill):
    tax_amt = bill * 0.18
    return bill + tax_amt


def distance_calc(x1, y1, x2, y2):
    inside = (x2-x1) ** 2 + (y2-y1) ** 2
    answer = inside ** 0.5
    return answer


print(distance_calc(0, 3, 0, 4))


def pythagcalc(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c
print(pythagcalc(1, 3))
