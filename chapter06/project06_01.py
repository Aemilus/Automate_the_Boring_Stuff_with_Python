#! /usr/bin/python3

import sys
from pathlib import Path

import pyperclip


SCRIPT_PATH = Path(sys.argv[0])

MESSAGES = {
    "hello": "Hi,\n"
             "My name is Johnny and I work in company X as a software engineer.\n"
             "You can contact me at +40 7xx xxx xxx or johnny@x.com\n"
             "Thanks",
    "ooo": "Hi,\n"
           "I'm currently out of office until xx/xx/2022.\n"
           "During my absence please contact my manager at xyz.\n"
           "Thanks",
    "meet": "Hi,\n"
            "I propose to setup a meeting on xx/xx/2022 at HH:mm your local time.\n"
            "Please let me know if suitable or propose a convenient time.\n"
            "Thanks",
}

VALID_KEYWORDS = list(MESSAGES.keys())


def print_usage():
    print(f"\nUsage: python3 {SCRIPT_PATH.name} <keyword>"
          f"\n\t<keyword>: one of the following values {VALID_KEYWORDS}")


if __name__ == '__main__':
    # check script arguments
    if len(sys.argv) != 2:
        print(f"\n*ERROR* Invalid arguments.")
        print_usage()
        sys.exit(-1)
    else:
        keyword = sys.argv[1]
        if keyword not in VALID_KEYWORDS:
            print(f"\n*ERROR* Keyword {keyword} not found.")
            print_usage()
            sys.exit(-2)

    # copy corresponding message
    msg = MESSAGES[keyword]
    pyperclip.copy(msg)
    print(f"\nBelow message has been copied to clipboard:\n"
          f"{msg}")
