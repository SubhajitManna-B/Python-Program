def sum_of_digits():
    number = int(input("Enter a number: "))
    return sum(int(digit) for digit in str(number))

print("Sum of digits: ", sum_of_digits())
