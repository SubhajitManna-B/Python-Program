def sum_series(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total -= 1 / i
        else:
            total += 1 / i
    return total

# user input
n = int(input("Enter the number of terms (n): "))

# Compute the sum of the series
series_sum = sum_series(n)
print(f"The sum of the series up to {n} terms is: {series_sum}")
