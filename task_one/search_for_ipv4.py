# a function that checks if a giving string is a valid IPv4 octet which is 0-255 integer value
# returns true if the conditions are met, otherwise false and it's not a valid ipv4 address
def check_ip4_octet(octet):
    try:
        # check if the octet is an integer
        if octet.isdigit():
            octet = int(octet)
            # check if its a valid value in the right range [0-255]
            if 0 <= octet <= 255:
                return True
        return False
    # catch the errors that might occur (before using isdigit func.)
    except ValueError or TypeError as e:
        return False


# function to check ipv4 validation
# takes the ip_address as a raw string and call check_ip4_octet to check each of the four octet validity separately
# it returns true if all the octets are valid and the address is represented by x.x.x.x where x is 0-255
def check_for_IPv4(ip_addr):
    ip = ip_addr.split(".")
    #ipv4 must have 4 octets
    if len(ip) == 4:
        # check each octet separately
        for octet in ip:
            if not check_ip4_octet(octet):
                return False
        return True

    return False