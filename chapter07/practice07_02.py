import re


if __name__ == '__main__':
    """
    Find first phone number inside a string.
    Split into groups the phone numbers by using parentheses
    """
    phone_regex = re.compile(r'(\d\d\d\d) (\d\d\d \d\d\d)')
    mo = phone_regex.search("Some phone numbers are here: 0700 000 000, 0711 111 111")
    # group() or group(0) is the entire matched string
    print(mo.group())
    print(mo.group(0))
    # group(1) is the 1st group in matched string bounded by parentheses
    print(mo.group(1))
    # group(2) is the 2nd group in matched string bounded by parentheses
    print(mo.group(2))
    # groups() is a tuple with all groups in matched string bounded by parentheses
    print(mo.groups())
