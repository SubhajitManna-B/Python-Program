def search_element(numbers, target):
    return target in numbers

# User input
numbers = list(map(int, input("Enter integers separated by space: ").split()))
target = int(input("Enter the element to search for: "))
found = search_element(numbers, target)
print(f"Element {target} found: {found}")
