from task_two.day_in_month import days_in_month

# a help function that calculates the correct date after the addition
# the function adds month by month as the total number to add with the help of days_in_month
# the function returns the new date after calculation
def main_calculator(date_tuple, num):
    try:
        dd, mm, yy = date_tuple
        while num > 0:
            # days_left(mm, yy, num, dd)
            #check
            days_left = days_in_month(mm, yy) - dd
            #
            if num > days_left:
                num = num-days_left
                dd = 1
                mm += 1
                # if the month extends above 12 , add 1 to the year and month back to 1
                if mm == 13:
                    mm = 1
                    yy += 1
                # as long as we have a number to add to the date
                while num > 0:
                    # can we add by month?
                    if num > days_in_month(mm, yy):
                        num -= days_in_month(mm, yy)
                        mm += 1
                        if mm == 13:
                            mm = 1
                            yy += 1
                    # do we need to jump to the last day of the month?
                    elif num == days_in_month(mm, yy):
                        dd = num
                        num = 0
                    else:
                        dd += num
                        dd -= 1
                        num = 0
                finished_date_tup = (dd, mm, yy)
                return finished_date_tup
            else:
                finished_date_tup = (dd+num, mm, yy)
                return finished_date_tup
    except TypeError as err:
        return err