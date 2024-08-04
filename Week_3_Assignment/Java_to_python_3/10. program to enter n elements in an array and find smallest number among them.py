def find_smallest(numbers):
    if not numbers:
        return None
    return min(numbers)

# User input
numbers = list(map(int, input("Enter integers separated by space: ").split()))
smallest = find_smallest(numbers)
print(f"Smallest number: {smallest}")
