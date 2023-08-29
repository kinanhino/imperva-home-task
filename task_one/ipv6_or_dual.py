from task_one.search_for_ipv4 import check_for_IPv4


# function to check ipv6 validation
# takes the ip_adress as a list separated by ':' colons
# calls check_ip6_hextet on the list's items, for the last hextet checks for possible ipv4 address which makes it a dual
# returns ipv6 or dual or Neither
def normal_or_dual_ipv6(ip_addr):
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


# function to check if a given string is a valid hextet value, which is 0000 to ffff
# returns true if all the chars are valid hexadecimal value or an empty string, otherwise false
def check_ip6_hextet(hextet):
    valid_characters = "0123456789abcdef"
    if len(hextet) < 5:
        for char in hextet:
            if char not in valid_characters:
                return False
        return True
    return False
