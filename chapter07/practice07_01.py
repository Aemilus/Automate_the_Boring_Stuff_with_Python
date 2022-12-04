import re


if __name__ == '__main__':
    """Find first phone number inside a string."""
    phone_regex = re.compile(r'\d\d\d\d \d\d\d \d\d\d')
    mo = phone_regex.search("Some phone numbers are here: 0700 000 000, 0711 111 111")
    if mo:
        result = mo.group()
        print(result)
