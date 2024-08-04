def power_without_operator(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Power: ", power_without_operator(base, exponent))
