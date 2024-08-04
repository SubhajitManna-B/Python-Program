import math

def compute_cos(x, n):
    cos_x = 0
    for i in range(n):
        sign = (-1) ** i
        term = (x ** (2 * i)) / math.factorial(2 * i)
        cos_x += sign * term
    return cos_x

# Get user input for x and n
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms in the series (n): "))

# Compute the cosine of x
cos_x = compute_cos(x, n)

# Print the result
print(f"The cosine of {x} radians, computed using {n} terms, is: {cos_x}")
