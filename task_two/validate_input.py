from task_two.splitter import split_helper


# a function to validate that the date is in a date format
# using the help of split_helper with '.' and '-'
# returns the correct tuple (False, "invalid message") or (True,dd,mm,year)
def validate_date_input(date):
    date_tup = split_helper(date, ".")
    if not date_tup[0]:
        date_tup = split_helper(date, "-")
        # if not date_tup[0]:
        #     return "Invalid Date Input"
    return date_tup

# a function to validate if the number is a correct positive integer
# the function accepts either integers or integers as strings
# it returns true if it's an integer, otherwise false
def validate_number_input(number_of_days):
    if str(number_of_days).isdigit():
        return True
    return False
