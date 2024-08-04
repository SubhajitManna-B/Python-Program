import math

def compute_sin(x, n):
    sin_x = 0
    for i in range(n):
        sign = (-1) ** i
        term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sin_x += sign * term
    return sin_x

# Get user input for x and n
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms in the series (n): "))

# Compute the sine of x
sin_x = compute_sin(x, n)

# Print the result
print(f"The sine of {x} radians, computed using {n} terms, is: {sin_x}")
