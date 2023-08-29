from task_one.search_for_ipv4 import check_for_IPv4
from task_one.which_ipv6_ver import which_ipv6_version


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

