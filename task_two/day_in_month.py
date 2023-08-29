from jdcal import is_leap


# a function to return the right days number of each month in the calendar
# including checking for leap year for the February month
# returns the number of days at the given month in a given year
def days_in_month(mm, yy):
    if mm in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mm in [4, 6, 9, 11]:
        return 30
    elif mm == 2:
        if is_leap(yy):
            return 29
        else:
            return 28
