def check_season(month):
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month'

# Get user input for the month
month = input("Enter the name of the month: ")
season = check_season(month)
print(f"The season for {month} is {season}.")
