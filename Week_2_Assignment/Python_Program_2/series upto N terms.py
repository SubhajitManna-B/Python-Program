def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def series_upto_n_terms():
    n = int(input("Enter number of terms: "))
    series = [factorial(i) for i in range(1, n + 1)]
    return series

print("Series: ", series_upto_n_terms())
