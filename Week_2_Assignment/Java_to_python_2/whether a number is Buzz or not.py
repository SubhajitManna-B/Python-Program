num = int(input("Enter a number: "))

if num % 10 == 7 or num % 7 == 0:
    print(f"{num} is a Buzz number.")
else:
    print(f"{num} is not a Buzz number.")
