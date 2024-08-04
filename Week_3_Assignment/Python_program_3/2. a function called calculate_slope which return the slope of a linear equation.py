def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'Slope is undefined'
    return (y2 - y1) / (x2 - x1)

# Get user input for the coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

slope = calculate_slope(x1, y1, x2, y2)
print(f"The slope of the line through ({x1}, {y1}) and ({x2}, {y2}) is {slope}.")


# for example use 2,3,5,7