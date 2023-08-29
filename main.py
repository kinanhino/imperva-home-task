# a function that checks if a giving string is a valid IPv4 octet, 0-255 integer value
def check_ip4_octet(octet):
    try:
        # check if the octet is an integer
        if octet.isdigit():
            octet = int(octet)
            # check if it's a valid value in the right range [0-255]
            if 0 <= octet <= 255:
                return True
        return False
    # catch the errors that might occur (before using isdigit func.)
    except ValueError and TypeError as e:
        return False


# function to check for v4 validity
# takes the ip_address as a raw string
def check_for_IPv4(ip_addr):
    # ipv4 is represented by x.x.x.x where x is 0-255
    ip = ip_addr.split(".")
    #ipv4 must have 4 octets
    if len(ip) == 4:
        # check each octet separately
        for octet in ip:
            if not check_ip4_octet(octet):
                return False
        return True

    return False


# function to check for v6 validity
# takes the ip_adress as a list seperated by ':' colons
def normal_or_dual_v6(ip_addr):
    # cut last hextet for ipv4 search
    last_hextet = ip_addr[-1]
    ip = ip_addr[:-1]
    if len(ip) < 8:
        for hextet in ip:
            # print(f"'{hextet}'")
            # check if a hextet is not a valid hextet and not empty (zeros) then it's not an ipv6 address
            if not check_ip6_hextet(hextet) and hextet != "":
                return "Neither"
        # last hextet (after last ':' colon) is actually an ipv4 address
        if check_for_IPv4(last_hextet) and len(ip) < 7:
            return "dual"
        # last hextet is a regular hextet
        elif check_ip6_hextet(last_hextet) or last_hextet == "":
            return "ipv6"
        else:
            return "Neither"
    else:
        return "Neither"


# function to check if a given string is a valid hextet value
def check_ip6_hextet(hextet):
    valid_characters = "0123456789abcdef"
    if len(hextet) < 5:
        for char in hextet:
            if char not in valid_characters:
                return False
        return True
    return False


def which_ipv6_version(ip_addr):
    normal_ipv6_dual = normal_or_dual_v6(ip_addr)
    ip_addr = ":".join(ip_addr)
    if normal_ipv6_dual == "ipv6":
        return f"{ip_addr} is a Valid IPv6 address"
    elif normal_ipv6_dual == "dual":
        return f"{ip_addr} is a Valid dual ip address"
    elif normal_ipv6_dual == "Neither":
        return f"{ip_addr} is Not a Valid ip address"
    else:
        return f"something is very wrong with that {ip_addr}"


# main function that checks if its a valid ip at all and calling the right function to get the version type
def check_valid_ip(ip_addr):
    ipv6 = ip_addr.split(":")
    ipv4 = ip_addr.split(".")
    # print(len(ipv4), len(ipv6))
    if len(ipv4) == 4:
        if check_for_IPv4(ip_addr):
            return f"{ip_addr} is a Valid IPv4 address"
    if len(ipv6) > 8 or len(ipv6) < 3:
        return f"{ip_addr} is Not a Valid ip address"
        # must be an inner else!!
    else:
        # it must be an ipv6
        return which_ipv6_version(ipv6)


import datetime
from task_two.task_two_main import add_days_to_date


if __name__ == '__main__':
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
    print()
    print("------------------------------")
    print()
    print("First Task Outputs")
    # print(check_valid_ip('127.45.04.22'))
    # print(check_valid_ip('427.45.04.22'))
    # print(check_valid_ip('127.45.0d.22'))
    # print(check_valid_ip('427.450.22'))
    # print(check_valid_ip('0f::'))
    # print(check_valid_ip('ffff::0f02'))
    print(check_valid_ip('fff::0f02:127.45.04.22'))
    print(check_valid_ip('fffff::0f02:127.45.04.22'))
    print(check_valid_ip('ffft::0f02:127.45.04.22'))
    print(check_valid_ip('ffff::0f02:127.45.dd4.22'))



    print(check_valid_ip('185.125.136.142'))
    print(check_valid_ip('fe80::1'))
    print(check_valid_ip('10.200.128.96'))
    print(check_valid_ip('10.200.555.96'))
    print(check_valid_ip('X.2!0.555.96'))