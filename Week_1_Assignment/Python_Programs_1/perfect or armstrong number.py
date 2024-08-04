def check_number_type(num):
    # Check if num is a perfect number
    def is_perfect_number(num):
        if num <= 0:
            return False
        sum_of_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == num
    
    # Check if num is an Armstrong number
    def is_armstrong_number(num):
        if num <= 0:
            return False
        num_str = str(num)
        num_digits = len(num_str)
        sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
        return sum_of_powers == num
    
    if is_perfect_number(num):
        return f"{num} is a perfect number."
    elif is_armstrong_number(num):
        return f"{num} is an Armstrong number."
    else:
        return f"{num} is neither a perfect number nor an Armstrong number."

# Example usage:
input_number = int(input("Enter a number to check its type: "))
result = check_number_type(input_number)
print(result)
