




import datetime
from task_two.task_two_main import add_days_to_date
from task_one.task_one_main import check_valid_ip

if __name__ == '__main__':

    print("First Task Outputs")
    print(check_valid_ip('185.125.136.142'))
    print(check_valid_ip('fe80::1'))
    print(check_valid_ip('10.200.128.96'))
    print(check_valid_ip('10.200.555.96'))
    print(check_valid_ip('X.2!0.555.96'))
    # print(check_valid_ip('127.45.04.22'))
    # print(check_valid_ip('427.45.04.22'))
    # print(check_valid_ip('127.45.0d.22'))
    # print(check_valid_ip('427.450.22'))
    # print(check_valid_ip('0f::'))
    # print(check_valid_ip('ffff::0f02'))
    # print(check_valid_ip('fff::0f02:127.45.04.22'))
    # print(check_valid_ip('fffff::0f02:127.45.04.22'))
    # print(check_valid_ip('ffft::0f02:127.45.04.22'))
    # print(check_valid_ip('ffff::0f02:127.45.dd4.22'))

    print()
    print("------------------------------")
    print()

    print("Second Task Outputs")
    # adding 3 years including a leap year '2004' (must output 21.3.2006)
    print(add_days_to_date("22.03.2003", (365 + 365 + 365)))
    # adding 366 to a leap year (must output 22.1.2005)
    print(add_days_to_date("22.01.2004", "366"))
    # adding 366 to a leap year (must output 22.10.2004)
    print(add_days_to_date("22.10.2003", "366"))
    # adding 366 to a no leap year (must output 23.1.3004)
    print(add_days_to_date("22.01.3003", 366))
    # adding 59 days to a leap year including february (output 30.3.2000)
    print(add_days_to_date("31.01.2000", 59))
    # adding 59 days to a no leap year including february (output 31.3.2100)
    print(add_days_to_date("31.01.2100", 59))
    # adding 31 to a month that has 31 days, (output 4.4.2000)
    print(add_days_to_date("4.03.2000", 31))
    # adding 9 to a date to check days functionality (output same date = 31.3.2000)
    print(add_days_to_date("22.3.2003", 9))
    # adding negative number as an integer to a date (output invalid days number)
    print(add_days_to_date("22.3.2003", -17))
    # adding negative number as a string to a date (output invalid days number)
    print(add_days_to_date("22.3.2003", "-17"))
    # checking None Type and No Input cases
    print(add_days_to_date("4.03.2000", None))
    print(add_days_to_date(None, 38))
    print(add_days_to_date(38))
    print(add_days_to_date())