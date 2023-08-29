from task_two.validate_input import validate_number_input, validate_date_input
from task_two.main_calculator import main_calculator


# the main function that gets called from the main
# input validation checks including special cases
# returns the final result if the calculation is valid, otherwise returns a specific error message
def add_days_to_date(date=None, number_of_days=None):
    try:
        if date is not None and number_of_days is not None:
            if number_of_days == 0 or number_of_days == "0":
                return date
            date_tuple = validate_date_input(date)
            # date tuple is (False / True, "invalid message" / dd,mm,yy)
            if not date_tuple[0]:
                # return invalid date input message
                return date_tuple[1]
            if not validate_number_input(number_of_days):
                return "Invalid number of days. Must be a positive integer"
            if type(number_of_days) == str:
                number_of_days = int(number_of_days)

            finished_tuple = main_calculator(date_tuple[1:], number_of_days)
            finished_tuple = [str(tup) for tup in finished_tuple]
            formatted_string = ".".join(finished_tuple)
            return formatted_string
        else:
            return "Input Values Cannot be None"

    except TypeError or AttributeError as err:
        return err
    except NameError as err:
        return err
