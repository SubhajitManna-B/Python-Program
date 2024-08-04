import math

def find_gcd():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return math.gcd(num1, num2)

print("GCD: ", find_gcd())
