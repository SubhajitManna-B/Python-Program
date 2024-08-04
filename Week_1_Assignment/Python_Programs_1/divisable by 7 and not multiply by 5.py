
def find_numbers():
    result = []
    for number in range(1000, 2001):
        if number % 7 == 0 and number % 5 != 0:
            result.append(number)
    return result


if __name__ == "__main__":
    numbers = find_numbers()
    print("Numbers between 1000 and 2000 that are divisible by 7 and not a multiple of 5:")
    print(numbers)
