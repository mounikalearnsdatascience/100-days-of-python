def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4 == 0:
       return True
    else:
        return False


# Example test
print(is_leap_year(2021))
