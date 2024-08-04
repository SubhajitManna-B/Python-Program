start, end = map(int, input("Enter the start and end of the interval: ").split())

print(f"Multiples of 10 between {start} and {end}: ", end="")
for i in range(start, end + 1):
    if i % 10 == 0:
        print(i, end=" ")
