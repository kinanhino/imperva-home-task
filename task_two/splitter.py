from task_two.day_in_month import days_in_month

# a help function to divide the date currectly
# the function accepts either dd.mm.year or dd-mm-year format
# the function returns either a string invalid input or the date as a tuple (dd,mm,year)
def split_helper(date, seperator):
    try:
        date_list = date.split(seperator)
        if len(date_list) == 3:
            dd = date_list[0]
            mm = date_list[1]
            yy = date_list[2]
            if dd.isdigit() and mm.isdigit() and yy.isdigit():
                dd, mm, yy = int(dd), int(mm), int(yy)
                # ^ made below code cleaner ^
                # check month and day validation
                if mm < 13 and dd <= days_in_month(mm, yy):
                    date_tuple = (True, dd, mm, yy)
                    return date_tuple

        date_tuple = (False, "Invalid date input")
        return date_tuple
    except AttributeError as err:
        return err