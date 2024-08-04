def calculate_sum_and_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers) if numbers else 0
    return total_sum, average

# User input
numbers = list(map(int, input("Enter integers separated by space: ").split()))
total_sum, average = calculate_sum_and_average(numbers)
print(f"Sum: {total_sum}, Average: {average}")
