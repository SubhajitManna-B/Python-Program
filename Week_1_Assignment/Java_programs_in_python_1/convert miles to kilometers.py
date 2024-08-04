def miles_to_kilometers():
    miles = float(input("Enter distance in miles: "))
    conversion_factor = 1.60934
    kilometers = miles * conversion_factor
    
    print(f"{miles} miles is equal to {kilometers:.2f} kilometers")

miles_to_kilometers()
