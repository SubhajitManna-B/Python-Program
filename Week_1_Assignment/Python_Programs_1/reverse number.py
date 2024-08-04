def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

number = int(input("Enter a number: "))

reversed_number = reverse_number(number)

print(f"The reverse of {number} is {reversed_number}")
