def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_krishnamurthy_number():
    number = int(input("Enter a number: "))
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(number))
    return sum_of_factorials == number

print("Is Krishnamurthy number: ", is_krishnamurthy_number())
