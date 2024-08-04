def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# User input
numbers = list(map(int, input("Enter integers separated by space: ").split()))
print(f"Sum of even numbers: {sum_of_even_numbers(numbers)}")
