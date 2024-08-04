# Mapping digits to their 8-segment display representations
segment_map = {
    '0': [" _ ", "| |", "|_|"],
    '1': ["   ", "  |", "  |"],
    '2': [" _ ", " _|", "|_ "],
    '3': [" _ ", " _|", " _|"],
    '4': ["   ", "|_|", "  |"],
    '5': [" _ ", "|_ ", " _|"],
    '6': [" _ ", "|_ ", "|_|"],
    '7': [" _ ", "  |", "  |"],
    '8': [" _ ", "|_|", "|_|"],
    '9': [" _ ", "|_|", " _|"]
}

def print_8_segment_number(number):
    number_str = str(number)
    rows = ["", "", ""]

    for digit in number_str:
        if digit in segment_map:
            for i in range(3):
                rows[i] += segment_map[digit][i] + " "
        else:
            print(f"Digit '{digit}' is not supported.")
            return

    for row in rows:
        print(row)

# Get user input for the number
number = input("Enter a number: ")

# Print the 8-segment display
print_8_segment_number(number)
