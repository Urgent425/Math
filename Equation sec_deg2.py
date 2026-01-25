
def racines(a,b,c):
    delta = b**2 - 4*a*c
    print(delta)
    if delta > 0:
        x_1 = ((-b + delta**0.5)/2*a)
        x_2 = ((-b - delta**0.5)/2*a)  
        print("(", x_1, x_2, ")")

    elif delta == 0:
        x_1 = (-b/2*a)
        x_2 = (-b/2*a)
        print("(", x_1, x_2, ")")

    else:
        print("Pas de solution dans R")

racines(1,4,4)
