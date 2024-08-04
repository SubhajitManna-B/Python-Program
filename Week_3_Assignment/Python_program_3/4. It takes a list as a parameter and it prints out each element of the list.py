def print_list(lst):
    for item in lst:
        print(item)

# Get user input for the list
user_input = input("Enter a list of elements separated by spaces: ")
lst = user_input.split()

# Print the list elements
print_list(lst)


# for example use    apple banana cherry