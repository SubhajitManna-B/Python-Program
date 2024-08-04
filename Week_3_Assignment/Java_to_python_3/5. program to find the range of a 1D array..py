def find_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)

# User input
numbers = list(map(int, input("Enter integers separated by space: ").split()))
print(f"Range: {find_range(numbers)}")
