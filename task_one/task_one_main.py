from task_one.search_for_ipv4 import check_for_IPv4
from task_one.which_ipv6_ver import which_ipv6_version


# main function that checks if its a valid ip at all and calling the right function to get the version type it uses
# check_for_IPv4 to search for a valid ipv4 address and which_ipv6_version to check for a valid ipv6 or dual address
# the function returns the version of the ip if it's a valid ip, otherwise return invalid ip
def check_valid_ip(ip_addr):
    try:
        if ip_addr is None:
            return "input address cannot be None"
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
            # then it might be an ipv6 or a dual ip
            return which_ipv6_version(ipv6)
    except TypeError as e:
        return e

