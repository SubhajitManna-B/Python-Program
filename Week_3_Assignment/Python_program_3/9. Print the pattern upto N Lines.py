def print_pattern(N):
    if N <= 0:
        print("N should be a positive integer.")
        return

    for i in range(1, N + 1):
        spaces = ' ' * (N - i)
        if i == 1:
            print(f"{spaces}.")
        else:
            line = '/' + ' ' * (2 * i - 3) + '\\'
            if i == N:
                line = '/' + '_' * (2 * i - 3) + '\\'
            print(f"{spaces}{line}")

# Get user input for N
N = int(input("Enter the number of lines (N): "))

# Print the pattern
print_pattern(N)
