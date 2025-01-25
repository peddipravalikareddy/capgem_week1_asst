def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

while True:
    year = input("Enter a year to check if it's a leap year (or 'exit' to quit): ")
    
    if year.lower() == 'exit':
        break
    
    try:
        year = int(year)
        if leap_year(year):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Please enter a valid year.")
