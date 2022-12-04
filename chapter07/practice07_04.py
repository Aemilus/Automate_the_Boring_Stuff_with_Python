import re


if __name__ == '__main__':
    """
    Sometimes there is a pattern that you want to match only optionally.
    That is, the regex should find a match regardless of whether that bit of text is there.
    The ? character flags the group that precedes it as an optional part of the pattern.
    """
    text1 = "My phone number is 0700000000"
    text2 = "My phone number is 0700-000-000"
    text3 = "My phone number is 0700 000 000"
    text4 = "My phone number is 0700 000-000"
    text5 = "My phone number is 0700000-000"
    text6 = "My phone number is 0700 000000"
    # in below regex expression the (-|\s)? is the optional group
    # it matches none or single occurrence of a white space or a hyphen
    phone_regex = re.compile(r'(\d\d\d\d)(-|\s)?(\d\d\d)(-|\s)?(\d\d\d)')
    for i in range(1, 7, 1):
        print(f"*** text{i} ***")
        mo = phone_regex.search(globals()[f"text{i}"])
        if mo:
            print(mo.group())
            print(mo.groups())
