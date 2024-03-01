def days_since_birthday(birthday):
    # Split birthday string into components
    day, month, year = map(int, birthday.split('-'))

    #  current year
    current_year = 2024

    # number of whole years since the birth year
    years_since_birth = current_year - year - 1

    # number of days (approximation, not accounting for leap years)
    days = years_since_birth * 365

    return days


# Example with my birthday
birthday = "11-07-2004"
print(days_since_birthday(birthday))


#didnt have time to paste all code here just the last one as i didnt know we had to keep it all in one place