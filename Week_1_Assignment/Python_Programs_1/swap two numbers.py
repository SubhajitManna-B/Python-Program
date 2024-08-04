def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1, num2 = swap(num1, num2)
print(f"After swapping: num1 = {num1}, num2 = {num2}")
