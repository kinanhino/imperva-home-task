from task_one.ipv6_or_dual import normal_or_dual_ipv6


# a function that prints out the right ipv6 version, otherwise not a valid ip-address, because we already checked for ipv4
# it calls the normal_ipv6_dual function that check for a valid ipv6
# returns the right message
def which_ipv6_version(ip_addr):
    normal_ipv6_dual = normal_or_dual_ipv6(ip_addr)
    ip_addr = ":".join(ip_addr)
    if normal_ipv6_dual == "ipv6":
        return f"{ip_addr} is a Valid IPv6 address"
    elif normal_ipv6_dual == "dual":
        return f"{ip_addr} is a Valid dual ip address"
    elif normal_ipv6_dual == "Neither":
        return f"{ip_addr} is Not a Valid ip address"
    else:
        return f"something is very wrong with that {ip_addr}"

