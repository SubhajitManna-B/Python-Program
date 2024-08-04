def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Function to generate prime numbers up to nth term
def generate_prime_series(n):
    primes = []
    number = 2  # Starting number to check for prime
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes

n = int(input("Enter the number of prime numbers to generate: "))

prime_series = generate_prime_series(n)

print(f"The first {n} prime numbers are: {prime_series}")
