import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return 'No real roots'

# input 
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = solve_quadratic_eqn(a, b, c)

if isinstance(roots, tuple):
    if len(roots) == 2:
        print(f"The roots of the quadratic equation are: {roots[0]} and {roots[1]}")
    else:
        print(f"The root of the quadratic equation is: {roots[0]}")
else:
    print(roots)


# for exmple use 1 -3 2