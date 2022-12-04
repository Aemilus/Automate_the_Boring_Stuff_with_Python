import re
import sys

if __name__ == '__main__':
    """Find first occurrence of 'green' or 'red' in given text."""
    color_regex = re.compile(r'green|red')
    # red is found first
    mo = color_regex.search("Semaphore colors are: red, yellow and green.")
    if mo:
        print(mo.group())
    # green is found first
    mo = color_regex.search("Semaphore colors are: green, yellow and red.")
    if mo:
        print(mo.group())

    """
    Find first occurrence of either 'sunset' or 'sunrise' in a text.
    Note how both words start with 'sun'.
    """
    text = "I like to watch the sunrise. Maybe I will watch the sunset too."
    sun_regex = re.compile(f'sun(rise|set)')
    mo = sun_regex.search(text)
    if mo:
        print(mo.group())
        # if you want to print the matched group/groups inside parentheses see below
        print(mo.group(1))
        print(mo.groups())
