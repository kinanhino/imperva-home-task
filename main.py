# a function that checks if a giving string is a valid IPv4 octet.
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
def check_for_IPv4(ip_addr):
    ip = ip_addr.split(".")
    if len(ip) == 4:
        for octet in ip:
            if not check_ip4_octet(octet):
                return False
        return True

    return False


def check_for_IPv6(ip_addr):
    last_hextet = ip_addr[-1]
    ip = ip_addr[:-1]
    if len(ip) < 8:
        for hextet in ip:
            # print(f"'{hextet}'")
            if not check_ip6_hextet(hextet) and hextet != "":
                return "Neither"
        # a dual ip must be y:y:y:y:y:y:x.x.x.x ,where x must be between 0-255 and y neither empty or 0000-ffff
        if check_for_IPv4(last_hextet) and len(ip) < 7:
            return "dual"
        elif check_ip6_hextet(last_hextet) or last_hextet == "":
            return "ipv6"
        else:
            return "Neither"
    else:
        return "Neither"


def check_ip6_hextet(hextet):
    valid_characters = "0123456789abcdef"
    if len(hextet) < 5:
        for char in hextet:
            if char not in valid_characters:
                return False
        return True
    return False


def which_version(ip_addr):
    normal_or_dual = check_for_IPv6(ip_addr)
    ip_addr = ":".join(ip_addr)
    if normal_or_dual == "ipv6":
        return f"{ip_addr} is a Valid IPv6 address"
    elif normal_or_dual == "dual":
        return f"{ip_addr} is a Valid dual ip address"
    elif normal_or_dual == "Neither":
        return f"{ip_addr} is Not a Valid ip address"
    else:
        return f"something is very wrong with that {ip_addr}"


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
        return which_version(ipv6)


if __name__ == '__main__':
    # print(check_valid_ip('127.45.04.22'))
    # print(check_valid_ip('427.45.04.22'))
    # print(check_valid_ip('127.45.0d.22'))
    # print(check_valid_ip('427.450.22'))
    # print(check_valid_ip('0f::'))
    # print(check_valid_ip('ffff::0f02'))
    print(check_valid_ip('fff::0f02:127.45.04.22'))
    print(check_valid_ip('ffft::0f02:127.45.04.22'))
    print(check_valid_ip('ffff::0f02:127.45.dd4.22'))



    print(check_valid_ip('185.125.136.142'))
    print(check_valid_ip('fe80::1'))
    print(check_valid_ip('10.200.128.96'))
    print(check_valid_ip('10.200.555.96'))
    print(check_valid_ip('X.2!0.555.96'))