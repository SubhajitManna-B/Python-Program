def print_table(rows):
    
    # Print each row
    for a in range(1, rows + 1):
        row = [a, a**0, a**1, a**2, a**3]
        print(" ".join(map(str, row)))

# Get user input for the number of rows
rows = int(input("Enter the number of rows: "))

# Print the table
print_table(rows)
