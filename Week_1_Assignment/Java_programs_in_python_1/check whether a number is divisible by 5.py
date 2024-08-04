def check_divisibility_by_5():
    number = int(input("Enter a number: "))
    if number % 5 == 0:
        print(f"{number} is divisible by 5.")
    else:
        print(f"{number} is not divisible by 5.")

check_divisibility_by_5()
