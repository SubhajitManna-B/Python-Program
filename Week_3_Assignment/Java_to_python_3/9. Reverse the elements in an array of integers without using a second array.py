def reverse_in_place(numbers):
    left, right = 0, len(numbers) - 1
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1

# User input
numbers = list(map(int, input("Enter integers separated by space: ").split()))
reverse_in_place(numbers)
print(f"Reversed array: {numbers}")
