def decimal_to_binary():
    number = int(input("Enter a decimal number: "))
    return bin(number).replace("0b", "")

print("Binary: ", decimal_to_binary())
