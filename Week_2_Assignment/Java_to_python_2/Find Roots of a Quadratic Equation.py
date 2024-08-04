import math

a, b, c = map(float, input("Enter coefficients a, b and c: ").split())

determinant = b**2 - 4*a*c
sqrt_val = math.sqrt(abs(determinant))

if determinant > 0:
    root1 = (-b + sqrt_val) / (2 * a)
    root2 = (-b - sqrt_val) / (2 * a)
    print("Roots are real and different.")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif determinant == 0:
    root = -b / (2 * a)
    print("Roots are real and the same.")
    print(f"Root: {root}")
else:
    print("Roots are complex and different.")
