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