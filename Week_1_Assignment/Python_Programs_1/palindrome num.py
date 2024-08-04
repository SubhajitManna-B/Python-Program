def is_palindrome_number(num):
    num_str = str(num)
    return num_str == num_str[::-1]

input_number = input("Enter a number to check if it's a palindrome: ")

try:
    input_number = int(input_number)
    if is_palindrome_number(input_number):
        print(f"{input_number} is a palindrome number.")
    else:
        print(f"{input_number} is not a palindrome number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
