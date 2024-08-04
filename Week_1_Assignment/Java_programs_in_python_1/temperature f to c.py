def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")

fahrenheit_to_celsius()
