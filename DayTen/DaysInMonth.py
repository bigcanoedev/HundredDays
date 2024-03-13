def is_leap(year):
    """
    Takes in a year and returns True if it is a leap year
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def days_in_month(year, month):
    """
    Takes in a year and month from the user and returns the amount of days.
    """
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]


year = int(input()) #Year
month = int(input()) #month
days = days_in_month(year, month)
print(days)