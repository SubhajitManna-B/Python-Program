def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Get user input for the list
user_input = input("Enter a list of elements separated by spaces: ")
arr = user_input.split()

# Reverse the list
reversed_arr = reverse_list(arr)

# Print the reversed list
print("Reversed list:")
print(' '.join(reversed_arr))



# for example use    a b c 